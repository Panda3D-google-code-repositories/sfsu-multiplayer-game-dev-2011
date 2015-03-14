package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateCash extends GameResponse {

    private int amount;
    private int cash;

    public ResponseUpdateCash() {
        responseCode = Constants.SMSG_UPDATE_CASH;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(amount);
        packet.addInt32(cash);
        return packet.getBytes();
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public void setCash(int cash) {
        this.cash = cash;
    }
}
