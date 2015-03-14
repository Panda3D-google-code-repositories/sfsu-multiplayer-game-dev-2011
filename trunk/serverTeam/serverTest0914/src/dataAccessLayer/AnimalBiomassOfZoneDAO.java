package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import model.AnimalBiomassOfZone;
import model.AnimalType;

import worldManager.gameEngine.Zone;

/**
 *
 * @author Partap Aujla
 */
public final class AnimalBiomassOfZoneDAO {

    private AnimalBiomassOfZoneDAO() {
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param zonePID which is intType.
     * @return Returns a list of AnimalBiomassOfZoneType by matching zonePID in
     * the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<AnimalBiomassOfZone> getByZonePID(int zonePID) throws SQLException {
        List<AnimalBiomassOfZone> returnAnimalBiomassOfZoneList = null;

        if (zonePID <= 0) {
            System.out.println("In AnimalBiomassOfZoneDAO.java -- zonePID value is: " + zonePID);
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnAnimalBiomassOfZoneList = new ArrayList<AnimalBiomassOfZone>();

            String query = "SELECT * FROM animal_biomass_of_zone WHERE bio_zone_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, zonePID);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    AnimalBiomassOfZone holdAnimalBiomassOfZone = new AnimalBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdAnimalBiomassOfZone.setAnimalTypeID(rs.getInt("animal_type_id"));
                    holdAnimalBiomassOfZone.setNumber(rs.getInt("number"));
                    holdAnimalBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnAnimalBiomassOfZoneList.add(holdAnimalBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(AnimalBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnAnimalBiomassOfZoneList;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param zone which is ZoneType. Extracts zonePidPk.
     * @return Returns a list of AnimalBiomassOfZoneType by matching zonePidPk,
     * extracted from zone, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<AnimalBiomassOfZone> getByZonePID(Zone zone) throws SQLException {
        List<AnimalBiomassOfZone> returnAnimalBiomassOfZoneList = null;

        if (zone == null || zone.getID() <= 0) {
            System.out.println("In AnimalBiomassOfZoneDAO.java -- zone is null or zonePidPk <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnAnimalBiomassOfZoneList = new ArrayList<AnimalBiomassOfZone>();

            String query = "SELECT * FROM animal_biomass_of_zone WHERE bio_zone_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, zone.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    AnimalBiomassOfZone holdAnimalBiomassOfZone = new AnimalBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdAnimalBiomassOfZone.setAnimalTypeID(rs.getInt("animal_type_id"));
                    holdAnimalBiomassOfZone.setNumber(rs.getInt("number"));
                    holdAnimalBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnAnimalBiomassOfZoneList.add(holdAnimalBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(AnimalBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnAnimalBiomassOfZoneList;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param animalTypeID which is intType.
     * @return Returns a list of AnimalBiomassOfZoneType by matching animalTypeID
     * in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<AnimalBiomassOfZone> getByAnimalTypeID(int animalTypeID) throws SQLException {
        List<AnimalBiomassOfZone> returnAnimalBiomassOfZoneList = null;

        if (animalTypeID <= 0) {
            System.out.println("In AnimalBiomassOfZoneDAO.java -- animalTypeID value is: " + animalTypeID);
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnAnimalBiomassOfZoneList = new ArrayList<AnimalBiomassOfZone>();

            String query = "SELECT * FROM animal_biomass_of_zone WHERE animal_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, animalTypeID);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    AnimalBiomassOfZone holdAnimalBiomassOfZone = new AnimalBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdAnimalBiomassOfZone.setAnimalTypeID(rs.getInt("animal_type_id"));
                    holdAnimalBiomassOfZone.setNumber(rs.getInt("number"));
                    holdAnimalBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnAnimalBiomassOfZoneList.add(holdAnimalBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(AnimalBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnAnimalBiomassOfZoneList;
    }

    /**
     * Function checks if passed argument is valid.  If not prints out
     * an appropriate message and returns null.
     * @param animalType which is AnimalTypeType. Extracts animal_type_id_pk.
     * @return Returns a list of AnimalBiomassOfZoneType by matching animal_type_id_pk,
     * extracted from animalType, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<AnimalBiomassOfZone> getByAnimalTypeID(AnimalType animalType) throws SQLException {
        List<AnimalBiomassOfZone> returnAnimalBiomassOfZoneList = null;

        if (animalType == null || animalType.getID() <= 0) {
            System.out.println("In AnimalBiomassOfZoneDAO.java -- animalType is null or animal_type_id_pk <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnAnimalBiomassOfZoneList = new ArrayList<AnimalBiomassOfZone>();

            String query = "SELECT * FROM animal_biomass_of_zone WHERE animal_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, animalType.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    AnimalBiomassOfZone holdAnimalBiomassOfZone = new AnimalBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdAnimalBiomassOfZone.setAnimalTypeID(rs.getInt("animal_type_id"));
                    holdAnimalBiomassOfZone.setNumber(rs.getInt("number"));
                    holdAnimalBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnAnimalBiomassOfZoneList.add(holdAnimalBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(AnimalBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnAnimalBiomassOfZoneList;
    }

    /**
     * Function checks if passed arguments are valid.  If not prints out
     * an appropriate message and returns null.
     * @param zonePID which is intType.
     * @param animalTypeID which is intType.
     * @return Returns a list of AnimalBiomassOfZoneType by matching both,
     * zonePID and animalTypeID, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<AnimalBiomassOfZone> getByZonePIDandAnimalTypeID(int zonePID, int animalTypeID) throws SQLException {
        List<AnimalBiomassOfZone> returnAnimalBiomassOfZoneList = null;

        if (animalTypeID <= 0 || zonePID <= 0) {
            System.out.println("In AnimalBiomassOfZoneDAO.java -- animalTypeID <= 0 or zonePID <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnAnimalBiomassOfZoneList = new ArrayList<AnimalBiomassOfZone>();
            String query = "SELECT * FROM animal_biomass_of_zone WHERE bio_zone_id = ? and animal_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, zonePID);
                pstmt.setInt(2, animalTypeID);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    AnimalBiomassOfZone holdAnimalBiomassOfZone = new AnimalBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdAnimalBiomassOfZone.setAnimalTypeID(rs.getInt("animal_type_id"));
                    holdAnimalBiomassOfZone.setNumber(rs.getInt("number"));
                    holdAnimalBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnAnimalBiomassOfZoneList.add(holdAnimalBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(AnimalBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnAnimalBiomassOfZoneList;
    }

    /**
     * Function checks if passed arguments are valid.  If not prints out
     * an appropriate message and returns null.
     * @param zone which is ZoneType. Extracts zonePidPk.
     * @param animalType which is AnimalTypeType. Extracts animal_type_id_pk.
     * @return Returns a list of AnimalBiomassOfZoneType by matching both
     * zonePidPk and animal_type_id_pk, extracted from zone and animalType
     * respectively, in the database.  If none found returns null.
     * @throws SQLException
     */
    public static List<AnimalBiomassOfZone> getByZonePIDandAnimalTypeID(Zone zone, AnimalType animalType) throws SQLException {
        List<AnimalBiomassOfZone> returnAnimalBiomassOfZoneList = null;

        if (zone == null || animalType == null || zone.getID() <= 0 || animalType.getID() <= 0) {
            System.out.println("In AnimalBiomassOfZoneDAO.java -- zone == null or animalType == null"
                    + " or zonePidPk <= 0 or animal_type_id_pk <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnAnimalBiomassOfZoneList = new ArrayList<AnimalBiomassOfZone>();

            String query = "SELECT * FROM animal_biomass_of_zone WHERE bio_zone_id = ? and animal_type_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, zone.getID());
                pstmt.setInt(2, animalType.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    AnimalBiomassOfZone holdAnimalBiomassOfZone = new AnimalBiomassOfZone(rs.getInt("bio_zone_id"));
                    holdAnimalBiomassOfZone.setAnimalTypeID(rs.getInt("animal_type_id"));
                    holdAnimalBiomassOfZone.setNumber(rs.getInt("number"));
                    holdAnimalBiomassOfZone.setBiomass(rs.getFloat("biomass"));
                    returnAnimalBiomassOfZoneList.add(holdAnimalBiomassOfZone);
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(AnimalBiomassOfZoneDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnAnimalBiomassOfZoneList;
    }
}