package worldManager.gameEngine;

import core.GameServer;

import dataAccessLayer.BiomassCSVDAO;
import dataAccessLayer.SpeciesCSVDAO;
import dataAccessLayer.ZoneDAO;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import metadata.Constants;

import model.SpeciesType;

import networking.response.ResponseChartBiomass;
import networking.response.ResponseDrinkWater;
import networking.response.ResponseRestart;

import simulationEngine.SimulationEngine;
import simulationEngine.SpeciesZoneType;

import worldManager.gameEngine.species.Animal;
import worldManager.gameEngine.species.Plant;
import worldManager.gameEngine.species.Organism;

/**
 *
 * @author Gary
 */
public class ZoneRunnable implements Runnable {

    public class ZoneData {

        private long gameScaleTime;
        private int currentTimeStep;
        private List<Organism> organismList;
        private HashMap<Integer, Integer> nodeList;

        public ZoneData(long gameScaleTime, int currentTimeStep, List<Organism> organismList, HashMap<Integer, Integer> nodeList) {
            this.gameScaleTime = gameScaleTime;
            this.currentTimeStep = currentTimeStep;
            this.organismList = organismList;
            this.nodeList = nodeList;
        }

        public long getGameScaleTime() {
            return gameScaleTime;
        }

        public int getCurrentTimeStep() {
            return currentTimeStep;
        }

        public List<Organism> getOrganismList() {
            return organismList;
        }
        
        public HashMap<Integer, Integer> getNodeList() {
            return nodeList;
        }
    }
    private Zone zone;
    private GameEngine gameEngine;
    private SimulationEngine simulationEngine;
    private String manipulationID;
    private boolean isRunning;
    private List<Organism> organismList;
    private HashMap<Integer, Integer> totalNodeList;
    private HashMap<Integer, Integer> totalSpeciesList;
    private Queue<ZoneData> waitList;

    public ZoneRunnable(Zone zone, GameEngine gameEngine, SimulationEngine simulationEngine, String manipulationID) {
        this.zone = zone;
        this.gameEngine = gameEngine;
        this.simulationEngine = simulationEngine;
        this.manipulationID = manipulationID;

        isRunning = true;
        waitList = new LinkedList<ZoneData>();
    }

    @Override
    public void run() {
        while (isRunning) {
            ZoneData data = waitList.poll();

            if (data != null) {
                System.out.println("Running Simulation for Player ID: " + zone.getEnvironment().getOwnerID());
                long milliseconds = System.currentTimeMillis();

                try {
                    zone.setPrevBiomass(zone.getTotalBiomass());
                    runStageOne(data);
                } catch (Exception ex) {
                    ex.printStackTrace();
                    System.err.println(ex.getMessage());
                }

                System.out.println("Total Time (Simulation): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");
            }

            try {
                Thread.sleep(50);
            } catch (InterruptedException ex) {
                System.err.println(ex.getMessage());
            }
        }

        System.out.println("Zone Runnable Ends");
    }

    public synchronized void run(long gameScaleTime, int currentTimeStep, List<Organism> organismList, HashMap<Integer, Integer> nodeList) {
        waitList.add(new ZoneData(gameScaleTime, currentTimeStep, organismList, nodeList));
    }

