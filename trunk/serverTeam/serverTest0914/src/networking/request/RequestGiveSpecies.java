package networking.request;

import core.GameServer;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import metadata.Constants;
import networking.response.ResponseGiveSpecies;
import utility.DataReader;

import worldManager.gameEngine.Zone;
import worldManager.gameEngine.species.Organism;

/**
 *
 * @author Gary
 */
public class RequestGiveSpecies extends GameRequest {

    // Data
    private int zone_id;
    private int player_id;
    private short size;
    private HashMap<Integer, Short> speciesList;
    // Responses
    private ResponseGiveSpecies responseGiveSpecies;

    public RequestGiveSpecies() {
        speciesList = new HashMap<Integer, Short>();
        responses.add(responseGiveSpecies = new ResponseGiveSpecies());
    }

    @Override
    public void parse() throws IOException {
        zone_id = DataReader.readInt(dataInput);
        player_id = DataReader.readInt(dataInput);
        size = DataReader.readShort(dataInput);

        for (int i = 0; i < size; i++) {
            int speciesTypeID = DataReader.readInt(dataInput);
            short organism_type = DataReader.readShort(dataInput);
            short amount = DataReader.readShort(dataInput);

            if (organism_type == Constants.ORGANISM_TYPE_PLANT) {
                speciesList.put(Constants.MODIFIER_PLANT + speciesTypeID, amount);
            } else if (organism_type == Constants.ORGANISM_TYPE_ANIMAL) {
                speciesList.put(Constants.MODIFIER_ANIMAL + speciesTypeID, amount);
            }
        }
    }

    @Override
    public void doBusiness() throws Exception {
        Zone zone = client.getWorld().getGameEngine().getZone(zone_id);

        if (zone != null) {
            for (int speciesTypeID : speciesList.keySet()) {
                short organism_type = 0;
                Integer amount = null;

                if (speciesTypeID / Constants.MODIFIER_PLANT == 1) {
                    organism_type = Constants.ORGANISM_TYPE_PLANT;
                    amount = zone.getTotalSpeciesCount(speciesTypeID);
                } else if (speciesTypeID / Constants.MODIFIER_ANIMAL == 1) {
                    organism_type = Constants.ORGANISM_TYPE_ANIMAL;
                    amount = zone.getTotalSpeciesCount(speciesTypeID);
                }

                if (amount != null) {
                    amount = Math.min(amount, speciesList.get(speciesTypeID));
                    int removeCount = Math.max(0, amount - speciesList.get(speciesTypeID));
                    
                    List<Organism> moveSpeciesList = new ArrayList<Organism>();
                    if (organism_type == Constants.ORGANISM_TYPE_PLANT) {
                        moveSpeciesList = zone.getPlantsByType(speciesTypeID % Constants.MODIFIER_PLANT);
                    } else if (organism_type == Constants.ORGANISM_TYPE_ANIMAL) {
                        moveSpeciesList = zone.getAnimalsByType(speciesTypeID % Constants.MODIFIER_ANIMAL);
                    }
                    
                    for (int i = removeCount; i > 0; ) {
                        if (moveSpeciesList.isEmpty()) {
                            break;
                        }
                    }
                }
            }
        }
    }
}
