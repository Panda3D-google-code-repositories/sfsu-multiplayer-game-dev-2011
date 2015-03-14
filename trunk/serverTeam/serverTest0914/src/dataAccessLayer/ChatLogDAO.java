package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 *
 * @author Gary
 */
public class ChatLogDAO {

    private ChatLogDAO() {
    }

    public static void createMessage(int player_id, String message) throws SQLException {
        String query = "INSERT INTO `chat_log` (`player_id`, `message`) VALUES (?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, player_id);
            pstmt.setString(2, message);
            pstmt.execute();

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
}
