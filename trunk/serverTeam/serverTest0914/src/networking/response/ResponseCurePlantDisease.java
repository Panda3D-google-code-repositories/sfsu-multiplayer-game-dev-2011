package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseCurePlantDisease extends GameResponse {

    private short plantID;
    private short diseaseID;

    public ResponseCurePlantDisease() {
        responseCode = Constants.SMSG_CURE_PLANT_DISEASE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(plantID);
        packet.addShort16(diseaseID);
        return packet.getBytes();
    }

    public void setPlantID(short plantID) {
        this.plantID = plantID;
    }

    public void setDiseaseID(int diseaseID) {
        this.diseaseID = (short) diseaseID;
    }
}
