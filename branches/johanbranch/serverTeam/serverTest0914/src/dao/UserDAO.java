package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * UserDAO extends DAO and will control the data access to testUserInfo table.(DAO is short for Data Access Object which is responsible for table access.)
 *
 * @author , Xuyuan
 */

public class UserDAO extends DAO{
    protected Connection connection = null;
    protected PreparedStatement ps = null;
    
    public UserDAO(){
        super();
    }

//    public void saveUser(String username, String password) throws SQLException{
//        this.connection=this.datasource.getConnection();
//        String query="INSERT INTO testUserInfo (username,password) VALUES(?,?)";
//        this.ps=this.connection.prepareStatement(query);
//        this.ps.setString(1, username);
//        this.ps.setString(2, password);
//        this.ps.execute();
//        this.ps.close();
//        this.connection.close();
//    }

    

}
