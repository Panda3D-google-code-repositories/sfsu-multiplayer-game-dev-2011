package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdatePlantNoWaterCount extends GameResponse {

    private short plantID;
    private short noWaterCount;

    public ResponseUpdatePlantNoWaterCount() {
        responseCode = Constants.SMSG_UPDATE_PLANT_NO_WATER_COUNT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(plantID);
        packet.addShort16(noWaterCount);
        return packet.getBytes();
    }

    public void setPlantID(short plantID) {
        this.plantID = plantID;
    }

    public void setNoWaterCount(short noWaterCount) {
        this.noWaterCount = noWaterCount;
    }
}
