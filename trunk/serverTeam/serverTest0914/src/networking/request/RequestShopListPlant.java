package networking.request;

import core.GameServer;

import dataAccessLayer.ShopDAO;

import java.io.IOException;
import java.util.List;

import model.PlantType;

import networking.response.ResponseShopListPlant;

/**
 *
 * @author Xuyuan
 */
public class RequestShopListPlant extends GameRequest {

    // Responses
    private ResponseShopListPlant responseShopListPlant;

    public RequestShopListPlant() {
        responses.add(responseShopListPlant = new ResponseShopListPlant());
    }

    @Override
    public void parse() throws IOException {
        //Do Nothing here.
    }

    @Override
    public void doBusiness() throws Exception {
        List<PlantType> plantList = ShopDAO.getPlantsUpToLevel(client.getAvatar().getLevel());
//        plantList.addAll(GameServer.getInstance().getPlantTypes());
        responseShopListPlant.setAllPlantType(plantList);
    }
}
