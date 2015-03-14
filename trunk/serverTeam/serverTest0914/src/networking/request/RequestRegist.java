package networking.request;

import dataAccessLayer.AvatarDAO;
import dataAccessLayer.PlayerDAO;

import java.io.IOException;

import metadata.Constants;

import model.Avatar;

import networking.response.ResponseRegist;

import utility.DataReader;

/**
 * This class extends the GameRequest class. It is responsible for handle the regist request.
 * 
 * @author , Xuyuan
 */
public class RequestRegist extends GameRequest {

    // Data
    private String username;
    private String email;
    private String password;
    private String first_name;
    private String last_name;
    // Responses
    private ResponseRegist responseRegist;

    /*
     * Initicate the the RequestRegist.
     */
    public RequestRegist() {
        responses.add(responseRegist = new ResponseRegist());
    }

    /*
     * Parse the request.
     */
    @Override
    public void parse() throws IOException {
        username = DataReader.readString(dataInput).trim();
        email = DataReader.readString(dataInput).trim();
        password = DataReader.readString(dataInput).trim();
//        first_name = DataReader.readString(dataInput).trim();
//        last_name = DataReader.readString(dataInput).trim();
        first_name = "???";
        last_name = "???";
    }

    /*
     * Use user manager to regist this user.
     */
    @Override
    public void doBusiness() throws Exception {
        if (!username.isEmpty() && !email.isEmpty() && email.split("@").length == 2 && password.matches("[a-fA-F0-9]{32}")) {
            if (PlayerDAO.containsEmail(email)) {
                responseRegist.setStatus((short) 1);
            } else if (PlayerDAO.containsUsername(username)) {
                responseRegist.setStatus((short) 2);
            } else {
                int player_id = PlayerDAO.createAccount(email, password, username, first_name, last_name, client.getIP());
                
                Avatar avatar = new Avatar(-1);
                avatar.setAvatarType(1);
                avatar.setCurrency(Constants.INITIAL_GOLD);
                avatar.setPlayerID(player_id);
                AvatarDAO.createAvatar(avatar);
                responseRegist.setStatus((short) 0);
            }
        }
    }
}
