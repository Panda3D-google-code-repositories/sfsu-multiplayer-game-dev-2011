package metadata;

import java.util.HashMap;
import networking.request.GameRequest;

/**
 * This class holds the request code number and the corresponding request class.
 *
 * @author 
 */
public class GameRequestTable {
    private static HashMap<Short, Class> requestNames;

    /*
     * Initicate the request table.
     */
    public static void init(){
        requestNames=new HashMap<Short, Class>();

        try{
            add(Constances.CMSG_REGISTER,"RequestRegist");
            
        }catch(ClassNotFoundException e){
            System.out.println(e.getMessage());
        }
    }

    /*
     * Add a piece of record to the rueqest table.
     */
    public static void add(short code, String name) throws ClassNotFoundException{
        requestNames.put(code, Class.forName("networking.request."+name));
    }

    /*
     * Get the request class by the given request code.
     */
    public static GameRequest get(short requestID){
        GameRequest request=null;

        try{
            Class name=requestNames.get(requestID);
            

            if(name!=null){
                request=(GameRequest)name.newInstance();
                
            }else{
                System.out.println("Invalid Request Code: "+requestID);
            }
        }catch(Exception e){
            System.out.println(e.getMessage());
        }

        return request;
    }
}
