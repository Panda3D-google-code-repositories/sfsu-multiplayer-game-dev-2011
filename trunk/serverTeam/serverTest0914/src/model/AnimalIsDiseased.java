package model;

/**
 *
 * @author Partap Aujla
 */
public class AnimalIsDiseased {

    private int animal_id;
    private int disease_id;

    public int getDiseaseID() {
        return disease_id;
    }

    public void setDiseaseID(int disease_id) {
        this.disease_id = disease_id;
    }

    public int getAnimalID() {
        return animal_id;
    }

    public void setAnimalID(int animal_id) {
        this.animal_id = animal_id;
    }
}
