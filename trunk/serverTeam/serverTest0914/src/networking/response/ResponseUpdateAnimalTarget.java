package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateAnimalTarget extends GameResponse {

    private short status;//0 means success, 1 means fail

    public ResponseUpdateAnimalTarget() {
        responseCode = Constants.SMSG_UPDATE_ANIMAL_TARGET;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        return packet.getBytes();
    }

    public short getStatus() {
        return status;
    }

    public void setStatus(short status) {
        this.status = status;
    }
}
