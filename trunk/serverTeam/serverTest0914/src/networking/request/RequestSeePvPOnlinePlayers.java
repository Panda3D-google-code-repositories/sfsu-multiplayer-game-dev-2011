package networking.request;

import java.io.IOException;
import java.util.List;

import networking.response.ResponseSeePvPOnlinePlayers;

/**
 *
 * @author Xuyuan
 */
public class RequestSeePvPOnlinePlayers extends GameRequest {

    // Responses
    private ResponseSeePvPOnlinePlayers responseSeePvPOnlinePlayers;

    public RequestSeePvPOnlinePlayers() {
        responses.add(responseSeePvPOnlinePlayers = new ResponseSeePvPOnlinePlayers());
    }

    @Override
    public void parse() throws IOException {
        //Do nothing here.
    }

    @Override
    public void doBusiness() throws Exception {
        List<String> onlinePlayers;
        onlinePlayers = client.getServer().getOnlinePlayersByCurrentPlayerLocation(1);//(0=MainLobby; 1=PvP Game Mode Lobby; 2=PvE Game Mode Lobby; 3=PvP World Lobby & PvP World; 4=PvE World Lobby & PvE World)
        responseSeePvPOnlinePlayers.setPvpPlayers(onlinePlayers);
    }
}
