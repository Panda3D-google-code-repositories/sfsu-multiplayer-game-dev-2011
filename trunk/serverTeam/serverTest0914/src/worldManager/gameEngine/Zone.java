package worldManager.gameEngine;

import core.GameServer;

import dataAccessLayer.ParamTableDAO;
import dataAccessLayer.ScoreCSVDAO;
import dataAccessLayer.ZoneNodeAddDAO;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

import metadata.Constants;

import model.Environment;
import model.Player;
import model.SpeciesType;

import networking.response.ResponseChartBiomass;

import simulationEngine.SimulationEngine;

import utility.GameTimer;
import utility.GameTimerCollection;

import worldManager.gameEngine.species.Animal;
import worldManager.gameEngine.species.Plant;
import worldManager.gameEngine.species.Organism;

/**
 *
 * @author KeithKong
 */
public class Zone {

    private int zone_id;
    private int order;
    private int env_id;
    private int row;
    private int column;
    private int type;
    private int environmentScore;
    private String manipulationID;
    private int currentTimeStep;
    private SimulationEngine simulationEngine;
    private long lastSimulationTime;
    private HashMap<Integer, Animal> animals;
    private HashMap<Integer, Plant> plants;
    private WaterSource waterSource;
    private GameEngine gameEngine;
    private boolean isEnable;
    private HashMap<Integer, Integer> totalSpeciesList;
    private float max_biomass;
    private GameTimer timeActiveTimer;
    private float totalBiomass;
    private Environment env;
    private HashMap<Short, Float> parametersList;
    private int daysCollapsed;
    private HashMap<Integer, Long> organismTimeAddedList;
    private ZoneRunnable zoneRunnable;
    private HashMap<Integer, Integer[]> birthList;
    private HashMap<Integer, Integer[]> deathList;
    private float prevBiomass;
    private HashMap<Integer, Integer[]> speciesList;
    private HashMap<Integer, Integer> addNodeList;
    private String score_csv;

    public Zone(int zone_id) {
        this.zone_id = zone_id;
        manipulationID = "";

        simulationEngine = new SimulationEngine();

        animals = new HashMap<Integer, Animal>();
        plants = new HashMap<Integer, Plant>();

        totalSpeciesList = new HashMap<Integer, Integer>();

        timeActiveTimer = new GameTimer();
        parametersList = new HashMap<Short, Float>();

        organismTimeAddedList = new HashMap<Integer, Long>();

        birthList = new HashMap<Integer, Integer[]>();
        deathList = new HashMap<Integer, Integer[]>();

        speciesList = new HashMap<Integer, Integer[]>();
        addNodeList = new HashMap<Integer, Integer>();
    }

    public int getID() {
        return zone_id;
    }

    public int setID(int zone_id) {
        return this.zone_id = zone_id;
    }

    public int getOrder() {
        return order;
    }

    public int setOrder(int order) {
        return this.order = order;
    }

    public int getEnvID() {
        return env_id;
    }

    public int setEnvID(int env_id) {
        return this.env_id = env_id;
    }

    public Environment getEnvironment() {
        return this.env;
    }

    public Environment setEnvironment(Environment env) {
        return this.env = env;
    }

    public int getCurrentTimeStep() {
        return currentTimeStep;
    }

    public int setCurrentTimeStep(int currentTimeStep) {
        return this.currentTimeStep = currentTimeStep;
    }

    public SimulationEngine getSimulationEngine() {
        return simulationEngine;
    }

    public SimulationEngine setSimulationEngine(SimulationEngine simulationEngine) {
        return this.simulationEngine = simulationEngine;
    }

    public long getLastSimulationTime() {
        return lastSimulationTime;
    }

