package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateGameScaleTime extends GameResponse {

    private long time;

    public ResponseUpdateGameScaleTime() {
        responseCode = Constants.SMSG_UPDATE_GAME_SCALE_TIME;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addLong(time);
        return packet.getBytes();
    }

    public void setTime(long time) {
        this.time = (long) time;
    }
}
