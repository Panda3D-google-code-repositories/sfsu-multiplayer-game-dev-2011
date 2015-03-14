package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import model.Environment;

import worldManager.gameEngine.Zone;

/**
 *
 * @author Partap Aujla
 */
public final class EnvironmentDAO {

    private EnvironmentDAO() {
    }

    /**
     * The function saves the passed environment to the database. However,
     * envIdPk(in environment) does not get stored  because this field is
     * automatically generated in database. Function checks if the passed
     * argument is valid.  If not prints an appropriate message.
     * @param environment which is EnvironmentType. Extracts inWorldIDFk,
     * envRow, and envColumn.
     * @throws SQLException
     */
    public static int createEnvironment(Environment environment) throws SQLException {
        int env_id = -1;

        String query = "INSERT INTO `environment` (`world_id`, `player_id`, `row`, `column`) VALUES (?, ?, ?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setInt(1, environment.getWorldID());
            pstmt.setInt(2, environment.getOwnerID());
            pstmt.setInt(3, environment.getRow());
            pstmt.setInt(4, environment.getColumn());
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
                env_id = rs.getInt(1);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return env_id;
    }

    public static Environment getEnvironment(int player_id, int world_id) throws SQLException {
        Environment environment = null;

        String query = "SELECT * FROM `environment` WHERE `world_id` = ? AND `player_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, world_id);
            pstmt.setInt(2, player_id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                environment = new Environment(rs.getInt("env_id"));
                environment.setWorldID(rs.getInt("world_id"));
                environment.setOwnerID(rs.getInt("player_id"));
                environment.setRow(rs.getInt("row"));
                environment.setColumn(rs.getInt("column"));
                environment.setEnvironmentScore(rs.getInt("score"));
                environment.setHighEnvScore(rs.getInt("high_score"));
                environment.setAccumulatedEnvScore(rs.getInt("accumulated_score"));

                List<Zone> zoneList = ZoneDAO.getZoneByEnvironmentID(environment.getID());

                for (Zone zone : zoneList) {
                    zone.setEnvironment(environment);
                }

                environment.setZones(zoneList);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return environment;
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message and returns null.
     * @param environment which is EnvironmentType. Extracts inWorldIDFk, 
     * envRow, and envColumn. 
     * @return Returns EnvironmentType which contains Avatar belonging to the
     * environment and List of zones belonging to the environment.  The returned
     * Environment is retrieved by matching all three inWorldIDFk, envRow, and
     * envColumn in the database.  If no Environment is found the returns null.
     * @throws SQLException
     */
    public static Environment getEnvironmentByWorldIDAndRowAndCol(Environment environment) throws SQLException {
        Environment returnEnvironment = null;

        String query = "SELECT * FROM `environment` WHERE `world_id` = ? AND `row` = ? AND `column` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, environment.getWorldID());
            pstmt.setInt(2, environment.getRow());
            pstmt.setInt(3, environment.getColumn());
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                returnEnvironment = new Environment(rs.getInt("env_id"));
                returnEnvironment.setWorldID(rs.getInt("world_id"));
                returnEnvironment.setOwnerID(rs.getInt("player_id"));
                returnEnvironment.setRow(rs.getInt("row"));
                returnEnvironment.setColumn(rs.getInt("column"));
                returnEnvironment.setEnvironmentScore(rs.getInt("score"));
                returnEnvironment.setHighEnvScore(rs.getInt("high_score"));
                returnEnvironment.setAccumulatedEnvScore(rs.getInt("accumulated_score"));
            }

            rs.close();
            pstmt.close();

            List<Zone> zoneList = ZoneDAO.getZoneByEnvironmentID(returnEnvironment.getID());

            for (Zone zone : zoneList) {
                zone.setEnvironment(returnEnvironment);
            }

            returnEnvironment.setZones(zoneList);
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnEnvironment;
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message and returns null.
     * @param world_id which is intType.
     * @return Returns a list of environments in the world with worldIdPk by
     * matching the worldIdPk in database.  Note each EnvironmentType contains
     * AvatarType belonging to that Environment as well as list of ZoneType
     * belonging to that Environment.  If no environment is found returns null.
     * @throws SQLException
     */
    public static List<Environment> getEnvironmentByWorldID(int world_id) throws SQLException {
        List<Environment> returnEnvironmentList = new ArrayList<Environment>();

        String query = "SELECT * FROM `environment` WHERE `world_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, world_id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                Environment env = new Environment(rs.getInt("env_id"));
                env.setWorldID(rs.getInt("world_id"));
                env.setOwnerID(rs.getInt("player_id"));
                env.setRow(rs.getInt("row"));
                env.setColumn(rs.getInt("column"));
                env.setEnvironmentScore(rs.getInt("score"));
                env.setHighEnvScore(rs.getInt("high_score"));
                env.setAccumulatedEnvScore(rs.getInt("accumulated_score"));

                returnEnvironmentList.add(env);
            }

            rs.close();
            pstmt.close();

            for (Environment env : returnEnvironmentList) {
                List<Zone> zoneList = ZoneDAO.getZoneByEnvironmentID(env.getID());
                
                for (Zone zone : zoneList) {
                    zone.setEnvironment(env);
                }
                
                env.setZones(zoneList);
            }
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnEnvironmentList;
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message and returns null.  Note this function does not
     * return the zones in the environment.  (Might need to be implemented. 
     * Check other implementations on how to accomplish )
     * @param envID
     * @return Returns the Environment which matches the passed argument in the
     * database.  If none found returns null.
     * @throws SQLException
     */
    public static Environment getEnvironmentByEnvID(int envID) throws SQLException {
        Environment env = null;

        String query = "SELECT * FROM `environment` WHERE `env_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, envID);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                env = new Environment(rs.getInt("env_id"));
                env.setWorldID(rs.getInt("world_id"));
                env.setOwnerID(rs.getInt("player_id"));
                env.setRow(rs.getInt("row"));
                env.setColumn(rs.getInt("column"));
                env.setEnvironmentScore(rs.getInt("score"));
                env.setHighEnvScore(rs.getInt("high_score"));
                env.setAccumulatedEnvScore(rs.getInt("accumulated_score"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return env;
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message.  The function matches the passed argument in the
     * database and then deletes it.
     * @throws SQLException
     */
    public static void deleteEnvironmentByID(int env_id) throws SQLException {
        String query = "DELETE FROM `avatar` WHERE `env_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, env_id);
            pstmt.executeUpdate();
            pstmt.close();

            String query1 = "DELETE FROM `environment` WHERE `env_id` = ?";
            pstmt = connection.prepareStatement(query1);
            pstmt.setInt(1, env_id);
            pstmt.executeUpdate();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static List<String[]> getBestEnvScore(int min_range, int max_range) throws SQLException {
        return getBestEnvScore(min_range, max_range, new ArrayList<String>());
    }

    public static List<String[]> getBestEnvScore(int min_range, int max_range, List<String> patternList) throws SQLException {
        List<String[]> scoreList = new ArrayList<String[]>();

        String query = "SELECT * FROM `environment` e JOIN `player` p ON e.`player_id` = p.`player_id`";

        if (!patternList.isEmpty()) {
            query += " WHERE p.`username` REGEXP '";

            for (int i = 0; i < patternList.size(); i++) {
                query += patternList.get(i);

                if (i < patternList.size() - 1) {
                    query += "|";
                }
            }

            query += "'";
        }

        query += " GROUP BY e.`player_id` ORDER BY e.`high_score` DESC LIMIT ?, ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, min_range);
            pstmt.setInt(2, max_range);

            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String[] score = new String[]{rs.getString("username"), rs.getString("high_score")};
                scoreList.add(score);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return scoreList;
    }
    
    public static List<String[]> getBestTotalEnvScore(int min_range, int max_range) throws SQLException {
        return getBestTotalEnvScore(min_range, max_range, new ArrayList<String>());
    }

    public static List<String[]> getBestTotalEnvScore(int min_range, int max_range, List<String> patternList) throws SQLException {
        List<String[]> scoreList = new ArrayList<String[]>();

        String query = "SELECT * FROM `environment` e JOIN `player` p ON e.`player_id` = p.`player_id`";

        if (!patternList.isEmpty()) {
            query += " WHERE p.`username` REGEXP '";

            for (int i = 0; i < patternList.size(); i++) {
                query += patternList.get(i);

                if (i < patternList.size() - 1) {
                    query += "|";
                }
            }

            query += "'";
        }

        query += " GROUP BY e.`player_id` ORDER BY e.`accumulated_score` DESC LIMIT ?, ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, min_range);
            pstmt.setInt(2, max_range);

            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String[] score = new String[]{rs.getString("username"), rs.getString("accumulated_score")};
                scoreList.add(score);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return scoreList;
    }

    public static List<String[]> getBestCurrentEnvScore(int min_range, int max_range) throws SQLException {
        return getBestCurrentEnvScore(min_range, max_range, new ArrayList<String>());
    }

    public static List<String[]> getBestCurrentEnvScore(int min_range, int max_range, List<String> patternList) throws SQLException {
        List<String[]> scoreList = new ArrayList<String[]>();

        String query = "SELECT * FROM `environment` e JOIN `player` p ON e.`player_id` = p.`player_id`";

        if (!patternList.isEmpty()) {
            query += " WHERE p.`username` REGEXP '";

            for (int i = 0; i < patternList.size(); i++) {
                query += patternList.get(i);

                if (i < patternList.size() - 1) {
                    query += "|";
                }
            }

            query += "'";
        }

        query += " GROUP BY e.`player_id` ORDER BY e.`score` DESC LIMIT ?, ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, min_range);
            pstmt.setInt(2, max_range);

            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String[] score = new String[]{rs.getString("username"), rs.getString("score")};
                scoreList.add(score);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return scoreList;
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message.  The function extracts envIdPk, inWorldIDFk, 
     * envRow, envColumn, and envMapID.  After extracting the information the 
     * function matches the envIdPk in the database and then updates the 
     * information for that environment with data from passed argument.
     * @param env which is EnvironmentType.
     * @throws SQLException
     */
    public static void updateEnvironment(Environment env) throws SQLException {
        String query = "UPDATE `environment` SET `world_id` = ?, `row` = ?, `column` = ? WHERE `env_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, env.getWorldID());
            pstmt.setInt(2, env.getRow());
            pstmt.setInt(3, env.getColumn());
            pstmt.setInt(4, env.getID());
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updateEnvironmentScore(int env_id, int envScore, int highEnvScore) throws SQLException {
        String query = "UPDATE `environment` SET `score` = ?, `high_score` = ? WHERE `env_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, envScore);
            pstmt.setInt(2, highEnvScore);
            pstmt.setInt(3, env_id);
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }

    public static void updateAccumEnvScore(int env_id, int score) throws SQLException {
        String query = "UPDATE `environment` SET `accumulated_score` = ? WHERE `env_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, score);
            pstmt.setInt(2, env_id);
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
}
