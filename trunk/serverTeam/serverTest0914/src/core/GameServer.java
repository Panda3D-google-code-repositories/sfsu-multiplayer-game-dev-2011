package core;

import configuration.GameServerConf;

import dataAccessLayer.AnimalTypeDAO;
import dataAccessLayer.AvatarDAO;
import dataAccessLayer.DAO;
import dataAccessLayer.PlantTypeDAO;
import dataAccessLayer.NatureControllerTypeDAO;
import dataAccessLayer.ShopDAO;

import java.io.IOException;
import java.net.Socket;
import java.net.ServerSocket;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Set;

import metadata.Constants;
import metadata.GameRequestTable;

import model.AnimalType;
import model.Avatar;
import model.Environment;
import model.PlantType;
import model.Player;
import model.PvEWorldMap;
import model.PvPWorldMap;
import model.SpeciesType;
import model.World;

import networking.response.GameResponse;
import networking.response.ResponseShopUnlock;
import networking.response.ResponseUpdateCash;
import networking.response.ResponseUpdateLevel;
import networking.response.ResponseUpdateXP;

import utility.ConfFileParser;
import utility.ExpTable;

import worldManager.gameEngine.GameEngine;
import worldManager.gameEngine.DiseaseType;
import worldManager.gameEngine.NatureControllerType;

/**
 * This class is the entry of Beast Reality Game Server. It does configurations and then runs.
 *
 * @author , Xuyuan
 */
public class GameServer {

    protected static GameServer gameServer;
    protected GameServerConf configuration;
    protected boolean ready = false;
    protected HashMap<Long, GameClient> activeThreads = new HashMap<Long, GameClient>();//All active threads(game clients).
    protected HashMap<Integer, Player> activePlayers = new HashMap<Integer, Player>();
    protected HashMap<Integer, World> activePvPWorld = new HashMap<Integer, World>();
    protected HashMap<Integer, World> activePvEWorld = new HashMap<Integer, World>();
    protected HashMap<Integer, PvEWorldMap> pveWorldMaps = new HashMap<Integer, PvEWorldMap>();
    protected HashMap<Integer, PvPWorldMap> pvpWorldMaps = new HashMap<Integer, PvPWorldMap>();
    protected HashMap<Integer, Integer> playerPositionTracker = new HashMap<Integer, Integer>();//Track the current position of player (0=MainLobby;1=pvpGameModeLobby;2=pveGameModeLobby)
    protected HashMap<Integer, GameEngine> activeGameEngine = new HashMap<Integer, GameEngine>();// Key is the world id, value is the game engine reference.
    protected HashMap<Integer, DiseaseType> diseaseTypes = new HashMap<Integer, DiseaseType>();
    protected HashMap<Integer, AnimalType> animalTypes = new HashMap<Integer, AnimalType>();
    protected static HashMap<Integer, AnimalType> animalNames = new HashMap<Integer, AnimalType>();
    protected static HashMap<Integer, PlantType> plantNames = new HashMap<Integer, PlantType>();
    protected HashMap<Integer, PlantType> plantTypes = new HashMap<Integer, PlantType>();
    protected HashMap<String, NatureControllerType> natureControllerTypes = new HashMap<String, NatureControllerType>();
    
