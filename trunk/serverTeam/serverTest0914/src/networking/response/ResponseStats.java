package networking.response;

import java.util.List;

import metadata.Constants;
import model.Stat;
import utility.GamePacket;


public class ResponseStats extends GameResponse {

    private short status;//0 means success; 1 means fail.
	private List<Stat> animalStatList;
	private List<Stat> plantStatList;

    public ResponseStats() {
        responseCode = Constants.SMSG_STATISTICS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        status = 0;
        if (animalStatList != null) {
            packet.addShort16(status);
            int size = animalStatList.size() + plantStatList.size();
            packet.addShort16((short)size );

            for (Stat st : animalStatList) {
                packet.addShort16((short) st.getActivityDay());
                packet.addString(st.getAnimalName());
                packet.addString(st.getActivityType());
                packet.addShort16((short) st.getCount());
                //packet.addInt32( st.getEnvironmentScore());
                //packet.addString(st.getActivityMessage());
            }
            
            for (Stat st : plantStatList) {
                packet.addShort16((short) st.getActivityDay());
                packet.addString(st.getPlantName());
                packet.addString(st.getActivityType());
                packet.addShort16((short) st.getCount());
                //packet.addInt32( st.getEnvironmentScore());
                //packet.addString(st.getActivityMessage());
            }
        }else{
        	packet.addShort16((short) 1);
        }
        return packet.getBytes();
    }

    public void setStatus(int status) {
        this.status = (short) status;
    }

	public void setAnimalStats(List<Stat> animalStatList) {
		this.animalStatList = animalStatList;
		
	}

	public void setPlantStatList(List<Stat> plantStatList) {
		this.plantStatList = plantStatList;
		
	}
    

}
