package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 *
 * @author Gary
 */
public final class ZoneGroupsDAO {

    private ZoneGroupsDAO() {
    }

    public static int createGroup(int zone_id, int species_id, float pos_x, float pos_y, float pos_z) throws SQLException {
        int group_id = -1;

        String query = "INSERT INTO `zone_groups` (`zone_id`, `species_id`, `pos_x`, `pos_y`, `pos_z`) VALUES (?, ?, ?, ?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setInt(1, zone_id);
            pstmt.setInt(2, species_id);
            pstmt.setFloat(3, pos_x);
            pstmt.setFloat(4, pos_y);
            pstmt.setFloat(5, pos_z);
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
                group_id = rs.getInt(1);
            }

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return group_id;
    }

    public static void removeGroup(int group_id) throws SQLException {
        String query = "DELETE FROM `zone_groups` WHERE `group_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, group_id);
            pstmt.executeUpdate();

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static HashMap<Integer, List<Object[]>> getGroups(int zone_id) throws SQLException {
        HashMap<Integer, List<Object[]>> groupList = new HashMap<Integer, List<Object[]>>();

        String query = "SELECT * FROM `zone_groups` WHERE `zone_id` = ? ORDER BY `species_id`";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, zone_id);

            ResultSet rs = pstmt.executeQuery();

            int prev_id = -1;

            List<Object[]> speciesList = null;

            while (rs.next()) {
                int species_id = rs.getInt("species_id");

                if (species_id != prev_id) {
                    speciesList = new ArrayList<Object[]>();
                    groupList.put(species_id, speciesList);
                }

                int group_id = rs.getInt("group_id");
                float[] position = new float[]{rs.getFloat("pos_x"), rs.getFloat("pos_y"), rs.getFloat("pos_z")};

                speciesList.add(new Object[]{group_id, position});
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return groupList;
    }
}
