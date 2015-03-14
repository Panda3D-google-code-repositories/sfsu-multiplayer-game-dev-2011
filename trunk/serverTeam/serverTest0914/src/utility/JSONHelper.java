package utility;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.lang.reflect.Type;
import java.util.Map;
import org.json.simple.JSONValue;
/**
 *
 * @author Xuyuan
 */
public class JSONHelper {
    public static String MapToJSON(Map map){
        String JSONString=JSONValue.toJSONString(map);
        return JSONString;
    }

    public static Map JSONTOMap(String JSONString){
        Gson gson=new Gson();
        Type type=new TypeToken<Map<Integer, Integer>>(){}.getType();
        Map<Integer, Integer> map=gson.fromJson(JSONString, type);
        return map;
    }
}
