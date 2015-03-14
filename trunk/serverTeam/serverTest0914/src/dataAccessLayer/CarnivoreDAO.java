package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import model.AnimalType;

/**
 * 
 * @author Partap Aujla
 */
public final class CarnivoreDAO {

    private CarnivoreDAO() {
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param animalType which is AnimalTypeType. Extracts animal_type_id_pk.
     * @return Returns a List of predator ids of passed argument, animalType.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getPredatorIDsByPrey(AnimalType animalType) throws SQLException {
        List<Integer> returnPredatorIDsList = new ArrayList<Integer>();

        String query = "SELECT * FROM `carnivore` WHERE `prey_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, animalType.getID());
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                returnPredatorIDsList.add(rs.getInt("predator_id"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPredatorIDsList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param animal_type_id which is intType.
     * @return Returns a List of predator ids of passed argument.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getPredatorIDsByPrey(int animal_type_id) throws SQLException {
        List<Integer> returnPredatorIDsList = new ArrayList<Integer>();

        String query = "SELECT * FROM `carnivore` WHERE `prey_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, animal_type_id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                returnPredatorIDsList.add(rs.getInt("predator_id"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPredatorIDsList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param animalType which is AnimalTypeType. Extracts animal_type_id_pk.
     * @return Returns a List of predator names of passed argument, animalType.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getPredatorNamesOfPrey(AnimalType animalType) throws SQLException {
        List<Integer> holdPredatorNameList = new ArrayList<Integer>();

//            String query = "SELECT DISTINCT a.species_name FROM animal_type a "
//                    + "JOIN carnivore c ON a.animal_type_id = c.predator_id "
//                    + "WHERE c.prey_id = ?";
        String query = "SELECT `predator_id` FROM `carnivore` "
                + "WHERE `prey_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, animalType.getID());
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                holdPredatorNameList.add(rs.getInt("predator_id"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return holdPredatorNameList;
    }

    public static HashMap<Integer, List<Integer>> getPreyToPredatorTable() throws SQLException {
        HashMap<Integer, List<Integer>> mapList = new HashMap<Integer, List<Integer>>();

        String query = "SELECT * FROM `carnivore` ORDER BY `prey_id` ASC";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            ResultSet rs = pstmt.executeQuery();

            int prey_id = -1, temp_id;
            List<Integer> predatorList = null;

            while (rs.next()) {
                temp_id = rs.getInt("prey_id");

                if (temp_id != prey_id) {
                    prey_id = temp_id;

                    if (!mapList.containsKey(prey_id)) {
                        predatorList = new ArrayList<Integer>();
                        mapList.put(prey_id, predatorList);
                    } else {
                        predatorList = mapList.get(prey_id);
                    }
                }

                predatorList.add(rs.getInt("predator_id"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return mapList;
    }

    public static HashMap<Integer, List<Integer>> getPredatorToPreyTable() throws SQLException {
        HashMap<Integer, List<Integer>> mapList = new HashMap<Integer, List<Integer>>();

        String query = "SELECT * FROM `carnivore` ORDER BY `predator_id` ASC";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            ResultSet rs = pstmt.executeQuery();

            int predator_id = -1, temp_id;
            List<Integer> preyList = null;

            while (rs.next()) {
                temp_id = rs.getInt("predator_id");

                if (temp_id != predator_id) {
                    predator_id = temp_id;

                    if (!mapList.containsKey(predator_id)) {
                        preyList = new ArrayList<Integer>();
                        mapList.put(predator_id, preyList);
                    } else {
                        preyList = mapList.get(predator_id);
                    }
                }

                preyList.add(rs.getInt("prey_id"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return mapList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param animalType which is AnimalTypeType. Extracts animal_type_id_pk.
     * @return Returns a List of prey names of passed argument, animalType.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<String> getPreyNamesByPredator(AnimalType animalType) throws SQLException {
        List<String> returnPreyNameList = new ArrayList<String>();

        String query = "SELECT DISTINCT a.species_name FROM animal_type a "
                + "JOIN carnivore c ON a.animal_type_id = c.prey_id "
                + "WHERE c.predator_id = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, animalType.getID());
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                returnPreyNameList.add(rs.getString("species_name"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPreyNameList;
    }

    public static List<Integer> getPreyNamesOfPredator(AnimalType animalType) throws SQLException {
        List<Integer> returnPreyIDsList = new ArrayList<Integer>();

//            String query = "SELECT a.species_name FROM carnivore c "
//                    + "JOIN animal_type a ON c.prey_id = a.animal_type_id "
//                    + "WHERE predator_id = ?";
        String query = "SELECT `prey_id` FROM `carnivore` "
                + "WHERE `predator_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, animalType.getID());
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                returnPreyIDsList.add(rs.getInt("prey_id"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPreyIDsList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param animalType which is AnimalTypeType. Extracts animal_type_id_pk.
     * @return Returns a List of prey ids of passed argument, animalType.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getPreyIDsByPredators(AnimalType animalType) throws SQLException {
        List<Integer> returnPreyIDsList = new ArrayList<Integer>();

        String query = "SELECT * FROM `carnivore` WHERE `predator_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, animalType.getID());
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                returnPreyIDsList.add(rs.getInt("prey_id"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPreyIDsList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param animal_type_id which is intType.
     * @return Returns a List of prey ids of passed argument.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getPreyIDsByPredators(int animal_type_id) throws SQLException {
        List<Integer> returnPreyIDsList = new ArrayList<Integer>();

        String query = "SELECT * FROM `carnivore` WHERE `predator_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, animal_type_id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                returnPreyIDsList.add(rs.getInt("prey_id"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPreyIDsList;
    }
}
