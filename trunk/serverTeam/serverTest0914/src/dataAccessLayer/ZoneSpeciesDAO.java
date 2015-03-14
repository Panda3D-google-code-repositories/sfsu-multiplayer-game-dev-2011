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
public final class ZoneSpeciesDAO {

    private ZoneSpeciesDAO() {
    }

    public static void createSpecies(int zone_id, int species_id, int num_groups, int amount) throws SQLException {
        String query = "INSERT INTO `zone_species` (`zone_id`, `species_id`, `num_groups`, `amount`) VALUES (?, ?, ?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, zone_id);
            pstmt.setInt(2, species_id);
            pstmt.setInt(3, num_groups);
            pstmt.setInt(4, amount);
            pstmt.execute();

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static HashMap<Integer, Integer[]> getSpecies(int zone_id) throws SQLException {
        HashMap<Integer, Integer[]> speciesList = new HashMap<Integer, Integer[]>();

        String query = "SELECT * FROM `zone_species` WHERE `zone_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, zone_id);

            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                int num_groups = rs.getInt("num_groups");
                int amount = rs.getInt("amount");

                speciesList.put(rs.getInt("species_id"), new Integer[]{num_groups, amount});
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return speciesList;
    }

    public static void updateSpecies(int zone_id, int species_id, int num_groups, int amount) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `zone_species` SET `num_groups` = ?, `amount` = ? WHERE `zone_id` = ? AND `species_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, num_groups);
            pstmt.setInt(2, amount);
            pstmt.setInt(3, zone_id);
            pstmt.setInt(4, species_id);
            pstmt.execute();

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updateGroups(int zone_id, int species_id, int num_groups) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `zone_species` SET `num_groups` = ? WHERE `zone_id` = ? AND `species_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, num_groups);
            pstmt.setInt(2, zone_id);
            pstmt.setInt(3, species_id);
            pstmt.execute();

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updateAmount(int zone_id, int species_id, int amount) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `zone_species` SET `amount` = ? WHERE `zone_id` = ? AND `species_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, amount);
            pstmt.setInt(2, zone_id);
            pstmt.setInt(3, species_id);
            pstmt.execute();

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
}
