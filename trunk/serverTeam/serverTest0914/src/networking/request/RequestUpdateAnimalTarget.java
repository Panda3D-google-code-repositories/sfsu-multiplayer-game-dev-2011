package networking.request;

import java.io.IOException;

import networking.response.ResponseUpdateAnimalTarget;
import utility.DataReader;
import worldManager.gameEngine.GameEngine;

/**
 *
 * @author Xuyuan
 */
public class RequestUpdateAnimalTarget extends GameRequest {

    // Data
    private int animalID;
    private int zoneID;
    private int xTarg;
    private int yTarg;
    // Responses
    private ResponseUpdateAnimalTarget responseUpdateAnimalTarget;

    public RequestUpdateAnimalTarget() {
        responses.add(responseUpdateAnimalTarget = new ResponseUpdateAnimalTarget());
    }

    @Override
    public void parse() throws IOException {
        animalID = DataReader.readShort(dataInput);
        zoneID = DataReader.readShort(dataInput);
        xTarg = DataReader.readShort(dataInput);
        yTarg = DataReader.readShort(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        GameEngine gameEngine = client.getWorld().getGameEngine();

        if (gameEngine != null) {
            gameEngine.run();
            gameEngine.updateAnimalTarget(animalID, zoneID, xTarg, yTarg);
        }
    }
}
