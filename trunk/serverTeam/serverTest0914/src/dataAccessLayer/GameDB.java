package dataAccessLayer;

import java.sql.SQLException;
import javax.sql.DataSource;
import configuration.DBConf;
import utility.ConfFileParser;

public class GameDB {

    private DBConf configuration;
    private DataSource dataSource;

    public GameDB() throws SQLException, ClassNotFoundException, InstantiationException, IllegalAccessException {
        configure();
        String connectURI = "jdbc:mysql://" + configuration.getDBURL() + "/" + configuration.getDBName() + "?" + "user=" + configuration.getDBUsername() + "&password=" + configuration.getDBPassword();
//        System.out.println(connectURI); //FOR DEBUG PURPOSES.
        dataSource = ConnectionPool.setupDataSource(connectURI);
    }

    private void configure() {
        configuration = new DBConf();
        ConfFileParser confFileParser = new ConfFileParser("conf/db.conf");
        configuration.setConfRecords(confFileParser.parse());
    }

    public DataSource getDataSource() {
        return dataSource;
    }
}