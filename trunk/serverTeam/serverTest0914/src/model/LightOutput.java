package model;

/**
 *
 * @author Partap Aujla
 */
public class LightOutput {

    private int world_id;
    private Integer day_index;
    private float output;

    public LightOutput() {
    }

    public Integer getDayIndex() {
        return day_index;
    }

    public void setDayIndex(Integer day_index) {
        this.day_index = day_index;
    }

    public float getOutput() {
        return output;
    }

    public void setOutput(float output) {
        this.output = output;
    }

    public int getWorldID() {
        return world_id;
    }

    public void setWorldID(int world_id) {
        this.world_id = world_id;
    }
}
