package worldManager.gameEngine;

import dataAccessLayer.NatureControllerDAO;

import java.sql.SQLException;
import java.util.List;
import java.util.Random;

/**
 *
 * @author Nathan Greco
 */
public class NatureController {

    private GameEngine gameEngine;
    private Random rand = new Random();
    private List<Float> lightOutput;
    private List<Float> rainOutput;
    private NatureControllerType nct;

    public NatureController(GameEngine gameEngine, NatureControllerType nct) {
        /////get all ecosystem data from NatureControllerType (see partap)        
        //array of references of DiseaseTypes
        this.gameEngine = gameEngine;

        try {
            NatureControllerDAO.doBusiness(this, gameEngine.getWorldID());
        } catch (SQLException m) {
            //exception caught. FREAK OUT.
        }

        //reference to NatureControllerType for current ecosystem
        this.nct = nct;

        //check if game was run before. if not, generate random data. if so, load saved data.
        while (lightOutput.size() < 30) {
            //calculate lightOutput array
            if (rand.nextFloat() < nct.getCloudyChance()) {
                lightOutput.add(1 - nct.getAverageCloud() + rand.nextFloat() * nct.getCloudRange() - nct.getCloudRange() / 2);
            } else {
                lightOutput.add((float) 1.0);
            }
        }

        while (rainOutput.size() < 30) {
            //calculate rainOutput array
            if (rand.nextFloat() < nct.getRainChance()) {
                rainOutput.add(nct.getAverageRain() + rand.nextFloat() * nct.getRainRange() - nct.getRainRange() / 2);
            } else {
                rainOutput.add((float) 0.0);
            }
        }
    }

    public void setLightOutput(List<Float> lightOutput) {
        this.lightOutput = lightOutput;
    }

    public void setRainOutput(List<Float> rainOutput) {
        this.rainOutput = rainOutput;
    }

    public float currentRainOutput() {
        return rainOutput.get(0);
    }

    public float currentLightOutput() {
        return lightOutput.get(0);
    }

    public NatureControllerType getNCT() {
        return nct;
    }

    public void run(long gameScaleTime, boolean isNewDay) {
        if (isNewDay) {
            //pop front Output, push new Output
            lightOutput.remove(0);
            rainOutput.remove(0);

            if (rand.nextFloat() < nct.getCloudyChance()) {
                lightOutput.add(1 - nct.getAverageCloud() + rand.nextFloat() * nct.getCloudRange() - nct.getCloudRange() / 2);
            } else {
                lightOutput.add((float) 1.0);
            }

            if (rand.nextFloat() < nct.getRainChance()) {
                rainOutput.add(1 - nct.getAverageRain() + rand.nextFloat() * nct.getRainRange() - nct.getRainRange() / 2);
            } else {
                rainOutput.add((float) 0.0);
            }

            //loop through each disease type for the given ecosystem.
            for (DiseaseType dt : nct.getDiseaseType()) {
                if (rand.nextFloat() < dt.getInfectChance()) {
                    //choose random zone
                    //pick a random animal in the zone that can be infected and infect it
                    //if no animal, no infection occurs
                }
            }
        }
    }
}
