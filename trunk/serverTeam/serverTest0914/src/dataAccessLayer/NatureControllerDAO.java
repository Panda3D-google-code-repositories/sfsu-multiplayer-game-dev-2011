package dataAccessLayer;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import model.LightOutput;
import model.RainOutput;

import worldManager.gameEngine.NatureController;

/**
 *
 * @author Partap Aujla
 */
public final class NatureControllerDAO {

    private NatureControllerDAO() {
    }

    /**
     * This function does business for game logic.  We Extract world id from the
     * passed gameEngine argument then use it to get information from the 
     * database.
     * @param nc
     * @param gameServer
     * @param gameEngine
     * @throws SQLException 
     */
    public static void doBusiness(NatureController nc, int world_id) throws SQLException {
        List<LightOutput> holdLightOutputs = LightOutputDAO.getByWorldID(world_id);
        List<RainOutput> holdRainOutputs = RainOutputDAO.getByWorldID(world_id);

        List<Float> returnLightOutputVals = new ArrayList<Float>();
        List<Float> returnRainOutputVals = new ArrayList<Float>();

        for (int i = 0; i < holdLightOutputs.size(); i++) {
            returnLightOutputVals.add(holdLightOutputs.get(i).getOutput());
        }

        nc.setLightOutput(returnLightOutputVals);

        for (int i = 0; i < holdRainOutputs.size(); i++) {
            returnRainOutputVals.add(holdRainOutputs.get(i).getOutput());
        }

        nc.setRainOutput(returnRainOutputVals);
    }
}