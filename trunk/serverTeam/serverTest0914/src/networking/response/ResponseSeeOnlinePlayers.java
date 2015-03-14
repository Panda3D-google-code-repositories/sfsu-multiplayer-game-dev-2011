package networking.response;

import java.util.List;
import metadata.Constants;
import model.Player;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseSeeOnlinePlayers extends GameResponse {

    private List<Player> onlinePlayers;

    public ResponseSeeOnlinePlayers() {
        responseCode = Constants.SMSG_SEEONLINEPLAYERS;
    }

    public void setOnlinePlayers(List<Player> onlinePlayers) {
        this.onlinePlayers = onlinePlayers;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16((short) onlinePlayers.size());

        for (Player player : onlinePlayers) {
            packet.addInt32(player.getID());
            packet.addString(player.getUsername());
        }

        return packet.getBytes();
    }
}
