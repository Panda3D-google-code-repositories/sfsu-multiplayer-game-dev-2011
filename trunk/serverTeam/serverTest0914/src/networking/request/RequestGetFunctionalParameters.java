package networking.request;

import core.GameServer;

import java.io.IOException;
import java.sql.SQLException;
import java.util.HashMap;

import dataAccessLayer.AnimalTypeDAO;
import dataAccessLayer.PlantTypeDAO;
import dataAccessLayer.PreyPredatorRatioDAO;

import metadata.Constants;
import networking.response.ResponseChangeFunctionalParams;
import networking.response.ResponseChangeParameters;
import networking.response.ResponseGetFunctionalParameter;
import utility.DataReader;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Gary
 */
public class RequestGetFunctionalParameters extends GameRequest {

    // Responses
    private ResponseGetFunctionalParameter responseGetFunctionalParameters;
	private String predator;
	private int predatorID;
	private short parameterType;
	private HashMap<String, Float> preyList;

    public RequestGetFunctionalParameters() {
        responses.add(responseGetFunctionalParameters = new ResponseGetFunctionalParameter());
    }

    @Override
    public void parse() throws IOException {
    	predator = DataReader.readString(dataInput);
    	System.out.println(predator);

    	parameterType = DataReader.readShort(dataInput);
    	System.out.println(parameterType);
    	
    	if(parameterType == Constants.PARAMETER_X_A){
	    	int playerId = client.getPlayer().getID();
	    	System.out.println(playerId);
	    	int zoneID = 0;
	    	//Let Predator be herbivore or carnivore or omnivore (The animal category) for parameterType 3
	    	if(predator.equalsIgnoreCase("Herbivore")){
	    		predatorID = 1;
	    	}else if(predator.equalsIgnoreCase("Carnivore")){
	    		predatorID = 2;
	    	}else if(predator.equalsIgnoreCase("Omnivore")){
	    		predatorID = 3;
	    	}
	    	try {
	    		preyList = PreyPredatorRatioDAO.getFunctionalParams(playerId, predatorID,parameterType);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	}else{
	    	int playerId = client.getPlayer().getID();
	    	System.out.println(playerId);
	    	int zoneID = 0;
			try {
				predatorID = AnimalTypeDAO.getByAnimalName(predator);
			} catch (SQLException e2) {
				// TODO Auto-generated catch block
				e2.printStackTrace();
			}
	    	System.out.println(predatorID);
	    	
	    	try {
	    		preyList = PreyPredatorRatioDAO.getFunctionalParams(playerId, predatorID,parameterType);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	}
    }

    @Override
    public void doBusiness() throws Exception {
    	if(preyList == null){
    		responseGetFunctionalParameters.setStatus((short) 1);
    	}else{
    		responseGetFunctionalParameters.setStatus((short) 0);
	    	responseGetFunctionalParameters.setParameterType(parameterType);
	    	responseGetFunctionalParameters.setParameter(preyList);
    	}
    }
}


