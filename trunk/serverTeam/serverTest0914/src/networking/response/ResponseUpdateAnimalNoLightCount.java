package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateAnimalNoLightCount extends GameResponse {

    private short plantID;
    private short noLightCount;

    public ResponseUpdateAnimalNoLightCount() {
        responseCode = Constants.SMSG_UPDATE_ANIMAL_NO_WATER_COUNT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(plantID);
        packet.addShort16(noLightCount);
        return packet.getBytes();
    }

    public short getNoLightCount() {
        return noLightCount;
    }

    public void setNoLightCount(short noLightCount) {
        this.noLightCount = noLightCount;
    }

    public short getPlantID() {
        return plantID;
    }

    public void setPlantID(short plantID) {
        this.plantID = plantID;
    }
}
