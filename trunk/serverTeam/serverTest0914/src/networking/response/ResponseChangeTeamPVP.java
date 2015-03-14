package networking.response;

import metadata.Constants;

import model.Environment;
import model.World;

import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseChangeTeamPVP extends GameResponse {

    private short status;
    private World world;

    public ResponseChangeTeamPVP() {
        responseCode = Constants.SMSG_CHANGE_TEAM_PVP;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
//        packet.addShort16(status);

        if (this.status == 0) {
            packet.addShort16((short) world.getEnvironments().size());
            for (Environment env : world.getEnvironments()) {
//                packet.addString(env.getAvatar().getPlayer().getUsername());
//                packet.addShort16((short)env.getEnvRow());
//
//                if(env.getAvatar().getAvatarType()!=null){
//                    packet.addString(env.getClient().getAvatar().getAvatarType());
//                }else{
//                    packet.addString("none");
//                }
//
//                packet.addShort16((short)env.getAvatar().getIsReady());
            }
        }

        return packet.getBytes();

    }

    public short getStatus() {
        return status;
    }

    public void setStatus(short status) {
        this.status = status;
    }

    public World getWorld() {
        return world;
    }

    public void setWorld(World world) {
        this.world = world;
    }
}
