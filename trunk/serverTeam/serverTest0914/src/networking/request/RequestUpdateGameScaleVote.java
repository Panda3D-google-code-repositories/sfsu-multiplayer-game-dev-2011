package networking.request;

import java.io.IOException;

import networking.response.ResponseUpdateGameScaleVote;
import utility.DataReader;
import worldManager.gameEngine.GameEngine;

/**
 *
 * @author Xuyuan
 */
public class RequestUpdateGameScaleVote extends GameRequest {

    // Data
    private short avatarID;
    private short vote;
    // Responses
    private ResponseUpdateGameScaleVote responseUpdateGameScaleVote;

    public RequestUpdateGameScaleVote() {
        responses.add(responseUpdateGameScaleVote = new ResponseUpdateGameScaleVote());
    }

    @Override
    public void parse() throws IOException {
        avatarID = DataReader.readShort(dataInput);
        vote = DataReader.readShort(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        GameEngine gameEngine = client.getWorld().getGameEngine();

        if (gameEngine != null) {
            gameEngine.run();
            gameEngine.updateGameScaleVote(avatarID, vote);
        }
    }
}
