package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;

/**
 *
 * @author Gary
 */
public final class DeathListDAO {

    private DeathListDAO() {
    }

    public static void createEntry(int zone_id, int species_id, int total) throws SQLException {
        String query_1 = "SELECT * FROM `death_list` WHERE `zone_id` = ? AND `species_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query_1);
            pstmt.setInt(1, zone_id);
            pstmt.setInt(2, species_id);

            ResultSet rs = pstmt.executeQuery();

            if (!rs.next()) {
                pstmt.close();

                String query_2 = "INSERT INTO `death_list` (`zone_id`, `species_id`, `total`) VALUES (?, ?, ?)";
                pstmt = connection.prepareStatement(query_2);
                pstmt.setInt(1, zone_id);
                pstmt.setInt(2, species_id);
                pstmt.setInt(3, total);
            } else {
                pstmt.close();

                String query_3 = "UPDATE `death_list` SET `total` = ? WHERE `zone_id` = ? AND `species_id` = ?";
                pstmt = connection.prepareStatement(query_3);
                pstmt.setInt(1, total);
                pstmt.setInt(2, zone_id);
                pstmt.setInt(3, species_id);
            }

            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
    
    public static void removeEntry(int zone_id, int species_id) throws SQLException {
        String query = "DELETE FROM `death_list` WHERE `zone_id` = ? AND `species_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, zone_id);
            pstmt.setInt(2, species_id);

            pstmt.executeUpdate();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static HashMap<Integer, Integer[]> getList(int zone_id) throws SQLException {
        HashMap<Integer, Integer[]> birthList = new HashMap<Integer, Integer[]>();

        String query = "SELECT * FROM `death_list` WHERE `zone_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, zone_id);

            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                int species_id = rs.getInt("species_id");
                int total = rs.getInt("total");
                int amount = rs.getInt("amount");
                birthList.put(species_id, new Integer[]{total, amount});
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return birthList;
    }

    public static void updateAmount(int zone_id, int species_id, int amount) throws SQLException {
        String query = "UPDATE `death_list` SET `amount` = ? WHERE `zone_id` = ? AND `species_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, amount);
            pstmt.setInt(2, zone_id);
            pstmt.setInt(3, species_id);

            pstmt.executeUpdate();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
}
