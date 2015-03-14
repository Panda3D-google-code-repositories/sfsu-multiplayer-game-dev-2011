package networking.response;

import java.util.List;

import metadata.Constants;

import model.Avatar;
import model.Player;
import model.World;

import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseLogin extends GameResponse {

    private short status;
    private Player player;
    private List<Avatar> avatarList;
    private List<World> worldList;
    private List<Integer> scoreList;

    public ResponseLogin() {
        responseCode = Constants.SMSG_AUTH;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

        if (status == 0) {
            packet.addInt32(player.getID());
            packet.addString(player.getUsername());

            packet.addShort16((short) avatarList.size());
            for (Avatar avatar : avatarList) {
                packet.addInt32(avatar.getID());
                packet.addString(player.getUsername());
                packet.addShort16((short) avatar.getLevel());
                packet.addInt32(avatar.getCurrency());
                packet.addString(player.getLastLogout());
            }

            packet.addShort16((short) worldList.size());
            for (World world : worldList) {
                packet.addInt32(world.getID());
                packet.addString(world.getGameName());
                
                boolean isNew = world.getPlayTime() == 0;
                packet.addBoolean(isNew);

                if (!isNew) {
                    packet.addShort16((short) world.getYear());
                    packet.addShort16((short) world.getMonth());
                    packet.addInt32((int) world.getPlayTime());
                    packet.addInt32(scoreList.get(worldList.indexOf(world)));
                }
            }
        }

        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

    public void setAvatarList(List<Avatar> avatarList) {
        this.avatarList = avatarList;
    }

    public void setWorldList(List<World> worldList, List<Integer> scoreList) {
        this.worldList = worldList;
        this.scoreList = scoreList;
    }
}
