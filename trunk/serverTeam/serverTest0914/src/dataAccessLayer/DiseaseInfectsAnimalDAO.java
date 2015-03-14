package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import worldManager.gameEngine.Disease;

/**
 *
 * @author Partap Aujla
 */
public final class DiseaseInfectsAnimalDAO {

    private DiseaseInfectsAnimalDAO() {
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message and returns null.
     * @param disease_id which is intType.  ID of the disease.
     * @return Returns a list of Animal IDs the passed disease, disease_id,
     * can infect.  If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getAnimalIDByDiseaseID(int disease_id) throws SQLException {
        List<Integer> returnAnimalIdsList = null;

        if (disease_id <= 0) {
            System.out.println("In DiseaseInfectsAnimalDAO.java -- disease_id, passed argument, value is: " + disease_id);
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnAnimalIdsList = new ArrayList<Integer>();

            String query = "SELECT * FROM disease_infects_animal WHERE disease_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, disease_id);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    returnAnimalIdsList.add(rs.getInt("animal_type_id"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(DiseaseInfectsAnimalDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnAnimalIdsList;
    }

    /**
     * Function checks if the passed argument is valid.  If not prints an
     * appropriate message and returns null.
     * @param disease which is DiseaseType.  Extracts disease_id_pk.
     * @return Returns a list of Animal IDs the passed disease can infect.
     * If none found returns null.
     * @throws SQLException
     */
    public static List<Integer> getAnimalIDByDiseaseID(Disease disease) throws SQLException {
        List<Integer> returnAnimalIdsList = null;

        if (disease == null || disease.getID() <= 0) {
            System.out.println("In DiseaseInfectsAnimalDAO.java -- disease is null or disease_id_pk <= 0");
            System.out.println("Expected value > 0\nReturning null.");
        } else {
            returnAnimalIdsList = new ArrayList<Integer>();

            String query = "SELECT * FROM disease_infects_animal WHERE disease_id = ?";

            Connection connection = null;
            PreparedStatement pstmt = null;

            try {
                connection = DAO.getDataSource().getConnection();
                pstmt = connection.prepareStatement(query);
                pstmt.setInt(1, disease.getID());
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()) {
                    returnAnimalIdsList.add(rs.getInt("animal_type_id"));
                }

                rs.close();
                pstmt.close();
            } catch (SQLException ex) {
                Logger.getLogger(DiseaseInfectsAnimalDAO.class.getName()).log(Level.SEVERE, null, ex);
            } finally {
                if (connection != null) {
                    connection.close();
                }
            }
        }

        return returnAnimalIdsList;
    }
}
