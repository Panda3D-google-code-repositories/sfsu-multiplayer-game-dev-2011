package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
import java.util.Date;

import model.Player;

/**
 *
 * @author Partap Aujla & Jagjit Singh
 */
public final class PlayerDAO {

    private PlayerDAO() {
    }

    /**
     * The function saves the passed player to the database. However,
     * playerIdPk(in player) does not get stored  because this field is
     * automatically generated in database. Function checks if passed argument
     * is valid.  If not prints out an appropriate message.
     * @param player which is PlayerType. Extracts userName, password, emailId,
     * and characterName.
     * @throws SQLException
     */
    public static int createAccount(String email, String password, String username, String first_name, String last_name, String last_ip) throws SQLException {
        int player_id = -1;

        String query = "INSERT INTO `player` (`username`, `email`, `password`, `first_name`, `last_name`, `last_ip`) VALUES (?, ?, ?, ?, ?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setString(1, username);
            pstmt.setString(2, email);
            pstmt.setString(3, password);
            pstmt.setString(4, first_name);
            pstmt.setString(5, last_name);
            pstmt.setString(6, last_ip);
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
                player_id = rs.getInt(1);
            }

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return player_id;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param player_id which is intType.
     * @return Returns PlayerType by matching player_id if found in the
     * database.  If not found then returns null.
     * @throws SQLException
     */
    public static Player getByPlayerID(int player_id) throws SQLException {
        Player returnPlayer = null;

        String query = "SELECT * FROM `player` WHERE `player_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, player_id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                returnPlayer = new Player(rs.getInt("player_id"));
                returnPlayer.setUsername(rs.getString("username"));
                returnPlayer.setPassword(rs.getString("password"));
                returnPlayer.setEmail(rs.getString("email"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPlayer;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param username which is StringType.
     * @return Returns a player by matching userName in database.  If none
     * found returns null.
     * @throws SQLException
     */
    public static Player getByUsername(String username) throws SQLException {
        Player returnPlayer = null;

        String query = "SELECT * FROM `player` WHERE `username` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, username);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                returnPlayer = new Player(rs.getInt("player_id"));
                returnPlayer.setUsername(rs.getString("username"));
                returnPlayer.setPassword(rs.getString("password"));
                returnPlayer.setEmail(rs.getString("email"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPlayer;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param player which is PlayerType. Extracts userName and password.
     * @return Returns a player by matching userName and password, both
     * extracted from player, in database.  If none found returns null.
     * @throws SQLException
     */
    public static Player getAccount(String email, String password) throws SQLException {
        Player player = null;

        String query = "SELECT * FROM `player` WHERE `email` = ? AND `password` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, email);
            pstmt.setString(2, password);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                player = new Player(rs.getInt("player_id"));
                player.setUsername(rs.getString("username"));
                player.setEmail(rs.getString("email"));
                player.setPassword(rs.getString("password"));
                player.setPlayTime(rs.getLong("play_time"));
                player.setLastLogout(rs.getString("last_logout"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return player;
    }

    public static boolean containsEmail(String email) throws SQLException {
        boolean status = false;

        String query = "SELECT * FROM `player` WHERE `email` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, email);
            ResultSet rs = pstmt.executeQuery();

            status = rs.next();

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return status;
    }

    public static boolean containsUsername(String username) throws SQLException {
        boolean status = false;

        String query = "SELECT * FROM `player` WHERE `username` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, username);
            ResultSet rs = pstmt.executeQuery();

            status = rs.next();

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return status;
    }

    public static void updateLogin(int player_id, String address) throws SQLException {
        String query = "UPDATE `player` SET `online` = 1, `last_login` = ?, `last_ip` = ?  WHERE `player_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setTimestamp(1, new Timestamp(new Date().getTime()));
            pstmt.setString(2, address);
            pstmt.setInt(3, player_id);
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updateLogout(int player_id, long play_time) throws SQLException {
        String query = "UPDATE `player` SET `online` = 0, `play_time` = ?, `last_logout` = ? WHERE `player_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setLong(1, play_time);
            pstmt.setTimestamp(2, new Timestamp(new Date().getTime()));
            pstmt.setInt(3, player_id);
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updatePlayTime(int player_id, long play_time) throws SQLException {
        String query = "UPDATE `player` SET `play_time` = ? WHERE `player_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setLong(1, play_time);
            pstmt.setInt(2, player_id);
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
}
