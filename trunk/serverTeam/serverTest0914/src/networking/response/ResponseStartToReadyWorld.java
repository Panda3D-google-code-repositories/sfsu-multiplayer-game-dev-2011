package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseStartToReadyWorld extends GameResponse {

    private short status;

    public ResponseStartToReadyWorld() {
        responseCode = Constants.SMSG_START_TO_READY_GAME;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }
}
