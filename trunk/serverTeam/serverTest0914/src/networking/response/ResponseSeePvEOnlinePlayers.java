package networking.response;

import java.util.ArrayList;
import java.util.List;
import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseSeePvEOnlinePlayers extends GameResponse {

    private short numberOfPlayers;
    private List<String> pvePlayers;

    public ResponseSeePvEOnlinePlayers() {
        responseCode = Constants.SMSG_SEE_PVE_ONLINE_PLAYERS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        if (pvePlayers != null) {
            numberOfPlayers = (short) pvePlayers.size();
            packet.addShort16(numberOfPlayers);
            for (String player : pvePlayers) {
                packet.addString(player);
            }
        }

        return packet.getBytes();
    }

    public void setPvEPlayers(List<String> pvePlayers) {
        this.pvePlayers = pvePlayers;
    }
}
