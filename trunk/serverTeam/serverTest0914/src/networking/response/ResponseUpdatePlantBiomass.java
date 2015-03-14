package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdatePlantBiomass extends GameResponse {

    private short plantID;
    private short biomass;
    private short targetBiomass;
    private short targetTime;

    public ResponseUpdatePlantBiomass() {
        responseCode = Constants.SMSG_UPDATE_PLANT_BIOMASS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(plantID);
        packet.addShort16(biomass);
        packet.addShort16(targetBiomass);
        packet.addShort16(targetTime);

        return packet.getBytes();
    }

    public void setPlantID(short plantID) {
        this.plantID = plantID;
    }

    public void setBiomass(int biomass) {
        this.biomass = (short) biomass;
    }

    public void setTargetBiomass(int targetBiomass) {
        this.targetBiomass = (short) targetBiomass;
    }

    public void setTargetTime(int targetTime) {
        this.targetTime = (short) targetTime;
    }
}