    private void runStageOne(ZoneData data) {
        System.out.println("Running Stage One...");
        long milliseconds = System.currentTimeMillis();

        NatureController natureController = gameEngine.getNatureController();

        float lightOutput = natureController.currentLightOutput();
        float rainOutput = natureController.currentRainOutput();

        int waterTarget = 0;
        float evaporationRate;

        boolean lostWater = false;

        WaterSource waterSource = zone.getWaterSource();

        if (waterSource != null) {
            waterSource.reachWaterTarget();

            waterTarget = waterSource.getWater();
            evaporationRate = natureController.getNCT().getEvaporationRate();

            if (evaporationRate > 0.0) {
                waterTarget = Math.min(0, (int) Math.round(waterTarget - evaporationRate * waterSource.getWater()));
            }

            if (rainOutput > 0.0) {
                waterTarget = Math.max(100, (int) Math.round(waterTarget + rainOutput * waterSource.getMaxWater()));
            }
        }

        organismList = data.getOrganismList();

        totalNodeList = new HashMap<Integer, Integer>();
        totalSpeciesList = new HashMap<Integer, Integer>();

        for (Organism organism : organismList) {
            SpeciesType species = organism.getSpeciesType();

            for (int node_id : species.getNodeList()) {
                Integer count = totalNodeList.get(node_id);

                if (count == null) {
                    totalNodeList.put(node_id, organism.getGroupSize() * species.getNodeAmount(node_id));
                } else {
                    totalNodeList.put(node_id, count + organism.getGroupSize() * species.getNodeAmount(node_id));
                }
            }

            int species_id = organism.getSpeciesTypeID();

            if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                ((Animal) organism).setHungerLevel(0);
            }

            Integer count = totalSpeciesList.get(species_id);

            if (count == null) {
                totalSpeciesList.put(species_id, organism.getGroupSize());
            } else {
                totalSpeciesList.put(species_id, count + organism.getGroupSize());
            }

            if (waterSource != null) {
                int wNF = organism.getSpeciesType().getWaterNeedFrequency();

                if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT && rainOutput > 0) {
                    organism.onGetDailyWater();
                } else if (wNF > waterTarget) {
                    waterTarget -= wNF;
                    organism.onGetDailyWater();

//                    if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
//                        ResponseDrinkWater waterResponse = new ResponseDrinkWater();
//                        waterResponse.setSpecies(organism);
//
//                        GameServer.getInstance().addResponseForWorld(gameEngine.getWorldID(), waterResponse);
//                    }
                } else {
                    organism.onNoDailyWater();
                    lostWater = true;
                }
            } else {
                if (rainOutput > 0) {
                    organism.onGetDailyWater();
                } else {
                    organism.onNoDailyWater();
                    lostWater = true;
                }
            }

            String str = "";
            if (organism.getOrganismType() == Constants.ORGANISM_TYPE_PLANT) {
                ((Plant) organism).manageDailyLight(lightOutput);
                str = String.valueOf(Constants.ORGANISM_TYPE_PLANT);
            } else if (organism.getOrganismType() == Constants.ORGANISM_TYPE_ANIMAL) {
                str = String.valueOf(Constants.ORGANISM_TYPE_ANIMAL);
            }

            str += organism.getSpeciesType().getID();
        }

        if (waterSource != null) {
            if (lostWater) {
                waterTarget = 0;
            }

            waterSource.setWaterTarget(waterTarget, (long) (data.getCurrentTimeStep() + 1) * 86400);
        }

        System.out.println("Total Time (Run Stage One): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");

        runStageTwo(data);

