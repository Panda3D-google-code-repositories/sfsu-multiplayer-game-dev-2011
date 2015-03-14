package networking.request;

import core.GameClient;
import core.GameServer;

import dataAccessLayer.AvatarDAO;
import dataAccessLayer.EnvironmentDAO;
import dataAccessLayer.PlayerDAO;
import dataAccessLayer.WorldDAO;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import metadata.Constants;

import model.Avatar;
import model.Environment;
import model.Player;
import model.World;

import networking.response.ResponseLogin;

import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestLogin extends GameRequest {

    // Data
    private String version;
    private String user_id;
    private String password;
    // Responses
    private ResponseLogin responseLogin;

    public RequestLogin() {
        responses.add(responseLogin = new ResponseLogin());
    }

    @Override
    public void parse() throws IOException {
        version = DataReader.readString(dataInput).trim();
        user_id = DataReader.readString(dataInput).trim();
        password = DataReader.readString(dataInput).trim();
    }

    @Override
    public void doBusiness() throws Exception {
        System.out.println("User '" + user_id + "' is connecting...");

        Player player = null;

        if (version.compareTo(Constants.CLIENT_VERSION) >= 0) {
            if (!user_id.isEmpty() && password.matches("[a-fA-F0-9]{32}")) {
                player = PlayerDAO.getAccount(user_id, password);
            }

            if (player == null) {
                responseLogin.setStatus((short) 1);//Username/password is wrong.
                System.out.println("User '" + user_id + "' has failed to log in.");
            } else {
                if (client.getPlayer() == null || player.getID() != client.getPlayer().getID()) {
                    GameClient thread = client.getServer().getThreadByPlayerID(player.getID());

                    if (thread != null) {
                        responseLogin.setStatus((short) 2);//Account is being used.
                        thread.stopClient();
                    } else {
                        PlayerDAO.updateLogin(player.getID(), client.getIP());
                        GameServer.getInstance().setActivePlayer(player);
                        player.setClient(client);
                        player.setLastSaved(System.currentTimeMillis());
                        player.startSaveTimer();
                        //Put the current user in its thread.
                        //Add the thread to active threads.
                        client.setPlayer(player);
                        client.getServer().addToActiveThreads(client);
                        //Set response information.
                        responseLogin.setStatus((short) 0);//Login succeeds!
                        responseLogin.setPlayer(player);

                        List<Avatar> avatarList = AvatarDAO.getAvatars(client.getPlayer().getID());
                        responseLogin.setAvatarList(avatarList);
                        
                        List<World> worldList = WorldDAO.getPlayerWorlds(client.getPlayer().getID());
                        List<Integer> scoreList = new ArrayList<Integer>();

                        for (World world : worldList) {
                            List<Environment> envList = EnvironmentDAO.getEnvironmentByWorldID(world.getID());

                            if (!envList.isEmpty()) {
                                for (Environment env : envList) {
                                    scoreList.add(env.getEnvironmentScore());
                                }
                            } else {
                                scoreList.add(0);
                            }
                        }

                        responseLogin.setWorldList(worldList, scoreList);

                        //Set the player's current position 0(0 means in the main lobby.)
                        client.getServer().trackPlayerPosition(player.getID(), Constants.LOCATION_MAIN_LOBBY);

                        System.out.println("User '" + player.getUsername() + "' has successfully logged in.");
                    }
                } else {
                    responseLogin.setStatus((short) 4);
                }
            }
        } else {
            responseLogin.setStatus((short) 3);
        }
    }
}
