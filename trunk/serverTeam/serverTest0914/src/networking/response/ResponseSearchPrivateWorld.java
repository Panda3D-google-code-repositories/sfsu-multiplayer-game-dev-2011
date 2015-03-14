package networking.response;

import metadata.Constants;

import model.PvEWorldMap;
import model.World;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseSearchPrivateWorld extends GameResponse {

    private short status;
    private World world;//The searched world.
    private PvEWorldMap pveMap;

    public ResponseSearchPrivateWorld() {
        responseCode = Constants.SMSG_SEARCH_PRIVATE_WORLD;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        if (status == 0) {
            packet.addString(world.getGameName());
            packet.addShort16((short) world.getGameMode());
        }
//        if (status == 0) {
//            if (world.getGameMode() == Constants.GAME_TYPE_PVP) {
//                packet.addShort16((short) 1);
//            } else if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
//                packet.addShort16((short) 0);
//            }
//
//            packet.addString(world.getGameName());
//            packet.addString(world.getEnvType());
//            packet.addShort16((short) world.getNumEnvironments());
//            if (world.getEnvironments() != null) {
//                for (Environment env : world.getEnvironments()) {
//                    packet.addString(env.getAvatar().getPlayer().getUserName());
//                    if (world.getGameMode() == Constants.GAME_TYPE_PVP) {
//                        packet.addShort16((short) env.getEnvRow());
//                        packet.addShort16((short) env.getEnvColumn());
//                    } else if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
//                        packet.addShort16((short) 0);
//                        pveMap = mapDAO.getPvEWorldMap(world.getWorldIdPk());
//                        packet.addShort16((short) pveMap.getPositionBasingOnRowAndCol(env.getEnvRow(), env.getEnvColumn()));
//                    }
//                    packet.addString(env.getAvatar().getAvatarType());
//                }
//            }
//        }

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
