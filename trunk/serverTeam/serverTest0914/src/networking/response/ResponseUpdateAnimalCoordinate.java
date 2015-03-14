package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateAnimalCoordinate extends GameResponse {

    private short status;//0 means success; 1 means fail.

    public ResponseUpdateAnimalCoordinate() {
        responseCode = Constants.SMSG_UPDATE_ANIMAL_COORDINATE;
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

    public void setStatus(int status) {
        this.status = (short) status;
    }
}
