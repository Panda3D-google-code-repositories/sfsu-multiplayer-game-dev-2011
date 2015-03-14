package networking.request;

import java.io.IOException;
import java.util.ArrayList;

import metadata.Constants;

import model.World;
import networking.response.ResponseGetPvPWorlds;

/**
 *
 * @author Xuyuan
 */
public class RequestGetPvPWorlds extends GameRequest {

    // Responses
    private ResponseGetPvPWorlds responseGetPvPWorlds;

    public RequestGetPvPWorlds() {
        responses.add(responseGetPvPWorlds = new ResponseGetPvPWorlds());
    }

    @Override
    public void parse() throws IOException {
        //Nothing here.
    }

    @Override
    public void doBusiness() throws Exception {
        responseGetPvPWorlds.setPvpWorlds(new ArrayList<World>(client.getServer().getActivePvPWorld().values()));

        //Set the player's current position 1(1 means in the pvp game mode lobby.)
        client.getServer().trackPlayerPosition(client.getPlayer().getID(), Constants.LOCATION_PVP_G_LOBBY);
    }
}
