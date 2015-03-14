package networking.request;

import dataAccessLayer.WorldDAO;
import dataAccessLayer.WorldMapDAO;

import java.io.IOException;

import metadata.Constants;

import model.PvEWorldMap;
import model.PvPWorldMap;
import model.World;

import networking.response.ResponseCreateNewWorld;

import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestCreateNewWorld extends GameRequest {

    // Data
    private World world;//Store the world information the client sends to server.
    // Responses
    private ResponseCreateNewWorld responseCreateNewWorld;

    public RequestCreateNewWorld() {
        world = new World(-1);
        responses.add(responseCreateNewWorld = new ResponseCreateNewWorld());
    }

    @Override
    public void parse() throws IOException {
        short worldType = DataReader.readShort(dataInput);

        if (worldType == 1) {
            world.setGameMode(Constants.GAME_TYPE_PVE);
        } else if (worldType == 2) {
            world.setGameMode(Constants.GAME_TYPE_PVP);
        }

        String name = DataReader.readString(dataInput);
        if (name.equals(".random")) {
            name = String.valueOf(client.getPlayer().getID()) + "_" + System.currentTimeMillis() % 100000;
        }
        world.setGameName(name);

        world.setMaxPlayers(DataReader.readShort(dataInput));
        world.setEnvType(DataReader.readString(dataInput));
        world.setAccessType(DataReader.readShort(dataInput));

        if (world.getAccessType() == Constants.PRIVACY_TYPE_PRIVATE) {
            world.setPassword(DataReader.readString(dataInput));
        }
    }

    @Override
    public void doBusiness() throws Exception {
        if (WorldDAO.containsWorldName(world.getGameName())) {
            responseCreateNewWorld.setStatus((short) 1);//World name is occupied.
            responseCreateNewWorld.setWorld(world);
        } else {
            responseCreateNewWorld.setStatus((short) 0);//World name is usable.
            responseCreateNewWorld.setWorld(world);
            responseCreateNewWorld.setCharName(client.getPlayer().getUsername());

            //Save world to database
            world.setCreatorID(client.getPlayer().getID());

            int world_id = WorldDAO.createWorld(world);
            world.setID(world_id);

            if (world.getGameMode() == Constants.GAME_TYPE_PVP) {
                client.getServer().addToActivePvPWorld(world);

                //Create a pvp map for this world
                PvPWorldMap pvpMap = new PvPWorldMap(world.getID(), world.getMaxPlayers());
                client.getServer().addPvPWorldMap(pvpMap);

                WorldMapDAO.savePvPWorldMap(pvpMap);
            } else if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
                client.getServer().addToActivePvEWorld(world);

                //Create a pve map for this world
                PvEWorldMap pveMap = new PvEWorldMap(world.getID());
                client.getServer().addPvEWorldMap(pveMap);

                WorldMapDAO.savePvEWorldMap(pveMap);
            }

            world.setGameEngine(client.getServer().createGameEngine(world));

            //Track the current position of this player.
            if (world.getGameMode() == Constants.GAME_TYPE_PVP) {
                client.getServer().trackPlayerPosition(client.getPlayer().getID(), Constants.LOCATION_PVP_W_LOBBY);
            } else if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
                client.getServer().trackPlayerPosition(client.getPlayer().getID(), Constants.LOCATION_PVE_W_LOBBY);
            }
        }
    }
}
