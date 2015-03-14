package networking.request;

import dataAccessLayer.AvatarDAO;
import dataAccessLayer.EnvironmentDAO;
import dataAccessLayer.ZoneDAO;

import java.io.IOException;
import java.util.List;
import java.util.Random;

import metadata.Constants;

import model.Environment;
import model.PvPWorldMap;
import model.World;

import networking.response.ResponseStartWorld;

import simulationEngine.SimulationEngine;

import utility.DataReader;

import worldManager.gameEngine.Zone;

/**
 *
 * @author Xuyuan
 */
public class RequestStartWorld extends GameRequest {

    // Data
    private String worldName;
    // Responses
    private ResponseStartWorld responseStartWorld;

    public RequestStartWorld() {
        responses.add(responseStartWorld = new ResponseStartWorld());
    }

    @Override
    public void parse() throws IOException {
        worldName = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        //If it is a pvp world, make sure that the two teams have equal number of players.
        World pvpWorld = client.getServer().getActivePvPWorld(worldName);
        if (pvpWorld != null) {//The world is a pvp world.
            PvPWorldMap map = client.getServer().getPvPWorldMap(pvpWorld.getID());
            System.out.println("Original PvP Map:");
            map.printObject();

            if (map != null) {
                int team0PlayerNum = map.getTeam0().size();
                int team1PlayerNum = map.getTeam1().size();
                if (team0PlayerNum > team1PlayerNum) {
                    int diff = team0PlayerNum - team1PlayerNum;
                    for (int i = 0; i < diff; i++) {
                        int playerPosition = map.removeLastOnePlayerFromTeamN(0);

                        //Remove the environment in row: 0, position: playerPosition of the current world.
                        Environment removedEnv = client.getServer().removeAnEnvFromWorld(pvpWorld.getID(), Constants.GAME_TYPE_PVP, 0, playerPosition);

                        EnvironmentDAO.deleteEnvironmentByID(removedEnv.getID());
                        AvatarDAO.deleteAvatarByID(client.getAvatar().getID());
                    }
                } else if (team1PlayerNum > team0PlayerNum) {
                    int diff = team1PlayerNum - team0PlayerNum;
                    for (int i = 0; i < diff; i++) {
                        int playerPosition = map.removeLastOnePlayerFromTeamN(1);

                        //Remove the environment in row: 0, position: playerPosition of the current world.
                        Environment removedEnv = client.getServer().removeAnEnvFromWorld(pvpWorld.getID(), Constants.GAME_TYPE_PVP, 0, playerPosition);

                        EnvironmentDAO.deleteEnvironmentByID(removedEnv.getID());
                        AvatarDAO.deleteAvatarByID(client.getAvatar().getID());
                    }
                }
            } else {
                System.out.println("PvP world map is null");
            }

        }

        //Until now the world, environment, avatar are ready for both buffer and database
        //After this block the zones will be ready for both buffer and database too.
        //In this block each environment will be assigned a map id.
        Random ran = new Random();
        World world = client.getServer().getOnlineActiveWorld(worldName);
        if (world != null) {
            for (Environment env : world.getEnvironments()) {
                if (env.getOwnerID() == client.getPlayer().getID()) {//Find the environment of the current player
                    if (!env.isOldEnvironment()) {//It is a new environment.
                        EnvironmentDAO.updateEnvironment(env);

                        //Handle the zones in this environment.
                        for (int i = 0; i < 3; i++) {
                            for (int j = 0; j < 3; j++) {
                                Zone zone = new Zone(-1);
                                zone.setOrder(i * 3 + j);
                                zone.setEnvID(env.getID());
                                zone.setRow(i);
                                zone.setColumn(j);
                                zone.setCurrentTimeStep(1);

                                //Handle part from Sonal-- create food web for each zone.
                                String networkName = String.valueOf(env.getID()) + "_" + String.valueOf(zone.getOrder());

                                SimulationEngine se = new SimulationEngine();
                                String manipulationId = se.createDefaultSubFoodweb(networkName).getManipulationId();//the primary key of the zone is unique.

                                zone.setManipulationID(manipulationId);

                                int zone_id = ZoneDAO.createZone(zone);
                                zone.setID(zone_id);

                                env.setZone(zone);
                            }
                        }
                    } else {//It is an old environment.
                        //It is an old environment.
                        List<Zone> zones = ZoneDAO.getZoneByEnvironmentId(env.getID());
                        env.setZones(zones);
                    }
                }

            }
        } else {
            System.out.println("The world is not active any more");
        }

        //Create the gameEngine here.
        client.getServer().createGameEngine(world);
    }
}
