package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import model.RainOutput;

/**
 *
 * @author Partap Aujla
 */
/**
 * This class is used to implement the Comparator.  We use this to sort an
 * List of RainOutput objects according to the day Index in each object.
 * 
 */
class dayIndexRainComparator implements Comparator<RainOutput> {

    /**
     * 
     * @param firstObj
     * @param secondObj
     * @return 
     */
    @Override
    public int compare(RainOutput firstObj, RainOutput secondObj) {
        return firstObj.getDayIndex().compareTo(secondObj.getDayIndex());
    }
}

public final class RainOutputDAO {

    private RainOutputDAO() {
    }

    /**
     * 
     * @param world_id which is intType.
     * @return A sorted list of RainOutput.  The List is sorted according to 
     * the day_index.  We match world_id in the database if no match found
     * returns null.
     * @throws SQLException 
     */
    public static List<RainOutput> getByWorldID(int world_id) throws SQLException {
        List<RainOutput> returnSortedRainOutputList = new ArrayList<RainOutput>();

        String query = "SELECT * FROM `rain_output` WHERE `world_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, world_id);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                RainOutput tempRainOutput = new RainOutput();
                tempRainOutput.setWorldID(rs.getInt("world_id"));
                tempRainOutput.setDayIndex(rs.getInt("day_index"));
                tempRainOutput.setOutput(rs.getFloat("output"));
                returnSortedRainOutputList.add(tempRainOutput);
            }

            rs.close();
            pstmt.close();

            Collections.sort(returnSortedRainOutputList, new dayIndexRainComparator());
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnSortedRainOutputList;
    }
}
