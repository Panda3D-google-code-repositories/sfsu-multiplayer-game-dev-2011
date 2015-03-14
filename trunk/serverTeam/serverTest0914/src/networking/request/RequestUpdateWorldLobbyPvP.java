package networking.request;

import java.io.IOException;

import model.World;
import networking.response.ResponseUpdateWorldLobbyPvP;
import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestUpdateWorldLobbyPvP extends GameRequest {

    // Data
    private String worldName;
    // Responses
    private ResponseUpdateWorldLobbyPvP responseUpdateWorldLobbyPvP;

    public RequestUpdateWorldLobbyPvP() {
        responses.add(responseUpdateWorldLobbyPvP = new ResponseUpdateWorldLobbyPvP());
    }

    @Override
    public void parse() throws IOException {
        worldName = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        World pvpWorld = client.getServer().getActivePvPWorld(worldName);

        if (pvpWorld != null) {
        }
    }
}
