package networking.response;

import java.util.List;

import metadata.Constants;

import model.AnimalType;
import model.PlantType;
import model.SpeciesType;

import utility.GamePacket;

/**
 *
 * @author Gary
 */
public class ResponseShopUnlock extends GameResponse {

    private List<SpeciesType> unlockList;

    public ResponseShopUnlock() {
        responseCode = Constants.SMSG_SHOP_UNLOCK;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);

        if (unlockList != null) {
            packet.addShort16((short) unlockList.size());

            for (SpeciesType species : unlockList) {
                packet.addShort16((short) species.getGroupType());

                if (species.getGroupType() == Constants.ORGANISM_TYPE_PLANT) {
                    PlantType plant = (PlantType) species;

                    packet.addShort16((short) plant.getID());
                    packet.addString(plant.getSpeciesName());
                    packet.addString(plant.getDescription());
                    packet.addString(plant.getCategory());
                    packet.addShort16((short) plant.getCost());

                    String predatorList = "";
                    for (SpeciesType predator : plant.getPredatorList(Constants.ORGANISM_TYPE_ANIMAL)) {
                        predatorList += predator.getSpeciesName() + ", ";
                    }
                    if (predatorList.endsWith(", ")) {
                        predatorList = predatorList.substring(0, predatorList.lastIndexOf(","));
                    }

                    packet.addString(predatorList);
                    packet.addInt32(plant.getModelID());
                    packet.addInt32((int) plant.getAvgBiomass());
                } else if (species.getGroupType() == Constants.ORGANISM_TYPE_ANIMAL) {
                    AnimalType animal = (AnimalType) species;

                    packet.addShort16((short) animal.getID());
                    packet.addString(animal.getSpeciesName());
                    packet.addString(animal.getDescription());
                    packet.addString(animal.getCategory());
                    packet.addShort16((short) animal.getCost());

                    String predatorList = "";
                    for (SpeciesType predator : animal.getPredatorList(Constants.ORGANISM_TYPE_ANIMAL)) {
                        predatorList += predator.getSpeciesName() + ", ";
                    }
                    if (predatorList.endsWith(", ")) {
                        predatorList = predatorList.substring(0, predatorList.lastIndexOf(","));
                    }

                    String preyList = "";
                    for (SpeciesType prey : animal.getPreyList(Constants.ORGANISM_TYPE_ANIMAL)) {
                        preyList += prey.getSpeciesName() + ", ";
                    }
                    for (SpeciesType prey : animal.getPreyList(Constants.ORGANISM_TYPE_PLANT)) {
                        preyList += prey.getSpeciesName() + ", ";
                    }
                    if (preyList.endsWith(", ")) {
                        preyList = preyList.substring(0, preyList.lastIndexOf(","));
                    }

                    packet.addString(predatorList);
                    packet.addString(preyList);

                    packet.addShort16((short) animal.getAvgBiomass());
                    packet.addShort16((short) animal.getMass());
                    packet.addShort16((short) animal.getMovtForce());
                    packet.addShort16((short) animal.getMaxForce());
                    packet.addInt32(animal.getModelID());
                    packet.addString(animal.getAnimalCategory());
                }
            }
        }

        return packet.getBytes();
    }

    public void setUnlockList(List<SpeciesType> unlockList) {
        this.unlockList = unlockList;
    }
}
