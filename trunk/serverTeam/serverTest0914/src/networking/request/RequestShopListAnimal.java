package networking.request;

import dataAccessLayer.ShopDAO;

import java.io.IOException;
import java.util.List;

import model.AnimalType;

import networking.response.ResponseShopListAnimal;

/**
 *
 * @author Xuyuan
 */
public class RequestShopListAnimal extends GameRequest {

    // Responses
    private ResponseShopListAnimal responseShopListAnimal;

    public RequestShopListAnimal() {
        responses.add(responseShopListAnimal = new ResponseShopListAnimal());
    }

    @Override
    public void parse() throws IOException {
        //Do Nothing here.
    }

    @Override
    public void doBusiness() throws Exception {
        List<AnimalType> animalList = ShopDAO.getAnimalsUpToLevel(client.getAvatar().getLevel());
        responseShopListAnimal.setAllAnimalType(animalList);
    }
}
