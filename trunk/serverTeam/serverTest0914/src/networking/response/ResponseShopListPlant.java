package networking.response;

import java.util.List;
import metadata.Constants;
import model.PlantType;
import model.SpeciesType;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseShopListPlant extends GameResponse {

    private List<PlantType> allPlantType;

    public ResponseShopListPlant() {
        responseCode = Constants.SMSG_SHOP_LIST_PLANT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);

        if (allPlantType != null) {
            packet.addShort16((short) allPlantType.size());

            for (PlantType pt : allPlantType) {
                packet.addShort16((short) pt.getID());
                packet.addString(pt.getSpeciesName());
                packet.addString(pt.getDescription());
                packet.addString(pt.getCategory());
                packet.addShort16((short) pt.getCost());

                String predatorList = "";
                for (SpeciesType predator : pt.getPredatorList(Constants.ORGANISM_TYPE_ANIMAL)) {
                    predatorList += predator.getSpeciesName() + ", ";
                }
                if (predatorList.endsWith(", ")) {
                    predatorList = predatorList.substring(0, predatorList.lastIndexOf(","));
                }

                packet.addString(predatorList);
                packet.addInt32(pt.getModelID());
                packet.addInt32((int) pt.getAvgBiomass());
            }
        }

        return packet.getBytes();
    }

    public void setAllPlantType(List<PlantType> allPlantType) {
        this.allPlantType = allPlantType;
    }
}