    public long setLastSimulationTime(long lastSimulationTime) {
        return this.lastSimulationTime = lastSimulationTime;
    }

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }

    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }

    public int getType() {
        return type;
    }

    public int setType(int type) {
        return this.type = type;
    }

    public String getScoreCSV() {
        return this.score_csv;
    }

    public String setScoreCSV(String score_csv) {
        return this.score_csv = score_csv;
    }

    public String getManipulationID() {
        return manipulationID;
    }

    public String setManipulationID(String manipulationID) {
        isEnable = !manipulationID.isEmpty();
        return this.manipulationID = manipulationID;
    }

    public int getTotalSpeciesCount(int species_type_id) {
        return totalSpeciesList.get(species_type_id);
    }

    public HashMap<Integer, Integer[]> getBirthList() {
        return birthList;
    }

    public HashMap<Integer, Integer[]> setBirthList(HashMap<Integer, Integer[]> birthList) {
        return this.birthList = birthList;
    }

    public HashMap<Integer, Integer[]> getDeathList() {
        return deathList;
    }

    public HashMap<Integer, Integer[]> setDeathList(HashMap<Integer, Integer[]> deathList) {
        return this.deathList = deathList;
    }
    
    public HashMap<Integer, Integer[]> getSpeciesList() {
        return speciesList;
    }
    
    public HashMap<Integer, Integer> getAddSpeciesList() {
        return addNodeList;
    }

    public HashMap<Integer, Integer> removeAddSpeciesList() {
        HashMap<Integer, Integer> nodeList = addNodeList;
        addNodeList = new HashMap<Integer, Integer>();
        return nodeList;
    }
    
    public void setAddNodeList(HashMap<Integer, Integer> addNodeList) {
        this.addNodeList = addNodeList;
    }

    public void addNewNode(int node_id, int amount) {
        try {
            if (addNodeList.containsKey(node_id)) {
                addNodeList.put(node_id, addNodeList.get(node_id) + amount);

                ZoneNodeAddDAO.updateAmount(zone_id, node_id, addNodeList.get(node_id));
            } else {
                addNodeList.put(node_id, amount);

                ZoneNodeAddDAO.createEntry(zone_id, node_id, amount);
            }
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void addOrganismByBirth(int species_id, int amount) {
        birthList.put(species_id, new Integer[]{amount, 0});
    }
    
    public void removeOrganismByDeath(int species_id, int amount) {
        deathList.put(species_id, new Integer[]{amount, 0});
    }

    public boolean containsOrganism(int organism_id) {
        return plants.containsKey(organism_id) || animals.containsKey(organism_id);
    }

    public List<Animal> getAnimals() {
        return new ArrayList<Animal>(animals.values());
    }

    public List<Organism> getAnimalsByType(int animal_type_id) {
        List<Organism> animalList = new ArrayList<Organism>();

        for (Animal animal : animals.values()) {
            if (animal.getSpeciesTypeID() == animal_type_id) {
                animalList.add(animal);
            }
        }

        return animalList;
    }

    public List<Animal> getAnimalsByTime(long gameScaleTime) {
        List<Animal> animalList = new ArrayList<Animal>();

        for (int organism_id : organismTimeAddedList.keySet()) {
            if (organismTimeAddedList.get(organism_id) <= gameScaleTime && animals.containsKey(organism_id)) {
                animalList.add(animals.get(organism_id));
            }
        }

        return animalList;
    }

    public List<Plant> getPlants() {
        return new ArrayList<Plant>(plants.values());
    }

    public List<Organism> getPlantsByType(int plant_type_id) {
        List<Organism> plantList = new ArrayList<Organism>();

        for (Plant plant : plants.values()) {
            if (plant.getSpeciesTypeID() == plant_type_id) {
                plantList.add(plant);
            }
        }

        return plantList;
    }

    public List<Organism> getPlantsByTime(long gameScaleTime) {
        List<Organism> plantList = new ArrayList<Organism>();

        for (int organism_id : organismTimeAddedList.keySet()) {
            if (organismTimeAddedList.get(organism_id) <= gameScaleTime && plants.containsKey(organism_id)) {
                plantList.add(plants.get(organism_id));
            }
        }

        return plantList;
    }
    
    public List<Organism> getOrganisms() {
        List<Organism> organismList = new ArrayList<Organism>();
        organismList.addAll(plants.values());
        organismList.addAll(animals.values());

        return organismList;
    }

    public List<Organism> getOrganismsBySpecies(int species_id) {
        List<Organism> organismList = new ArrayList<Organism>();

        for (Animal animal : animals.values()) {
            if (animal.getSpeciesTypeID() == species_id) {
                organismList.add(animal);
            }
        }

        for (Plant plant : plants.values()) {
            if (plant.getSpeciesTypeID() == species_id) {
                organismList.add(plant);
            }
        }

        return organismList;
    }

    public void addOrganism(Organism organism, int count, long gameScaleTime) {
        for (int node_id : organism.getSpeciesType().getNodeList()) {
            SpeciesType species = GameServer.getInstance().getSpeciesTypeByNodeID(node_id);

            if (species != null) {
                int amount = count * species.getNodeAmount(node_id);
                setTotalBiomass((float) (totalBiomass + species.getAvgBiomass() * amount));
            }
        }

        organismTimeAddedList.put(organism.getID(), gameScaleTime);

        if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
            plants.put(organism.getID(), (Plant) organism);
        } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
            animals.put(organism.getID(), (Animal) organism);
        }

        int species_id = organism.getSpeciesTypeID();
        Integer total = totalSpeciesList.get(species_id);

        if (total == null) {
            totalSpeciesList.put(species_id, count);
        } else {
            totalSpeciesList.put(species_id, total + count);
        }

        updateEnvironmentScore();
    }

    public void removeOrganism(Organism organism, int count, long gameScaleTime) {
        for (int node_id : organism.getSpeciesType().getNodeList()) {
            SpeciesType species = GameServer.getInstance().getSpeciesTypeByNodeID(node_id);

            if (species != null) {
                int amount = count * species.getNodeAmount(node_id);
                setTotalBiomass((float) Math.max(0, totalBiomass - species.getAvgBiomass() * amount));
            }
        }

        organism.setGroupSize(organism.getGroupSize() - count);

        if (organism.getGroupSize() == 0) {
            if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                plants.remove(organism.getID());
            } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                animals.remove(organism.getID());
            }

            organismTimeAddedList.remove(organism.getID());
        }

        int species_id = organism.getSpeciesTypeID();
        totalSpeciesList.put(species_id, Math.max(0, totalSpeciesList.get(species_id) - count));

        updateEnvironmentScore();
    }

    public WaterSource getWaterSource() {
        return this.waterSource;
    }

    public WaterSource setWaterSource(WaterSource waterSource) {
        return this.waterSource = waterSource;
    }

    public void updateScore() {
        updateEnvironmentScore();

        try {
            score_csv += "\n" + currentTimeStep + "," + environmentScore;
            ScoreCSVDAO.createCSV(zone_id, score_csv);

            ResponseChartBiomass responseChartBiomass = new ResponseChartBiomass();
            responseChartBiomass.setType((short) 2);
            responseChartBiomass.setCSV(score_csv);

            GameServer.getInstance().addResponseForUser(env.getOwnerID(), responseChartBiomass);
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
        }

        if (env != null) {
            env.updateAccumEnvScore();
        }
    }

    private void updateEnvironmentScore() {
        double biomass = 0;

        for (int speciesTypeID : totalSpeciesList.keySet()) {
            SpeciesType speciesType = null;

            if (speciesTypeID > Constants.MODIFIER_PLANT) {
                speciesType = GameServer.getInstance().getPlantType(speciesTypeID);
            } else {
                speciesType = GameServer.getInstance().getAnimalType(speciesTypeID);
            }

            biomass += speciesType.getAvgBiomass() * Math.pow(totalSpeciesList.get(speciesTypeID), speciesType.getTrophicLevel());
        }

        if (biomass > 0) {
            biomass = Math.round(Math.log(biomass) / Math.log(2)) * 5;
        }

        environmentScore = (int) Math.round(Math.pow(biomass, 2) + Math.pow(totalSpeciesList.size(), 2));

        if (env != null) {
            env.updateEnvironmentScore();
        }
    }

    public int getEnvironmentScore() {
        return environmentScore;
    }
    
    public float getPrevBiomass() {
        return prevBiomass;
    }
    
    public float setPrevBiomass(float prevBiomass) {
        return this.prevBiomass = prevBiomass;
    }

    public float getMaxBiomass() {
        return max_biomass;
    }

    public float setMaxBiomass(float max_biomass) {
        return this.max_biomass = max_biomass;
    }

    public float getTotalBiomass() {
        return totalBiomass;
    }

    public void setTotalBiomass(float totalBiomass) {
        this.totalBiomass = totalBiomass;

        max_biomass = Math.max(max_biomass, totalBiomass);

        if (totalBiomass >= max_biomass && totalBiomass >= 1000) {
            if (String.valueOf((int) totalBiomass).length() > String.valueOf((int) max_biomass).length()) {
                Player player = GameServer.getInstance().getActivePlayer(gameEngine.getWorld().getEnvByID(env_id).getOwnerID());
                GameServer.getInstance().updateExperience(player, 1000);
            }
        }
    }

    public Animal findPredator(Organism organism) {
        Animal predator = null;

        int species_id = organism.getSpeciesType().getID();
        double distance = -1;

        List<Animal> predatorList = getAnimals();
        Collections.shuffle(predatorList);

        for (Animal animal : predatorList) {
            if (animal.getID() != organism.getID() && (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT || animal.getHungerLevel() < 1.0f)) {
                List<Integer> preyList = null;

                if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                    preyList = animal.getSpeciesType().getPreyIDs(Constants.ORGANISM_TYPE_PLANT);
                } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                    preyList = animal.getSpeciesType().getPreyIDs(Constants.ORGANISM_TYPE_ANIMAL);
                }

                if (preyList != null) {
                    for (int prey_id : preyList) {
                        if (prey_id == species_id) {
                            double temp = Math.sqrt(Math.pow(animal.getX() - organism.getX(), 2) + Math.pow(animal.getY() - organism.getY(), 2));

                            if (distance == -1 || temp < distance) {
                                distance = temp;
                                predator = animal;
                            }
                        }
                    }
                }
            }
        }

        return predator;
    }

    public HashMap<Short, Float> getParameters() {
        return parametersList;
    }

    public HashMap<Short, Float> setParameters(HashMap<Short, Float> parametersList) {
        return this.parametersList = parametersList;
    }

    public void modifyParameters(HashMap<Short, Float> parametersList) {
        if (isEnable) {
            System.out.println("Modifying Parameters, User ID: " + env.getOwnerID());
            this.parametersList = parametersList;
            simulationEngine.setParameters(currentTimeStep, manipulationID, parametersList);

            try {
                ParamTableDAO.updateParameters(zone_id, parametersList);
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }
        }
    }
    
    public void modifyFunctionalParameters(HashMap<Short, Float> parametersList,int parameterType, int predatorID) {
        if (isEnable) {
            System.out.println("Modifying Parameters, User ID: " + env.getOwnerID());
            this.parametersList = parametersList;
            simulationEngine.setFunctionalParameters(currentTimeStep, manipulationID, parametersList,parameterType,predatorID);

//            try {
//                ParamTableDAO.updateParameters(zone_id, parametersList);
//            } catch (SQLException ex) {
//                System.err.println(ex.getMessage());
//            }
        }
    }    

    public void updateAnimalTarget(int animalID, int xTarg, int yTarg) {
        Animal animal = animals.get(animalID);

        if (animal != null) {
            animal.setTargetPos(xTarg, yTarg, 0);
        }
    }

    public void updateAnimalCoors(int animalID, int xCoor, int yCoor) {
        Animal animal = animals.get(animalID);

        if (animal != null) {
            animal.setPos(xCoor, yCoor, 0);
        }
    }
    
    public ZoneRunnable createRunnable() {
        return zoneRunnable = new ZoneRunnable(this, gameEngine, simulationEngine, manipulationID);
    }
    
    public ZoneRunnable getRunnable() {
        return zoneRunnable;
    }

    public void removeRunnable() {
        zoneRunnable.end();
    }
    
    public HashMap<Integer, Integer> getTotalSpeciesList() {
        return totalSpeciesList;
    }
    
    public int getDaysCollapsed() {
        return daysCollapsed;
    }
    
    public int setDaysCollapsed(int days) {
        return this.daysCollapsed = days;
    }

    public GameEngine getGameEngine() {
        return gameEngine;
    }

    public GameEngine setGameEngine(GameEngine gameEngine) {
        return this.gameEngine = gameEngine;
    }

    public boolean isEnable() {
        return isEnable;
    }

    public boolean setEnable(boolean status) {
        return this.isEnable = status;
    }

    public void startTimeActiveTimer() {
        Player player = GameServer.getInstance().getActivePlayer(gameEngine.getWorld().getEnvByID(env_id).getOwnerID());
        timeActiveTimer.schedule(new GameTimerCollection.ZoneTimeTimer(player, this), 60000, 60000);
    }

    public boolean stopTimeActiveTimer() {
        return timeActiveTimer.end();
    }

    public void restart() {
//        for (Animal animal : new ArrayList<Animal>(animals.values())) {
//            gameEngine.removeOrganism(animal, null, zone_id, animal.getGroupSize());
//        }
//
//        for (Plant plant : new ArrayList<Plant>(plants.values())) {
//            gameEngine.removeOrganism(plant, null, zone_id, plant.getGroupSize());
//        }

        totalSpeciesList.clear();

        parametersList.put(Constants.PARAMETER_K, 1000.f);
        parametersList.put(Constants.PARAMETER_R, 1.f);
        parametersList.put(Constants.PARAMETER_X, 0.5f);
        parametersList.put(Constants.PARAMETER_X_A, 0.5f);
        parametersList.put(Constants.PARAMETER_E, 1.f);
        parametersList.put(Constants.PARAMETER_A, 0.f);
        parametersList.put(Constants.PARAMETER_Q, 0.f);
        parametersList.put(Constants.PARAMETER_D, 0.f);

        try {
            ParamTableDAO.updateParameters(zone_id, parametersList);
        } catch (SQLException ex) {
            System.err.println(ex.getMessage());
        }

        stopTimeActiveTimer();
        startTimeActiveTimer();

        environmentScore = 0;
        currentTimeStep = 1;

        max_biomass = 0;
        totalBiomass = 0;

        daysCollapsed = 0;
    }
}