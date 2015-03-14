package networking.response;

import java.util.ArrayList;
import java.util.List;
import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseSeePvPOnlinePlayers extends GameResponse {

    private short numberOfPlayers;
    private List<String> pvpPlayers;

    public ResponseSeePvPOnlinePlayers() {
        responseCode = Constants.SMSG_SEE_PVP_ONLINE_PLAYERS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        if (pvpPlayers != null) {
            numberOfPlayers = (short) pvpPlayers.size();
            packet.addShort16(numberOfPlayers);
            for (String player : pvpPlayers) {
                packet.addString(player);
            }
        }

        return packet.getBytes();
    }

    public void setPvpPlayers(List<String> pvpPlayers) {
        this.pvpPlayers = pvpPlayers;
    }
}
