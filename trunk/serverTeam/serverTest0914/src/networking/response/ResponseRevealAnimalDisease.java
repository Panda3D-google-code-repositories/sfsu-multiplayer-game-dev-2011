package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseRevealAnimalDisease extends GameResponse {

    private short animalID;
    private short diseaseID;

    public ResponseRevealAnimalDisease() {
        responseCode = Constants.SMSG_REVEAL_ANIMAL_DISEASE;
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
