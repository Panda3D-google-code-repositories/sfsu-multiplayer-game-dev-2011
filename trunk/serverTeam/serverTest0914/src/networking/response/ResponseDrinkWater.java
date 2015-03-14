package networking.response;

import metadata.Constants;
import utility.GamePacket;
import worldManager.gameEngine.species.Organism;

/**
 *
 * @author Gary
 */
public class ResponseDrinkWater extends GameResponse {

    private Organism species;

    public ResponseDrinkWater() {
        responseCode = Constants.SMSG_DRINK_WATER;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(species.getID());

        return packet.getBytes();
    }

    public void setSpecies(Organism species) {
        this.species = species;
    }
}
