package networking.response;

import java.lang.reflect.Field;

/**
 * This class is an abstract class. Each response class needs to extend this class to implement the necessary functions.
 *
 * @author , Xuyuan
 */
public abstract class GameResponse {

    protected byte[] responseInBytes;//This is constructed from the respone object.
    protected short responseCode;
    /*
     * Construct the reponse object to bytes.
     */

    public abstract byte[] constructResponseInBytes();

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