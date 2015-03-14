package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import worldManager.gameEngine.Disease;
import worldManager.gameEngine.NatureControllerType;

/**
 *
 * @author Partap Aujla
 */
public final class NatureControllerTypeDAO {

    private NatureControllerTypeDAO() {
    }

    /**
     * 
     * @return This function returns a list of all the Nature Controller Type
     * from the database.
     * @throws SQLException 
     */
    public static List<NatureControllerType> getAllNatureController() throws SQLException {
        List<NatureControllerType> returnNCT = new ArrayList<NatureControllerType>();

        String query = "SELECT * FROM `nature_controller`";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                NatureControllerType holdNCT = new NatureControllerType(rs.getInt("nature_controller_id"));
                holdNCT.setEcosystemType(rs.getString("ecosystem_type"));
                holdNCT.setCloudyChance(rs.getFloat("cloudy_chance"));
                holdNCT.setAverageCloud(rs.getFloat("average_cloud"));
                holdNCT.setCloudRange(rs.getFloat("cloud_range"));
                holdNCT.setRainChance(rs.getFloat("rain_chance"));
                holdNCT.setAverageRain(rs.getFloat("average_rain"));
                holdNCT.setRainRange(rs.getFloat("rain_range"));
                holdNCT.setEvaporationRate(rs.getFloat("evaporation_rate"));
                returnNCT.add(holdNCT);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnNCT;
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message and returns null.
     * @param nature_controller_id which is intType.
     * @return Returns NatureControllerType by matching the passed
     * nature_controller_id to the database.  Note NatureControllerType
     * contains DiseaseType.  If none found returns null.
     * @throws SQLException
     */
    public static NatureControllerType getByNatureControllerID(int nature_controller_id) throws SQLException {
        NatureControllerType returnNatureControllerType = null;

        String query = "SELECT * FROM `nature_controller` WHERE `nature_controller_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, nature_controller_id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                returnNatureControllerType = new NatureControllerType(rs.getInt("nature_controller_id"));
                returnNatureControllerType.setEcosystemType(rs.getString("ecosystem_type"));
                returnNatureControllerType.setCloudyChance(rs.getFloat("cloudy_chance"));
                returnNatureControllerType.setAverageCloud(rs.getFloat("average_cloud"));
                returnNatureControllerType.setCloudRange(rs.getFloat("cloud_range"));
                returnNatureControllerType.setRainChance(rs.getFloat("rain_chance"));
                returnNatureControllerType.setAverageRain(rs.getFloat("average_rain"));
                returnNatureControllerType.setRainRange(rs.getFloat("rain_range"));
                returnNatureControllerType.setEvaporationRate(rs.getFloat("evaporation_rate"));

                Disease holdDisease = DiseaseDAO.getByDiseaseID(rs.getInt("disease_id"));
                //...
                //Ask Nathan;
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnNatureControllerType;
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message and returns null.
     * @param world_id which is intType.
     * @return Returns NatureControllerType by matching the passed
     * nature_controller_id to the database.  Note NatureControllerType
     * contains DiseaseType.  If none found returns null.
     * @throws SQLException
     */
    public static NatureControllerType getByWorldID(int world_id) throws SQLException {
        NatureControllerType returnNatureControllerType = null;

        String query = "SELECT * FROM `world` w JOIN `nature_controller` n ON w.`nature_controller_id` = n.`nature_controller_id` WHERE `world_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, world_id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                returnNatureControllerType = new NatureControllerType(rs.getInt("nature_controller_id"));
                returnNatureControllerType.setEcosystemType(rs.getString("ecosystem_type"));
                returnNatureControllerType.setCloudyChance(rs.getFloat("cloudy_chance"));
                returnNatureControllerType.setAverageCloud(rs.getFloat("average_cloud"));
                returnNatureControllerType.setCloudRange(rs.getFloat("cloud_range"));
                returnNatureControllerType.setRainChance(rs.getFloat("rain_chance"));
                returnNatureControllerType.setAverageRain(rs.getFloat("average_rain"));
                returnNatureControllerType.setRainRange(rs.getFloat("rain_range"));
                returnNatureControllerType.setEvaporationRate(rs.getFloat("evaporation_rate"));

                Disease holdDisease = DiseaseDAO.getByDiseaseID(rs.getInt("disease_id"));
                //...
                //Ask Nathan;
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnNatureControllerType;
    }
}
