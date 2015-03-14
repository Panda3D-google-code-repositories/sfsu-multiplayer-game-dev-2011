package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;

import metadata.Constants;

/**
 *
 * @author Gary
 */
public final class ParamTableDAO {

    private ParamTableDAO() {
    }

    public static int createParameters(int zone_id) throws SQLException {
        int param_id = -1;

        String query = "INSERT INTO `param_table` (`zone_id`) VALUES (?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setInt(1, zone_id);
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
                param_id = rs.getInt(1);
            }

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return param_id;
    }

    public static HashMap<Short, Float> getByZoneID(int zone_id) throws SQLException {
        HashMap<Short, Float> parametersList = new HashMap<Short, Float>();

        String query = "SELECT * FROM `param_table` WHERE `zone_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, zone_id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                parametersList.put(Constants.PARAMETER_K, rs.getFloat("p_k"));
                parametersList.put(Constants.PARAMETER_R, rs.getFloat("p_r"));
                parametersList.put(Constants.PARAMETER_X, rs.getFloat("p_x"));
                parametersList.put(Constants.PARAMETER_X_A, rs.getFloat("a_x"));
                parametersList.put(Constants.PARAMETER_E, rs.getFloat("a_e"));
                parametersList.put(Constants.PARAMETER_A, rs.getFloat("a_a"));
                parametersList.put(Constants.PARAMETER_Q, rs.getFloat("a_q"));
                parametersList.put(Constants.PARAMETER_D, rs.getFloat("a_d"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return parametersList;
    }

    public static void updateParameters(int zone_id, HashMap<Short, Float> parametersList) throws SQLException {
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            String query = "UPDATE `param_table` SET `p_k` = ?, `p_r` = ?, `p_x` = ?, `a_x` = ?, `a_e` = ?, `a_a` = ?, `a_q` = ?, `a_d` = ? WHERE `zone_id` = ?";

            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setFloat(1, parametersList.get(Constants.PARAMETER_K));
            pstmt.setFloat(2, parametersList.get(Constants.PARAMETER_R));
            pstmt.setFloat(3, parametersList.get(Constants.PARAMETER_X));
            pstmt.setFloat(4, parametersList.get(Constants.PARAMETER_X_A));
            pstmt.setFloat(5, parametersList.get(Constants.PARAMETER_E));
            pstmt.setFloat(6, parametersList.get(Constants.PARAMETER_A));
            pstmt.setFloat(7, parametersList.get(Constants.PARAMETER_Q));
            pstmt.setFloat(8, parametersList.get(Constants.PARAMETER_D));
            pstmt.setInt(9, zone_id);
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
}