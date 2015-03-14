package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateGameScaleVote extends GameResponse {

    private short avgVote;

    public ResponseUpdateGameScaleVote() {
        responseCode = Constants.SMSG_VOTE_GAME_SCALE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(avgVote);
        return packet.getBytes();
    }

    public void setAvgVote(short avgVote) {
        this.avgVote = avgVote;
    }
}
