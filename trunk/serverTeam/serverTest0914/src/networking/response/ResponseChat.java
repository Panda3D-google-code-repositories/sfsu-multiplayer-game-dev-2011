package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseChat extends GameResponse {

    private short status;
    private String name;
    private String message;
    private short type;

    public ResponseChat() {
        responseCode = Constants.SMSG_CHAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        packet.addShort16(type);

        if (type == 0) {
            packet.addString(name);
            packet.addString(message);
        } else {
            packet.addString(message);
        }
        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }

    public String setName(String name) {
        return this.name = name;
    }

    public String setMessage(String message) {
        return this.message = message;
    }

    public void setType(short type) {
        this.type = type;
    }
}
