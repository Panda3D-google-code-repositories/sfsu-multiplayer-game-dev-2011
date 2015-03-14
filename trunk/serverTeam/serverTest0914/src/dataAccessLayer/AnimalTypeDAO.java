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
import model.AnimalType;

/**
 *
 * @author Partap Aujla
 */
public final class AnimalTypeDAO {

    private AnimalTypeDAO() {
    }

    public static List<AnimalType> getAnimals() throws SQLException {
        return getAnimals(new int[]{});
    }

    public static List<AnimalType> getAnimals(int[] excludeList) throws SQLException {
        List<AnimalType> animalList = new ArrayList<AnimalType>();

        String query = "SELECT * FROM `animal_type`";

        if (excludeList.length > 0) {
            String newExcludeList = Arrays.toString(excludeList);
            query += " WHERE `animal_type_id` NOT IN (" + newExcludeList.substring(1, newExcludeList.length() - 1) + ")";
        }

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                AnimalType animal = new AnimalType(rs.getInt("animal_type_id"));
                animal.setSpeciesName(rs.getString("species_name"));
                animal.setCost(rs.getInt("cost"));
                animal.setDescription(rs.getString("description"));
                animal.setCategory(rs.getString("category"));
                animal.setAvgBiomass(rs.getInt("max_biomass"));
                animal.setWaterBiomassLoss(rs.getInt("water_biomass_loss"));
                animal.setDietType(rs.getShort("diet_type"));
                animal.setWaterNeedFrequency(rs.getInt("water_need_frequency"));
                animal.setMetabolism(rs.getFloat("metabolism"));

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

                animal.setNodeList(newNodeList);
                animal.setNodeAmountList(nodeAmountList);

                animal.setTrophicLevel(rs.getFloat("trophic_level"));
                animal.setModelID(rs.getInt("model_id"));
                animal.setMass(rs.getInt("mass"));
                animal.setMovtForce(rs.getInt("movt_force"));
                animal.setMaxForce(rs.getInt("max_force"));
                animal.setHealChance(rs.getFloat("heal_chance"));
                animal.setAnimalCategory(rs.getString("animal_category"));
                animal.setGroupCapacity(rs.getInt("group_capacity"));

                animalList.add(animal);
            }

            rs.close();
            pstmt.close();

            HashMap<Integer, List<Integer>> cPredatorMap = CarnivoreDAO.getPreyToPredatorTable();
            HashMap<Integer, List<Integer>> cPreyMap = CarnivoreDAO.getPredatorToPreyTable();
            HashMap<Integer, List<Integer>> hPreyMap = HerbivoreDAO.getPredatorToPreyTable();

            for (AnimalType animal : animalList) {
                int animal_id = animal.getID();

                if (cPredatorMap.containsKey(animal_id)) {
                    for (int predator_id : cPredatorMap.get(animal_id)) {
                        animal.addPredatorID(predator_id, Constants.ORGANISM_TYPE_ANIMAL);
                    }
                }

                if (cPreyMap.containsKey(animal_id)) {
                    for (int prey_id : cPreyMap.get(animal_id)) {
                        animal.addPreyID(prey_id, Constants.ORGANISM_TYPE_ANIMAL);
                    }
                }

                if (hPreyMap.containsKey(animal_id)) {
                    for (int prey_id : hPreyMap.get(animal_id)) {
                        animal.addPreyID(prey_id, Constants.ORGANISM_TYPE_PLANT);
                    }
                }
            }
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return animalList;
    }

    /**
     * The function checks to make sure the passed argument is valid.  If not
     * prints an appropriate message. 
     * @param animal_type_id which is intType.
     * @return Returns species name by matching animalTypeID in database. If
     * none found returns null.
     * @throws SQLException
     */
    public static String getNameByAnimalTypeID(int animal_type_id) throws SQLException {
        String name = null;

        String query = "SELECT `species_name` FROM `animal_type` WHERE `animal_type_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, animal_type_id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                name = rs.getString("species_name");
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return name;
    }
    
    public static int getByAnimalName(String animalName) throws SQLException {
    	
    	String name = animalName.trim();
    	System.out.println("name " + name);
    	int animalTypeId = 0;
//        SELECT animal_type_id FROM `animal_type` WHERE species_name = 'Buffalo'
        String query = "SELECT animal_type_id FROM `animal_type` WHERE `species_name` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, name);
            ResultSet rs = pstmt.executeQuery();

            if(rs.next()){
	            animalTypeId = rs.getInt("animal_type_id");
	            System.out.println("animalTypeId " + animalTypeId);
            }
            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return animalTypeId;
    }
    
    
    public static int getByAnimalNodeIndex(int speciesId) throws SQLException {
    	int nodeIdx = 0;
        String query = "SELECT node_list FROM `animal_type` WHERE `animal_type_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, speciesId);
            ResultSet rs = pstmt.executeQuery();

            if(rs.next()){
            	nodeIdx = rs.getInt("node_list");
            	System.out.println("nodeIdx " + nodeIdx);
            }
            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return nodeIdx;
    }
}
