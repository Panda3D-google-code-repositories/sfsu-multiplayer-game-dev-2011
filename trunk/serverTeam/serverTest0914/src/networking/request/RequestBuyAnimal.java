package networking.request;

import java.io.IOException;

import metadata.Constants;

import networking.response.ResponseBuyAnimal;

import utility.DataReader;

import worldManager.gameEngine.GameEngine;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Xuyuan
 */
public class RequestBuyAnimal extends GameRequest {

    // Data
    private short animalTypeID;
    private short zoneID;
    private float xCoor;
    private float yCoor;
    private int amount;
    // Responses
    private ResponseBuyAnimal responseBuyAnimal;

    public RequestBuyAnimal() {
        responses.add(responseBuyAnimal = new ResponseBuyAnimal());
    }

    @Override
    public void parse() throws IOException {
        animalTypeID = DataReader.readShort(dataInput);
        zoneID = DataReader.readShort(dataInput);
        xCoor = DataReader.readFloat(dataInput);
        yCoor = DataReader.readFloat(dataInput);

        amount = 1;
    }

    @Override
    public void doBusiness() throws Exception {
        if (client.getWorld() != null) {
            GameEngine gameEngine = client.getWorld().getGameEngine();

            if (gameEngine != null) {
                Zone zone = gameEngine.getZone(zoneID);

                if (zone != null && zone.isEnable()) {
                    if (client.getPlayer().getID() == client.getWorld().getEnvByID(zone.getEnvID()).getOwnerID()) {
                        int tempMoney = client.getAvatar().getCurrency();
                        short status = gameEngine.buyOrganism(Constants.ORGANISM_TYPE_ANIMAL, client.getPlayer().getID(), animalTypeID, amount, zoneID, xCoor, yCoor);
                        responseBuyAnimal.setStatus(status);
                        responseBuyAnimal.setAnimalTypeID(animalTypeID);
                        responseBuyAnimal.setSpentAmount(tempMoney - client.getAvatar().getCurrency());
                    }
                }
            } else {
                responseBuyAnimal.setStatus(1);
            }
        }
    }
}
