package networking.request;

import core.GameServer;

import dataAccessLayer.BiomassCSVDAO;
import dataAccessLayer.BirthListDAO;
import dataAccessLayer.DeathListDAO;
import dataAccessLayer.EnvironmentDAO;
import dataAccessLayer.ParamTableDAO;
import dataAccessLayer.PreyPredatorRatioDAO;
import dataAccessLayer.ScoreCSVDAO;
import dataAccessLayer.SpeciesCSVDAO;
import dataAccessLayer.WaterSourceDAO;
import dataAccessLayer.WorldDAO;
import dataAccessLayer.WorldMapDAO;
import dataAccessLayer.ZoneDAO;
import dataAccessLayer.ZoneGroupsDAO;
import dataAccessLayer.ZoneNodeAddDAO;
import dataAccessLayer.ZoneSpeciesDAO;
import dataAccessLayer.ZoneTypeDAO;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

import metadata.Constants;

import model.Environment;
import model.PvEWorldMap;
import model.World;
import model.ZoneType;

import networking.response.ResponseBirthAnimal;
import networking.response.ResponseBirthPlant;
import networking.response.ResponseChat;
import networking.response.ResponseCreateEnv;
import networking.response.ResponseGetEnv;
import networking.response.ResponseJoinPvEWorld;

import networking.response.ResponseSeeOnlinePlayers;
import org.datacontract.schemas._2004._07.ManipulationParameter.NodeBiomass;

import simulationEngine.SimulationEngine;
import simulationEngine.SpeciesZoneType;

import utility.DataReader;

import worldManager.gameEngine.WaterSource;
import worldManager.gameEngine.Zone;
import worldManager.gameEngine.species.Animal;
import worldManager.gameEngine.species.Organism;
import worldManager.gameEngine.species.Plant;

/**
 *
 * @author Xuyuan
 */
public class RequestJoinPvEWorld extends GameRequest {

    // Data
    private String worldName;
    // Responses
    private ResponseJoinPvEWorld responseJoinPvEWorld;
    private ResponseGetEnv responseGetEnv;

    public RequestJoinPvEWorld() {
        responses.add(responseJoinPvEWorld = new ResponseJoinPvEWorld());
        responses.add(responseGetEnv = new ResponseGetEnv());
    }

