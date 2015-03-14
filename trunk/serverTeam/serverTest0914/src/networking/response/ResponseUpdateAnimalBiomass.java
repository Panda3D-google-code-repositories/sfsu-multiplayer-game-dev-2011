package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateAnimalBiomass extends GameResponse {

    private short animalID;
    private short biomass;
    private short targetBiomass;
    private short targetTime;

    public ResponseUpdateAnimalBiomass() {
        responseCode = Constants.SMSG_UPDATE_ANIMAL_BIOMASS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(animalID);
        packet.addShort16(biomass);
        packet.addShort16(targetBiomass);
        packet.addShort16(targetTime);

        return packet.getBytes();
    }

    public void setAnimalID(int animalID) {
        this.animalID = (short) animalID;
    }

    public void setBiomass(int biomass) {
        this.biomass = (short) biomass;
    }

    public void setTargetBiomass(int targetBiomass) {
        this.targetBiomass = (short) targetBiomass;
    }

    public void setTargetTime(long targetTime) {
        this.targetTime = (short) targetTime;
    }
}
