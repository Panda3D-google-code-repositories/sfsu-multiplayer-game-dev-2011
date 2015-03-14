package dao;

import gameDB.GameDB;
import javax.sql.DataSource;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;

/**
 * This class is the base class for all *DAO classes. It gets the gameDB bean maintained by Spring. So we don't have to pass it through layers but use it directly.
 *
 * @author , Xuyuan
 */
public class DAO {
    protected GameDB gameDB;
    protected DataSource datasource;
   
    public DAO(){
        XmlBeanFactory beanFactory = new XmlBeanFactory(new ClassPathResource("gameDB/SpringForDB.xml"));
        this.gameDB= (GameDB) beanFactory.getBean("gameDB");
        this.datasource= this.gameDB.getDataSource();
      
    }
}
