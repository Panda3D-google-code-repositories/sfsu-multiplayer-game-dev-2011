package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseCureAnimalDisease extends GameResponse {

    private short animalID;
    private short diseaseID;

    public ResponseCureAnimalDisease() {
        responseCode = Constants.SMSG_CURE_ANIMAL_DISEASE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(animalID);
        packet.addShort16(diseaseID);
        return packet.getBytes();
    }

    public void setAnimalID(int animalID) {
        this.animalID = (short) animalID;
    }

    public void setDiseaseID(int diseaseID) {
        this.diseaseID = (short) diseaseID;
    }
}