    @Override
    public void parse() throws IOException {
        worldName = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        /* 1. If the pve world is active, the player is a new user
         * 2. If the pve world is active, the player is an old user
         * 3. If the pve world is non-active, the player is a new user
         * 4. If the pve world is non-active, the player is an old user.
         */
        World world = client.getServer().getActivePvEWorld(worldName);

        if (worldName.equals("NEW201204")) {
            world = WorldDAO.getWorldByPlayerID(client.getPlayer().getID());

            if (world != null) {
                world.setGameEngine(client.getServer().createGameEngine(world));
                world.setEnvironments(EnvironmentDAO.getEnvironmentByWorldID(world.getID()));

                client.getServer().addToActivePvEWorld(world);
                client.getServer().addPvEWorldMap(WorldMapDAO.getPvEWorldMapByWorldID(world.getID()));
            } else if (world == null) {
                world = new World(-1);
                world.setGameMode(Constants.GAME_TYPE_PVE);
                world.setGameName(String.valueOf(client.getPlayer().getID()) + "_" + System.currentTimeMillis() % 100000);
                world.setMaxPlayers(100);
                world.setEnvType("Savanna");
                world.setAccessType(Constants.PRIVACY_TYPE_PUBLIC);
                world.setCreatorID(client.getPlayer().getID());

                int world_id = WorldDAO.createWorld(world);
                world.setID(world_id);

                client.getServer().addToActivePvEWorld(world);

                PvEWorldMap pveMap = new PvEWorldMap(world.getID());
                client.getServer().addPvEWorldMap(pveMap);

                WorldMapDAO.savePvEWorldMap(pveMap);

                world.setGameEngine(client.getServer().createGameEngine(world));
            }
        }

        if (world == null) {
            world = WorldDAO.getWorldByName(worldName);

            if (world != null) {
                world.setGameEngine(client.getServer().createGameEngine(world));
                world.setEnvironments(EnvironmentDAO.getEnvironmentByWorldID(world.getID()));

                client.getServer().addToActivePvEWorld(world);
                client.getServer().addPvEWorldMap(WorldMapDAO.getPvEWorldMapByWorldID(world.getID()));
            }
        }

        if (world != null && !world.hasPlayer(client.getPlayer().getID())) {//If the pve world is active
            //Try to see if the environment of the current player is in the world buffer.
            if (world.hasEnvironmentOfPlayer(client.getPlayer().getID())) {
                responseJoinPvEWorld.setStatus((short) 0);
                responseJoinPvEWorld.setWorld(world);

                world.setPlayer(client.getPlayer());
                responseGetEnv.setWorld(world);
                client.setWorld(world);

                WorldDAO.updateLastPlayed(world.getID());

                for (Environment env : world.getEnvironments()) {
                    for (Zone zone : env.getZones()) {
                        if (zone.isEnable()) {
                            zone.setScoreCSV(ScoreCSVDAO.getCSV(zone.getID()));

                            zone.setParameters(ParamTableDAO.getByZoneID(zone.getID()));
                            PreyPredatorRatioDAO.createParameters(world.getCreatorID(),zone.getID());
                            HashMap<Integer, Integer[]> speciesList = ZoneSpeciesDAO.getSpecies(zone.getID());
                            HashMap<Integer, List<Object[]>> groupList = ZoneGroupsDAO.getGroups(zone.getID());

                            for (int species_id : speciesList.keySet()) {
                                Integer[] value = speciesList.get(species_id);
                                int num_groups = value[0], amount = value[1];

                                if (amount != 0 && num_groups != 0) {
                                    List<Object[]> groups = groupList.get(species_id);
                                    world.getGameEngine().createExistingOrganisms(species_id, zone.getID(), num_groups, amount, groups, Constants.CREATE_STATUS_DEFAULT);
                                }
                            }

                            zone.setBirthList(BirthListDAO.getList(zone.getID()));
                            zone.setDeathList(DeathListDAO.getList(zone.getID()));

                            zone.setAddNodeList(ZoneNodeAddDAO.getList(zone.getID()));
                        }
                    }
                }
            } else {
                if (world.getEnvironments().size() < world.getMaxPlayers()) {
                    responseJoinPvEWorld.setStatus((short) 0);
                    responseJoinPvEWorld.setWorld(world);

                    //Create an environment for this player
                    PvEWorldMap map = client.getServer().getPvEWorldMap(world.getID());

                    if (map != null) {
                        int position = map.assignEnvironmentPosition();
                        int row = map.getRow(position);
                        int col = map.getCol(position);

                        WorldMapDAO.updatePvEWorldMap(map);

                        //Create a new environment for this user.
                        Environment env = new Environment(-1);
                        env.setOwnerID(client.getPlayer().getID());
                        env.setPos(row, col);
                        env.setWorldID(world.getID());

                        int env_id = EnvironmentDAO.createEnvironment(env);
                        env.setID(env_id);

                        Random random = new Random();

                        //Handle the zones in this environment.
                        for (int i = 0; i < 3; i++) {
                            for (int j = 0; j < 3; j++) {
                                Zone zone = new Zone(-1);
                                zone.setOrder(i * 3 + j);
                                zone.setEnvID(env.getID());
                                zone.setEnvironment(env);
                                zone.setRow(i);
                                zone.setColumn(j);
                                zone.setCurrentTimeStep(1);

                                zone.setType(random.nextInt(3) + 1);

                                int zone_id = ZoneDAO.createZone(zone);
                                zone.setID(zone_id);

                                ParamTableDAO.createParameters(zone_id);
                                PreyPredatorRatioDAO.createParameters(world.getCreatorID(),zone_id);
                                zone.setParameters(ParamTableDAO.getByZoneID(zone_id));

                                ZoneType zoneType = ZoneTypeDAO.getZoneType(zone.getType());

                                if (zoneType.containsWater()) {
                                    WaterSource waterSource = new WaterSource(-1);
                                    waterSource.setMaxWater(100);
                                    waterSource.setWater(100);
                                    waterSource.setZoneID(zone_id);

                                    int water_source_id = WaterSourceDAO.createWaterSource(waterSource);
                                    waterSource.setID(water_source_id);

                                    zone.setWaterSource(waterSource);
                                }

                                env.setZone(zone);
                            }
                        }

                        for (Environment e : world.getEnvironments()) {
                            for (Zone zone : e.getZones()) {
                                if (zone.isEnable()) {
                                    for (Organism organism : zone.getOrganisms()) {
                                        if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                                            ResponseBirthPlant responseBirthPlant = new ResponseBirthPlant();
                                            responseBirthPlant.setPlant((Plant) organism);
                                            responses.add(responseBirthPlant);
                                        } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                                            ResponseBirthAnimal responseBirthAnimal = new ResponseBirthAnimal();
                                            responseBirthAnimal.setAnimal((Animal) organism);
                                            responses.add(responseBirthAnimal);
                                        }
                                    }
                                }
                            }
                        }

                        ResponseCreateEnv responseCreateEnv = new ResponseCreateEnv();
                        responseCreateEnv.setEnvironment(env);
                        client.getServer().addResponseToOtherPeopleInTheSameWorld(client.getId(), world.getID(), responseCreateEnv);

                        Zone startZone = env.getZones().get(0);

                        SimulationEngine se = startZone.getSimulationEngine();
                        String networkName = "WoB-" + env.getID() + "." + startZone.getOrder() + "-" + System.currentTimeMillis() % 100000;

                        int nodeList[] = {13, 20, 31};
                        startZone.setManipulationID(se.createAndRunSeregenttiSubFoodweb(nodeList, networkName, 0, 0, false));

                        ZoneDAO.updateManipulationID(startZone.getID(), startZone.getManipulationID());

                        List<NodeBiomass> lNodeBiomass = new ArrayList<NodeBiomass>();

                        lNodeBiomass.add(new NodeBiomass(GameServer.getInstance().getSpeciesTypeByNodeID(13).getAvgBiomass() * 10 / Constants.BIOMASS_SCALE, 13));
                        lNodeBiomass.add(new NodeBiomass(GameServer.getInstance().getSpeciesTypeByNodeID(20).getAvgBiomass() * 10 / Constants.BIOMASS_SCALE, 20));
                        lNodeBiomass.add(new NodeBiomass(GameServer.getInstance().getSpeciesTypeByNodeID(31).getAvgBiomass() * 10 / Constants.BIOMASS_SCALE, 31));

                        if (!lNodeBiomass.isEmpty()) {
                            System.out.println("Updating Initial Biomass...");
                            se.updateBiomass(startZone.getManipulationID(), lNodeBiomass, 0);
                        }

                        se.getBiomass(startZone.getManipulationID(), 0, 0);

                        world.setEnvironment(env);
                        world.setPlayer(client.getPlayer());
                        responseGetEnv.setWorld(world);
                        client.setWorld(world);

                        WorldDAO.updateLastPlayed(world.getID());
                        WorldDAO.updateWorldProperties(world);

                        int initialAmount = 3;

                        for (SpeciesZoneType szt : se.getSpecies().values()) {
                            int species_id = GameServer.getInstance().getSpeciesTypeByNodeID(szt.getNodeIndex()).getID();

                            se.setParameter(0, szt, startZone.getManipulationID(), Constants.PARAMETER_X, szt.getParamX());

                            world.getGameEngine().createOrganisms(species_id, startZone.getID(), initialAmount, Constants.CREATE_STATUS_DEFAULT);
                            world.getGameEngine().createOrganismsByBirth(species_id, startZone.getID(), szt.getSpeciesCount() - initialAmount);
                        }

                        try {
                            String csv = null;

                            while (true) {
                                csv = se.getBiomassCSVString(startZone.getManipulationID());

                                if (!csv.isEmpty()) {
                                    break;
                                } else {
                                    System.out.println("Error: CSV [" + startZone.getManipulationID() + "] Retrieval Failed!");
                                }
                            }

                            BiomassCSVDAO.createCSV(startZone.getManipulationID(), GameServer.removeNodesFromCSV(csv));
                            SpeciesCSVDAO.createCSV(startZone.getManipulationID(), GameServer.convertBiomassCSVtoSpeciesCSV(csv));

                            String score_csv = ",\"Environment Score\"\n1,0";
                            ScoreCSVDAO.createCSV(startZone.getID(), score_csv);
                            startZone.setScoreCSV(score_csv);
                        } catch (Exception ex) {
                            ex.printStackTrace();
                            System.err.println(ex.getMessage());
                        }
                    }
                } else {
                    responseJoinPvEWorld.setStatus((short) 1); // World Full
                }
            }

            if (world.getPlayers().size() == 1) {
                world.getGameEngine().start();
            }
        }

        ResponseChat responseChat = new ResponseChat();
        responseChat.setMessage("[" + client.getPlayer().getUsername() + "] has logged on.");
        responseChat.setType((short) 1);

        GameServer.getInstance().addResponseForAllOnlinePlayers(client.getId(), responseChat);

        ResponseSeeOnlinePlayers responsePlayers = new ResponseSeeOnlinePlayers();
        responsePlayers.setOnlinePlayers(GameServer.getInstance().getActivePlayers());

        GameServer.getInstance().addResponseForAllOnlinePlayers(client.getId(), responsePlayers);

        //Track the player' position (4 means PvE World lobby or PvE world.)
        client.getServer().trackPlayerPosition(client.getPlayer().getID(), Constants.LOCATION_PVE_W_LOBBY);

        //Add the response to all the players in the same world.
//            client.getServer().addResponseForWorld(world.getID(), response);
    }
}
