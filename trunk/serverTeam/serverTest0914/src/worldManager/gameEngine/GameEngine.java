package worldManager.gameEngine;

import core.GameServer;

import dataAccessLayer.AnimalStatDAO;
import dataAccessLayer.BirthListDAO;
import dataAccessLayer.DeathListDAO;
import dataAccessLayer.PlantStatDAO;
import dataAccessLayer.UserActionsDAO;
import dataAccessLayer.WorldDAO;
import dataAccessLayer.ZoneGroupsDAO;
import dataAccessLayer.ZoneNodeAddDAO;
import dataAccessLayer.ZoneSpeciesDAO;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import metadata.Constants;

import model.Avatar;
import model.Player;
import model.SpeciesType;
import model.World;

import networking.response.ResponseBirthAnimal;
import networking.response.ResponseBirthPlant;
import networking.response.ResponseKillAnimal;
import networking.response.ResponseKillPlant;
import networking.response.ResponseUpdateTime;

import utility.OrganismComparator;

import worldManager.gameEngine.species.Animal;
import worldManager.gameEngine.species.Plant;
import worldManager.gameEngine.species.Organism;
import worldManager.geom.Point;

/**
 *
 * @author KeithKong
 */
public class GameEngine {

    protected World world;
    protected short gameMode;
    protected long gameScaleTime; //how many ingame seconds have passed
    protected float gameScale; //how much _gameScaleTime passes in one real second
    protected long lastRunTime;
    protected int startMonth;
    protected int startYear;
    protected int currentMonth; // current gameScale day
    protected String ecoSysType; //For example: Savana
    protected HashMap<Integer, Zone> zones;
    protected HashMap<Point, Zone> pointZones;
    protected NatureController natureController;
    protected GameServer gameServer;
    protected boolean isActive;
    protected ExecutorService executorService;
    protected boolean isReady;
    protected int unique_id = 100000;

    public GameEngine(World world) {
        /*get game data from db in this order:
         * gameScaleTime
         * currentDay
         * ecosystem type string
         * gameMode?
         * Avatars
         * Zones
         */

        this.world = world;
        gameServer = GameServer.getInstance();

        lastRunTime = System.currentTimeMillis();
        zones = new HashMap<Integer, Zone>();
        pointZones = new HashMap<Point, Zone>();

        gameScaleTime = world.getSeconds();
        startMonth = world.getMonth();
        startYear = world.getYear();
        currentMonth = world.getMonth();
        ecoSysType = world.getEnvType();
        gameMode = world.getGameMode();

        createNatureController(ecoSysType);

//        updateGameScale();
        gameScale = world.getTimeRate() * Constants.TIME_MODIFIER;

        executorService = Executors.newCachedThreadPool();
        isReady = true;
    }

    public void saveGameStateToDB() {
        //this will trigger all data to be saved to the db
    }

    /* FOR DB */
    public int getWorldID() {
        return world.getID();
    }

    public World getWorld() {
        return world;
    }

    public Zone getZone(int zone_id) {
        return zones.get(zone_id);
    }

    public void setEcoSysType(String ecoSysType) {
        this.ecoSysType = ecoSysType;
    }

    public String getEcoSysType() {
        return this.ecoSysType;
    }

    public void setGameMode(short mode) {
        gameMode = mode;
    }
    
    public float getGameScale() {
        return gameScale;
    }
    
    public float setGameScale(float gameScale) {
        return this.gameScale = gameScale;
    }

    public long getGameScaleTime() {
        return gameScaleTime;
    }

    public void setGameScaleTime(long gameScaleTime) {
        this.gameScaleTime = gameScaleTime;
    }

    public int getCurrentDay() {
        return currentMonth;
    }

    public void setCurrentDay(int currentDay) {
        this.currentMonth = currentDay;
    }

    public void createNatureController(String type) {
        NatureControllerType ncType = gameServer.getNatureControllerType(type);
        natureController = new NatureController(this, ncType);
    }
    
    public NatureController getNatureController() {
        return natureController;
    }
    
    public List<Zone> getZoneList() {
        return new ArrayList<Zone>(zones.values());
    }

    public void addZone(Zone zone) {
        zone.setLastSimulationTime(gameScaleTime);
        zone.setGameEngine(this);

        zones.put(zone.getID(), zone);
        pointZones.put(new Point(zone.getColumn(), zone.getRow()), zone);

        if (zone.isEnable()) {
            executorService.submit(zone.createRunnable());
        }
    }

