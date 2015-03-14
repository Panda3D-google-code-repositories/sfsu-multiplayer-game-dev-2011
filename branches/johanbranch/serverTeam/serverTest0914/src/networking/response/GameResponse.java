package networking.response;

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

    /*
     * Print the response. It is for our testing.
     */
    public abstract void printResponse();
}
