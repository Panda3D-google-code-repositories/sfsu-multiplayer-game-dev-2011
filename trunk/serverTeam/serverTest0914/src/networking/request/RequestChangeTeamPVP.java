package networking.request;

import dataAccessLayer.AvatarDAO;
import dataAccessLayer.EnvironmentDAO;
import dataAccessLayer.WorldMapDAO;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

import model.Environment;
import model.PvPWorldMap;
import model.World;

import networking.response.ResponseChangeTeamPVP;

import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestChangeTeamPVP extends GameRequest {

    // Data
    private String worldName;
    private short teamNumber;
    // Responses
    private ResponseChangeTeamPVP responseChangeTeamPVP;

    public RequestChangeTeamPVP() {
        responses.add(responseChangeTeamPVP = new ResponseChangeTeamPVP());

    }

    @Override
    public void parse() throws IOException {
        worldName = DataReader.readString(dataInput);
        teamNumber = DataReader.readShort(dataInput);

        System.out.println("****Parse start*****");
        System.out.println("Worldname:" + worldName);
        System.out.println("TeamNumber:" + teamNumber);
        System.out.println("****Parse end*****");
    }

    @Override
    public void doBusiness() throws Exception {
        World world = client.getServer().getActivePvPWorld(worldName);

        if (world != null) {
            for (Environment env : world.getEnvironments()) {
                if (env.getOwnerID() == client.getPlayer().getID()) {
                    int teamNo = env.getRow();
                    int position = env.getColumn();

                    if (teamNo != teamNumber) {
                        PvPWorldMap map = client.getServer().getPvPWorldMap(world.getID());

                        //Try to join new team
                        int newPosition = map.getPositionInNewTeam(teamNumber);
                        if (newPosition >= 0) {//Change team successful!
                            //Quit old team
                            map.quitOldTeamAndPosition(teamNo, position);
                            //Update the map
                            WorldMapDAO.updatePvPWorldMap(map);

                            //Update environment.
                            int row = teamNumber;
                            int col = newPosition;
                            env.setRow(row);
                            env.setColumn(col);
                            EnvironmentDAO.updateEnvironment(env);

                            //Update avatar
                            client.getAvatar().setTeamNo(row);
                            AvatarDAO.updateAvatar(client.getAvatar());

                            responseChangeTeamPVP.setWorld(world);
                        } else {
                            System.out.println("The target team is full already.");
                        }
                    } else {
                        System.out.println("Team number is the same.");
                    }
                }
            }
        } else {
            System.out.println("World with the name does not exist");
        }

        if (responseChangeTeamPVP.getStatus() == 0) {
            client.getServer().addResponseForWorld(world.getID(), responseChangeTeamPVP);
        }
    }
}
