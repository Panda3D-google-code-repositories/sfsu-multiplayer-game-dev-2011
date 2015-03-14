package dataAccessLayer;

import core.GameServer;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import model.AnimalType;
import model.PlantType;

/**
 *
 * @author Gary
 */
public final class ShopDAO {

    private ShopDAO() {
    }

    public static List<AnimalType> getAnimalsByLevel(int level) throws SQLException {
        List<AnimalType> shopList = new ArrayList<AnimalType>();

        String query = "SELECT * FROM `shop` WHERE `type` = 0 AND `level` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, level);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String[] tempList = rs.getString("items").split(",");

                for (String item_id : tempList) {
                    shopList.add(GameServer.getInstance().getAnimalType(Integer.parseInt(item_id)));
                }
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return shopList;
    }

    public static List<AnimalType> getAnimalsUpToLevel(int level) throws SQLException {
        return getAnimalsUpToLevel(level, "");
    }

    public static List<AnimalType> getAnimalsUpToLevel(int level, String type) throws SQLException {
        List<AnimalType> shopList = new ArrayList<AnimalType>();

        String query = "SELECT * FROM `shop` WHERE `type` = 0 AND `level` <= ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, level);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String[] tempList = rs.getString("items").split(",");

                for (String item_id : tempList) {
                    AnimalType animal = GameServer.getInstance().getAnimalType(Integer.parseInt(item_id));

                    if (type.isEmpty() || animal.getDescription().equalsIgnoreCase(type)) {
                        shopList.add(animal);
                    }
                }
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return shopList;
    }
    
    public static List<PlantType> getPlantsByLevel(int level) throws SQLException {
        List<PlantType> shopList = new ArrayList<PlantType>();

        String query = "SELECT * FROM `shop` WHERE `type` = 1 AND `level` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, level);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String[] tempList = rs.getString("items").split(",");

                for (String item_id : tempList) {
                    shopList.add(GameServer.getInstance().getPlantType(Integer.parseInt(item_id)));
                }
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return shopList;
    }

    public static List<PlantType> getPlantsUpToLevel(int level) throws SQLException {
        List<PlantType> shopList = new ArrayList<PlantType>();

        String query = "SELECT * FROM `shop` WHERE `type` = 1 AND `level` <= ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, level);
            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                String[] tempList = rs.getString("items").split(",");

                for (String item_id : tempList) {
                    shopList.add(GameServer.getInstance().getPlantType(Integer.parseInt(item_id)));
                }
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return shopList;
    }
}
