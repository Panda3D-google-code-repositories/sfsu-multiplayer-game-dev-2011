package networking.response;

import metadata.Constants;
import model.World;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseCreateNewWorld extends GameResponse {

    private short status;
    private World world;
    private String charName;

    public ResponseCreateNewWorld() {
        responseCode = Constants.SMSG_CREATE_NEW_WORLD;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);//status

        if (world.getGameMode() == Constants.GAME_TYPE_PVE) {
            packet.addShort16((short) 1);
        } else if (world.getGameMode() == Constants.GAME_TYPE_PVP) {
            packet.addShort16((short) 2);
        }

        if (status == 0) {
            packet.addInt32(world.getID());
            //world name
            packet.addString(world.getGameName());
            //ecosystem
            packet.addString(world.getEnvType());
            //max player number
            packet.addShort16((short) world.getMaxPlayers());

            //Character name
            packet.addString(charName);
            packet.addFloat(world.getTimeRate());
        }

        return packet.getBytes();

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

    public String getCharName() {
        return charName;
    }

    public void setCharName(String charName) {
        this.charName = charName;
    }
}
