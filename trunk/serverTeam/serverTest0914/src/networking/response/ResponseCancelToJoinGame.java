package networking.response;

import metadata.Constants;

import model.Environment;
import model.World;

import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseCancelToJoinGame extends GameResponse {

    private World world;
    private Short status = 0;

    public ResponseCancelToJoinGame() {
        responseCode = Constants.SMSG_CANCEL_TO_JOIN_GAME;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        if (world != null) {
            if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
                packet.addShort16((short) 0);
                packet.addShort16(status);
            } else if (world.getGameMode() == Constants.GAME_TYPE_PVP) {
                packet.addShort16((short) 1);

                if (world.getEnvironments() != null) {
                    packet.addShort16((short) world.getEnvironments().size());

                    if (world.getGameMode() == Constants.GAME_TYPE_PVP) {
                        for (Environment env : world.getEnvironments()) {
//                            packet.addString(env.getAvatar().getPlayer().getUsername());
                            packet.addShort16((short) env.getRow());
                            packet.addShort16((short) env.getColumn());
                        }
                    } else if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
                        for (Environment env : world.getEnvironments()) {
//                            packet.addString(env.getAvatar().getPlayer().getUsername());
                            packet.addShort16((short) env.getRow());
                            packet.addShort16((short) env.getColumn());
                        }
                    }

//                    for (Environment env : world.getEnvironments()) {
//                        packet.addString(env.getClient().getAvatar().getAvatarType());
//                        packet.addShort16((short) env.getClient().getAvatar().getIsReady());
//                    }

                }
            }
        }

        return packet.getBytes();
    }

    public World getWorld() {
        return world;
    }

    public void setWorld(World world) {
        this.world = world;
    }

    public Short getStatus() {
        return status;
    }

    public void setStatus(Short status) {
        this.status = status;
    }
}
