package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

import model.PvEWorldMap;
import model.PvPWorldMap;
import model.World;

/**
 *
 * @author Partap Aujla
 */
public final class WorldMapDAO {

    private WorldMapDAO() {
    }

    /**
     * The function saves the passed map to the database. However,
     * tableId(in map) does not get stored  because this field is
     * automatically generated in database.  Note since this function is for
     * PvPWorldMap the square_size is empty and therefore by default set to 0.
     * Function checks if passed argument is valid.  If not prints out an
     * appropriate message.
     * @param map which is PvPWorldMapType. Extracts worldIDFk, team0Map, and
     * team1Map.
     * @throws SQLException
     */
    public static void savePvPWorldMap(PvPWorldMap map) throws SQLException {
        if (map == null || map.getWorldID() <= 0) {
            System.out.println("In WorldMapDAO.java -- map is null or worldIDFk <= 0");
            System.out.println("Expected value > 0");
        } else {
            String query = "INSERT INTO world_map(world_id, team0_map, team1_map, square_size) VALUES(?, ?, ?, ?)";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, map.getWorldID());
                pstmt.setString(2, map.getTeam0Map());
                pstmt.setString(3, map.getTeam1Map());
                pstmt.setInt(4, 0);
                pstmt.execute();
                pstmt.close();
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }
    }

    /**
     * Note since this function is for PvPWorldMap the square_size is empty and
     * therefore not retrieved. Function checks if passed argument is valid.
     * If not prints out an appropriate message.
     * @param worldId which is intType.
     * @return Returns a PvPWorldMapType from database by matching worldIDFk
     * If none found returns null.
     * @throws SQLException
     */
    public static PvPWorldMap getPvPWorldMapByWorldID(int worldId) throws SQLException {
        PvPWorldMap returnPvPWorldMap = null;

        if (worldId <= 0) {
            System.out.println("In WorldMapDAO.java -- worldId, passed argument, value is: " + worldId);
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            String query = "SELECT * FROM world_map WHERE world_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, worldId);
                ResultSet rs = pstmt.executeQuery();

                if (rs.next()) {
                    returnPvPWorldMap = new PvPWorldMap();
                    returnPvPWorldMap.setTableID(rs.getInt("table_id"));
                    returnPvPWorldMap.setWorldID(rs.getInt("world_id"));
                    returnPvPWorldMap.setTeam0Map(rs.getString("team0_map"));
                    returnPvPWorldMap.setTeam1Map(rs.getString("team1_map"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(WorldMapDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPvPWorldMap;
    }

    /**
     * Note since this function is for PvPWorldMap the square_size is empty and
     * therefore not retrieved. Function checks if passed argument is valid.
     * If not prints out an appropriate message.
     * @param map which is PvPWorldMapType. Extracts worldIDFk.
     * @return Returns a PvPWorldMapType from database by matching worldIDFk
     * which is extracted from passed map. If none found returns null.
     * @throws SQLException
     */
    public static PvPWorldMap getPvPWorldMapByWorldID(PvPWorldMap map) throws SQLException {
        PvPWorldMap returnPvPWorldMap = null;

        if (map == null || map.getWorldID() <= 0) {
            System.out.println("In WorldMapDAO.java -- map is null or worldIDFk <= 0");
            System.out.println("Expected value > 0\nReturning null");
        } else {
            String query = "SELECT * FROM world_map WHERE world_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, map.getWorldID());
                ResultSet rs = pstmt.executeQuery();

                if (rs.next()) {
                    returnPvPWorldMap = new PvPWorldMap();
                    returnPvPWorldMap.setTableID(rs.getInt("table_id"));
                    returnPvPWorldMap.setWorldID(rs.getInt("world_id"));
                    returnPvPWorldMap.setTeam0Map(rs.getString("team0_map"));
                    returnPvPWorldMap.setTeam1Map(rs.getString("team1_map"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(WorldMapDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPvPWorldMap;
    }

    /**
     * Note since this function is for PvPWorldMap the square_size is empty and
     * therefore not retrieved. Function checks if passed argument is valid.
     * If not prints out an appropriate message.
     * @param world which is WorldType. Extracts worldIdPk.
     * @return Returns a PvPWorldMapType from database by matching worldIDFk
     * which is extracted from passed worldIdPk. If none found returns null.
     * @throws SQLException
     */
    public static PvPWorldMap getPvPWorldMapByWorldID(World world) throws SQLException {
        PvPWorldMap returnPvPWorldMap = null;

        if (world == null || world.getID() <= 0) {
            System.out.println("In WorldMapDAO.java -- world is null or worldIdPk <= 0");
            System.out.println("Expected value > 0\nReturning null");
        } else {
            String query = "SELECT * FROM world_map WHERE world_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, world.getID());
                ResultSet rs = pstmt.executeQuery();

                if (rs.next()) {
                    returnPvPWorldMap = new PvPWorldMap();
                    returnPvPWorldMap.setTableID(rs.getInt("table_id"));
                    returnPvPWorldMap.setWorldID(rs.getInt("world_id"));
                    returnPvPWorldMap.setTeam0Map(rs.getString("team0_map"));
                    returnPvPWorldMap.setTeam1Map(rs.getString("team1_map"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(WorldMapDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPvPWorldMap;
    }

    /**
     * The function updates PvPWorldMap.  First from the passed map worldIDFk
     * is extracted and used to check if the PvPWorldMap exists in the database.
     * If it does not exist then prints the appropriate message.  If the
     * PvPWorldMap does exist in the database then tableId is retrieved and
     * stored.  Then the retrieved tableId is used to update the
     * PvPWorldMap with data from passed map.  The information updated is
     * team0Map and team1Map. PvPWorldMap do not have square size and therefore
     * it's set to 0. Function checks if passed argument is valid.  If not
     * prints out an appropriate message.
     * @param map which is PvPworldMapType. Extracts worldIDFk.
     * @throws SQLException
     */
    public static void updatePvPWorldMap(PvPWorldMap map) throws SQLException {
        if (map == null || map.getWorldID() <= 0) {
            System.out.println("In WorldMapDAO.java -- map is null or worldIDFk <= 0");
            System.out.println("Expected value > 0");
        } else {
            PvPWorldMap checkPvPWorldMap = getPvPWorldMapByWorldID(map);

            if (checkPvPWorldMap == null || checkPvPWorldMap.getTableID() == 0) {
                System.out.println("PvPWorldMap does not exist in the database.");
            } else {
                String query = "UPDATE world_map SET world_id = ?, team0_map = ?, team1_map = ?, square_size = ? WHERE table_id = ?";

                Connection connection = null;
                PreparedStatement pstmt = null;

                try {
                    connection = DAO.getDataSource().getConnection();
                    pstmt = connection.prepareStatement(query);
                    pstmt.setInt(1, map.getWorldID());
                    pstmt.setString(2, map.getTeam0Map());
                    pstmt.setString(3, map.getTeam1Map());
                    pstmt.setInt(4, 0);
                    pstmt.setInt(5, checkPvPWorldMap.getTableID());
                    pstmt.execute();
                    pstmt.close();
                } finally {
                    if (connection != null) {
                        connection.close();
                    }
                }
            }
        }
    }

    /**
     * The function saves the passed map to the database. However,
     * tableId(in map) does not get stored  because this field is
     * automatically generated in database.  Note since this function is for
     * PvEWorldMap the team1map is empty and therefore by default set to N/A.
     * Function checks if passed argument is valid.  If not prints out an
     * appropriate message.
     * @param map which is PvPWorldMapType. Extracts worldIDFk, team0Map, and
     * squareSize.
     * @throws SQLException
     */
    public static void savePvEWorldMap(PvEWorldMap map) throws SQLException {
        if (map == null || map.getWorldID() <= 0) {
            System.out.println("In WorldMapDAO.java -- map is null or worldIDFk <= 0");
            System.out.println("Expected value > 0");
        } else {
            String query = "INSERT INTO world_map(world_id, team0_map, team1_map, square_size) VALUES(?, ?, ?, ?)";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, map.getWorldID());
                pstmt.setString(2, map.getTeam0Map());
                pstmt.setString(3, "N/A");
                pstmt.setInt(4, map.getSquareSize());
                pstmt.execute();
                pstmt.close();
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }
    }

    /**
     * Note since this function is for PvEWorldMap team1Map is empty and
     * therefore not retrieved. Function checks if passed argument is valid.
     * If not prints out an appropriate message.
     * @param worldId which is intType.
     * @return Returns a PvEWorldMapType from database by matching worldIDFk
     * If none found returns null.
     * @throws SQLException
     */
    public static PvEWorldMap getPvEWorldMapByWorldID(int worldId) throws SQLException {
        PvEWorldMap returnPvEWorldMap = null;

        if (worldId <= 0) {
            System.out.println("In WorldMapDAO.java -- worldId, passed argument, value is: " + worldId);
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            String query = "SELECT * FROM world_map WHERE world_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, worldId);
                ResultSet rs = pstmt.executeQuery();

                if (rs.next()) {
                    returnPvEWorldMap = new PvEWorldMap(rs.getInt("world_id"));
                    returnPvEWorldMap.setTableId(rs.getInt("table_id"));
                    returnPvEWorldMap.setTeam0Map(rs.getString("team0_map"));
                    returnPvEWorldMap.setSquareSize(rs.getInt("square_size"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(WorldMapDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPvEWorldMap;
    }

    /**
     * Note since this function is for PvEWorldMap team1Map is empty and
     * therefore not retrieved. Function checks if passed argument is valid.
     * If not prints out an appropriate message.
     * @param map which is PvEWorldMapType. Extracts worldIDFk.
     * @return Returns a PvEWorldMapType from database by matching worldIDFk,
     * which is extracted from passed map. If none found returns null.
     * @throws SQLException
     */
    public static PvEWorldMap getPvEWorldMapByWorldID(PvEWorldMap map) throws SQLException {
        PvEWorldMap returnPvEWorldMap = null;

        if (map == null || map.getWorldID() <= 0) {
            System.out.println("In WorldMapDAO.java -- map is null or worldIDFk <= 0");
            System.out.println("Expected value > 0\nReturning null");
        } else {
            String query = "SELECT * FROM world_map WHERE world_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, map.getWorldID());
                ResultSet rs = pstmt.executeQuery();

                if (rs.next()) {
                    returnPvEWorldMap = new PvEWorldMap(rs.getInt("world_id"));
                    returnPvEWorldMap.setTableId(rs.getInt("table_id"));
                    returnPvEWorldMap.setTeam0Map(rs.getString("team0_map"));
                    returnPvEWorldMap.setSquareSize(rs.getInt("square_size"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(WorldMapDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPvEWorldMap;
    }

    /**
     * Note since this function is for PvEWorldMap team1Map is empty and
     * therefore not retrieved. Function checks if passed argument is valid.
     * If not prints out an appropriate message.
     * @param world which is WorldType. Extracts worldIdPk.
     * @return Returns a PvEWorldMapType from database by matching worldIdPk,
     * which is extracted from passed world. If none found returns null.
     * @throws SQLException
     */
    public static PvEWorldMap getPvEWorldMapByWorldID(World world) throws SQLException {
        PvEWorldMap returnPvEWorldMap = null;

        if (world == null || world.getID() <= 0) {
            System.out.println("In WorldMapDAO.java -- world is null or worldIdPk <= 0");
            System.out.println("Expected value > 0\nReturning null");
        } else {
            String query = "SELECT * FROM world_map WHERE world_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, world.getID());
                ResultSet rs = pstmt.executeQuery();

                if (rs.next()) {
                    returnPvEWorldMap = new PvEWorldMap(rs.getInt("world_id"));
                    returnPvEWorldMap.setTableId(rs.getInt("table_id"));
                    returnPvEWorldMap.setTeam0Map(rs.getString("team0_map"));
                    returnPvEWorldMap.setSquareSize(rs.getInt("square_size"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(WorldMapDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPvEWorldMap;
    }

    /**
     * The function updates PvEWorldMap.  First from the passed map worldIDFk
     * is extracted and used to check if the PvEWorldMap exists in the database.
     * If it does not exist then prints the appropriate message.  If the
     * PvEWorldMap does exist in the database then tableId is retrieved and
     * stored.  Then the retrieved tableId is used to update the
     * PvEWorldMap with data from the passed map.  The information updated is
     * team0Map and team1Map. PvEWorldMap do not have team1Map and therefore
     * it's set to N/A. Function checks if passed argument is valid.  If not
     * prints out an appropriate message.
     * @param map which is PvEworldMapType. Extracts worldIDFk.
     * @throws SQLException
     */
    public static void updatePvEWorldMap(PvEWorldMap map) throws SQLException {
        if (map == null || map.getWorldID() <= 0) {
            System.out.println("In WorldMapDAO.java -- map is null or worldIDFk <= 0");
            System.out.println("Expected value > 0");
        } else {
            PvEWorldMap checkPvEWorldMap = getPvEWorldMapByWorldID(map.getWorldID());
            if (checkPvEWorldMap == null || checkPvEWorldMap.getTableId() == 0) {
                System.out.println("PvEWorldMap does not exist in the database.");
            } else {
                String query = "UPDATE world_map SET world_id = ?, team0_map = ?, team1_map = ?, square_size = ? WHERE table_id = ?";

                Connection connection = null;
                PreparedStatement pstmt = null;

                try {
                    connection = DAO.getDataSource().getConnection();
                    pstmt = connection.prepareStatement(query);
                    pstmt.setInt(1, map.getWorldID());
                    pstmt.setString(2, map.getTeam0Map());
                    pstmt.setString(3, "N/A");
                    pstmt.setInt(4, map.getSquareSize());
                    pstmt.setInt(5, checkPvEWorldMap.getTableId());
                    pstmt.execute();
                    pstmt.close();
                } finally {
                    if (connection != null) {
                        connection.close();
                    }
                }
            }
        }
    }
}
