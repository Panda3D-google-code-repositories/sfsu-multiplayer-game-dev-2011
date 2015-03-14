package networking.response;

import metadata.Constants;

import model.Environment;

import utility.GamePacket;

import worldManager.gameEngine.WaterSource;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Gary
 */
public class ResponseCreateEnv extends GameResponse {

    private Environment env;

    public ResponseCreateEnv() {
        responseCode = Constants.SMSG_CREATE_ENV;
    }

    @Override
    public byte[] constructResponseInBytes() {;
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(env.getID());
        packet.addShort16((short) env.getRow());
        packet.addShort16((short) env.getColumn());
        packet.addInt32(env.getOwnerID());
        packet.addInt32(env.getEnvironmentScore());

        for (Zone zone : env.getZones()) {
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

        return packet.getBytes();
    }

    public void setEnvironment(Environment env) {
        this.env = env;
    }
}
