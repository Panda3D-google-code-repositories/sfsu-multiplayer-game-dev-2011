package networking.response;

import java.util.List;

import metadata.Constants;
import model.World;
import utility.GamePacket;

/**
 *
 * @author Gary
 */
public class ResponseGetPlayerWorlds extends GameResponse {

    private List<World> worldList;

    public ResponseGetPlayerWorlds() {
        responseCode = Constants.SMSG_GET_PLAYER_WORLDS;
    }

    public void setWorlds(List<World> worldList) {
        this.worldList = worldList;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);

        packet.addShort16((short) worldList.size());

        for (World w : worldList) {
            packet.addShort16(w.getAccessType());
            packet.addShort16((short) 1);
            packet.addString(w.getGameName());
            packet.addShort16((short) w.getEnvironments().size());
            packet.addShort16((short) w.getMaxPlayers());
            packet.addString(w.getEnvType());
        }

        return packet.getBytes();
    }
}
