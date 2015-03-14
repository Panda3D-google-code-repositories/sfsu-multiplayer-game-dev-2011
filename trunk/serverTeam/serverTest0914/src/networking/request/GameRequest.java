package networking.request;

import core.GameClient;

import java.io.DataInputStream;
import java.io.IOException;
import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.List;

import networking.response.GameResponse;

/**
 * This class is an abstract class. Each request class needs to extend this class to implement the necessary functions.
 *
 * @author Xuyuan
 */
public abstract class GameRequest {

    protected GameClient client;
    protected DataInputStream dataInput;//Input stream which contains request values.
    protected List<GameResponse> responses;
    protected int request_id;

    public GameRequest() {
        responses = new ArrayList<GameResponse>();
    }

    public int getID() {
        return request_id;
    }

    public int setID(int request_id) {
        return this.request_id = request_id;
    }
    /*
     * Set the inputStream.
     */

    public void setDataInputStream(DataInputStream dataInput) {
        this.dataInput = dataInput;
    }

    public void setGameClient(GameClient client) {
        this.client = client;
    }

    /*
     * Parse the request from the inputStream.
     */
    public abstract void parse() throws IOException;

    /*
     * Do real business and at the same time create the response object.
     */
    public abstract void doBusiness() throws Exception;

    /*
     * Get the response object.
     */
    public List<GameResponse> getResponses() {
        return responses;
    }

    @Override
    public String toString() {
        String str = "";

        str += "-----" + "\n";
        str += getClass().getName() + "\n";
        str += "\n";

        for (Field field : getClass().getDeclaredFields()) {
            try {
                str += field.getName() + " - " + field.get(this) + "\n";
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
            }
        }

        str += "-----";

        return str;
    }
}