package worldManager.gameEngine;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Nathan Greco
 */
public class NatureControllerType {

    private int nature_controller_id;
    private String ecosystemType;
    private float cloudyChance;
    private float averageCloud;
    private float cloudRange;
    private float rainChance;
    private float averageRain;
    private float rainRange;
    private float evaporationRate;
    private List<DiseaseType> diseaseType;

    public NatureControllerType(int nature_controller_id) {
        this.nature_controller_id = nature_controller_id;
        diseaseType = new ArrayList<DiseaseType>();
    }

    public void run() {
    }

    public int getID() {
        return nature_controller_id;
    }

    public void setID(int nature_controller_id) {
        this.nature_controller_id = nature_controller_id;
    }

    public float getAverageCloud() {
        return averageCloud;
    }

    public void setAverageCloud(float averageCloud) {
        this.averageCloud = averageCloud;
    }

    public float getAverageRain() {
        return averageRain;
    }

    public void setAverageRain(float averageRain) {
        this.averageRain = averageRain;
    }

    public float getCloudRange() {
        return cloudRange;
    }

    public void setCloudRange(float cloudRange) {
        this.cloudRange = cloudRange;
    }

    public float getCloudyChance() {
        return cloudyChance;
    }

    public void setCloudyChance(float cloudyChance) {
        this.cloudyChance = cloudyChance;
    }

    public String getEcosystemType() {
        return ecosystemType;
    }

    public void setEcosystemType(String ecosystemType) {
        this.ecosystemType = ecosystemType;
    }

    public float getEvaporationRate() {
        return evaporationRate;
    }

    public void setEvaporationRate(float evaporationRate) {
        this.evaporationRate = evaporationRate;
    }

    public float getRainChance() {
        return rainChance;
    }

    public void setRainChance(float rainChance) {
        this.rainChance = rainChance;
    }

    public float getRainRange() {
        return rainRange;
    }

    public void setRainRange(float rainRange) {
        this.rainRange = rainRange;
    }

    public List<DiseaseType> getDiseaseType() {
        return diseaseType;
    }
}
