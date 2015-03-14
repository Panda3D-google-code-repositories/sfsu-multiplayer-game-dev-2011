package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 *
 * @author Gary
 */
public final class UserActionsCSVDAO {

    private UserActionsCSVDAO() {
    }

    public static void createCSV(String manipulation_id, String csv) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query_1 = "SELECT * FROM `user_actions_csv` WHERE `manipulation_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query_1);
            pstmt.setString(1, manipulation_id);
            ResultSet rs = pstmt.executeQuery();

            if (!rs.next()) {
                pstmt.close();

                String query_2 = "INSERT INTO `user_actions_csv` (`manipulation_id`, `csv`) VALUES (?, ?)";
                pstmt = connection.prepareStatement(query_2);
                pstmt.setString(1, manipulation_id);
                pstmt.setString(2, csv);
            } else {
                pstmt.close();

                String query_3 = "UPDATE `user_actions_csv` SET `csv` = ? WHERE `manipulation_id` = ?";
                pstmt = connection.prepareStatement(query_3);
                pstmt.setString(1, csv);
                pstmt.setString(2, manipulation_id);
            }

            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
}
