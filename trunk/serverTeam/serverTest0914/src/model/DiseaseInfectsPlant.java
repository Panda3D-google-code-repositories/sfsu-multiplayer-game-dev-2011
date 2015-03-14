package model;

/**
 * IS THIS FILE NEEDED?
 * @author Partap Aujla
 */
public class DiseaseInfectsPlant {

    private int disease_id;
    private int plant_type_id;

    public int getPlantTypeID() {
        return plant_type_id;
    }

    public void setPlantTypeID(int plant_type_id) {
        this.plant_type_id = plant_type_id;
    }

    public int getDiseaseID() {
        return disease_id;
    }

    public void setDiseaseID(int disease_id) {
        this.disease_id = disease_id;
    }
}
