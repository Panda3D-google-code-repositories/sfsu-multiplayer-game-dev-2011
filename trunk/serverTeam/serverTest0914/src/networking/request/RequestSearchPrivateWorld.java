package networking.request;

import dataAccessLayer.WorldDAO;

import java.io.IOException;
import java.sql.SQLException;

import metadata.Constants;

import model.World;
import networking.response.ResponseSearchPrivateWorld;
import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestSearchPrivateWorld extends GameRequest {

    // Data
    private World world;
    // Responses
    private ResponseSearchPrivateWorld responseSearchPrivateWorld;

    public RequestSearchPrivateWorld() {
        world = new World(-1);
        responses.add(responseSearchPrivateWorld = new ResponseSearchPrivateWorld());
    }

    @Override
    public void parse() throws IOException {
        world.setGameName(DataReader.readString(dataInput));
        world.setPassword(DataReader.readString(dataInput));
    }

    @Override
    public void doBusiness() throws Exception {
        //PvP and PvE worlds will be stored in db. After a pvp world ends, it will be deleted from db. 
        World wld = null;

        try {
            wld = WorldDAO.getPrivateWorldByWorldNameAndPassword(world);

            if (wld != null) {
                System.out.println("*****Searched world from db start*****");
                wld.toString();
                System.out.println("*****Searched world from db end*****");
            } else {
                System.out.println("Searched world is null");
            }
        } catch (SQLException ex) {
        }

        if (wld != null) {
            if (wld.getEnvironments().size() < wld.getMaxPlayers()) {
                if (wld.getGameMode() == Constants.GAME_TYPE_PVP && wld.isHasStarted()) {
                    responseSearchPrivateWorld.setStatus((short) 1);
                    System.out.println("The pvp world has been started");
                } else {//The world could be join
                    responseSearchPrivateWorld.setStatus((short) 0);
                    responseSearchPrivateWorld.setWorld(wld);
                }

            } else {
                responseSearchPrivateWorld.setStatus((short) 1);
                System.out.println("The world is full");
            }
        } else {
            responseSearchPrivateWorld.setStatus((short) 1);
            System.out.println("The world name or password is wrong");
        }


//        if (wld != null && wld.getNumEnvironments() < wld.getMaxPlayers()) {
//            response.setStatus((short) 0);
//            response.setWorld(wld);
//
//            wld.setNumEnvironments(wld.getNumEnvironments() + 1);
//            worldDAO.updateWorld(wld);
//
//            //Assign a position for this player.
//            int row = 0;//The row of the environment.
//            int col = 0;//The collumn of the environment.
//            if (wld.getGameMode() == Constants.GAME_TYPE_PVP) {
//                PvPWorldMap map = client.getServer().getPvPWorldMap(world.getWorldIdPk());
//                if (map != null) {
//                    map.assignEnvironmentPosition();
//                    row = map.getRow();
//                    col = map.getCol();
//                    mapDAO.updatePvPWorldMap(map);
//                } else {
//                    System.out.println("In RequestSearchPrivateWorld.java---map is null");
//                }
//            } else if (wld.getGameMode() == Constants.GAME_TYPE_PVE) {
//                PvEWorldMap map = client.getServer().getPvEWorldMap(world.getWorldIdPk());
//                if (map == null) {
//                    map = mapDAO.getPvEWorldMap(world.getWorldIdPk());
//                }
//
//                if (map != null) {
//                    int position = map.assignEnvironmentPosition();
//                    row = map.getRow(position);
//                    col = map.getCol(position);
//                    mapDAO.updatePvEWorldMap(map);
//                } else {
//                    System.out.println("In RequestSearchPrivateWorld.java---map is null");
//                }
//            }
//
//            //Create a new environment for this user.
//            Environment env = new Environment(world.getWorldIdPk());
//            env.setEnvRow(row);
//            env.setEnvColumn(col);
//            //envDAO.saveEnvironment(env);
//            world.getEnvironments().add(env);
//
//            //Create an avatar for this user.
//            //Environment environ = envDAO.getEnvironmentByWorldIDAndPosition(env);
//            Avatar ava = new Avatar(client.getPlayer());
//            env.setAvatar(ava);
//
//            //Set the player's current position 4(4 means in the pve world lobby.)
//            if(wld.getGameMode() == Constants.GAME_TYPE_PVP){
//                client.getServer().trackPlayerPosition(client.getPlayer().getUserName(), 3);//In PvP world lobby.
//            }else if(wld.getGameMode() == Constants.GAME_TYPE_PVE){
//                client.getServer().trackPlayerPosition(client.getPlayer().getUserName(), 4);//In PvE world lobby.
//            }
//
//
//        } else {
//            response.setStatus((short) 1);
//        }
    }
}