//        if (zone.getTotalSpecies() == 0) {
//            if (zone.getDaysCollapsed() >= 10) {
//                ResponseRestart responseRestart = new ResponseRestart();
//                responseRestart.setStatus(true);
//                GameServer.getInstance().addResponseForWorld(gameEngine.getWorldID(), responseRestart);
//            } else if (zone.getDaysCollapsed() >= 3) {
//                gameEngine.createOrganismByResponse(Constants.ORGANISM_TYPE_PLANT, 5, zone.getEnvironment().getOwnerID(), zone.getID(), 50, Constants.GROUP_SIZE, Constants.CREATE_STATUS_BIRTH);
//            }
//        }

        if (totalSpeciesList.isEmpty()) {
            zone.setDaysCollapsed(zone.getDaysCollapsed() + 1);
        } else {
            zone.setDaysCollapsed(0);
        }
    }

    private void runStageTwo(ZoneData data) {
        System.out.println("Running Stage Two...");
        long milliseconds = System.currentTimeMillis();

        HashMap<Integer, Integer> speciesDifference = new HashMap<Integer, Integer>();
        HashMap<Integer, SpeciesZoneType> speciesTypes = simulationEngine.getPrediction(data.getNodeList(), manipulationID, data.getCurrentTimeStep());

        createCSVs();

        try {
            System.out.println("Interpreting Biomass Results...");

            for (SpeciesZoneType species : speciesTypes.values()) {
                Integer speciesCount = totalNodeList.get(species.getNodeIndex());

                if (speciesCount != null) {
                    speciesDifference.put(species.getNodeIndex(), species.getSpeciesCount() - speciesCount);
                } else {
                    speciesDifference.put(species.getNodeIndex(), species.getSpeciesCount());
                }
            }

            List<Integer> speciesList = new ArrayList<Integer>(totalSpeciesList.keySet());
            Collections.shuffle(speciesList);

            for (int species_id : speciesList) {
                SpeciesType species = GameServer.getInstance().getSpecies(species_id);

                int gDiff = 0, rDiff = 0;
                boolean hasGrowth = true, hasReduced = true;

                for (int node_id : species.getNodeList()) {
                    int diff = speciesDifference.get(node_id) / species.getNodeAmount(node_id);

                    // Check Growth
                    if (diff > 0) {
                        gDiff = gDiff == 0 ? diff : Math.min(diff, gDiff);
                    } else {
                        hasGrowth = false;
                    }

                    // Check Reduction
                    if (diff < 0) {
                        rDiff = rDiff == 0 ? diff : Math.max(diff, rDiff);
                    } else {
                        hasReduced = false;
                    }
                }

                if (hasGrowth) {
                    System.out.println("  " + species.getSpeciesName() + " Species[" + species.getID() + "] increased by " + gDiff);

                    for (int node_id : species.getNodeList()) {
                        int amount = gDiff * species.getNodeAmount(node_id);
                        speciesDifference.put(node_id, speciesDifference.get(node_id) - amount);

                        System.out.println("    Node[" + node_id + "] increased by " + amount);
                    }

                    gameEngine.createOrganismsByBirth(species.getID(), zone.getID(), gDiff);
                } else if (hasReduced) {
                    System.out.println("  " + species.getSpeciesName() + " Species[" + species.getID() + "] decreased by " + Math.abs(rDiff));

                    for (int node_id : species.getNodeList()) {
                        int amount = rDiff * species.getNodeAmount(node_id);
                        speciesDifference.put(node_id, speciesDifference.get(node_id) - amount);

                        System.out.println("    Node[" + node_id + "] decreased by " + Math.abs(amount));
                    }

                    gameEngine.removeOrganismsByDeath(species.getID(), zone.getID(), Math.abs(rDiff));
                }
            }

            ZoneDAO.updateBiomass(zone.getID(), zone.getMaxBiomass(), zone.getPrevBiomass(), zone.getTotalBiomass());

            zone.getEnvironment().updateEnvironmentScore();

            zone.setCurrentTimeStep(zone.getCurrentTimeStep() + 1);
            ZoneDAO.updateTimeStep(zone.getID(), zone.getCurrentTimeStep());
        } catch (SQLException ex) {
            System.err.println(ex.getMessage());
            ex.printStackTrace();
        }

        zone.setLastSimulationTime(data.getGameScaleTime());

        System.out.println("Total Time (Run Stage Two): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");

        gameEngine.isReady(true);
    }

    public void createCSVs() {
        String csv = simulationEngine.getBiomassCSVString(manipulationID);

        try {
            String biomass_csv = GameServer.removeNodesFromCSV(csv);
            BiomassCSVDAO.createCSV(manipulationID, biomass_csv);

            biomass_csv = biomass_csv.substring(0, biomass_csv.lastIndexOf("\n"));

            ResponseChartBiomass responseChartBiomass = new ResponseChartBiomass();
            responseChartBiomass.setType((short) 0);
            responseChartBiomass.setCSV(biomass_csv);

            GameServer.getInstance().addResponseForUser(zone.getEnvironment().getOwnerID(), responseChartBiomass);
        } catch (Exception ex) {
            ex.printStackTrace();
            System.err.println(ex.getMessage());
        }

        try {
            String species_csv = GameServer.convertBiomassCSVtoSpeciesCSV(csv);
            SpeciesCSVDAO.createCSV(manipulationID, species_csv);

            species_csv = species_csv.substring(0, species_csv.lastIndexOf("\n"));

            ResponseChartBiomass responseChartBiomass = new ResponseChartBiomass();
            responseChartBiomass.setType((short) 1);
            responseChartBiomass.setCSV(species_csv);

            GameServer.getInstance().addResponseForUser(zone.getEnvironment().getOwnerID(), responseChartBiomass);
        } catch (Exception ex) {
            ex.printStackTrace();
            System.err.println(ex.getMessage());
        }
    }

    public void end() {
        isRunning = false;
    }
}
