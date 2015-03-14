package networking.response;

import metadata.Constants;

import model.Environment;
import model.World;

import utility.GamePacket;

import worldManager.gameEngine.WaterSource;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Xuyuan
 */
public class ResponseGetEnv extends GameResponse {

    private short status;
    private World world;

    public ResponseGetEnv() {
        responseCode = Constants.SMSG_GET_ENV;
    }

    @Override
    public byte[] constructResponseInBytes() {;
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

        if (status == 0) {
            packet.addShort16((short) world.getEnvironments().size());

            for (Environment env : world.getEnvironments()) {
                packet.addInt32(env.getID());
                packet.addShort16((short) env.getRow());
                packet.addShort16((short) env.getColumn());
                packet.addInt32(env.getOwnerID());
                packet.addInt32(env.getEnvironmentScore());

                for (Zone zone : env.getZones()) {
                    packet.addBoolean(zone.isEnable());
                    packet.addShort16((short) zone.getID());
                    packet.addShort16((short) zone.getType());

                    WaterSource waterSource = zone.getWaterSource();
                    packet.addBoolean(waterSource != null);

                    if (waterSource != null) {
                        packet.addInt32(waterSource.getID());
                        packet.addInt32(waterSource.getMaxWater());
                        packet.addInt32(waterSource.getWater());
                    }
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

    public short getStatus() {
        return status;
    }

    public void setStatus(short status) {
        this.status = status;
    }
}
