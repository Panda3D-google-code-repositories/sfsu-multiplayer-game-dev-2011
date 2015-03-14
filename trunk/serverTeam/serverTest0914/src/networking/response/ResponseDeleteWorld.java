package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Gary
 */
public class ResponseDeleteWorld extends GameResponse {

    private short status;
    private int world_id;

    public ResponseDeleteWorld() {
        responseCode = Constants.SMSG_DELETE_WORLD;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        packet.addInt32(world_id);

        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }

    public void setWorldID(int world_id) {
        this.world_id = world_id;
    }
}
