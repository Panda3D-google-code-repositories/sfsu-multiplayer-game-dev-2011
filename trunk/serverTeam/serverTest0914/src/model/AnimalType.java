package model;

import java.lang.reflect.Field;
import metadata.Constants;

/**
 *
 * @author Partap Aujla
 */
public class AnimalType extends SpeciesType {

    private short diet_type;
    private float metabolism;
    private int mass;
    private int movt_force;
    private int max_force;
    private String animalCategory;

    public AnimalType(int species_id) {
        group_type = Constants.ORGANISM_TYPE_ANIMAL;
        this.species_id = species_id;
    }

    public int getMass() {
        return mass;
    }

    public void setMass(int mass) {
        this.mass = mass;
    }

    public int getMaxForce() {
        return max_force;
    }

    public void setMaxForce(int max_force) {
        this.max_force = max_force;
    }

    public int getMovtForce() {
        return movt_force;
    }

    public void setMovtForce(int movt_force) {
        this.movt_force = movt_force;
    }

    public short getDietType() {
        return diet_type;
    }

    public void setDietType(short diet_type) {
        this.diet_type = diet_type;
    }

    public float getMetabolism() {
        return metabolism;
    }

    public void setMetabolism(float metabolism) {
        this.metabolism = metabolism;
    }
    
    public void setAnimalCategory(String category){
    	this.animalCategory = category;
    }
    
    public String getAnimalCategory(){
    	return this.animalCategory;
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
