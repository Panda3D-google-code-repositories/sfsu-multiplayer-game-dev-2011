package networking.request;

import core.GameServer;

import java.io.IOException;

import model.World;

/**
 *
 * @author Gary
 */
public class RequestLeaveWorld extends GameRequest {

    // Data
    // Responses
    public RequestLeaveWorld() {
    }

    @Override
    public void parse() throws IOException {
    }

    @Override
    public void doBusiness() throws Exception {
        World world = client.getWorld();

        if (world != null) {
            world.removePlayer(client.getPlayer().getID());

            if (world.getPlayers().isEmpty()) {
                GameServer.getInstance().removeWorldAndWorldMapFromBuffer(world.getID(), world.getGameMode());
            }
        }
    }
}
