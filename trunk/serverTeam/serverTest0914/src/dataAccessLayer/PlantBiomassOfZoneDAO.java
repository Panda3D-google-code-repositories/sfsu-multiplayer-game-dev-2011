package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import model.PlantBiomassOfZone;
import model.PlantType;

import worldManager.gameEngine.Zone;

/**
 *
 * @author Partap Aujla
 */
public final class PlantBiomassOfZoneDAO {

    private PlantBiomassOfZoneDAO() {
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param zonePID which is intType.
     * @return Returns a list of PlantBiomassOfZoneType by matching zonePID in
     * the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<PlantBiomassOfZone> getByZonePID(int zonePID) throws SQLException {
        List<PlantBiomassOfZone> returnPlantBiomassOfZoneList = null;

        if (zonePID <= 0) {
            System.out.println("In PlantBiomassOfZoneDAO.java -- zonePID value is: " + zonePID);
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPlantBiomassOfZoneList = new ArrayList<PlantBiomassOfZone>();

            String query = "SELECT * FROM plant_biomass_of_zone WHERE bio_zone_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, zonePID);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    PlantBiomassOfZone holdPlantBiomassOfZone = new PlantBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdPlantBiomassOfZone.setPlantTypeID(rs.getInt("plant_type_id"));
                    holdPlantBiomassOfZone.setNumber(rs.getInt("number"));
                    holdPlantBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnPlantBiomassOfZoneList.add(holdPlantBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(PlantBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPlantBiomassOfZoneList;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param zone which is ZoneType. Extracts zonePidPk.
     * @return Returns a list of PlantBiomassOfZoneType by matching zonePidPk,
     * extracted from zone, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<PlantBiomassOfZone> getByZonePID(Zone zone) throws SQLException {
        List<PlantBiomassOfZone> returnPlantBiomassOfZoneList = null;

        if (zone == null || zone.getID() <= 0) {
            System.out.println("In PlantBiomassOfZoneDAO.java -- zone is null or zonePidPk <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPlantBiomassOfZoneList = new ArrayList<PlantBiomassOfZone>();

            String query = "SELECT * FROM plant_biomass_of_zone WHERE bio_zone_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, zone.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    PlantBiomassOfZone holdPlantBiomassOfZone = new PlantBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdPlantBiomassOfZone.setPlantTypeID(rs.getInt("plant_type_id"));
                    holdPlantBiomassOfZone.setNumber(rs.getInt("number"));
                    holdPlantBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnPlantBiomassOfZoneList.add(holdPlantBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(PlantBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPlantBiomassOfZoneList;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param plantTypeID which is intType.
     * @return Returns a list of PlantBiomassOfZoneType by matching plantTypeID
     * in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<PlantBiomassOfZone> getByPlantTypeID(int plantTypeID) throws SQLException {
        List<PlantBiomassOfZone> returnPlantBiomassOfZoneList = null;

        if (plantTypeID <= 0) {
            System.out.println("In PlantBiomassOfZoneDAO.java -- plantTypeID value is: " + plantTypeID);
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPlantBiomassOfZoneList = new ArrayList<PlantBiomassOfZone>();

            String query = "SELECT * FROM plant_biomass_of_zone WHERE plant_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, plantTypeID);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    PlantBiomassOfZone holdPlantBiomassOfZone = new PlantBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdPlantBiomassOfZone.setPlantTypeID(rs.getInt("plant_type_id"));
                    holdPlantBiomassOfZone.setNumber(rs.getInt("number"));
                    holdPlantBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnPlantBiomassOfZoneList.add(holdPlantBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(PlantBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPlantBiomassOfZoneList;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param plantType which is PlantTypeType. Extracts plant_type_id_pk.
     * @return Returns a list of PlantBiomassOfZoneType by matching plant_type_id_pk,
     * extracted from plantType, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<PlantBiomassOfZone> getByPlantTypeID(PlantType plantType) throws SQLException {
        List<PlantBiomassOfZone> returnPlantBiomassOfZoneList = null;

        if (plantType == null || plantType.getID() <= 0) {
            System.out.println("In PlantBiomassOfZoneDAO.java -- plantType is null or plant_type_id_pk <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPlantBiomassOfZoneList = new ArrayList<PlantBiomassOfZone>();

            String query = "SELECT * FROM plant_biomass_of_zone WHERE plant_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, plantType.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    PlantBiomassOfZone holdPlantBiomassOfZone = new PlantBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdPlantBiomassOfZone.setPlantTypeID(rs.getInt("plant_type_id"));
                    holdPlantBiomassOfZone.setNumber(rs.getInt("number"));
                    holdPlantBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnPlantBiomassOfZoneList.add(holdPlantBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(PlantBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPlantBiomassOfZoneList;
    }

    /**
     * Function checks if passed arguments are valid.  If not prints out
     * an appropriate message and returns null.
     * @param zonePID which is intType.
     * @param plantTypeID which is intType.
     * @return Returns a list of PlantBiomassOfZoneType by matching both,
     * zonePID and plantTypeID, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<PlantBiomassOfZone> getByZonePIDandPlantTypeID(int zonePID, int plantTypeID) throws SQLException {
        List<PlantBiomassOfZone> returnPlantBiomassOfZoneList = null;

        if (plantTypeID <= 0 || zonePID <= 0) {
            System.out.println("In PlantBiomassOfZoneDAO.java -- plantTypeID <= 0 or zonePID <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPlantBiomassOfZoneList = new ArrayList<PlantBiomassOfZone>();

            String query = "SELECT * FROM plant_biomass_of_zone WHERE bio_zone_id = ? and plant_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, zonePID);
                pstmt.setInt(2, plantTypeID);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    PlantBiomassOfZone holdPlantBiomassOfZone = new PlantBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdPlantBiomassOfZone.setPlantTypeID(rs.getInt("plant_type_id"));
                    holdPlantBiomassOfZone.setNumber(rs.getInt("number"));
                    holdPlantBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnPlantBiomassOfZoneList.add(holdPlantBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(PlantBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPlantBiomassOfZoneList;
    }

    /**
     * Function checks if passed arguments are valid.  If not prints out
     * an appropriate message and returns null.
     * @param zone which is ZoneType. Extracts zonePidPk.
     * @param plantType which is PlantType. Extracts plant_type_id_pk.
     * @return Returns a list of PlantBiomassOfZoneType by matching both
     * zonePidPk and plant_type_id_pk, extracted from zone and plantType
     * respectively, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<PlantBiomassOfZone> getByZonePIDandPlantTypeID(Zone zone, PlantType plantType) throws SQLException {
        List<PlantBiomassOfZone> returnPlantBiomassOfZoneList = null;

        if (zone == null || plantType == null || zone.getID() <= 0 || plantType.getID() <= 0) {
            System.out.println("In PlantBiomassOfZoneDAO.java -- zone == null or plantType == null"
                    + " or zonePidPk <= 0 or plant_type_id_pk <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnPlantBiomassOfZoneList = new ArrayList<PlantBiomassOfZone>();

            String query = "SELECT * FROM plant_biomass_of_zone WHERE bio_zone_id = ? and plant_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, zone.getID());
                pstmt.setInt(2, plantType.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    PlantBiomassOfZone holdPlantBiomassOfZone = new PlantBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdPlantBiomassOfZone.setPlantTypeID(rs.getInt("plant_type_id"));
                    holdPlantBiomassOfZone.setNumber(rs.getInt("number"));
                    holdPlantBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnPlantBiomassOfZoneList.add(holdPlantBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(PlantBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnPlantBiomassOfZoneList;
    }
}