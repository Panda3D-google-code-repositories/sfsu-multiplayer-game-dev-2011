package configuration;

import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author Xuyuan
 */
//DB configrations.
public class DBConf {
    private Map<String, String> confRecords;

    public DBConf(){
        this.confRecords=new HashMap<String,String>();
    }

    public void setConfRecords(Map<String, String> confRecords){     
        this.confRecords=confRecords;     
    }

    public String getDBURL(){
        return this.confRecords.get("DBURL");
    }

    public String getDBName(){
        return this.confRecords.get("DBName");
        
    }

    public String getDBUsername(){
        return this.confRecords.get("DBUsername");
        
    }

    public String getDBPassword(){
        return this.confRecords.get("DBPassword");
        
    }
}