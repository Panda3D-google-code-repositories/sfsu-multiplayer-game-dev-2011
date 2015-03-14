package networking.request;

import java.io.IOException;
import java.util.ArrayList;

import metadata.Constants;

import model.World;
import networking.response.ResponseGetPvEWorlds;

/**
 *
 * @author Xuyuan
 */
public class RequestGetPvEWorlds extends GameRequest {

    // Responses
    private ResponseGetPvEWorlds responseGetPvEWorlds;

    public RequestGetPvEWorlds() {
        responses.add(responseGetPvEWorlds = new ResponseGetPvEWorlds());
    }

    @Override
    public void parse() throws IOException {
        //Nothing here.
    }

    @Override
    public void doBusiness() throws Exception {
        responseGetPvEWorlds.setPublicPvEWorlds(new ArrayList<World>(client.getServer().getActivePvEWorld().values()));

        //Set the player's current position 2(2 means in the pve game mode lobby.)
        client.getServer().trackPlayerPosition(client.getPlayer().getID(), Constants.LOCATION_PVE_G_LOBBY);
    }
}
