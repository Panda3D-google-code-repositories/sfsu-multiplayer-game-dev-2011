package networking.request;

import java.io.IOException;

import model.World;
import networking.response.GameResponse;

import worldManager.gameEngine.GameEngine;

/**
 *
 * @author Xuyuan
 */
public class RequestHeartbeat extends GameRequest {

    public RequestHeartbeat() {
    }

    @Override
    public void parse() throws IOException {
        //Do nothing here.
    }

    @Override
    public void doBusiness() throws Exception {
        for (GameResponse response : client.getUpdates()) {
            try {
                client.getOutputStream().write(response.constructResponseInBytes());
            } catch (IOException ex) {
                System.err.println(ex.getMessage());
            }
        }

        World world = client.getWorld();

        if (world != null) {
            GameEngine gameEngine = world.getGameEngine();
            if (gameEngine != null) {
                gameEngine.run();
            }
        }
    }
}
