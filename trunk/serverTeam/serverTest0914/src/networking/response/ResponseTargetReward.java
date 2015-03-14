package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Gary
 */
public class ResponseTargetReward extends GameResponse {

    private int target_id;
    private short type;
    private int amount;

    public ResponseTargetReward() {
        responseCode = Constants.SMSG_TARGET_REWARD;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(target_id);
        packet.addShort16(type);
        packet.addInt32(amount);
        return packet.getBytes();
    }

    public void setTargetID(int target_id) {
        this.target_id = target_id;
    }

    public void setType(short type) {
        this.type = type;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
}
