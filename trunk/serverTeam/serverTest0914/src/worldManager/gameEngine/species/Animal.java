package worldManager.gameEngine.species;

import java.util.ArrayList;
import java.util.List;

import metadata.Constants;

import worldManager.gameEngine.DiseaseType;

/**
 *
 * @author KeithKong
 */
public class Animal extends Organism {

    private int loyalty;
    private float hungerLevel;
    private ArrayList<DiseaseType> diseases;

    public Animal(int animal_id) {
        organism_type = Constants.ORGANISM_TYPE_ANIMAL;
        organism_id = animal_id;

        hungerLevel = 0.0f;
        diseases = new ArrayList<DiseaseType>();
    }

    public List<DiseaseType> getDiseases() {
        return diseases;
    }

    /* FOR DB */
    public void addDisease(int diseaseID) {
        //Grab GameServer... somehow...
    }

    /* END FOR DB */
    @Override
    public void onNoDailyWater() {
        noWaterCount++;
        setTargetBiomass(targetBiomass - speciesType.getWaterBiomassLoss());
    }

    public int getLoyalty() {
        return loyalty;
    }

    public int setLoyalty(int loyalty) {
        return this.loyalty = loyalty;
    }

    public void onDayPass(int avatarID) {
        if (avatarID == player_id) {
            if (loyalty > 0) {
                loyalty--;
            }
        } else {
            loyalty++;

            if (loyalty >= 7) {
                player_id = avatarID;
                loyalty = 0;
            }
        }
    }

    public float getHungerLevel() {
        return hungerLevel;
    }

    public float setHungerLevel(float hungerLevel) {
        return this.hungerLevel = hungerLevel;
    }
}
