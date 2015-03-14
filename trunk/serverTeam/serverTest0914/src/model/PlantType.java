package model;

import java.lang.reflect.Field;
import metadata.Constants;

/**
 *
 * @author Partap Aujla
 */
public class PlantType extends SpeciesType {

    private int lightNeedFrequency;
    private float grow_radius;

    public PlantType(int species_id) {
        group_type = Constants.ORGANISM_TYPE_PLANT;
        this.species_id = species_id;
    }

    public float getGrowRadius() {
        return grow_radius;
    }

    public void setGrowRadius(float grow_radius) {
        this.grow_radius = grow_radius;
    }

    public int getLightNeedFrequency() {
        return lightNeedFrequency;
    }

    public int setLightNeedFrequency(int lightNeedFrequency) {
        return this.lightNeedFrequency = lightNeedFrequency;
    }

    @Override
    public String toString() {
        String str = "";

        str += "-----" + "\n";
        str += getClass().getName() + "\n";
        str += "\n";

        for (Field field : getClass().getDeclaredFields()) {
            try {
                str += field.getName() + " - " + field.get(this) + "\n";
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
            }
        }

        str += "-----";

        return str;
    }
}
