package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseSetUserPrimaryAvatar extends GameResponse {

    private short isTrue;//0 means not true, 1 means true

    public ResponseSetUserPrimaryAvatar() {
        responseCode = Constants.SMSG_SET_USER_PRIMARY_AVATAR;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(isTrue);
        return packet.getBytes();
    }

    public void setIsTrue(int isTrue) {
        this.isTrue = (short) isTrue;
    }
}
