package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseMoveAnimal extends GameResponse {

    private short status;
    private short xTarg;
    private short yTarg;

    public ResponseMoveAnimal() {
        responseCode = Constants.SMSG_MOVE_ANIMAL;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);
        if (status == 0) {//0 means moving is successful.
            packet.addShort16(xTarg);
            packet.addShort16(yTarg);
        }

        return packet.getBytes();
    }

    public short getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = (short) status;
    }

    public short getxTarg() {
        return xTarg;
    }

    public void setxTarg(int xTarg) {
        this.xTarg = (short) xTarg;
    }

    public short getyTarg() {
        return yTarg;
    }

    public void setyTarg(int yTarg) {
        this.yTarg = (short) yTarg;
    }
}
