package networking.request;

import core.GameServer;

import dataAccessLayer.ZoneDAO;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import metadata.Constants;

import model.Environment;
import model.World;

import networking.response.ResponseRestart;

import org.datacontract.schemas._2004._07.ManipulationParameter.NodeBiomass;

import simulationEngine.SimulationEngine;
import simulationEngine.SpeciesZoneType;
import simulationEngine.SpeciesZoneType.SpeciesTypeEnum;

import utility.DataReader;

import worldManager.gameEngine.Zone;

/**
 * 
 * @author Gary
 */
public class RequestRestart extends GameRequest {

    // Data
    private boolean status;
    // Responses
    private ResponseRestart responseRestart;

    public RequestRestart() {
        responses.add(responseRestart = new ResponseRestart());
    }

    @Override
    public void parse() throws IOException {
        status = DataReader.readBoolean(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        if (status) {
            World world = client.getWorld();

            if (world != null) {
                Environment env = world.getEnvByUserID(client.getPlayer().getID());

                for (Zone zone : env.getZones()) {
                    if (zone.isEnable()) {
                        zone.restart();

                        SimulationEngine se = new SimulationEngine();
                        zone.setSimulationEngine(se);

                        String networkName = "WoB-" + env.getID() + "." + zone.getOrder() + "-" + System.currentTimeMillis() % 100000;

                        int nodeList[] = {1, 8, 9};
                        zone.setManipulationID(se.createAndRunSeregenttiSubFoodweb(nodeList, networkName, 0, 0, false));

                        ZoneDAO.updateManipulationID(zone.getID(), zone.getManipulationID());

//                        se.setCarryingCapacity(0, 5, zone.getManipulationID(), 3000);

                        List<NodeBiomass> lNodeBiomass = new ArrayList<NodeBiomass>();

                        lNodeBiomass.add(new NodeBiomass(GameServer.getInstance().getSpeciesTypeByNodeID(1).getAvgBiomass() * 10, 1));
                        lNodeBiomass.add(new NodeBiomass(GameServer.getInstance().getSpeciesTypeByNodeID(8).getAvgBiomass() * 5, 8));
                        lNodeBiomass.add(new NodeBiomass(GameServer.getInstance().getSpeciesTypeByNodeID(9).getAvgBiomass() * 5, 9));

                        if (!lNodeBiomass.isEmpty()) {
                            se.updateBiomass(zone.getManipulationID(), lNodeBiomass, 0);
                        }

                        se.getBiomass(zone.getManipulationID(), 0, 0);

                        for (SpeciesZoneType szt : se.getSpecies().values()) {
                            int species_id = GameServer.getInstance().getSpeciesTypeByNodeID(szt.getNodeIndex()).getID();

//                            if (szt.getType() == SpeciesTypeEnum.ANIMAL) {
//                                world.getGameEngine().createOrganismByResponse(Constants.ORGANISM_TYPE_ANIMAL, species_id, client.getPlayer().getID(), zone.getID(), szt.getSpeciesCount(), 1, Constants.CREATE_STATUS_DEFAULT);
//                            } else if (szt.getType() == SpeciesTypeEnum.PLANT) {
//                                world.getGameEngine().createOrganismByResponse(Constants.ORGANISM_TYPE_PLANT, species_id, client.getPlayer().getID(), zone.getID(), szt.getSpeciesCount(), Constants.GROUP_SIZE, Constants.CREATE_STATUS_DEFAULT);
//                            }
                        }
                    }
                }
            }
        }
    }
}