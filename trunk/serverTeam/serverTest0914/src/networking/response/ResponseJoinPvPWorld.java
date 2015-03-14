package networking.response;

import metadata.Constants;
import model.Environment;
import model.World;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseJoinPvPWorld extends GameResponse {

    private short status;
    private World world;

    public ResponseJoinPvPWorld() {
        responseCode = Constants.SMSG_JOIN_PVP_WORLD;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

        if (status == 0) {//The player could join this world.
            if (world != null) {
                packet.addString(world.getGameName());
                packet.addString(world.getEnvType());
                packet.addShort16((short) world.getEnvironments().size());
                for (Environment env : world.getEnvironments()) {
//                    packet.addString(env.getAvatar().getPlayer().getUsername());
//                    packet.addShort16((short) env.getEnvRow());
//                    packet.addShort16((short) env.getEnvColumn());
//                    packet.addString(env.getAvatar().getAvatarType());
                }
            } else {
                System.out.println("World is null");
            }

        }

        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }

    public void setWorld(World world) {
        this.world = world;
    }
}
