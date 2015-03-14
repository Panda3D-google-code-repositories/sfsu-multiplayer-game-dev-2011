package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateOnlinePlayer extends GameResponse {

    public ResponseUpdateOnlinePlayer() {
        responseCode = Constants.SMSG_UPDATE_ONLINE_PLAYERS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16((short) 0);
        return packet.getBytes();
    }
}
