package model;

/**
 * IS THIS FILE NEEDED? 
 * @author Partap Aujla
 */
public class DiseaseInfectsAnimal {

    private int disease_id;
    private int animal_type_id;

    public int getDiseaseID() {
        return disease_id;
    }

    public void setDiseaseID(int disease_id) {
        this.disease_id = disease_id;
    }

    public int getAnimalTypeID() {
        return animal_type_id;
    }

    public void setAnimalTypeID(int animal_type_id) {
        this.animal_type_id = animal_type_id;
    }
}
