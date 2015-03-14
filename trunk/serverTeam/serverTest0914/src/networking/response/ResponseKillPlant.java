package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseKillPlant extends GameResponse {

    private int plant_id;
    private int predator_id;//Since this one is optional, if this one does not have a value, please fill it with -1.
    private short count;

    public ResponseKillPlant() {
        responseCode = Constants.SMSG_KILL_PLANT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(plant_id);
        packet.addInt32(predator_id);
        packet.addShort16(count);
        return packet.getBytes();
    }

    public void setPlantID(int plant_id) {
        this.plant_id = plant_id;
    }

    public void setPredatorID(int predator_id) {
        this.predator_id = predator_id;
    }

    public void setCount(int count) {
        this.count = (short) count;
    }
}
