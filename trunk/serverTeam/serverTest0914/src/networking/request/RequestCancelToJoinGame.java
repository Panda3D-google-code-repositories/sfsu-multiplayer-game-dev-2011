package networking.request;

import dataAccessLayer.AvatarDAO;
import dataAccessLayer.EnvironmentDAO;
import dataAccessLayer.WorldDAO;
import dataAccessLayer.WorldMapDAO;

import java.io.IOException;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

import metadata.Constants;

import model.Environment;
import model.PvEWorldMap;
import model.PvPWorldMap;
import model.World;

import networking.response.ResponseCancelToJoinGame;

import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestCancelToJoinGame extends GameRequest {

    // Data
    private String worldName;
    // Responses
    private ResponseCancelToJoinGame responseCancelToJoinGame;

    public RequestCancelToJoinGame() {
        responses.add(responseCancelToJoinGame = new ResponseCancelToJoinGame());
    }

    @Override
    public void parse() throws IOException {
        worldName = DataReader.readString(dataInput);
        System.out.println("Parse---world name:" + worldName);
    }

    @Override
    public void doBusiness() throws Exception {
        World world = client.getServer().getOnlineActiveWorld(worldName);

        if (world != null) {
            if (world.getEnvironments() != null) {
                for (Environment env : world.getEnvironments()) {
                    if (env.getOwnerID() == client.getPlayer().getID()) {
                        //Remove the environment from the world
                        world.getEnvironments().remove(env);

                        WorldDAO.updateWorldProperties(world);

                        //Update the world map.
                        if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
                            PvPWorldMap pvpMap = client.getServer().getPvPWorldMap(world.getID());
                            pvpMap.quitOldTeamAndPosition(env.getRow(), env.getColumn());
                            pvpMap.printObject();

                            WorldMapDAO.updatePvPWorldMap(pvpMap);
                        } else if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
                            PvEWorldMap pveMap = client.getServer().getPvEWorldMap(world.getID());
                            int position = pveMap.getPositionBasingOnRowAndCol(env.getRow(), env.getColumn());
                            pveMap.quitPosition(position);
                            pveMap.toString();

                            WorldMapDAO.updatePvEWorldMap(pveMap);
                        }

                        //Delete the environment from database.
                        EnvironmentDAO.deleteEnvironmentByID(env.getID());
                        AvatarDAO.deleteAvatarByID(client.getAvatar().getID());

                        client.setAvatar(null);
                        client.setWorld(null);
                    }
                }


                if (world.getEnvironments().isEmpty()) {//No one else in the world.
                    //Delete the world in the database.
                    try {
                        //No one else in the world.
                        //Delete the world in the database.
                        WorldDAO.removeWorld(world.getID());
                    } catch (SQLException ex) {
                    }

                    //Remove the world and worldMap in the buffer
                    client.getServer().removeWorldAndWorldMapFromBuffer(world.getID(), world.getGameMode());
                }

                responseCancelToJoinGame.setWorld(world);
            } else {
                System.out.println("world.getEnvironment() is null");
            }

            client.getServer().addResponseForWorld(world.getID(), responseCancelToJoinGame);
        } else {
            System.out.println("World is not active any more");
        }
    }
}
