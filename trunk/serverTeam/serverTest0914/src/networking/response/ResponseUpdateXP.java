package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateXP extends GameResponse {

    private int amount;
    private int total;

    public ResponseUpdateXP() {
        responseCode = Constants.SMSG_UPDATE_XP;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(amount);
        packet.addInt32(total);
        return packet.getBytes();
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public void setTotal(int total) {
        this.total = total;
    }
}
