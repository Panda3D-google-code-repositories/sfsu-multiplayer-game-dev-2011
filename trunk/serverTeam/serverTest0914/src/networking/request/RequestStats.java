package networking.request;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import core.GameServer;
import dataAccessLayer.AnimalStatDAO;
import dataAccessLayer.PlantStatDAO;

import model.PlantType;
import model.Stat;
import networking.response.ResponseBuyAnimal;
import networking.response.ResponseStats;

import utility.DataReader;

import worldManager.gameEngine.GameEngine;
import worldManager.gameEngine.Zone;


public class RequestStats extends GameRequest {


    private ResponseStats responseStats;
	private short activityStartDay;
	private short activityEndDay;
	private int playerId;

	public RequestStats() {
        responses.add(responseStats = new ResponseStats());
    }

    @Override
    public void parse() throws IOException {
    	activityStartDay = DataReader.readShort(dataInput);
    	activityEndDay = DataReader.readShort(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
    	List<Stat> animalStatList = new ArrayList<Stat>();
    	List<Stat> plantStatList = new ArrayList<Stat>();
        if (client.getWorld() != null) {
            GameEngine gameEngine = client.getWorld().getGameEngine();

            if (gameEngine != null) {
            	playerId = client.getPlayer().getID();

                int zone_id = client.getWorld().getEnvironments().get(0).getZones().get(0).getID();
            	animalStatList.addAll(AnimalStatDAO.getAnimalStats(activityStartDay, activityEndDay,playerId, zone_id));
            	plantStatList.addAll(PlantStatDAO.getPlantStats(activityStartDay, activityEndDay,playerId, zone_id));
            	responseStats.setAnimalStats(animalStatList);
            	responseStats.setPlantStatList(plantStatList);
            }
        }
    }
}
