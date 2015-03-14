package dataAccessLayer;

import javax.sql.DataSource;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;

/**
 *
 * @author Partap Aujla
 */
public final class DAO {

    private GameDB gameDB;
    private DataSource datasource;
    private static DAO dao;

    private DAO() {
        System.out.println("\n----------INITIATING DB CONNECTION-----------\n");
        XmlBeanFactory beanFactory = new XmlBeanFactory(new ClassPathResource("dataAccessLayer/SpringForDB.xml"));
        gameDB = (GameDB) beanFactory.getBean("gameDB");
        datasource = gameDB.getDataSource();
        System.out.println("\n----------SUCCESSFULLY FINISHED SETTING UP DB CONNECTION-----------\n");
    }

    public static DAO getInstance() {
        if (dao == null) {
            dao = new DAO();
        }
        return dao;
    }

    public static DataSource getDataSource() {
        return dao.datasource;
    }
}