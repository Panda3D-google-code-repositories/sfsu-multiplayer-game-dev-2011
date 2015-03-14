package networking.response;

import java.util.HashMap;

import metadata.Constants;
import utility.GamePacket;

public class ResponseChangeFunctionalParams extends GameResponse{
    private short status;
    private HashMap<Short, Float> parameterList;

    public ResponseChangeFunctionalParams() {
        responseCode = Constants.SMSG_CHANGE_FUNCTIONAL_PARAMETERS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

//        if (status == 0) {
//            packet.addShort16((short) parameterList.size());
//
//            for (short parameter : parameterList.keySet()) {
//                packet.addShort16(parameter);
//                packet.addFloat(parameterList.get(parameter));
//            }
//        }

        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }

    public void setParameter(HashMap<Short, Float> parameterList) {
        this.parameterList = parameterList;
    }
}
