package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import model.Avatar;

/**
 *
 * @author Partap Aujla
 */
public final class AvatarDAO {

    private AvatarDAO() {
    }

    /**
     * The function saves the passed avatar to the database.  Although, the
     * AvatarType contains a PlayerType the function only stores the player id
     * and no other Player information. Also, avatarIdPk(in avatar) does not get
     * stored  because this field is automatically generated in database.
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message.
     * @param avatar which is AvatarType. Extracts avatarType, experience,
     * abilityPoints, inEnvIDFk, currency, player, teamNo, envPosition, level,
     * environment_score, and gamescale_vote.
     * @throws SQLException
     */
    public static int createAvatar(Avatar avatar) throws SQLException {
        int avatar_id = -1;

        String query = "INSERT INTO `avatar` (`type`, `experience`, `ability_points`, `currency`, `player_id`) VALUES (?, ?, ?, ?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setInt(1, avatar.getAvatarType());
            pstmt.setInt(2, avatar.getExperience());
            pstmt.setInt(3, avatar.getAbilityPoints());
            pstmt.setInt(4, avatar.getCurrency());
            pstmt.setInt(5, avatar.getPlayerID());
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
                avatar_id = rs.getInt(1);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return avatar_id;
    }

    public static Avatar getAvatar(int avatar_id) throws SQLException {
        Avatar avatar = null;

        String query = "SELECT * FROM `avatar` WHERE `avatar_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, avatar_id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                avatar = new Avatar(rs.getInt("avatar_id"));
                avatar.setAvatarType(rs.getInt("type"));
                avatar.setExperience(rs.getInt("experience"));
                avatar.setAbilityPoints(rs.getInt("ability_points"));
                avatar.setCurrency(rs.getInt("currency"));
                avatar.setLevel(rs.getInt("level"));
                avatar.setGameScaleVote(rs.getInt("gamescale_vote"));
                avatar.setLastPlayed(rs.getString("last_played"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return avatar;
    }

    public static List<Avatar> getAvatars(int player_id) throws SQLException {
        List<Avatar> avatars = new ArrayList<Avatar>();

        String query = "SELECT * FROM `avatar` WHERE `player_id` = ? ORDER BY `last_played` DESC";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, player_id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                Avatar avatar = new Avatar(rs.getInt("avatar_id"));
                avatar.setAvatarType(rs.getInt("type"));
                avatar.setExperience(rs.getInt("experience"));
                avatar.setAbilityPoints(rs.getInt("ability_points"));
                avatar.setCurrency(rs.getInt("currency"));
                avatar.setLevel(rs.getInt("level"));
                avatar.setGameScaleVote(rs.getInt("gamescale_vote"));
                avatar.setLastPlayed(rs.getString("last_played"));

                avatars.add(avatar);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return avatars;
    }

    /**
     * Checks the database for an avatar by avatarID.  If found deletes it.
     * Checks the passed argument to make sure correct value if invalid prints
     * the appropriate message.
     * @param avatar_id which is intType.
     * @throws SQLException
     */
    public static void deleteAvatarByID(int avatar_id) throws SQLException {
        String query = "DELETE FROM `avatar` WHERE `avatar_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, avatar_id);
            pstmt.executeUpdate();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    /**
     * The function updates the passed avatar to the database. However,
     * avatarIdPk(in avatar) does not get updated  because this field is
     * automatically generated in database.  Before the value is updated in
     * database the function checks to see if any numeric value is less than 0
     * and if any Object value is null.  If that is the case then the
     * function prints out appropriate message.  The function also checks to
     * make sure that the avatar being updated exists.  If it does not then
     * prints out appropriate message.
     * @param avatar which is AvatarType. Extracts avatarType, experience,
     * abilityPoints, inEnvIDFk, currency, player(from which extracts playerIdPk),
     * teamNo, envPostion, level, environment_score, and gamescale_vote.
     * @throws SQLException
     */
    public static void updateAvatar(Avatar avatar) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `avatar` SET `type` = ?, `experience` = ?, `ability_points` = ?, `currency` = ?, `player_id` = ?, `env_position` = ?, `level` = ?, `gamescale_vote` = ? WHERE `avatar_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, avatar.getAvatarType());
            pstmt.setInt(2, avatar.getExperience());
            pstmt.setInt(3, avatar.getAbilityPoints());
            pstmt.setInt(4, avatar.getCurrency());
            pstmt.setInt(5, avatar.getPlayerID());
            pstmt.setInt(6, avatar.getLevel());
            pstmt.setInt(7, avatar.getGameScaleVote());
            pstmt.setInt(8, avatar.getID());
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    /**
     * The function checks to make sure the passed argument is valid -Breeder,
     * Planter, or Weather Man. If not prints the appropriate message.
     * @param avatarType which is StringType.
     * @return Returns the first AvatarType which matches the passed argument,
     * avatarType, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static Avatar getAvatarByAvatarTypeSpecialUse(String avatarType) throws SQLException {
        Avatar returnFirstAvatar = null;

        List<Avatar> holdAvatarList = new ArrayList<Avatar>();

        String query = "SELECT * FROM `avatar` WHERE `type` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, avatarType);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                Avatar holdAvatar = new Avatar(rs.getInt("avatar_id"));
                holdAvatar.setAvatarType(rs.getInt("type"));
                holdAvatar.setExperience(rs.getInt("experience"));
                holdAvatar.setAbilityPoints(rs.getInt("ability_points"));
                holdAvatar.setCurrency(rs.getInt("currency"));
                holdAvatar.setPlayerID(rs.getInt("player_id"));
                holdAvatar.setLevel(rs.getInt("level"));
                holdAvatar.setGameScaleVote(rs.getInt("gamescale_vote"));
                holdAvatarList.add(holdAvatar);
            }

            rs.close();
            pstmt.close();

            if (!holdAvatarList.isEmpty()) {
                returnFirstAvatar = holdAvatarList.get(0);
            }
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnFirstAvatar;
    }

    public static void updateExperience(Avatar avatar) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `avatar` SET `experience` = ? WHERE `avatar_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, avatar.getExperience());
            pstmt.setInt(2, avatar.getID());
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updateCurrency(Avatar avatar) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `avatar` SET `currency` = ? WHERE `avatar_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, avatar.getCurrency());
            pstmt.setInt(2, avatar.getID());
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updateLevel(Avatar avatar) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `avatar` SET `level` = ? WHERE `avatar_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, avatar.getLevel());
            pstmt.setInt(2, avatar.getID());
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updateLastPlayed(int avatar_id, String last_played) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `avatar` SET `last_played` = ? WHERE `avatar_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, avatar_id);
            pstmt.setString(2, last_played);
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
}
