package networking.response;

import java.util.List;

import metadata.Constants;
import model.World;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseGetPvPWorlds extends GameResponse {

    private List<World> pvpWorlds;

    public ResponseGetPvPWorlds() {
        responseCode = Constants.SMSG_GET_PVP_WORLDS;
    }

    public void setPvpWorlds(List<World> pvpWorlds) {
        this.pvpWorlds = pvpWorlds;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16((short) pvpWorlds.size());

        for (World world : pvpWorlds) {
            packet.addString(world.getGameName());
            packet.addShort16((short) world.getEnvironments().size());
            packet.addShort16((short) world.getMaxPlayers());
            packet.addString(world.getEnvType());
        }

        return packet.getBytes();
    }
}
