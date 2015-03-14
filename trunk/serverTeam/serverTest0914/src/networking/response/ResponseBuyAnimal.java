package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseBuyAnimal extends GameResponse {

    private int status;
    private int animalTypeID;
    private int amount;

    public ResponseBuyAnimal() {
        responseCode = Constants.SMSG_BUY_ANIMAL;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16((short) status);
        packet.addInt32(animalTypeID);
        packet.addInt32(amount);
        return packet.getBytes();
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public void setAnimalTypeID(int animalTypeID) {
        this.animalTypeID = animalTypeID;
    }

    public void setSpentAmount(int amount) {
        this.amount = amount;
    }
}
