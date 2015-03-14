package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdatePlantNoLightCount extends GameResponse {

    private short plantID;
    private short noLightCount;

    public ResponseUpdatePlantNoLightCount() {
        responseCode = Constants.SMSG_UPDATE_PLANT_NO_LIGHT_COUNT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(plantID);
        packet.addShort16(noLightCount);
        return packet.getBytes();
    }

    public void setPlantID(short plantID) {
        this.plantID = plantID;
    }

    public void setNoLightCount(short noLightCount) {
        this.noLightCount = noLightCount;
    }
}
