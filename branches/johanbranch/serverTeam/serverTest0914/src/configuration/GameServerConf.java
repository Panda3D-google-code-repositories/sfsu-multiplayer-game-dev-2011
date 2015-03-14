package configuration;

import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author Xuyuan
 */
//Game Server Configurations. 
public class GameServerConf {
    private Map<String, String> confRecords;

    public GameServerConf(){
        this.confRecords=new HashMap<String,String>();
    }

    public void setConfRecords(Map<String, String> confRecords){
        this.confRecords=confRecords;
    }

    public int getPortNumber(){
        return Integer.valueOf(this.confRecords.get("portNumber"));
    }

}
