package networking.request;

import core.GameServer;

import java.io.IOException;
import java.util.HashMap;

import metadata.Constants;
import networking.response.ResponseChangeParameters;
import utility.DataReader;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Gary
 */
public class RequestChangeParameters extends GameRequest {

    // Data
    private HashMap<Short, Float> parameterList;
    // Responses
    private ResponseChangeParameters responseChangeParameters;

    public RequestChangeParameters() {
        parameterList = new HashMap<Short, Float>();
        responses.add(responseChangeParameters = new ResponseChangeParameters());
    }

    @Override
    public void parse() throws IOException {
        for (int i = 0; i < 8; i++) {
            float value = DataReader.readFloat(dataInput);

            if (i != Constants.PARAMETER_K) {
                value = Math.min(Math.max(0, value), 1);
            } else {
                value = Math.max(0, value);
            }

            parameterList.put((short) i, value);
        }
    }

    @Override
    public void doBusiness() throws Exception {
        for (Zone zone : client.getWorld().getEnvByUserID(client.getPlayer().getID()).getZones()) {
            if (zone.isEnable()) {
                zone.modifyParameters(parameterList);
            }
        }

        responseChangeParameters.setParameter(parameterList);

//        int experience = 0;

//        for (short parameter : parameterList.keySet()) {
//            experience += 100;
//        }
//
//        GameServer.getInstance().updateExperience(client.getPlayer(), experience);
    }
}
