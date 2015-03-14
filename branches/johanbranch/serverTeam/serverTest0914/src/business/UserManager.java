package business;

import dao.UserDAO;
import java.sql.SQLException;
import networking.response.ResponseRegist;
import model.User;
/**
 * This class is responsible for user business process.
 *
 * @author , Xuyuan
 */

public class UserManager {
    private UserDAO userDAO;//User manager uses it to access user table.
    private ResponseRegist response;//The resonse is created during the business process(like this.regist(String username, String password)).

    /*
     * Initicate UserManager.
     */
    public UserManager(ResponseRegist response) throws Exception{
        this.response=response;
        this.userDAO=new UserDAO();
    }

    /*
     * Regist user and create response.
     */
    public void regist(User user){
        if(user!=null){
            //this.userDAO.saveUser(user);
            this.response.setNotification("success");
        }else{
            this.response.setNotification("Fail");
        }
    }

}
