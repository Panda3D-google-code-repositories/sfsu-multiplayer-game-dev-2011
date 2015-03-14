package networking.request;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import networking.response.GameResponse;

/**
 * This class is an abstract class. Each request class needs to extend this class to implement the necessary functions.
 *
 * @author , Xuyuan
 */
public abstract class GameRequest {
    protected DataInputStream dataInput;//Input stream which contains request values.

    /*
     * Set the inputStream.
     */
    public void setDataInputStream(DataInputStream dataInput){
        this.dataInput=dataInput;
    }

    /*
     * Parse the request from the inputStream.
     */
    public abstract void parse() throws IOException;

    /*
     * Do real business and at the same time create the response object.
     */
    public abstract void doBusiness();

    /*
     * Get the response object.
     */
    public abstract GameResponse getResponse();
    
}
