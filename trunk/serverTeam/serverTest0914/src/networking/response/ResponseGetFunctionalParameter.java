package networking.response;

import java.util.HashMap;

import metadata.Constants;
import utility.GamePacket;

public class ResponseGetFunctionalParameter extends GameResponse{
    private short status;
    private HashMap<String, Float> preyList;
	private int parameterType;

    public ResponseGetFunctionalParameter() {
        responseCode = Constants.SMSG_GET_FUNCTIONAL_PARAMETERS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(status);

        if (status == 0) {
        	packet.addShort16((short) this.parameterType);
            packet.addShort16((short) preyList.size());

            for (String parameter : preyList.keySet()) {
                packet.addString(parameter);
                packet.addFloat(preyList.get(parameter));
            }
        }

        return packet.getBytes();
    }

    public void setStatus(short status) {
        this.status = status;
    }

    public void setParameter(HashMap<String, Float> preyList) {
        this.preyList = preyList;
    }
    
    public void setParameterType(int parameterType){
    	this.parameterType = parameterType;
    }
}
