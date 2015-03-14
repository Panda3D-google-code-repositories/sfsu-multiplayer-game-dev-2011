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
public class RequestParams extends GameRequest {

    // Data
    private HashMap<Short, Float> parameterList;
    // Responses
    private ResponseChangeParameters responseChangeParameters;

    public RequestParams() {
        parameterList = new HashMap<Short, Float>();
        responses.add(responseChangeParameters = new ResponseChangeParameters());
    }

    @Override
    public void parse() throws IOException {
    }

    @Override
    public void doBusiness() throws Exception {
        for (Zone zone : client.getWorld().getEnvByUserID(client.getPlayer().getID()).getZones()) {
            if (zone.isEnable()) {
                parameterList = zone.getParameters();
                break;
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
