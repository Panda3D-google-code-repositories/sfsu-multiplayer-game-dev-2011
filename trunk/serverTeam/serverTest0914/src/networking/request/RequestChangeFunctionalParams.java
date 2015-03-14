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
import utility.DataReader;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Gary
 */
public class RequestChangeFunctionalParams extends GameRequest {

    // Data
    private HashMap<Short, Float> parameterList;		//parameterList is preyId vs value
    // Responses
    private ResponseChangeFunctionalParams responseChangeFunctionalParameters;
	private short parameterType;
	private String predator;
	private short preyListSize;
	private HashMap<String,Float> preyInterferenceValues = new HashMap<String,Float>();
	private String key;
	private Float value;
	private int preyID;
	private int predatorID;
	private HashMap<Short, Float> finalList;

    public RequestChangeFunctionalParams() {
        parameterList = new HashMap<Short, Float>();
        finalList = new HashMap<Short, Float>();
        responses.add(responseChangeFunctionalParameters = new ResponseChangeFunctionalParams());
    }

    @Override
    public void parse() throws IOException {
    	parameterType = DataReader.readShort(dataInput);
    	System.out.println(parameterType);
    	predator = DataReader.readString(dataInput);
    	System.out.println(predator);
    	preyListSize = DataReader.readShort(dataInput);
    	System.out.println(preyListSize);
    	
    	int playerId = client.getPlayer().getID();
    	System.out.println(playerId);
    	int zoneID = 0;
    	if(parameterType == Constants.PARAMETER_X_A){
	    	//Let Predator be herbivore or carnivore or omnivore (The animal category) for parameterType 3
	    	if(predator.equalsIgnoreCase("Herbivore")){
	    		predatorID = 1;
	    	}else if(predator.equalsIgnoreCase("Carnivore")){
	    		predatorID = 2;
	    	}else if(predator.equalsIgnoreCase("Omnivore")){
	    		predatorID = 3;
	    	}
    	}else{
			try {
				predatorID = AnimalTypeDAO.getByAnimalName(predator);
			} catch (SQLException e2) {
				// TODO Auto-generated catch block
				e2.printStackTrace();
			}
    	}
    	System.out.println("predatorid is " + predatorID + " parameterType " + parameterType);
    	for (int i =0; i<preyListSize;i++){
	    		key = DataReader.readString(dataInput);
	    		value = DataReader.readFloat(dataInput);
	    		preyInterferenceValues.put(key, value);
	    		try {
					preyID = AnimalTypeDAO.getByAnimalName(key);
					if(preyID == 0){
						//It may be a plant
						preyID = PlantTypeDAO.getByPlantName(key);
					}
				} catch (SQLException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
	    		System.out.println("key = "+ key + " preyID "+ preyID + " value " + value);
		    	try {
	    			PreyPredatorRatioDAO.insertParams(playerId, zoneID, parameterType,predatorID,preyID,value);
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				parameterList.put((short)preyID, value);
    	}

    	for (Short speciesId: parameterList.keySet()){
    		Float value = parameterList.get(speciesId);
    		int animalNodelist = 0;
    		int[] plantNodeList = null;
			try {
				animalNodelist = AnimalTypeDAO.getByAnimalNodeIndex(speciesId);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    		if(animalNodelist == 0){
    			try {
					plantNodeList = PlantTypeDAO.getByPlantNodeIndex(speciesId);
					for(int i =0; i< plantNodeList.length;i++){
						int index = plantNodeList[i];
						finalList.put((short) index, value);
					}
				} catch (SQLException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				

    		}else{
    			finalList.put((short) animalNodelist, value);
    		}
    	}
    }

    @Override
    public void doBusiness() throws Exception {
        for (Zone zone : client.getWorld().getEnvByUserID(client.getPlayer().getID()).getZones()) {
            if (zone.isEnable()) {
                zone.modifyFunctionalParameters(finalList,parameterType,predatorID);
            }
        }

//        responseChangeFunctionalParameters.setParameter(parameterList);

    }
}