    /* END FOR DB */
    public Zone getRandomZone() {
        int index = (int) ((double) zones.size() * Math.random());

        for (Integer key : zones.keySet()) {
            if (index <= 0) {
                return zones.get(key);
            }
            index--;
        }

        return null;
    }

    public void start() {
        lastRunTime = System.currentTimeMillis();
        isActive = true;
    }

    public boolean isReady() {
        return isReady;
    }

    public boolean isReady(boolean isReady) {
        return this.isReady = isReady;
    }

    public void run() {
        if (isActive) {
            if (isReady) {
                long currentRunTime = System.currentTimeMillis();
                long seconds = (currentRunTime - lastRunTime) / 1000;
                long time_diff = (long) (seconds * gameScale);

                if (time_diff > 0) {
                    gameScaleTime += time_diff;

                    world.setPlayTime(world.getPlayTime() + seconds);

                    int prevMonth = currentMonth;
                    int day = (int) (gameScaleTime / (Constants.MONTH_DURATION / 30)) + 1;
                    currentMonth = startMonth + (int) (gameScaleTime / Constants.MONTH_DURATION);

                    world.setDays(day);
                    world.setSeconds(gameScaleTime % Constants.MONTH_DURATION);

                    boolean isNewMonth = currentMonth > prevMonth;

                    natureController.run(gameScaleTime, isNewMonth);

                    if (isNewMonth) {
                        world.setMonth((currentMonth - 1) % 12 + 1);
                        world.setYear(startYear + (currentMonth - 1) / 12);

                        try {
                            WorldDAO.updateTime(world);
                        } catch (SQLException ex) {
                            System.err.println(ex.getMessage());
                        }

                        ResponseUpdateTime responseUpdateTime = new ResponseUpdateTime();
                        responseUpdateTime.setMonth(world.getMonth());
                        responseUpdateTime.setYear(world.getYear());
                        responseUpdateTime.setDuration(Constants.MONTH_DURATION);
                        responseUpdateTime.setRate(gameScale);
                        GameServer.getInstance().addResponseForWorld(world.getID(), responseUpdateTime);

                        for (Player player : world.getPlayers()) {
                            GameServer.getInstance().updateExperience(player, 300);
                            GameServer.getInstance().updateCash(player, 350);
                        }
                    }

                    for (Zone z : zones.values()) {
                        if (z.isEnable()) {
                            if (isNewMonth) {
                                checkBirthList(z, 1.0f, 1.0f);
                                checkDeathList(z, 1.0f, 1.0f);
                            } else if (day % 5 == 0) {
                                checkBirthList(z, 0.05f, 0.1f);
                                checkDeathList(z, 0.05f, 0.1f);
                            } else if (day % 2 == 0) {
                                checkBirthList(z, 0.05f, 0.025f);
                                checkDeathList(z, 0.05f, 0.025f);
                            }

                            if (isNewMonth) {
                                z.updateScore();

                                List<Organism> organismList = new ArrayList<Organism>();
                                organismList.addAll(z.getPlantsByTime(gameScaleTime));
                                organismList.addAll(z.getAnimalsByTime(gameScaleTime));

                                isReady = false;

                                HashMap<Integer, Integer> addNodeList = z.removeAddSpeciesList();
                                z.getRunnable().run(gameScaleTime, z.getCurrentTimeStep(), organismList, addNodeList);

                                for (int node_id : addNodeList.keySet()) {
                                    try {
                                        ZoneNodeAddDAO.removeEntry(z.getID(), node_id);
                                    } catch (SQLException ex) {
                                        System.out.println(ex.getMessage());
                                    }
                                }
                            }
                        }
                    }

                    lastRunTime = currentRunTime;
                }
            }
        }
    }

    private void checkBirthList(Zone zone, float percent, float chance) {
        percent = Math.min(percent, 1.0f);
        HashMap<Integer, Integer[]> birthList = zone.getBirthList();

        if (!birthList.isEmpty()) {
            Random random = new Random();

            for (int species_id : new ArrayList<Integer>(birthList.keySet())) {
                if (random.nextFloat() <= chance) {
                    Integer[] value = birthList.get(species_id);
                    int total = value[0], amount = value[1];

                    int remaining = total - amount;
                    int numBirths = (int) Math.min(Math.ceil(total * percent), remaining);

                    createOrganisms(species_id, zone.getID(), numBirths, Constants.CREATE_STATUS_BIRTH);

                    value[1] += numBirths;

                    try {
                        if (value[1] < value[0]) {
                            BirthListDAO.updateAmount(zone.getID(), species_id, value[1]);
                        } else {
                            birthList.remove(species_id);
                            BirthListDAO.removeEntry(zone.getID(), species_id);
                        }
                    } catch (SQLException ex) {
                        System.err.println(ex.getMessage());
                    }

                    Player player = GameServer.getInstance().getActivePlayer(zone.getEnvironment().getOwnerID());
                    SpeciesType species = GameServer.getInstance().getSpecies(species_id);
                    GameServer.getInstance().updateExperience(player, (int) Math.ceil(species.getCost() * 0.75));
                }
            }
        }
    }

