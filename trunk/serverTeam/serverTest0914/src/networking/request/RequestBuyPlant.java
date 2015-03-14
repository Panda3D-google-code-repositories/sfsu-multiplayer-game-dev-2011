package networking.request;

import java.io.IOException;

import metadata.Constants;

import networking.response.ResponseBuyPlant;

import utility.DataReader;

import worldManager.gameEngine.GameEngine;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Xuyuan
 */
public class RequestBuyPlant extends GameRequest {

    // Data
    private short plantTypeID;
    private short zoneID;
    private float xCoor;
    private float yCoor;
    private int amount;
    // Responses
    private ResponseBuyPlant responseBuyPlant;

    public RequestBuyPlant() {
        responses.add(responseBuyPlant = new ResponseBuyPlant());
    }

    @Override
    public void parse() throws IOException {
        plantTypeID = DataReader.readShort(dataInput);
        zoneID = DataReader.readShort(dataInput);
        xCoor = DataReader.readFloat(dataInput);
        yCoor = DataReader.readFloat(dataInput);
        
        amount = 1;

        if (plantTypeID == 1005) {
            amount = 25;
        }
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
                        short status = gameEngine.buyOrganism(Constants.ORGANISM_TYPE_PLANT, client.getPlayer().getID(), plantTypeID, amount, zoneID, xCoor, yCoor);

                        responseBuyPlant.setStatus(status);
                        responseBuyPlant.setPlantTypeID(plantTypeID);
                        responseBuyPlant.setSpentAmount(tempMoney - client.getAvatar().getCurrency());
                    }
                }
            } else {
                responseBuyPlant.setStatus(1);
            }
        }
    }
}
