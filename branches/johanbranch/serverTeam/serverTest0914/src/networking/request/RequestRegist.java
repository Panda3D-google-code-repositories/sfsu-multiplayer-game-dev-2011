package networking.request;

import java.io.IOException;
import networking.response.GameResponse;
import business.UserManager;
import model.User;
import networking.response.ResponseRegist;
import utility.DataReader;

/**
 * This class extends the GameRequest class. It is responsible for handle the regist request.
 * 
 * @author , Xuyuan
 */
public class RequestRegist extends GameRequest{
    private User newUser;
    private UserManager userMgr;//This object will handle the user business.
    private ResponseRegist response;

    /*
     * Initicate the the RequestRegist.
     */
    public RequestRegist() throws Exception{
        this.newUser=new User();
        this.response=new ResponseRegist();
        this.userMgr=new UserManager(this.response);
    }

    /*
     * Parse the request.
     */
    @Override
    public void parse() throws IOException {
        this.newUser.setUserName(DataReader.readString(dataInput));
        this.newUser.setPassword(DataReader.readString(dataInput));
        this.newUser.setConfirm(DataReader.readString(dataInput));
        this.newUser.setEmail(DataReader.readString(dataInput));
        this.newUser.setCharName(DataReader.readString(dataInput));
        System.out.println("In Request Login=====");
        System.out.println("User Name: "+this.newUser.getUserName());
        System.out.println("Password: "+this.newUser.getPassword());
        System.out.println("Confirm: "+this.newUser.getConfirm());
        System.out.println("Email: "+this.newUser.getEmail());
        System.out.println("Char Name: "+this.newUser.getCharName());
    }

    /*
     * Use user manager to regist this user.
     */
    @Override
    public void doBusiness() {
        this.userMgr.regist(this.newUser);
    }

    @Override
    public GameResponse getResponse() {
        return this.response;
    }

}