    private void checkDeathList(Zone zone, float percent, float chance) {
        percent = Math.min(percent, 1.0f);        
        HashMap<Integer, Integer[]> deathList = zone.getDeathList();

        if (!deathList.isEmpty()) {
            Random random = new Random();

            for (int species_id : new ArrayList<Integer>(deathList.keySet())) {
                if (random.nextFloat() <= chance) {
                    Integer[] value = deathList.get(species_id);
                    int total = value[0], amount = value[1];

                    int remaining = total - amount;
                    int numDeaths = (int) Math.min(Math.ceil(total * percent), remaining);

                    removeOrganisms(species_id, zone.getID(), numDeaths, Constants.REMOVE_STATUS_DEATH);

                    value[1] += numDeaths;

                    try {
                        if (value[1] < value[0]) {
                            DeathListDAO.updateAmount(zone.getID(), species_id, value[1]);
                        } else {
                            deathList.remove(species_id);
                            DeathListDAO.removeEntry(zone.getID(), species_id);
                        }
                    } catch (SQLException ex) {
                        System.err.println(ex.getMessage());
                    }
                }
            }
        }
    }

    public void updateAnimalTarget(int animalID, int zoneID, int xTarg, int yTarg) {
        Zone zone = zones.get(zoneID);

        if (zone != null) {
            zone.updateAnimalTarget(animalID, xTarg, yTarg);
        }
    }

    public void updateAnimalCoors(int animalID, int zoneID, int xCoor, int yCoor) {
        Zone zone = zones.get(zoneID);

        if (zone != null) {
            zone.updateAnimalCoors(animalID, xCoor, yCoor);
        }
    }
    
    public int getUniqueID() {
        return unique_id++;
    }

    private Organism createOrganism(int species_id, int group_size) {
        return createOrganism(getUniqueID(), species_id, group_size);
    }

    private Organism createOrganism(int organism_id, int species_id, int group_size) {
        Organism organism = null;

        if (species_id / 1000 == 1) {
            organism = new Plant(organism_id);
        } else {
            organism = new Animal(organism_id);
        }

        organism.setSpeciesTypeID(species_id);
        organism.setBiomass(organism.getSpeciesType().getAvgBiomass());
        organism.setGroupSize(group_size);

        return organism;
    }

