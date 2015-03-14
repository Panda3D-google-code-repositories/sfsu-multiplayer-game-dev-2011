package networking.request;

import java.io.IOException;
import java.util.List;

import networking.response.ResponseSeePvEOnlinePlayers;

/**
 *
 * @author Xuyuan
 */
public class RequestSeePvEOnlinePlayers extends GameRequest {

    // Responses
    private ResponseSeePvEOnlinePlayers responseSeePvEOnlinePlayers;

    public RequestSeePvEOnlinePlayers() {
        responses.add(responseSeePvEOnlinePlayers = new ResponseSeePvEOnlinePlayers());
    }

    @Override
    public void parse() throws IOException {
        //Do nothing here.
    }

    @Override
    public void doBusiness() throws Exception {
        List<String> onlinePlayers;
        onlinePlayers = client.getServer().getOnlinePlayersByCurrentPlayerLocation(2);//(0=MainLobby; 1=PvP Game Mode Lobby; 2=PvE Game Mode Lobby; 3=PvP World Lobby & PvP World; 4=PvE World Lobby & PvE World)
        responseSeePvEOnlinePlayers.setPvEPlayers(onlinePlayers);
    }
}
