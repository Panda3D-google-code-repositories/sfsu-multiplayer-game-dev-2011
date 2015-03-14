package model;

/**
 *
 * @author Partap Aujla
 */
public class Carnivore {

    private int prey_id;
    private int predator_id;

    public Carnivore(int prey_id, int predator_id) {
        this.prey_id = prey_id;
        this.predator_id = predator_id;
    }

    public int getPredatorID() {
        return predator_id;
    }

    public void setPredatorID(int predator_id) {
        this.predator_id = predator_id;
    }

    public int getPreyID() {
        return prey_id;
    }

    public void setPreyID(int prey_id) {
        this.prey_id = prey_id;
    }
}