    /*
     * Initiate the game server.
     */
    public GameServer() throws SQLException {
        configuration = new GameServerConf();

        GameRequestTable.init();
        ExpTable.init();

        if (DAO.getInstance() == null) {
            System.exit(-1);
        }

        System.out.println("Loading Plant Types...");
        for (PlantType plant : PlantTypeDAO.getPlants()) {
            plantTypes.put(plant.getID(), plant);
            plantNames.put(plant.getID(), plant);
        }

        System.out.println("Loading Animal Types...");
        for (AnimalType animal : AnimalTypeDAO.getAnimals(new int[]{54, 58, 62, 76, 78, 79, 81, 84})) {
            animalTypes.put(animal.getID(), animal);
            animalNames.put(animal.getID(), animal);
        }

        System.out.println("Resolving Predators...");
        for (PlantType plant : plantTypes.values()) {
            for (int predator_id : plant.getPredatorIDs(Constants.ORGANISM_TYPE_ANIMAL)) {
                if (animalTypes.containsKey(predator_id)) {
                    plant.resolvePredator(animalTypes.get(predator_id));
                }
            }
        }

        for (AnimalType animal : animalTypes.values()) {
            for (int predator_id : animal.getPredatorIDs(Constants.ORGANISM_TYPE_ANIMAL)) {
                if (animalTypes.containsKey(predator_id)) {
                    animal.resolvePredator(animalTypes.get(predator_id));
                }
            }
        }

        System.out.println("Resolving Preys...");
        for (AnimalType animal : animalTypes.values()) {
            for (int prey_id : animal.getPreyIDs(Constants.ORGANISM_TYPE_ANIMAL)) {
                if (animalTypes.containsKey(prey_id)) {
                    animal.resolvePrey(animalTypes.get(prey_id));
                }
            }

            for (int prey_id : animal.getPreyIDs(Constants.ORGANISM_TYPE_PLANT)) {
                if (plantTypes.containsKey(prey_id)) {
                    animal.resolvePrey(plantTypes.get(prey_id));
                }
            }
        }

        System.out.println("Loading Nature Controller Types...");
        for (NatureControllerType natureController : NatureControllerTypeDAO.getAllNatureController()) {
            natureControllerTypes.put(natureController.getEcosystemType(), natureController);
        }

        System.out.println();
        
    }

    public NatureControllerType getNatureControllerType(String type) {
        return natureControllerTypes.get(type);
    }

    public DiseaseType getDiseaseType(int diseaseTypeID) {
        return diseaseTypes.get(diseaseTypeID);
    }

    public List<AnimalType> getAnimalTypes() {
        return new ArrayList<AnimalType>(animalTypes.values());
    }

    public AnimalType getAnimalType(int animalTypeID) {
        return animalTypes.get(animalTypeID);
    }
    
    public static String getAnimalName(int animalTypeID) {
    	if(animalNames.get(animalTypeID) == null){
    		return null;
    	}
        return animalNames.get(animalTypeID).getSpeciesName();
    }
    
    public static String getPlantName(int plantTypeID) {
    	if(plantNames.get(plantTypeID) == null){
    		return null;
    	}
        return plantNames.get(plantTypeID).getSpeciesName();
    }

    public List<PlantType> getPlantTypes() {
        return new ArrayList<PlantType>(plantTypes.values());
    }

    public PlantType getPlantType(int plantTypeID) {
        return plantTypes.get(plantTypeID);
    }

    public SpeciesType getSpecies(int species_id) {
        SpeciesType species = null;

        if (plantTypes.containsKey(species_id)) {
            species = plantTypes.get(species_id);
        } else if (animalTypes.containsKey(species_id)) {
            species = animalTypes.get(species_id);
        }

        return species;
    }

    public SpeciesType getSpeciesTypeByNodeID(int node_id) {
        return getSpeciesTypeByNodeList(new int[]{node_id});
    }

    public SpeciesType getSpeciesTypeByNodeList(int[] nodeList) {
        for (AnimalType animal : animalTypes.values()) {
            if (animal.equalsNodeList(nodeList)) {
                return (SpeciesType) animal;
            }
        }

        for (PlantType plant : plantTypes.values()) {
            if (plant.equalsNodeList(nodeList)) {
                return (SpeciesType) plant;
            }
        }

        return null;
    }

    /**
     * Create the game engine of a world and put it in the game engine list.
     *
     * @param worldID           The id of the world of the game engine.
     */
    public GameEngine createGameEngine(World world) {
        GameEngine gameEngine = new GameEngine(world);
        activeGameEngine.put(world.getID(), gameEngine);
        return gameEngine;
    }

    /**
     * Delete the game engine of a world from the game engine list.
     *
     * @param worldID           The id of the world of the game engine.
     */
    public GameEngine deleteGameEngine(int worldID) {
        return activeGameEngine.remove(worldID);
    }

