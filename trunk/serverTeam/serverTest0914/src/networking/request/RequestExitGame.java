package networking.request;

import java.io.IOException;

import networking.response.ResponseExitGame;

/**
 *
 * @author Xuyuan
 */
public class RequestExitGame extends GameRequest {

    // Responses
    private ResponseExitGame responseExitGame;

    public RequestExitGame() {
        responses.add(responseExitGame = new ResponseExitGame());
    }

    @Override
    public void parse() throws IOException {
    }

    @Override
    public void doBusiness() throws Exception {
        client.stopClient();
    }
}
