package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import core.GameServer;
public final class PreyPredatorRatioDAO {

	private PreyPredatorRatioDAO(){
		
	}
	
    public static int insertParams(int playerId, int zoneID, int parameterType,int predatorID,int preyID,float percentValue) throws SQLException {
        int animalStatId = -1;
        //INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`)
        //VALUES (1,2,3,4,5,80)
        // ON DUPLICATE KEY UPDATE `percent_manipulated`= 80

        String query = "INSERT INTO `predator_prey_ratio` (`player_id`, `zone_id`, `parameter_type`, `predator_id`,`prey_id`, `percent_manipulated`) VALUES (?, ?, ?, ?, ?, ?) ON DUPLICATE KEY UPDATE `percent_manipulated`=?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setInt(1, playerId);
            pstmt.setInt(2, zoneID);
            pstmt.setInt(3, parameterType);
            pstmt.setInt(4, predatorID);
            pstmt.setInt(5, preyID);
            pstmt.setFloat(6, percentValue);
            pstmt.setFloat(7, percentValue);
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
            	animalStatId = rs.getInt(1);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return animalStatId;
    }
    
    public static HashMap<String,Float> getFunctionalParams(int playerId, int predatorId, int parameterType)throws SQLException {
    	//SELECT prey_id,percent_manipulated FROM `predator_prey_ratio` WHERE player_id = 2 and predator_id = 2 and parameter_type =3
    	HashMap<String,Float> hashmap = new HashMap<String,Float>();
    	
    	String query = "SELECT prey_id,percent_manipulated FROM `predator_prey_ratio` WHERE player_id = ? and predator_id = ? and parameter_type =?";
        Connection connection = null;
        PreparedStatement pstmt = null;
        int preyId;
        float percentValue;
        String preyName;
        
        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setInt(1, playerId);
            pstmt.setInt(2, predatorId); 
            pstmt.setInt(3, parameterType);
            ResultSet rs = pstmt.executeQuery();

            while(rs.next()) {
            	preyId = rs.getInt("prey_id");
            	percentValue = rs.getFloat("percent_manipulated");
            	
            	preyName = GameServer.getAnimalName(preyId);
            	if(preyName == null){
            		preyName = GameServer.getPlantName(preyId);
            		if(preyName == null){
            			return null;
            		}
            	}
            	System.out.println(preyName + " " + percentValue);
            	hashmap.put(preyName, percentValue);
            }

            rs.close();
            pstmt.close();
        } catch (SQLException ex) {
            Logger.getLogger(PreyPredatorRatioDAO.class.getName()).log(Level.SEVERE, null, ex);
        }finally {
            if (connection != null) {
                connection.close();
            }
        }
    	
    	return hashmap;
    }

	public static void createParameters(int creatorID, int zone_id) {
		//System.out.println("Creating Parameters in the PreyPredatorRatio Table");
	}

}

