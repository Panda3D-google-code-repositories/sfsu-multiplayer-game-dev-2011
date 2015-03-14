package networking.request;

import dataAccessLayer.BiomassCSVDAO;
import dataAccessLayer.ScoreCSVDAO;
import dataAccessLayer.SpeciesCSVDAO;

import java.io.IOException;

import model.World;
import networking.response.ResponseChartBiomass;
import utility.DataReader;

import worldManager.gameEngine.Zone;

/**
 *
 * @author Gary
 */
public class RequestChartBiomass extends GameRequest {

    private short type;

    public RequestChartBiomass() {
    }

    @Override
    public void parse() throws IOException {
        type = DataReader.readShort(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {

        if (type == 0) {
            World world = client.getWorld();

            if (world != null) {
                for (Zone zone : world.getGameEngine().getZoneList()) {
                    if (zone.isEnable()) {
                        String csv = BiomassCSVDAO.getCSV(zone.getManipulationID());

                        if (csv != null) {
                            csv = csv.substring(0, csv.lastIndexOf("\n"));

                            ResponseChartBiomass responseChartBiomass = new ResponseChartBiomass();
                            responseChartBiomass.setType(type);
                            responseChartBiomass.setCSV(csv);

                            responses.add(responseChartBiomass);
                        }
                    }
                }
            }
        } else if (type == 1) {
            World world = client.getWorld();

            if (world != null) {
                for (Zone zone : world.getGameEngine().getZoneList()) {
                    if (zone.isEnable()) {
                        String csv = SpeciesCSVDAO.getCSV(zone.getManipulationID());

                        if (csv != null) {
                            csv = csv.substring(0, csv.lastIndexOf("\n"));

                            ResponseChartBiomass responseChartBiomass = new ResponseChartBiomass();
                            responseChartBiomass.setType(type);
                            responseChartBiomass.setCSV(csv);

                            responses.add(responseChartBiomass);
                        }
                    }
                }
            }
        } else if (type == 2) {
            World world = client.getWorld();

            if (world != null) {
                for (Zone zone : world.getGameEngine().getZoneList()) {
                    if (zone.isEnable()) {
                        String csv = ScoreCSVDAO.getCSV(zone.getID());

                        if (csv != null) {
                            ResponseChartBiomass responseChartBiomass = new ResponseChartBiomass();
                            responseChartBiomass.setType(type);
                            responseChartBiomass.setCSV(csv);

                            responses.add(responseChartBiomass);
                        }
                    }
                }
            }
        }
    }
}
