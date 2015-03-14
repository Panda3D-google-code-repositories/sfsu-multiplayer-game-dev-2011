package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateAnimalNoWaterCount extends GameResponse {

    private short plantID;
    private short noWaterCount;

    public ResponseUpdateAnimalNoWaterCount() {
        responseCode = Constants.SMSG_UPDATE_ANIMAL_NO_WATER_COUNT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(plantID);
        packet.addShort16(noWaterCount);
        return packet.getBytes();
    }

    public short getNoWaterCount() {
        return noWaterCount;
    }

    public void setNoWaterCount(short noWaterCount) {
        this.noWaterCount = noWaterCount;
    }

    public short getPlantID() {
        return plantID;
    }

    public void setPlantID(short plantID) {
        this.plantID = plantID;
    }
}
