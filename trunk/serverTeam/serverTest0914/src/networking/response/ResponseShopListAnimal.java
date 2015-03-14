package networking.response;

import java.util.List;
import metadata.Constants;
import model.AnimalType;
import model.SpeciesType;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseShopListAnimal extends GameResponse {

    private List<AnimalType> allAnimalType;

    public ResponseShopListAnimal() {
        responseCode = Constants.SMSG_SHOP_LIST_ANIMAL;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);

        if (allAnimalType != null) {
            packet.addShort16((short) allAnimalType.size());

            for (AnimalType at : allAnimalType) {
                packet.addShort16((short) at.getID());
                packet.addString(at.getSpeciesName());
                packet.addString(at.getDescription());
                packet.addString(at.getCategory());
                packet.addShort16((short) at.getCost());

                String predatorList = "";
                for (SpeciesType predator : at.getPredatorList(Constants.ORGANISM_TYPE_ANIMAL)) {
                    predatorList += predator.getSpeciesName() + ", ";
                }
                if (predatorList.endsWith(", ")) {
                    predatorList = predatorList.substring(0, predatorList.lastIndexOf(","));
                }

                String preyList = "";
                for (SpeciesType prey : at.getPreyList(Constants.ORGANISM_TYPE_ANIMAL)) {
                    preyList += prey.getSpeciesName() + ", ";
                }
                for (SpeciesType prey : at.getPreyList(Constants.ORGANISM_TYPE_PLANT)) {
                    preyList += prey.getSpeciesName() + ", ";
                }
                if (preyList.endsWith(", ")) {
                    preyList = preyList.substring(0, preyList.lastIndexOf(","));
                }

                packet.addString(predatorList);
                packet.addString(preyList);

                packet.addShort16((short) at.getAvgBiomass());
                packet.addShort16((short) at.getMass());
                packet.addShort16((short) at.getMovtForce());
                packet.addShort16((short) at.getMaxForce());
                packet.addInt32(at.getModelID());
                packet.addString(at.getAnimalCategory());
            }
        }

        return packet.getBytes();
    }

    public void setAllAnimalType(List<AnimalType> allAnimalType) {
        this.allAnimalType = allAnimalType;
    }
}
