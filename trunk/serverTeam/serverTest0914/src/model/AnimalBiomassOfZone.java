package model;

/**
 *
 * @author Partap Aujla
 */
public class AnimalBiomassOfZone {

    private int bio_zone_id;
    private int animal_type_id;
    private int number;
    private float biomass;

    public AnimalBiomassOfZone(int bio_zone_id) {
        this.bio_zone_id = bio_zone_id;
    }

    public float getBiomass() {
        return biomass;
    }

    public void setBiomass(float biomass) {
        this.biomass = biomass;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public int getID() {
        return bio_zone_id;
    }

    public void setID(int bio_zone_id) {
        this.bio_zone_id = bio_zone_id;
    }

    public int getAnimalTypeID() {
        return animal_type_id;
    }

    public void setAnimalTypeID(int animal_type_id) {
        this.animal_type_id = animal_type_id;
    }
}
