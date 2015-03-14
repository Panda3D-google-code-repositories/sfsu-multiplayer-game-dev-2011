package networking.request;

import core.GameServer;

import java.io.IOException;

import networking.response.ResponseSeeOnlinePlayers;

/**
 *
 * @author Xuyuan
 */
public class RequestSeeOnlinePlayers extends GameRequest {

    // Responses
    private ResponseSeeOnlinePlayers responseSeeOnlinePlayers;

    public RequestSeeOnlinePlayers() {
        responses.add(responseSeeOnlinePlayers = new ResponseSeeOnlinePlayers());
    }

    @Override
    public void parse() throws IOException {
        //Nothing here.
    }

    @Override
    public void doBusiness() throws Exception {
        responseSeeOnlinePlayers.setOnlinePlayers(GameServer.getInstance().getActivePlayers());
    }
}
