package model;

/**
 *
 * @author Partap Aujla
 */
public class PlantBiomassOfZone {

    private int bio_zone_id;
    private int plant_type_id;
    private int number;
    private float biomass;

    public PlantBiomassOfZone(int bio_zone_id) {
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

    public int getPlantTypeID() {
        return plant_type_id;
    }

    public void setPlantTypeID(int plant_type_id) {
        this.plant_type_id = plant_type_id;
    }
}
