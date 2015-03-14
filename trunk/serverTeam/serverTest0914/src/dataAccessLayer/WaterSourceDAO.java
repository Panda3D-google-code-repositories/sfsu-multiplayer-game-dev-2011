package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import worldManager.gameEngine.WaterSource;

/**
 *
 * @author Partap Aujla
 */
public final class WaterSourceDAO {

    private WaterSourceDAO() {
    }

    /**
     * The function saves the passed argument to the database. The function
     * checks the passed argument is not null if it is then prints the appropriate
     * message.
     * @param waterSource
     * @throws SQLException
     */
    public static int createWaterSource(WaterSource waterSource) throws SQLException {
        int water_source_id = -1;

        String query = "INSERT INTO `water_source` (`water`, `max_water`, `water_radius`, `location_x`, `location_y`, `location_z`, `zone_id`) VALUES (?, ?, ?, ?, ?, ?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setInt(1, waterSource.getWater());
            pstmt.setInt(2, waterSource.getMaxWater());
            pstmt.setInt(3, waterSource.getRadius());
            pstmt.setFloat(4, waterSource.getX());
            pstmt.setFloat(5, waterSource.getY());
            pstmt.setFloat(6, waterSource.getZ());
            pstmt.setInt(7, waterSource.getZoneID());
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
                water_source_id = rs.getInt(1);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return water_source_id;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out an
     * appropriate message.
     * @param zone_id which is intType.
     * @return Returns a list of WaterSource in a passed zonePID by matching
     * it in the database. If none found returns null.
     * @throws SQLException
     */
    public static List<WaterSource> getByZoneID(int zone_id) throws SQLException {
        List<WaterSource> waterSourceList = new ArrayList<WaterSource>();

        String query = "SELECT * FROM `water_source` WHERE `zone_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, zone_id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                WaterSource waterSource = new WaterSource(rs.getInt("water_source_id"));
                waterSource.setWater(rs.getInt("water"));
                waterSource.setMaxWater(rs.getInt("max_water"));
                waterSource.setRadius(rs.getInt("water_radius"));
                waterSource.setX(rs.getFloat("location_x"));
                waterSource.setY(rs.getFloat("location_y"));
                waterSource.setZ(rs.getFloat("location_z"));
                waterSource.setZoneID(rs.getInt("zone_id"));
                waterSourceList.add(waterSource);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return waterSourceList;
    }
}