    public void createOrganisms(int species_id, int zone_id, int amount, short status) {
        Zone zone = zones.get(zone_id);

        if (zone != null) {
            List<Organism> organismList = zone.getOrganismsBySpecies(species_id);

            if (!organismList.isEmpty()) {
                Collections.sort(organismList, OrganismComparator.GroupSizeComparatorASC);
            }

            HashMap<Organism, Integer> numBirthList = new HashMap<Organism, Integer>();

            int size = organismList.size();
            
            for (int i = 0; i < Math.max(Constants.MAX_SPECIES_SIZE, size) && amount > 0; i++) {
                SpeciesType species = GameServer.getInstance().getSpecies(species_id);

                Organism organism = null;
                int numBirths = 0;

                if (i < size) {
                    organism = organismList.get(i);
                    int numSpace = species.getGroupCapacity() - organism.getGroupSize();

                    if (numSpace > 0) {
                        numBirths = Math.min(numSpace, amount);
                        amount -= numBirths;

                        organism.setGroupSize(organism.getGroupSize() + numBirths);
                    }
                } else {
                    numBirths = Math.min(amount, species.getGroupCapacity());
                    amount -= numBirths;

                    organism = createOrganism(species_id, numBirths);
                    organismList.add(organism);
                }

                if (numBirths > 0) {
                    if (numBirthList.containsKey(organism)) {
                        numBirthList.put(organism, numBirthList.get(organism) + numBirths);
                    } else {
                        numBirthList.put(organism, numBirths);
                    }
                }
            }

            if (amount > 0) {
                int numOrganisms = organismList.size();
                int newBirths = amount / numOrganisms, remainder = amount % numOrganisms;

                for (int i = 0; i < numOrganisms && amount > 0; i++) {
                    int numBirths = i < remainder ? newBirths + 1 : newBirths;
                    amount -= numBirths;

                    Organism organism = organismList.get(i);
                    organism.setGroupSize(organism.getGroupSize() + numBirths);

                    if (numBirths > 0) {
                        if (numBirthList.containsKey(organism)) {
                            numBirthList.put(organism, numBirthList.get(organism) + numBirths);
                        } else {
                            numBirthList.put(organism, numBirths);
                        }
                    }
                }
            }

            for (Organism organism : numBirthList.keySet()) {
                createOrganismByResponse(organism, numBirthList.get(organism), zone_id, status, Constants.CREATE_SYSTEM);
            }

//            if (organismList.size() < Constants.MAX_SPECIES_SIZE) {
//                int numFreeSlots = Constants.MAX_SPECIES_SIZE - organismList.size();
//                int groupSize = amount / numFreeSlots, remainder = amount % numFreeSlots;
//
//                for (int i = 0; i < numFreeSlots && amount > 0; i++) {
//                    int numBirths = i < remainder ? groupSize + 1 : groupSize;
//                    amount -= numBirths;
//
//                    Organism organism = createOrganism(species_id, numBirths);
//                    createOrganismByResponse(organism, numBirths, zone_id, status, Constants.CREATE_SYSTEM);
//                }
//            } else {
//                Collections.sort(organismList, OrganismComparator.GroupSizeComparatorASC);
//
//                int numOrganisms = organismList.size();
//                int newBirths = amount / numOrganisms, remainder = amount % numOrganisms;
//
//                for (int i = 0; i < numOrganisms && amount > 0; i++) {
//                    int numBirths = i < remainder ? newBirths + 1 : newBirths;
//                    amount -= numBirths;
//
//                    Organism organism = organismList.get(i);
//                    organism.setGroupSize(organism.getGroupSize() + numBirths);
//                    createOrganismByResponse(organism, numBirths, zone_id, status, Constants.CREATE_SYSTEM);
//                }
//            }
        }
    }

