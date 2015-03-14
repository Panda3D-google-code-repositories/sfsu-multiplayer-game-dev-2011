package networking.response;

import metadata.Constants;

import model.World;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseJoinPvEWorld extends GameResponse {

    private short status;
    private World world;

    public ResponseJoinPvEWorld() {
        responseCode = Constants.SMSG_JOIN_PVE_WORLD;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

//        if (status == 0) {//The player could join this world.
//            packet.addString(world.getGameName());
//            packet.addString(world.getEnvType());
//            packet.addShort16((short) world.getEnvironments().size());
//            for (Environment env : world.getEnvironments()) {
//                packet.addString(env.getAvatar().getPlayer().getUserName());
//                packet.addShort16((short) env.getAvatar().getEnvPosition());
//                packet.addString(env.getAvatar().getAvatarType());
//            }
//        }

        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }

    public void setWorld(World world) {
        this.world = world;
    }
}
