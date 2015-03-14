package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Gary
 */
public class ResponseRestart extends GameResponse {

    private boolean status;

    public ResponseRestart() {
        responseCode = Constants.SMSG_RESTART;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addBoolean(status);

        return packet.getBytes();
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
}
