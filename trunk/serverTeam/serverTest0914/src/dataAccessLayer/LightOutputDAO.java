package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import model.LightOutput;

/**
 *
 * @author Partap Aujla
 */
/**
 * This class is used to implement the Comparator.  We use this to sort an
 * List of LightOutput objects according to the day Index in each object.
 * 
 */
class dayIndexLightComparator implements Comparator<LightOutput> {

    /**
     * 
     * @param firstObj
     * @param secondObj
     * @return 
     */
    @Override
    public int compare(LightOutput firstObj, LightOutput secondObj) {
        return firstObj.getDayIndex().compareTo(secondObj.getDayIndex());
    }
}

public final class LightOutputDAO {

    private LightOutputDAO() {
    }

    /**
     * 
     * @param world_id which is intType.
     * @return A sorted list of LightOutput.  The List is sorted according to 
     * the day_index.  We match world_id in the database if no match found
     * returns null.
     * @throws SQLException 
     */
    public static List<LightOutput> getByWorldID(int world_id) throws SQLException {
        List<LightOutput> returnSortedLightOutputList = null;

        String query = "SELECT * FROM light_output WHERE world_id = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, world_id);
            ResultSet rs = pstmt.executeQuery();

            returnSortedLightOutputList = new ArrayList<LightOutput>();

            while (rs.next()) {
                LightOutput tempLightOutput = new LightOutput();
                tempLightOutput.setWorldID(rs.getInt("world_id"));
                tempLightOutput.setDayIndex(rs.getInt("day_index"));
                tempLightOutput.setOutput(rs.getFloat("output"));
                returnSortedLightOutputList.add(tempLightOutput);
            }

            rs.close();
            pstmt.close();

            Collections.sort(returnSortedLightOutputList, new dayIndexLightComparator());
        } catch (SQLException ex) {
            Logger.getLogger(LightOutputDAO.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnSortedLightOutputList;
    }
}