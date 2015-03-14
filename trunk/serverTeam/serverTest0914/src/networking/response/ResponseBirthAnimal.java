package networking.response;

import metadata.Constants;
import utility.GamePacket;
import worldManager.gameEngine.species.Animal;

/**
 *
 * @author Xuyuan
 */
public class ResponseBirthAnimal extends GameResponse {

    private Animal animal;
    private short status;
    private int count;

    public ResponseBirthAnimal() {
        responseCode = Constants.SMSG_BIRTH_ANIMAL;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        packet.addInt32(animal.getID());
        packet.addString(animal.getSpeciesType().getSpeciesName());
        packet.addShort16((short) animal.getSpeciesType().getModelID());
        packet.addShort16((short) animal.getSpeciesTypeID());
        packet.addInt32(animal.getPlayerID());
        packet.addInt32(animal.getZoneID());
        packet.addShort16((short) animal.getBiomass());
        packet.addFloat(animal.getX());
        packet.addFloat(animal.getY());
        packet.addFloat(animal.getZ());
        packet.addShort16((short) animal.getGroupSize());
        packet.addShort16((short) count);

        return packet.getBytes();
    }
    
    public void setCount(int count) {
        this.count = count;
    }

    public void setAnimal(Animal animal) {
        this.animal = animal;
    }

    public void setStatus(short status) {
        this.status = status;
    }
}
