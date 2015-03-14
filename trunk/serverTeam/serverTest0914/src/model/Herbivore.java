package model;

/**
 *
 * @author Partap Aujla
 */
public class Herbivore {

    private int animal_type_id;
    private int plant_type_id;

    public Herbivore(int animal_type_id, int plant_type_id) {
        this.animal_type_id = animal_type_id;
        this.plant_type_id = plant_type_id;
    }

    public int getAnimalTypeID() {
        return animal_type_id;
    }

    public void setAnimalTypeID(int animal_type_id) {
        this.animal_type_id = animal_type_id;
    }

    public int getPlantTypeID() {
        return plant_type_id;
    }

    public void setPlantTypeID(int plant_type_id) {
        this.plant_type_id = plant_type_id;
    }
}
