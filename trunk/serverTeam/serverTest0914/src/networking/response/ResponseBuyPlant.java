package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseBuyPlant extends GameResponse {

    private int status;
    private int plantTypeID;
    private int amount;

    public ResponseBuyPlant() {
        responseCode = Constants.SMSG_BUY_PLANT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16((short) status);
        packet.addInt32(plantTypeID);
        packet.addInt32(amount);
        return packet.getBytes();
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public void setPlantTypeID(int plantTypeID) {
        this.plantTypeID = plantTypeID;
    }

    public void setSpentAmount(int amount) {
        this.amount = amount;
    }
}
