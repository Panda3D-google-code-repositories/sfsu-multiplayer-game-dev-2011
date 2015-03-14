package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateAnimalOwner extends GameResponse {

    private short animalID;
    private short newAvatarID;

    public ResponseUpdateAnimalOwner() {
        responseCode = Constants.SMSG_UPDATE_ANIMAL_OWNER;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(animalID);
        packet.addShort16(newAvatarID);
        return packet.getBytes();
    }

    public void setAnimalID(int animalID) {
        this.animalID = (short) animalID;
    }

    public void setNewAvatarID(int newAvatarID) {
        this.newAvatarID = (short) newAvatarID;
    }
}
