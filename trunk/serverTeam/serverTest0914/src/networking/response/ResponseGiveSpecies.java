package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Gary
 */
public class ResponseGiveSpecies extends GameResponse {

    private short status;

    public ResponseGiveSpecies() {
        responseCode = Constants.SMSG_GIVE_SPECIES;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }
}
