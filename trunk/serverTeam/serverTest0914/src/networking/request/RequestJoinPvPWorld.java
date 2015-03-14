package networking.request;

import dataAccessLayer.AvatarDAO;
import dataAccessLayer.EnvironmentDAO;
import dataAccessLayer.WorldDAO;
import dataAccessLayer.WorldMapDAO;

import java.io.IOException;
import java.sql.SQLException;

import metadata.Constants;

import model.Avatar;
import model.Environment;
import model.PvPWorldMap;
import model.World;

import networking.response.ResponseJoinPvPWorld;

import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestJoinPvPWorld extends GameRequest {

    // Data
    private String worldName;
    // Responses
    private ResponseJoinPvPWorld responseJoinPvPWorld;

    public RequestJoinPvPWorld() {
        responses.add(responseJoinPvPWorld = new ResponseJoinPvPWorld());
    }

    @Override
    public void parse() throws IOException {
        worldName = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        //The target world is PvP world, so it is only searched in the active pvp worlds.
        World world = client.getServer().getActivePvPWorld(worldName);

        if (world != null) {//The requested world exists
            System.out.println("*******The pvp world start*******");
            world.toString();
            System.out.println("*******The pvp world end*******");

            if (world.isHasStarted()) {//The requested PvP world has started.
                responseJoinPvPWorld.setStatus((short) 1);
                System.out.println("The world has started");
            } else {
                if (world.getEnvironments().size() < world.getMaxPlayers()) {
                    responseJoinPvPWorld.setStatus((short) 0);
                    responseJoinPvPWorld.setWorld(world);

                    WorldDAO.updateWorldProperties(world);

                    //Set the world to the current thread.
                    client.setWorld(world);

                    //Create an environment for this player
                    int row = 0;//The row of the environment.
                    int col = 0;//The collumn of the environment.
                    PvPWorldMap map = client.getServer().getPvPWorldMap(world.getID());
                    if (map != null) {
                        map.assignEnvironmentPosition();
                        row = map.getRow();
                        col = map.getCol();

                        System.out.println("*****A PvP Map start*****");
                        map.printObject();
                        System.out.println("*****A PvP Map end*****");

                        try {
                            WorldMapDAO.updatePvPWorldMap(map);
                        } catch (SQLException ex) {
                        }
                    } else {
                        System.out.println("In RequestJoinPvPWorld.java---map is null");
                    }

                    //Create a new environment for this user.
                    Environment env = new Environment(world.getID());
                    env.setRow(row);
                    env.setColumn(col);
                    try {
                        EnvironmentDAO.createEnvironment(env);
                    } catch (SQLException ex) {
                    }

                    Environment sameEnv = null;
                    try {
                        sameEnv = EnvironmentDAO.getEnvironmentByWorldIDAndRowAndCol(env);//Get the environment out of db just to get its id which is generated in db.
                        if (sameEnv != null) {
                            sameEnv.toString();
                        } else {
                            System.out.println("The environment from db is null.");
                        }
                    } catch (SQLException ex) {
                    }

                    world.getEnvironments().add(sameEnv);
                    System.out.println("*****World start*****");
                    world.toString();
                    System.out.println("*****World end*****");

                    //Create an avatar for this user.
                    Avatar ava = new Avatar(-1);
                    ava.setPlayerID(client.getPlayer().getID());
                    //Set [team_no] & [envPosition] for this avatar.
                    ava.setTeamNo(sameEnv.getRow());

                    int avatar_id = AvatarDAO.createAvatar(ava);

                    ava.setPlayerID(client.getPlayer().getID());

                    client.setAvatar(ava);
                    client.setWorld(world);


                    System.out.println("*****{At the end of RequestCreateNewWorld}World start*****");
                    world.toString();
                    System.out.println("*****{At the end of RequestCreateNewWorld}World end*****");

                    //Track the current position of this player.
                    client.getServer().trackPlayerPosition(client.getPlayer().getID(), Constants.LOCATION_PVP_W_LOBBY);

                    //Add this response too all the players in the same world.
                    client.getServer().addResponseForWorld(world.getID(), responseJoinPvPWorld);

                } else {
                    responseJoinPvPWorld.setStatus((short) 1);
                    System.out.println("The world is full already.");
                }
            }
        } else {//The request world does not exist any more.
            responseJoinPvPWorld.setStatus((short) 1);
        }
    }
}
