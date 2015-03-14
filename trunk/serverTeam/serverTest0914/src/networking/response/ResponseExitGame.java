package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseExitGame extends GameResponse {

    private short status = 0;

    public ResponseExitGame() {
        responseCode = Constants.SMSG_SAVE_EXIT_GAME;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        return packet.getBytes();
    }
}
