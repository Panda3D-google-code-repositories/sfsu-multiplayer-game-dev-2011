package gameDB;

import java.sql.SQLException;
import javax.sql.DataSource;
import configuration.DBConf;
import utility.ConfFileParser;

/**
 *
 * @author , Xuyuan
 */

public class GameDB {
    private DBConf configuration;
    private DataSource dataSource;

    public GameDB() throws SQLException, ClassNotFoundException, InstantiationException, IllegalAccessException{    
        this.configure();
        String connectURI="jdbc:mysql://"+this.configuration.getDBURL()+"/"+this.configuration.getDBName()+"?"+"user="+this.configuration.getDBUsername()+"&password="+this.configuration.getDBPassword();
        System.out.println(connectURI);
        this.dataSource=ConnectionPool.setupDataSource(connectURI);
    }

    private void configure(){
        this.configuration=new DBConf();
        ConfFileParser confFileParser=new ConfFileParser("conf/db.conf");
        this.configuration.setConfRecords(confFileParser.parse());
    }

    public DataSource getDataSource(){
        return this.dataSource;
    }

}
