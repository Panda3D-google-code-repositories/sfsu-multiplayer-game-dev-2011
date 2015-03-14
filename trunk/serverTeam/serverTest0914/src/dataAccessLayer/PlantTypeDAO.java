package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

import metadata.Constants;
import model.PlantType;

/**
 *
 * @author Partap Aujla
 */
public final class PlantTypeDAO {

    private PlantTypeDAO() {
    }

    public static List<PlantType> getPlants() throws SQLException {
        return getPlants(new int[]{});
    }

    public static List<PlantType> getPlants(int[] excludeList) throws SQLException {
        List<PlantType> plantList = new ArrayList<PlantType>();

        String query = "SELECT * FROM `plant_type`";

        if (excludeList.length > 0) {
            String newExcludeList = Arrays.toString(excludeList);
            query += " WHERE `plant_type_id` NOT IN (" + newExcludeList.substring(1, newExcludeList.length() - 1) + ")";
        }

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                PlantType plant = new PlantType(rs.getInt("plant_type_id"));
                plant.setSpeciesName(rs.getString("species_name"));
                plant.setCost(rs.getInt("cost"));
                plant.setDescription(rs.getString("description"));
                plant.setCategory(rs.getString("category"));
                plant.setAvgBiomass(rs.getInt("max_biomass"));
                plant.setWaterNeedFrequency(rs.getInt("water_need_frequency"));
                plant.setLightNeedFrequency(rs.getInt("light_need_frequency"));
                plant.setGrowRadius(rs.getFloat("grow_radius"));
                plant.setCarryingCapacity(rs.getFloat("carrying_capacity"));

                String[] nodeList = rs.getString("node_list").split(",");

                int[] newNodeList = new int[nodeList.length];
                HashMap<Integer, Integer> nodeAmountList = new HashMap<Integer, Integer>();

                for (int i = 0; i < nodeList.length; i++) {
                    String[] nodePair = nodeList[i].split(":");

                    newNodeList[i] = Integer.parseInt(nodePair[0]);

                    if (nodePair.length == 1) {
                        nodeAmountList.put(newNodeList[i], 1);
                    } else {
                        nodeAmountList.put(newNodeList[i], Integer.parseInt(nodePair[1]));
                    }
                }

                plant.setNodeList(newNodeList);
                plant.setNodeAmountList(nodeAmountList);

                plant.setTrophicLevel(rs.getFloat("trophic_level"));
                plant.setGrowthRate(rs.getFloat("growth_rate"));
                plant.setModelID(rs.getInt("model_id"));
                plant.setHealChance(rs.getFloat("heal_chance"));
                plant.setGroupCapacity(rs.getInt("group_capacity"));
                plantList.add(plant);
            }

            rs.close();
            pstmt.close();

            HashMap<Integer, List<Integer>> hPredatorMap = HerbivoreDAO.getPreyToPredatorTable();

            for (PlantType plant : plantList) {
                int plant_id = plant.getID();

                if (hPredatorMap.containsKey(plant_id)) {
                    for (int predator_id : hPredatorMap.get(plant_id)) {
                        plant.addPredatorID(predator_id, Constants.ORGANISM_TYPE_ANIMAL);
                    }
                }
            }
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return plantList;
    }

    /**
     * The function checks to make sure the passed argument is valid.  If not
     * prints an appropriate message.
     * @param plantTypeID which is intType.
     * @return Returns species name by matching plantTypeID in database. If
     * none found returns null.
     * @throws SQLException
     */
    public static String getNameByPlantTypeID(int plantTypeID) throws SQLException {
        String returnPlantName = null;

        String query = "SELECT `species_name` FROM `plant_type` WHERE `plant_type_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, plantTypeID);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                returnPlantName = rs.getString("species_name");
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPlantName;
    }
    
    public static int getByPlantName(String plantName) throws SQLException {
    	String name = plantName.trim();
    	System.out.println("name " + name);
    	int plantTypeId = 0;
//        SELECT animal_type_id FROM `animal_type` WHERE species_name = 'Buffalo'
        String query = "SELECT plant_type_id FROM `plant_type` WHERE `species_name` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, name);
            ResultSet rs = pstmt.executeQuery();

            if(rs.next()){
	            plantTypeId = rs.getInt("plant_type_id");
	            System.out.println("plantTypeId " + plantTypeId);
            }
            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return plantTypeId;
    }
    
    public static int[] getByPlantNodeIndex(int speciesId) throws SQLException {
    	String[] nodeList;
    	int[] newNodeList = null;
//        SELECT animal_type_id FROM `animal_type` WHERE species_name = 'Buffalo'
        String query = "SELECT node_list FROM `plant_type` WHERE `plant_type_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, speciesId);
            ResultSet rs = pstmt.executeQuery();

            if(rs.next()){
            	nodeList = rs.getString("node_list").split(",");
                newNodeList = new int[nodeList.length];
                HashMap<Integer, Integer> nodeAmountList = new HashMap<Integer, Integer>();

                for (int i = 0; i < nodeList.length; i++) {
                    String[] nodePair = nodeList[i].split(":");

                    newNodeList[i] = Integer.parseInt(nodePair[0]);

                    if (nodePair.length == 1) {
                        nodeAmountList.put(newNodeList[i], 1);
                    } else {
                        nodeAmountList.put(newNodeList[i], Integer.parseInt(nodePair[1]));
                    }
                }
            }
            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return newNodeList;
    }
}