    public void createExistingOrganisms(int species_id, int zone_id, int num_groups, int amount, List<Object[]> groups, short status) {
        int groupSize = amount / num_groups, remainder = amount % num_groups;

        for (int i = 0; i < num_groups && amount > 0; i++) {
            int numBirths = i < remainder ? groupSize + 1 : groupSize;
            amount -= numBirths;

            if (groups != null && i < groups.size()) {
                Object[] group = groups.get(i);
                int group_id = (Integer) group[0];
                float[] position = (float[]) group[1];

                Organism organism = createOrganism(group_id, species_id, numBirths);

                if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                    createOrganismByResponse(organism, numBirths, zone_id, status, position[0], position[1], Constants.CREATE_LOAD);
                } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                    createOrganismByResponse(organism, numBirths, zone_id, status, Constants.CREATE_LOAD);
                }
            } else {
                Organism organism = createOrganism(species_id, numBirths);
                createOrganismByResponse(organism, numBirths, zone_id, status, Constants.CREATE_LOAD);
            }
        }
    }

    public void createOrganismsByBirth(int species_id, int zone_id, int amount) {
        Zone zone = zones.get(zone_id);

        if (zone != null) {
            zone.addOrganismByBirth(species_id, amount);

            try {
                BirthListDAO.createEntry(zone_id, species_id, amount);
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }
        }
    }
    public void createOrganismByResponse(Organism organism, int amount, int zone_id, short status, short type) {
        Random random = new Random();
        createOrganismByResponse(organism, amount, zone_id, status, 3 + random.nextInt(26), 3 + random.nextInt(26), type);
    }

    public void createOrganismByResponse(Organism organism, int amount, int zone_id, short status, float x, float y, short type) {
        Zone zone = zones.get(zone_id);

        if (zone != null) {
            try {
                HashMap<Integer, Integer[]> speciesList = zone.getSpeciesList();

                int species_id = organism.getSpeciesTypeID();
                Integer[] species = speciesList.get(species_id);

                if (species == null) {
                    speciesList.put(species_id, new Integer[]{0, 0});
                    
                    if (type != Constants.CREATE_LOAD) {
                        ZoneSpeciesDAO.createSpecies(zone_id, species_id, 0, 0);
                    }
                }

                Integer[] value = speciesList.get(species_id);

                if (!zone.containsOrganism(organism.getID())) {
                    value[0]++;

                    if (type == Constants.CREATE_USER) {
                        ZoneGroupsDAO.createGroup(zone_id, species_id, x, y, 0);
                    }
                }

                value[1] += amount;

                if (type != Constants.CREATE_LOAD) {
                    ZoneSpeciesDAO.updateSpecies(zone_id, species_id, value[0], value[1]);
                }

                organism.setX(x);
                organism.setY(y);

                organism.setZoneID(zone_id);
                zone.addOrganism(organism, amount, gameScaleTime);

                if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                    ResponseBirthPlant responseBirthPlant = new ResponseBirthPlant();
                    responseBirthPlant.setPlant((Plant) organism);
                    responseBirthPlant.setStatus(status);
                    responseBirthPlant.setCount(amount);

                    GameServer.getInstance().addResponseForWorld(world.getID(), responseBirthPlant);
                } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                    ResponseBirthAnimal responseBirthAnimal = new ResponseBirthAnimal();
                    responseBirthAnimal.setAnimal((Animal) organism);
                    responseBirthAnimal.setStatus(status);
                    responseBirthAnimal.setCount(amount);

                    GameServer.getInstance().addResponseForWorld(world.getID(), responseBirthAnimal);
                }

                if (status == Constants.CREATE_STATUS_BIRTH) {
                    if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                        PlantStatDAO.insertPlantStat(organism.getID(), organism.getSpeciesTypeID(), zone.getCurrentTimeStep(), "Birth", zone.getEnvironment().getEnvironmentScore(), null, zone.getEnvironment().getOwnerID(), zone_id);
                    } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                        AnimalStatDAO.insertAnimalStat(organism.getID(), organism.getSpeciesTypeID(), zone.getCurrentTimeStep(), "Birth", zone.getEnvironment().getEnvironmentScore(), null, zone.getEnvironment().getOwnerID(), zone_id);
                    }
                }
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }
        }
    }
    
    public void removeOrganisms(int species_id, int zone_id, int amount, short status) {
        Zone zone = zones.get(zone_id);

        if (zone != null) {
            List<Organism> organismList = zone.getOrganismsBySpecies(species_id);

            if (!organismList.isEmpty()) {
                Collections.sort(organismList, OrganismComparator.GroupSizeComparatorASC);

                int numOrganisms = organismList.size();

                for (int i = 0; i < numOrganisms && amount > 0; i++) {
                    Organism organism = organismList.get(numOrganisms - 1 - i);

                    int numDeaths = Math.min(organism.getGroupSize(), amount);
                    amount -= numDeaths;

                    Animal predator = zone.findPredator(organism);

                    if (predator != null) {
                        predator.setHungerLevel(1);
                    }

                    removeOrganismByResponse(organism, predator, zone_id, numDeaths, status);
                }
            }
        }
    }

    public void removeOrganismsByDeath(int species_id, int zone_id, int amount) {
        Zone zone = zones.get(zone_id);

        if (zone != null) {
            zone.removeOrganismByDeath(species_id, amount);

            try {
                DeathListDAO.createEntry(zone_id, species_id, amount);
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }
        }
    }

    public void removeOrganismByResponse(Organism organism, Animal predator, int zone_id, int amount, short status) {
        Zone zone = zones.get(zone_id);

        if (zone != null) {
            try {
                zone.removeOrganism(organism, amount, gameScaleTime);

                HashMap<Integer, Integer[]> speciesList = zone.getSpeciesList();

                int species_id = organism.getSpeciesTypeID();
                Integer[] value = speciesList.get(species_id);

                if (!zone.containsOrganism(organism.getID())) {
                    value[0]--;

                    ZoneGroupsDAO.removeGroup(organism.getID());
                }

                value[1] -= amount;
                ZoneSpeciesDAO.updateSpecies(zone_id, species_id, value[0], value[1]);

                if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                    ResponseKillPlant responseKillPlant = new ResponseKillPlant();
                    responseKillPlant.setPlantID(organism.getID());
                    responseKillPlant.setCount(amount);
                    responseKillPlant.setPredatorID(predator != null ? predator.getID() : 0);

                    GameServer.getInstance().addResponseForWorld(world.getID(), responseKillPlant);
                } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                    ResponseKillAnimal responseKillAnimal = new ResponseKillAnimal();
                    responseKillAnimal.setAnimalID(organism.getID());
                    responseKillAnimal.setCount(amount);
                    responseKillAnimal.setPredatorID(predator != null ? predator.getID() : 0);

                    GameServer.getInstance().addResponseForWorld(world.getID(), responseKillAnimal);
                }

                if (status == Constants.REMOVE_STATUS_DEATH) {
                    String message = predator != null ? "Eaten" : "Death";

                    if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                        PlantStatDAO.insertPlantStat(organism.getID(), organism.getSpeciesTypeID(), zone.getCurrentTimeStep(), message, zone.getEnvironment().getEnvironmentScore(), message, zone.getEnvironment().getOwnerID(), zone.getID());
                    } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                        AnimalStatDAO.insertAnimalStat(organism.getID(), organism.getSpeciesTypeID(), zone.getCurrentTimeStep(), message, zone.getEnvironment().getEnvironmentScore(), message, zone.getEnvironment().getOwnerID(), zone.getID());
                    }
                }
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }
        }
    }

    public short buyOrganism(int organism_type, int player_id, int species_id, int amount, int zone_id, float xCoor, float yCoor) {
        Player player = GameServer.getInstance().getActivePlayer(player_id);
        Avatar avatar = player.getAvatar();

        if (avatar != null) {
            SpeciesType species = null;

            if (organism_type == Constants.ORGANISM_TYPE_PLANT) {
                species = GameServer.getInstance().getPlantType(species_id);
            } else if (organism_type == Constants.ORGANISM_TYPE_ANIMAL) {
                species = GameServer.getInstance().getAnimalType(species_id);
            }

            boolean canBuy = avatar.spendCash(species.getCost());

            if (canBuy) {
                GameServer.getInstance().updateCash(player, 0);

                Zone zone = zones.get(zone_id);

                if (zone != null) {
                    Organism organism = createOrganism(species_id, amount);

                    for (int node_id : organism.getSpeciesType().getNodeList()) {
                        zone.addNewNode(node_id, amount * organism.getSpeciesType().getNodeAmount(node_id));
                    }

                    createOrganismByResponse(organism, organism.getGroupSize(), zone_id, Constants.CREATE_STATUS_PURCHASE, xCoor, yCoor, Constants.CREATE_USER);

                    try {
                        if (organism_type == Constants.ORGANISM_TYPE_PLANT) {
                            PlantStatDAO.insertPlantStat(organism.getID(), species_id, currentMonth, "Purchase", world.getEnvByUserID(player_id).getEnvironmentScore(), null, player_id, zone_id);
                        } else if (organism_type == Constants.ORGANISM_TYPE_ANIMAL) {
                            AnimalStatDAO.insertAnimalStat(organism.getID(), species_id, currentMonth, "Purchase", world.getEnvByUserID(player_id).getEnvironmentScore(), null, player_id, zone_id);
                        }

                        for (int node_id : species.getNodeList()) {
                            UserActionsDAO.createAction(zone.getManipulationID(), zone.getCurrentTimeStep(), 0, node_id, GameServer.getInstance().getSpeciesTypeByNodeID(node_id).getAvgBiomass() * organism.getGroupSize());
                        }
                    } catch (SQLException ex) {
                        System.err.println(ex.getMessage());
                    }

                    GameServer.getInstance().updateExperience(player, species.getCost() * 2);

                    return 0;
                }
            }
        }

        return 1;
    }

    public boolean buyResearch(int avatarID, boolean useAbilityPoint, int researchID, int zoneID) {
        return false;
    }

    public boolean buyVaccine(int avatarID, boolean useAbilityPoint, int vaccineID, int zoneID) {
        return false;
    }

    public boolean updateGameScaleVote(int avatarID, int gameScaleVote) {
//        Avatar avatar = avatars.get(avatarID);
//
//        if (avatar != null && avatar.setGameScaleVote(gameScaleVote)) {
//            updateGameScale();
//            return true;
//        }
        return false;
    }

    private void updateGameScale() {
//        int numAvatars = avatars.size();
//        int totalVotes = 0;
//
//        for (Avatar avatar : avatars.values()) {
//            totalVotes += avatar.getGameScaleVote();
//        }
//
//        if (gameMode == Constants.GAME_TYPE_PVP) {
//            gameScale = (int) (288 * ((double) totalVotes / (double) numAvatars));
//        } else {
//            gameScale = (int) (36 * ((double) totalVotes / (double) numAvatars));
//        }
    }

    public void end() {
        for (Zone zone : zones.values()) {
            if (zone.isEnable()) {
                zone.stopTimeActiveTimer();
                zone.removeRunnable();
            }
        }
    }
}
