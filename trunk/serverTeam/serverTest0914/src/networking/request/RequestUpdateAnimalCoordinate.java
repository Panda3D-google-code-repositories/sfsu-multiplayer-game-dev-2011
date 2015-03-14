package networking.request;

import java.io.IOException;

import networking.response.ResponseUpdateAnimalCoordinate;
import utility.DataReader;
import worldManager.gameEngine.GameEngine;

/**
 *
 * @author Xuyuan
 */
public class RequestUpdateAnimalCoordinate extends GameRequest {

    // Data
    private int animalID;
    private int zoneID;
    private int xCoor;
    private int yCoor;
    // Responses
    private ResponseUpdateAnimalCoordinate responseUpdateAnimalCoordinate;

    public RequestUpdateAnimalCoordinate() {
        responses.add(responseUpdateAnimalCoordinate = new ResponseUpdateAnimalCoordinate());
    }

    @Override
    public void parse() throws IOException {
        animalID = DataReader.readShort(dataInput);
        zoneID = DataReader.readShort(dataInput);
        xCoor = DataReader.readShort(dataInput);
        yCoor = DataReader.readShort(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        GameEngine gameEngine = client.getWorld().getGameEngine();

        if (gameEngine != null) {
            gameEngine.run();
            gameEngine.updateAnimalCoors(animalID, zoneID, xCoor, yCoor);
        }
    }
}
