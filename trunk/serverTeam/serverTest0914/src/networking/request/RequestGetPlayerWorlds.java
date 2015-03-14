package networking.request;

import dataAccessLayer.WorldDAO;

import java.io.IOException;

import metadata.Constants;

import networking.response.ResponseGetPlayerWorlds;
import utility.DataReader;

/**
 *
 * @author Gary
 */
public class RequestGetPlayerWorlds extends GameRequest {

    // Data
    private int player_id;
    // Responses
    private ResponseGetPlayerWorlds responseGetPlayerWorlds;

    public RequestGetPlayerWorlds() {
        responses.add(responseGetPlayerWorlds = new ResponseGetPlayerWorlds());
    }

    @Override
    public void parse() throws IOException {
        player_id = DataReader.readInt(dataInput);

        if (player_id == 0) {
            player_id = client.getPlayer().getID();
        }
    }

    @Override
    public void doBusiness() throws Exception {
        responseGetPlayerWorlds.setWorlds(WorldDAO.getPlayerWorlds(player_id));

        client.getServer().trackPlayerPosition(client.getPlayer().getID(), Constants.LOCATION_PVE_G_LOBBY);
    }
}
