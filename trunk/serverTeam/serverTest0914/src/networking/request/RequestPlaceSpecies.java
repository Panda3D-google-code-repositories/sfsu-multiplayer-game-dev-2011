package networking.request;

import java.io.IOException;

import networking.response.ResponsePlaceSpecies;
import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestPlaceSpecies extends GameRequest {

    // Data
    private short animalID;
    private short zoneID;
    private short xCoor;
    private short yCoor;
    // Responses
    private ResponsePlaceSpecies responsePlaceAnimal;

    public RequestPlaceSpecies() {
        responses.add(responsePlaceAnimal = new ResponsePlaceSpecies());
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
        //TO DO 
    }
}
