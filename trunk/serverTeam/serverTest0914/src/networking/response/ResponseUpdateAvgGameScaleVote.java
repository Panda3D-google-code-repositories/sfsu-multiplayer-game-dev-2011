package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateAvgGameScaleVote extends GameResponse {

    private short avgVote;

    public ResponseUpdateAvgGameScaleVote() {
        responseCode = Constants.SMSG_UPDATE_AVG_GAME_SCALE_VOTE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(avgVote);
        return packet.getBytes();
    }
}
