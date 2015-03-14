package networking.response;

import java.util.List;

import metadata.Constants;
import model.World;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseGetPvEWorlds extends GameResponse {

    private List<World> worldList;

    public ResponseGetPvEWorlds() {
        responseCode = Constants.SMSG_GET_PVE_WORLDS;
    }

    public void setPublicPvEWorlds(List<World> worldList) {
        this.worldList = worldList;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);

        packet.addShort16((short) worldList.size());

        if (worldList != null) {
            for (World w : worldList) {
                packet.addShort16(w.getAccessType());
                packet.addShort16((short) 1);
                packet.addString(w.getGameName());
                packet.addShort16((short) w.getEnvironments().size());
                packet.addShort16((short) w.getMaxPlayers());
                packet.addString(w.getEnvType());
            }
        }

        return packet.getBytes();
    }
}
