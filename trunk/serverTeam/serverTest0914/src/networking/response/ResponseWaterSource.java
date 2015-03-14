package networking.response;

import metadata.Constants;

import model.Environment;
import model.World;

import utility.GamePacket;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Xuyuan
 */
public class ResponseWaterSource extends GameResponse {

    private short status;
    private World world;

    public ResponseWaterSource() {
        responseCode = Constants.SMSG_REQUESTWATERSOURCES;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

        if (status == 0) {
            if (world != null) {
                packet.addShort16((short) world.getEnvironments().size());
                for (Environment env : world.getEnvironments()) {
                    for (Zone zone : env.getZones()) {
//                        if (zone.getWaters().size() > 0) {
//                            packet.addShort16((short) zone.getID());
//                            packet.addInt32(zone.getWaters().get(0).getLocationX());
//                            packet.addInt32(zone.getWaters().get(0).getLocationY());
//                            packet.addInt32(zone.getWaters().get(0).getLocationZ());
//                        }
                    }
                }
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
