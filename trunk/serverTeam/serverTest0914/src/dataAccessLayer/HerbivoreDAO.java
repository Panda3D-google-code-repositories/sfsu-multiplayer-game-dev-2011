package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import model.AnimalType;
import model.PlantType;

/**
 * 
 * @author Partap Aujla
 */
public final class HerbivoreDAO {

    private HerbivoreDAO() {
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param plantType which is PlantTypeType. Extracts plant_type_id_pk.
     * @return Returns a List of predator names of passed argument, plantType.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<String> getPredatorNamesByPrey(PlantType plantType) throws SQLException {
        List<String> holdPredatorNameList = null;

        if (plantType == null || plantType.getID() <= 0) {
            System.out.println("In HerbivoreDAO.java -- plantType is null or plant_type_id_pk <= 0.");
            System.out.println("Expected value > 0\nReturning null");
        } else {
            holdPredatorNameList = new ArrayList<String>();

            String query = "SELECT DISTINT a.species_name FROM animal_type a "
                    + "JOIN herbivore h ON a.animal_type_id = h.animal_type_id "
                    + "WHERE h.plant_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, plantType.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    holdPredatorNameList.add(rs.getString("species_name"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(HerbivoreDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return holdPredatorNameList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param plantType which is PlantTypeType. Extracts plant_type_id_pk.
     * @return Returns a List of predator ids of passed argument, plantType.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getPredatorIDsByPrey(PlantType plantType) throws SQLException {
        List<Integer> returnPredatorIDsList = null;

        if (plantType == null || plantType.getID() <= 0) {
            System.out.println("In HerbivoreDAO.java -- plantType is null or plant_type_id_pk <= 0.");
            System.out.println("Expected value > 0\nReturning null");
        } else {
            returnPredatorIDsList = new ArrayList<Integer>();

            String query = "SELECT a.animal_type_id FROM animal_type a "
                    + "JOIN herbivore h ON a.animal_type_id = h.animal_type_id "
                    + "WHERE h.plant_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, plantType.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    returnPredatorIDsList.add(rs.getInt("animal_type_id"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(HerbivoreDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPredatorIDsList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param plant_type_id_pk which is intType.
     * @return Returns a List of predator ids of passed argument.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getPredatorIDsByPrey(int plant_type_id_pk) throws SQLException {
        List<Integer> returnPredatorIDsList = null;

        if (plant_type_id_pk <= 0) {
            System.out.println("In HerbivoreDAO.java -- plant_type_id_pk <= 0.");
            System.out.println("Expected value > 0\nReturning null");
        } else {
            returnPredatorIDsList = new ArrayList<Integer>();

            String query = "SELECT * FROM herbivore WHERE plant_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, plant_type_id_pk);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    returnPredatorIDsList.add(rs.getInt("animal_type_id"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(HerbivoreDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPredatorIDsList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param animalType which is AnimalTypeType. Extracts animal_type_id.
     * @return Returns a List of prey names of passed argument, animalType.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<String> getPreyNamesByPredator(AnimalType animalType) throws SQLException {
        List<String> returnPreyNameList = null;

        if (animalType == null || animalType.getID() <= 0) {
            System.out.println("In HerbivoreDAO -- animalType is null or animal_type_id <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPreyNameList = new ArrayList<String>();

            String query = "SELECT DISTINCT p.species_name FROM plant_type p "
                    + "JOIN herbivore h ON p.plant_type_id_pk = h.plant_type_id WHERE h.animal_type_id = ?";

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
            } catch (SQLException ex) {
                Logger.getLogger(CarnivoreDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPreyNameList;
    }

    public static HashMap<Integer, List<Integer>> getPredatorToPreyTable() throws SQLException {
        HashMap<Integer, List<Integer>> mapList = new HashMap<Integer, List<Integer>>();

        String query = "SELECT * FROM `herbivore` ORDER BY `animal_type_id` ASC";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            ResultSet rs = pstmt.executeQuery();

            int animal_id = -1, temp_id;
            List<Integer> plantList = null;

            while (rs.next()) {
                temp_id = rs.getInt("animal_type_id");

                if (temp_id != animal_id) {
                    animal_id = temp_id;

                    if (!mapList.containsKey(animal_id)) {
                        plantList = new ArrayList<Integer>();
                        mapList.put(animal_id, plantList);
                    } else {
                        plantList = mapList.get(animal_id);
                    }
                }

                plantList.add(rs.getInt("plant_type_id"));
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

    public static HashMap<Integer, List<Integer>> getPreyToPredatorTable() throws SQLException {
        HashMap<Integer, List<Integer>> mapList = new HashMap<Integer, List<Integer>>();

        String query = "SELECT * FROM `herbivore` ORDER BY `plant_type_id` ASC";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            ResultSet rs = pstmt.executeQuery();

            int plant_id = -1, temp_id;
            List<Integer> animalList = null;

            while (rs.next()) {
                temp_id = rs.getInt("plant_type_id");

                if (temp_id != plant_id) {
                    plant_id = temp_id;

                    if (!mapList.containsKey(plant_id)) {
                        animalList = new ArrayList<Integer>();
                        mapList.put(plant_id, animalList);
                    } else {
                        animalList = mapList.get(plant_id);
                    }
                }

                animalList.add(rs.getInt("animal_type_id"));
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

    public static List<Integer> getPreyNamesOfPredator(AnimalType animalType) throws SQLException {
        List<Integer> returnPreyIDsList = null;

        if (animalType == null || animalType.getID() <= 0) {
            System.out.println("In HerbivoreDAO -- animalType is null or animal_type_id <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPreyIDsList = new ArrayList<Integer>();

//            String query = "SELECT p.species_name FROM herbivore h "
//                    + "JOIN plant_type p ON h.plant_type_id = p.plant_type_id_pk "
//                    + "WHERE animal_type_id = ?";
            String query = "SELECT plant_type_id FROM herbivore "
                    + "WHERE animal_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, animalType.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    returnPreyIDsList.add(rs.getInt("plant_type_id"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(CarnivoreDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPreyIDsList;
    }

    /**
     * The function checks for invalid arguments.  If passed argument is invalid
     * prints out an appropriate message.
     * @param animalType which is AnimalTypeType. Extracts animal_type_id.
     * @return Returns a List of prey ids of passed argument, animalType.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getPreyIDsByPredator(AnimalType animalType) throws SQLException {
        List<Integer> returnPreyIDsList = null;

        if (animalType == null || animalType.getID() <= 0) {
            System.out.println("In HerbivoreDAO -- animalType is null or animal_type_id <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPreyIDsList = new ArrayList<Integer>();

            String query = "SELECT * FROM herbivore WHERE animal_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, animalType.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    returnPreyIDsList.add(rs.getInt("plant_type_id"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(CarnivoreDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
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
    public static List<Integer> getPreyIDsByPredator(int animal_type_id) throws SQLException {
        List<Integer> returnPreyIDsList = null;

        if (animal_type_id <= 0) {
            System.out.println("In HerbivoreDAO -- animal_type_id <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPreyIDsList = new ArrayList<Integer>();

            String query = "SELECT * FROM herbivore WHERE animal_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, animal_type_id);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    returnPreyIDsList.add(rs.getInt("plant_type_id"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(CarnivoreDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPreyIDsList;
    }
}
