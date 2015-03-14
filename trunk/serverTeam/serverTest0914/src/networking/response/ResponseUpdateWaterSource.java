package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateWaterSource extends GameResponse {

    private short waterSourceID;
    private short zoneID;
    private short waterAmount;
    private short targetWaterAmount;
    private short targetTime;

    public ResponseUpdateWaterSource() {
        responseCode = Constants.SMSG_UPDATE_WATER_SOURCE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(waterSourceID);
        packet.addShort16(zoneID);
        packet.addShort16(waterAmount);
        packet.addShort16(targetWaterAmount);
        packet.addShort16(targetTime);
        return packet.getBytes();
    }

    public void setTargetWaterAmount(short targetWaterAmount) {
        this.targetWaterAmount = targetWaterAmount;
    }

    public void setWaterAmount(short waterAmount) {
        this.waterAmount = waterAmount;
    }

    public void setWaterSourceID(short waterSourceID) {
        this.waterSourceID = waterSourceID;
    }

    public void setZoneID(short zoneID) {
        this.zoneID = zoneID;
    }

    public void setTargetTime(short targetTime) {
        this.targetTime = targetTime;
    }
}
