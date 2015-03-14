package networking.response;

import utility.GamePacket;
import metadata.Constants;

/**
 * This class extends GameResponse and is responsible for handle the regist response.
 *
 * @author , Xuyuan
 */
public class ResponseRegist extends GameResponse {

    private short status;

    public ResponseRegist() {
        responseCode = Constants.SMSG_REGISTER;
    }
    /*
     * Return the response in the format of bytes.
     */

    public void setStatus(short status) {
        this.status = status;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

        return packet.getBytes();
    }
}