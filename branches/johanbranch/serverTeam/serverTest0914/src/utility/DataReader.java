package utility;

import java.io.DataInputStream;
import java.io.IOException;
/**
 * This class facilitates reading data from data streams.
 *
 * @author 
 */

public class DataReader {
    /*
     * Read one short from the DataInputStream. Used for Python client pydatagram decoding.
     */
    public static short readShort(DataInputStream in) throws IOException{
        if(in.available()>0){
            return Short.reverseBytes(in.readShort());
        }

        return -1;
    }

    /*
     * Read one int from the DataInputStream. Used fro Python client pydatagram decoding. 
     */
    public static int readInt(DataInputStream in) throws IOException{
       if(in.available()>0){
           return Integer.reverseBytes(in.readInt());
       }

       return -1;
    }

    /*
     * Read one boolean from the DataInputStream.
     */
    public static boolean readBoolean(DataInputStream in) throws IOException{
        if(in.available()>0){
            return in.readBoolean();
        }

        return false;
    }

    /*
     * Read a string from the DataInputStream. 
     */
    public static String readString(DataInputStream in) throws IOException{
        short length=readShort(in);
        byte[] aString=new byte[length];
        in.read(aString, 0, length);
        return (new String(aString));
    }

   
}
