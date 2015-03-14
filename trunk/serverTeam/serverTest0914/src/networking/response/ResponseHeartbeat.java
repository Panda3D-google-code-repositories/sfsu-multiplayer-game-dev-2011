package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseHeartbeat extends GameResponse {

    public ResponseHeartbeat() {
        responseCode = Constants.SMSG_HEARTBEAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        //If clients get this response, it does nothing.
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16((short) 0);
        return packet.getBytes();
    }
}
