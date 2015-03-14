package worldManager.gameEngine;

/**
 *
 * @author KeithKong
 */
public class WaterSource {

    private int water_source_id;
    private int water;
    private int maxWater;
    private int radius;
    private int targetWater;
    private long targetWaterTime;
    private float[] position;
    private int zone_id;

    public WaterSource(int water_source_id) {
        this.water_source_id = water_source_id;
        position = new float[]{0, 0, 0};
    }

    public int getID() {
        return water_source_id;
    }

    public void setID(int water_source_id) {
        this.water_source_id = water_source_id;
    }

    public int getWater() {
        return water;
    }

    public int setWater(int water) {
        targetWater = water;
        return this.water = water;
    }

    public int getMaxWater() {
        return maxWater;
    }

    public int setMaxWater(int maxWater) {
        return this.maxWater = maxWater;
    }

    public void setWaterTarget(int targetWater, long targetWaterTime) {
        if (targetWater < 0) {
            this.targetWater = 0;
        } else if (targetWater > maxWater) {
            this.targetWater = maxWater;
        } else {
            this.targetWater = targetWater;
        }

        this.targetWaterTime = targetWaterTime;
    }

    public void reachWaterTarget() {
        water = targetWater;
    }

    public int getRadius() {
        return radius;
    }

    public int setRadius(int radius) {
        return this.radius = radius;
    }

    public float getX() {
        return position[0];
    }

    public void setX(float x) {
        position[0] = x;
    }

    public float getY() {
        return position[1];
    }

    public void setY(float y) {
        position[1] = y;
    }

    public float getZ() {
        return position[2];
    }

    public void setZ(float z) {
        position[2] = z;
    }

    public float[] getPos() {
        return position;
    }

    public float[] setPos(float x, float y, float z) {
        position[0] = x;
        position[1] = y;
        position[2] = z;

        return position;
    }

    public int getZoneID() {
        return zone_id;
    }

    public void setZoneID(int zone_id) {
        this.zone_id = zone_id;
    }
}
