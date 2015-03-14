package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateAnimalZone extends GameResponse {

    private short animalID;
    private short newZoneID;

    public ResponseUpdateAnimalZone() {
        responseCode = Constants.SMSG_UPDATE_ANIMAL_ZONE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(animalID);
        packet.addShort16(newZoneID);
        return packet.getBytes();
    }

    public void setNewZoneID(short newZoneID) {
        this.newZoneID = newZoneID;
    }

    public void setAnimalID(short animalID) {
        this.animalID = animalID;
    }
}
