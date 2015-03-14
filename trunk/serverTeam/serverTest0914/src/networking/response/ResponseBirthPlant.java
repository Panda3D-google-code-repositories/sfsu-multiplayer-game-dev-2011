package networking.response;

import metadata.Constants;
import utility.GamePacket;
import worldManager.gameEngine.species.Plant;

/**
 *
 * @author Xuyuan
 */
public class ResponseBirthPlant extends GameResponse {

    private Plant plant;
    private short status;
    private int count;

    public ResponseBirthPlant() {
        responseCode = Constants.SMSG_BIRTH_PLANT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        packet.addInt32(plant.getID());
        packet.addString(plant.getSpeciesType().getSpeciesName());
        packet.addShort16((short) plant.getSpeciesType().getModelID());
        packet.addShort16((short) plant.getSpeciesTypeID());
        packet.addInt32(plant.getPlayerID());
        packet.addInt32(plant.getZoneID());
        packet.addShort16((short) plant.getBiomass());
        packet.addFloat(plant.getX());
        packet.addFloat(plant.getY());
        packet.addFloat(plant.getZ());
        packet.addShort16((short) plant.getGroupSize());
        packet.addShort16((short) count);

        return packet.getBytes();
    }
    
    public void setCount(int count) {
        this.count = count;
    }

    public void setPlant(Plant plant) {
        this.plant = plant;
    }

    public void setStatus(short status) {
        this.status = status;
    }
}