    /*
     * Configure the game server by reading from file conf/gameServer.conf.
     */
    private void configure() {
        ConfFileParser confFileParser = new ConfFileParser("conf/gameServer.conf");
        configuration.setConfRecords(confFileParser.parse());
    }

    /*
     * Get ready by starting the configuration process and setting ready flag.
     */
    private void getReady() {
        configure();
        ready = true;
    }

    private boolean isReady() {
        return ready;
    }

    /*
     * Run the game server.
     */
    private void run() {
        ServerSocket listenSocket;
        int serverPort = configuration.getPortNumber();

        try {
            //Start to listen on a certain port.
            listenSocket = new ServerSocket(serverPort);
            System.out.println("Server has started on port:" + listenSocket.getLocalPort());
            System.out.println("Waiting for clients...");

            while (true) {
                try {
                    //A clientSocket will represent a connection between the client and this server.
                    Socket clientSocket = listenSocket.accept();
                    System.out.println("A Connection Established!");

                    //Create a client on a thread and pass the clientSocket to it.
                    GameClient client = new GameClient(clientSocket, this);
                    client.start();
                } catch (IOException e) {
                    System.out.println(e.getMessage());
                }
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    /** fine
     * Inspect all the GameClient threads.
     *
     */
    public void printAllGameClientThreads() {
        System.out.println("******All GameClient Threads Start******");
        for (Long key : activeThreads.keySet()) {
            GameClient aClient = activeThreads.get(key);
            aClient.toString();
        }

        System.out.println("******All GameClient Threads End******");
    }

    /** fine
     * Inspect the position of all the online players
     *
     */
    public void printAllPlayersTrackingInfo() {
        System.out.println("********All Players' Tracking info Start*******");
        for (Integer key : playerPositionTracker.keySet()) {
            System.out.print(key + "   :   ");
            System.out.println(playerPositionTracker.get(key));
        }
        System.out.println("********All Players' Tracking info End*******");
    }

    /** fine
     * Inspect all the active PvP Worlds
     * 
     */
    public void printAllActivePvPWorlds() {
        System.out.println("********All the active PvP Worlds Start*******");
        for (Integer key : activePvPWorld.keySet()) {
            World pvpWorld = activePvPWorld.get(key);
            pvpWorld.toString();
        }
        System.out.println("********All the active PvP Worlds End*******");
    }

    /** fine
     * Inspect all the world maps
     *
     */
    public void printAllMaps() {
        System.out.println("********All maps start**********");
        System.out.println("All PvP maps====================");
        for (Integer key : pvpWorldMaps.keySet()) {
            PvPWorldMap pvpMap = pvpWorldMaps.get(key);
            pvpMap.printObject();
        }

        System.out.println("All PvE maps====================");
        for (Integer key : pveWorldMaps.keySet()) {
            PvEWorldMap pveMap = pveWorldMaps.get(key);
            pveMap.toString();
        }
        System.out.println("********All maps end**********");
    }

    /** fine
     * Get the GameClient thread for the player with the id of playerID
     *
     * @param playerID		the id of the player 
     * @return		 	the GameClient thread
     */
    public GameClient getThreadByPlayerID(int playerID) {
        for (GameClient aClient : activeThreads.values()) {
            if (aClient.getPlayer().getID() == playerID) {
                return aClient;
            }
        }

        return null;
    }

    public GameClient getThreadByAvatarID(int avatarID) {
        for (GameClient aClient : activeThreads.values()) {
            if (aClient.getAvatar().getID() == avatarID) {
                return aClient;
            }
        }

        return null;
    }

    /**
     * Get the GameClient thread by username.
     *
     * @param username          The username of the player who has that thread.
     * @return                  The target GameClient thread.
     */
    public GameClient getThreadByPlayerUserName(String userName) {
        for (GameClient aClient : activeThreads.values()) {
            if (aClient.getPlayer().getUsername().equals(userName)) {
                return aClient;
            }
        }

        return null;
    }

    public int getNumberOfCurrentThreads() {
        return activeThreads.size();
    }

    /**
     * Get the GameClient thread by team.
     *
     * @param pvpWorldID            The id of the PvP world.
     * @param teamID                The id of the team in that PvP world.
     * @return                      The list of the GameClient threads which are in that team of that PvP world.
     *
     */
    public List<GameClient> getThreadsByTeam(int pvpWorldID, int teamID) {
        List<GameClient> clients = new ArrayList<GameClient>();

        Set<Integer> keySet = activePvPWorld.keySet();
        for (Integer key : keySet) {
            World pvpWorld = activePvPWorld.get(key);
            if (pvpWorld.getID() == pvpWorldID) {
                for (Environment env : pvpWorld.getEnvironments()) {
//                    if (env.getAvatar().getTeamNo() == teamID) {
//                        int userID = env.getAvatar().getPlayer().getID();
//                        GameClient client = getThreadByPlayerID(userID);
//                        clients.add(client);
//                    }
                }
            }
        }

        return clients;
    }

    /**
     * Get the threads of all the players in the world
     *
     * @param worldID           The id of the world
     * @return                  The list of threads of the players in the world
     */
    public List<GameClient> getClientsByWorld(int worldID) {
        List<GameClient> clients = new ArrayList<GameClient>();
        
        for (GameClient client : activeThreads.values()) {
            if (client.getWorld() != null) {
                if (client.getWorld().getID() == worldID) {
                    clients.add(client);
                }
            }
        }

        return clients;
    }

    public void addToActiveThreads(GameClient client) {
        activeThreads.put(client.getId(), client);
    }
    
    public List<Player> getActivePlayers() {
        return new ArrayList<Player>(activePlayers.values());
    }

    public Player getActivePlayer(int player_id) {
        return activePlayers.get(player_id);
    }

    public void setActivePlayer(Player player) {
        activePlayers.put(player.getID(), player);
    }
    
    public void removeActivePlayer(int player_id) {
        activePlayers.remove(player_id);
    }
    
    public static String removeNodesFromCSV(String csv) {
        String[] tempCSV = csv.split("\n");
        String[] nameList = tempCSV[0].split(",\"");

        for (int i = 1; i < nameList.length; i++) {
            String name = nameList[i];
            int node_id = Integer.valueOf(name.substring(name.indexOf("[") + 1, name.lastIndexOf("]")));

            SpeciesType species = GameServer.getInstance().getSpeciesTypeByNodeID(node_id);
            nameList[i] = "\"" + species.getSpeciesName() + "\"";
        }

        tempCSV[0] = Arrays.toString(nameList).replaceAll(", ", ",");
        tempCSV[0] = tempCSV[0].substring(1, tempCSV[0].length() - 1) + "\n";

        csv = tempCSV[0];
        for (int i = 1; i < tempCSV.length; i++) {
            csv += tempCSV[i];

            if (i < tempCSV.length - 1) {
                csv += "\n";
            }
        }

        return csv;
    }

    public static String convertBiomassCSVtoSpeciesCSV(String csv) {
        List<String[]> someList = new ArrayList<String[]>();
        String[] csvList = csv.split("\n");

        someList.add(csvList[0].split(",\""));

        for (int i = 1; i < csvList.length; i++) {
            String item = csvList[i];
            someList.add(item.split(",", -1));
        }

        List<SpeciesType> speciesList = new ArrayList<SpeciesType>();
        speciesList.add(null);

        for (int i = 1; i < someList.get(0).length; i++) {
            String name = someList.get(0)[i];
            int node_id = Integer.valueOf(name.substring(name.indexOf("[") + 1, name.lastIndexOf("]")));

            SpeciesType species = GameServer.getInstance().getSpeciesTypeByNodeID(node_id);
            speciesList.add(species);

            someList.get(0)[i] = "\"" + species.getSpeciesName() + "\"";
        }

        for (int i = 1; i < someList.size(); i++) {
            String[] item = someList.get(i);

            for (int j = 1; j < item.length; j++) {
                if (!item[j].isEmpty()) {
                    item[j] = String.valueOf((int) Math.ceil(Double.valueOf(item[j]) * Constants.BIOMASS_SCALE / speciesList.get(j).getAvgBiomass()));
                }
            }
        }

        csv = "";
        for (String[] item : someList) {
            String newItem = Arrays.toString(item);
            if (someList.indexOf(item) == 0) {
                newItem = newItem.replaceAll(", ", ",");
            } else {
                newItem = newItem.replaceAll(" ", "");
            }

            csv += newItem.substring(1, newItem.length() - 1);
            
            if (someList.indexOf(item) < someList.size() - 1) {
                csv += "\n";
            }
        }
        
        return csv;
    }

    /**
     * Remove a world from buffer
     *
     * @param worldID           The id of the world which will be removed from buffer.
     */
    public void removeWorldAndWorldMapFromBuffer(int worldID, int gameMode) {
        if (gameMode == Constants.GAME_TYPE_PVP) {
            activePvPWorld.remove(worldID);
            pvpWorldMaps.remove(worldID);
        } else if (gameMode == Constants.GAME_TYPE_PVE) {
            activePvEWorld.remove(worldID);
            pveWorldMaps.remove(worldID);
        }
    }

    /**
     * Move a player out of playerPositionTracker.
     *
     * @param username             The username of the player
     */
    public void deletePlayerOutOfPositionTracker(int player_id) {
//        System.out.println("The position tracker info before removing is:");
//        printAllPlayersTrackingInfo();
//        System.out.println("*********End 1***********");

        playerPositionTracker.remove(player_id);

//        System.out.println("The position tracker info after removing is:");
//        printAllPlayersTrackingInfo();
//        System.out.println("*********End 2***********");
    }

    /**
     * Delete a player's GameClient thread out of the activeThreads
     *
     * @param threadID              The id of the thread.
     */
    public void deletePlayerThreadOutOfActiveThreads(Long threadID) {
        activeThreads.remove(threadID);
    }

    /** fine
     * Get the online players by the location of current player.
     * If the location of current player is 0(in main lobby), he/she can see all the online players;
     * If the location of current player is 1(in pvp game mode lobby), he/she can see the online players who are in the pvp game mode lobby(1) or in the pvp world lobby(3))
     * If the location of current player is 2(in pve game mode lobby), he/she can see the online players who are in the pve game mode lobby(2) or in the pve world lobby(4))
     *
     * @param location     the location of the current player(0=MainLobby; 1=PvP Game Mode Lobby; 2=PvE Game Mode Lobby; 3=PvP World Lobby & PvP World; 4=PvE World Lobby & PvE World)
     * @return             the list of players the current player expects to see
     */
    public List<String> getOnlinePlayersByCurrentPlayerLocation(int location) {
        List<String> onlinePlayers = new ArrayList<String>();

        if (location == Constants.LOCATION_MAIN_LOBBY) {
            for (Integer key : playerPositionTracker.keySet()) {
                onlinePlayers.add(getThreadByPlayerID(key).getPlayer().getUsername());
            }
        } else if (location == Constants.LOCATION_PVP_G_LOBBY) {
            for (Integer key : playerPositionTracker.keySet()) {
                if (playerPositionTracker.get(key) == Constants.LOCATION_PVP_G_LOBBY || playerPositionTracker.get(key) == Constants.LOCATION_PVP_W_LOBBY) {
                    onlinePlayers.add(getThreadByPlayerID(key).getPlayer().getUsername());
                }
            }
        } else if (location == Constants.LOCATION_PVE_G_LOBBY) {
            for (Integer key : playerPositionTracker.keySet()) {
                if (playerPositionTracker.get(key) == Constants.LOCATION_PVE_G_LOBBY || playerPositionTracker.get(key) == Constants.LOCATION_PVE_W_LOBBY) {
                    onlinePlayers.add(getThreadByPlayerID(key).getPlayer().getUsername());
                }
            }
        }

        return onlinePlayers;
    }

    /** fine
     * Get the current position of the player with the username
     *
     * @param username          the username of the player
     * @return		 	the position of the player(0=MainLobby; 1=PvP Game Mode Lobby; 2=PvE Game Mode Lobby; 3=PvP World Lobby & PvP World; 4=PvE World Lobby & PvE World)
     */
    public int getPositionOfAPlayer(int player_id) {
        return playerPositionTracker.get(player_id);
    }

//    public List<String> getPvPOnlinePlayers() {
//        List<String> pvpOnlinePlayers = new ArrayList<String>();
//        Set<String> keySet = this.playerPositionTracker.keySet();
//        for (String key : keySet) {
//            if (this.playerPositionTracker.get(key) == 1) {
//                pvpOnlinePlayers.add(key);
//            }
//        }
//        return pvpOnlinePlayers;
//    }
//
//    public List<String> getPvEOnlinePlayers() {
//        List<String> pveOnlinePlayers = new ArrayList<String>();
//        Set<String> keySet = this.playerPositionTracker.keySet();
//        for (String key : keySet) {
//            if (this.playerPositionTracker.get(key) == 2) {
//                pveOnlinePlayers.add(key);
//            }
//        }
//        return pveOnlinePlayers;
//    }
    /** fine
     * Add the world to active PvP world list
     *
     * @param world		a PvP world
     */
    public void addToActivePvPWorld(World world) {
        activePvPWorld.put(world.getID(), world);
    }

    /** fine
     * Get all the active PvE World
     *
     */
    public HashMap<Integer, World> getActivePvPWorld() {
        return activePvPWorld;
    }

    /** fine
     * Add the world to active PvE world list
     *
     * @param world		a PvE world
     */
    public void addToActivePvEWorld(World world) {
        activePvEWorld.put(world.getID(), world);
    }

    public HashMap<Integer, World> getActivePvEWorld() {
        return activePvEWorld;
    }

    /** fine
     * Get the PvP world from the active PvP world list.
     *
     * @param pvpWorldName          The name of the PvP world.
     * @return                      The PvP world with the name of pvpWorldName
     */
    public World getActivePvPWorld(String pvpWorldName) {//Search a pvp world by name from active pvp worlds.
        for (World world : getActivePvPWorld().values()) {
            if (world.getGameName().equals(pvpWorldName)) {//Find the target pvp world.
                return world;
            }
        }
        return null;
    }

    /** fine
     * Get the PvE world from the active PvE world list.
     *
     * @param pveWorldName          The name of the PvE world.
     * @return                      The PvE world with the name of pveWorldName
     */
    public World getActivePvEWorld(String pveWorldName) {//Search a pve world by name from active pve worlds.
        for (World world : getActivePvEWorld().values()) {
            if (world.getGameName().equals(pveWorldName)) {//Find the target pve world.
                return world;
            }
        }
        return null;
    }

    /** fine
     * Add a PvP world map to the PvP world map list
     *
     * @param map		a PvP world map
     */
    public void addPvPWorldMap(PvPWorldMap map) {
        pvpWorldMaps.put(map.getWorldID(), map);
    }

    /** fine
     * Add a PvE world map to the PvE world map list
     *
     * @param map		a PvE world map
     */
    public void addPvEWorldMap(PvEWorldMap map) {
        pveWorldMaps.put(map.getWorldID(), map);
    }

    public PvEWorldMap getPvEWorldMap(int worldID) {
        return pveWorldMaps.get(worldID);
    }

    public PvPWorldMap getPvPWorldMap(int worldID) {
        return pvpWorldMaps.get(worldID);
    }

    /** fine
     * Track the position of a player before he/she goes to the world.
     *
     * @param playerName	the username of the player
     * @param position          the position of the player(0=MainLobby; 1=PvP Game Mode Lobby; 2=PvE Game Mode Lobby; 3=PvP World Lobby & PvP World; 4=PvE World Lobby & PvE World)
     * 
     */
    public void trackPlayerPosition(int player_id, int position) {
        playerPositionTracker.put(player_id, position);
    }

    public GameEngine getGameEngineByWorldID(int worldID) {
        return activeGameEngine.get(worldID);
    }

    /**
     * Remove an environment from the world
     *
     * @param  worldID              The id of the target world
     * @param  worldType            GameMode: pvp/pve
     * @param  row                  The row of the environment
     * @param  col                  The col of the environment
     */
    public Environment removeAnEnvFromWorld(int worldID, int worldType, int row, int col) {
        Environment env = null;
        if (worldType == Constants.GAME_TYPE_PVP) {
            World pvpWorld = activePvPWorld.get(worldID);
            if (pvpWorld != null) {
                env = pvpWorld.getEnvByRowAndCol(row, col);
                if (env != null) {
                    pvpWorld.getEnvironments().remove(env);
                } else {
                    System.out.println("In GameServer.java---no env with the given row and col.");
                }
            }
        }
        if (worldType == Constants.GAME_TYPE_PVE) {
            World pveWorld = activePvEWorld.get(worldID);
            if (pveWorld != null) {
                env = pveWorld.getEnvByRowAndCol(row, col);
                if (env != null) {
                    pveWorld.getEnvironments().remove(env);
                } else {
                    System.out.println("In GameServer.java---no env with the given row and col.");
                }
            }
        }

        return env;
    }

    /**
     * Get an active world with the name of worldName
     *
     * @param worldName             The name of the target world
     */
    public World getOnlineActiveWorld(String worldName) {
        World world = getActivePvPWorld(worldName);
        if (world == null) {
            world = getActivePvEWorld(worldName);
        }
        return world;
    }

    public void addResponseForAvatar(int avatarID, GameResponse response) {
        GameClient client = getThreadByAvatarID(avatarID);

        if (client != null) {
            client.addResponseForUpdate(response);
        } else {
            System.out.println("In addResponseForAvatar--client is null");
        }
    }

    public void addResponseForUser(int userID, GameResponse response) {
        GameClient client = getThreadByPlayerID(userID);

        if (client != null) {
            client.addResponseForUpdate(response);
        } else {
            System.out.println("In addResponseForUser--client is null");
        }
    }

    public void addResponseForUser(String username, GameResponse response) {
        GameClient client = getThreadByPlayerUserName(username);

        if (client != null) {
            client.addResponseForUpdate(response);
        } else {
            System.out.println("In addResponseForUser--client is null");
        }
    }

    /**
     * Add a response for all people in the same team in a PvP world.
     *
     * @param pvpWorldID            The if of the PvP world.
     * @param teamID                The id of the team.
     * @param response              The response which will be added.
     * 
     */
    public void addResponseForTeamInPvP(int pvpWorldID, int teamID, GameResponse response) {
        List<GameClient> clients = getThreadsByTeam(pvpWorldID, teamID);

        if (clients != null) {
            for (GameClient client : clients) {
                client.addResponseForUpdate(response);
            }
        }
    }

    /** fine
     * Add a response object for all the players in the same world.
     *
     * @param worldID           The id of the world
     * @param response          The response object which will be added to all the players in the world.
     */
    public void addResponseForWorld(int worldID, GameResponse response) {
        List<GameClient> clients = getClientsByWorld(worldID);

        for (GameClient client : clients) {
            client.addResponseForUpdate(response);
        }
    }

    /**
     * Add a response for all people in the same world.
     *
     * @param currentThreadID           The id of the thread of the player who sends this response.
     * @param worldID                   The id of the target world.
     * @param respone                   The response which will be added.
     */
    public void addResponseToOtherPeopleInTheSameWorld(Long currentThreadID, int worldID, GameResponse response) {
        for (GameClient client : getClientsByWorld(worldID)) {
            if (client.getId() != currentThreadID) {
                client.addResponseForUpdate(response);
            }
        }
    }

    /**
     * Add a response for all the online players.
     *
     * @param response       The response which will be added.
     * 
     */
    public void addResponseForAllOnlinePlayers(long exclusiveClientID, GameResponse response) {
        for (GameClient client : activeThreads.values()) {
            if (client.getId() != exclusiveClientID) {
                client.addResponseForUpdate(response);
            }

        }
    }

    /**
     * Add Response for all the players who are in the same game mode (PvP/PvE)
     *
     * @param gameMode              PvP/PvE
     * @param response              The response which will be added.
     * 
     */
    public void addResponseForAllPlayersInTheSameGameMode(long exclusiveClientID, int gameMode, GameResponse response) {
        List<String> players = null;
        if (gameMode == Constants.GAME_TYPE_PVP) {
            players = getOnlinePlayersByCurrentPlayerLocation(1);
        } else if (gameMode == Constants.GAME_TYPE_PVE) {
            players = getOnlinePlayersByCurrentPlayerLocation(2);
        }

        if (players != null) {
            for (String player : players) {
                GameClient client = getThreadByPlayerUserName(player);
                if (client != null && client.getId() != exclusiveClientID) {
                    client.addResponseForUpdate(response);
                } else {
                    System.out.println("In GameServer. java --- There is a client in playerPositionTracker but his/her thread is not active any longer...");
                }
            }
        }
    }

    public void updateCash(Player player, int amount) {
        Avatar avatar = player.getAvatar();
        avatar.setCurrency(Math.min(Constants.MAX_GOLD, avatar.getCurrency() + amount));

        try {
            AvatarDAO.updateCurrency(avatar);
        } catch (SQLException ex) {
            System.err.println(ex.getMessage());
        }

        ResponseUpdateCash updateResponse = new ResponseUpdateCash();
        updateResponse.setAmount(amount);
        updateResponse.setCash(avatar.getCurrency());

        addResponseForUser(player.getID(), updateResponse);
    }

    public void updateExperience(Player player, int amount) {
        amount *= Constants.MULTIPLIER_EXP;

        Avatar avatar = player.getAvatar();
        avatar.setExperience(Math.min(ExpTable.getExp(Constants.MAX_LEVEL - 1), avatar.getExperience() + amount));

        try {
            AvatarDAO.updateExperience(avatar);
        } catch (SQLException ex) {
            System.err.println(ex.getMessage());
        }

        int oldLevel = avatar.getLevel(), newLevel = ExpTable.getLevel(avatar.getExperience());

        if (newLevel > oldLevel) {
            avatar.setLevel(newLevel);

            try {
                AvatarDAO.updateLevel(avatar);
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }

            ResponseUpdateLevel updateLevelResponse = new ResponseUpdateLevel();
            updateLevelResponse.setAmount(newLevel - oldLevel);
            updateLevelResponse.setLevel(newLevel);

            String range = String.valueOf(ExpTable.getExpToAdvance(oldLevel + 1));
            for (int i = oldLevel + 2; i <= newLevel; i++) {
                range += "," + ExpTable.getExpToAdvance(i);
            }
            updateLevelResponse.setRange(range);

            addResponseForUser(player.getID(), updateLevelResponse);

            updateCash(player, amount);

            List<SpeciesType> unlockList = new ArrayList<SpeciesType>();

            try {
                for (int i = oldLevel + 1; i <= newLevel; i++) {
                    unlockList.addAll(ShopDAO.getAnimalsByLevel(i));
                    unlockList.addAll(ShopDAO.getPlantsByLevel(i));
                }

                ResponseShopUnlock unlockResponse = new ResponseShopUnlock();
                unlockResponse.setUnlockList(unlockList);

                GameServer.getInstance().addResponseForUser(player.getID(), unlockResponse);
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }
        }

        ResponseUpdateXP updateResponse = new ResponseUpdateXP();
        updateResponse.setAmount(amount);
        updateResponse.setTotal(avatar.getExperience());

        addResponseForUser(player.getID(), updateResponse);
    }

    public static GameServer getInstance() {
        return gameServer;
    }

    public static void main(String args[]) throws SQLException {
        gameServer = new GameServer();

        gameServer.getReady();

        if (gameServer.isReady()) {
            gameServer.run();
        }
    }
}
