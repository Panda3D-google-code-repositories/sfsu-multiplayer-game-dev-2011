package dataAccessLayer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import core.GameServer;

import model.Avatar;
import model.Stat;

public final class PlantStatDAO {

	private PlantStatDAO(){
		
	}
	
    public static int insertPlantStat(int plantInstanceID,int plantTypeID,int currentDay,String activity,int envScore,String message,int playerID, int zoneID) throws SQLException {
        int plantStatId = -1;
        //Insert into plant_stat(`plant_instance_id`, `plant_type_id`, `activity_day`, `activity_type`,`env_score`) values ( 1 , 10, 1, 'birth',10000)
        String query = "INSERT INTO `plant_stat` (`plant_instance_id`, `plant_type_id`, `activity_day`, `activity_type`,`env_score`,`activity_message`,`player_id`,`zone_id`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setInt(1, plantInstanceID);
            pstmt.setInt(2, plantTypeID);
            pstmt.setInt(3, currentDay);
            pstmt.setString(4, activity);
            pstmt.setInt(5, envScore);
            pstmt.setString(6, message);
            pstmt.setInt(7, playerID);
            pstmt.setInt(8, zoneID);
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
            	plantStatId = rs.getInt(1);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return plantStatId;
    }

    public static List<Stat> getPlantStats(int activityStartDay, int activityEndDay,int playerId, int zone_id) throws SQLException{
    	 
    	List<Stat> statsList = new ArrayList<Stat>();

        //String query = "select activity_day,`animal_type_id`, activity_type, count(*), env_score, activity_message from animal_stat where ((activity_day >= ? && activity_day<=?)&& player_id=? ) group by `animal_type_id`,`activity_type` order by activity_day,activity_type";

    	//String query = "select activity_day,`animal_type_id`, activity_type, env_score, activity_message from animal_stat where ((activity_day >= ? && activity_day<=?)&& player_id=? ) group by `animal_type_id`,`activity_type` order by activity_day,activity_type";
    	
    	//String query = "SELECT activity_day,plant_type_id, activity_type, env_score, activity_message FROM  `plant_stat` WHERE ((activity_day >= ? && activity_day <= ? ) && player_id = ? )ORDER BY activity_day";
    	
    	String query = "SELECT  `activity_day` ,  `plant_type_id` ,  `activity_type` , COUNT( * ) AS plant_count FROM plant_stat WHERE player_id = ? AND zone_id = ? AND (`activity_day` BETWEEN ? AND ?) GROUP BY  `activity_day` ,  `plant_type_id` ,  `activity_type`";
        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, playerId);
            pstmt.setInt(2, zone_id);
            pstmt.setInt(3, activityStartDay);
            pstmt.setInt(4, activityEndDay);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
            	Stat stats = new Stat();
            	stats.setActivityDay(rs.getInt("activity_day"));
            	int plantTypeID = rs.getInt("plant_type_id");
            	stats.setPlantTypeId(plantTypeID);
            	stats.setActivityType(rs.getString("activity_type"));
            	stats.setCount(rs.getInt("plant_count"));
            	//stats.setEnvironmentScore(rs.getInt("env_score"));
            	//stats.setActivityMessage(rs.getString("activity_message"));
           	
            	String plantName= GameServer.getPlantName(plantTypeID);
            	stats.setPlantName(plantName);
            	statsList.add(stats);
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return statsList;
    }

}
