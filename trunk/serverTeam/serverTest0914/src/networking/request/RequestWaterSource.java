package networking.request;

import dataAccessLayer.WaterSourceDAO;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

import model.Environment;

import networking.response.ResponseWaterSource;

import utility.DataReader;

import worldManager.gameEngine.WaterSource;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Xuyuan
 */
public class RequestWaterSource extends GameRequest {

    // Data
    private List<WaterSource> waters;
    // Responses
    private ResponseWaterSource responseWaterSource;

    public RequestWaterSource() {
        waters = new ArrayList<WaterSource>();
        responses.add(responseWaterSource = new ResponseWaterSource());
    }

    @Override
    public void parse() throws IOException {
        System.out.println("At the start of parse of RequestWaterSource..");
        for (int i = 0; i < 6; i++) {
            int x;
            int y;
            int z;
            short zoneID;

            x = DataReader.readInt(dataInput);
            y = DataReader.readInt(dataInput);
            z = DataReader.readInt(dataInput);
            zoneID = DataReader.readShort(dataInput);

            System.out.println("zoneid:" + zoneID);
            System.out.println("x:" + x);
            System.out.println("y:" + y);
            System.out.println("z:" + z);


            WaterSource ws = new WaterSource(-1);
            ws.setPos(x, y, z);
            ws.setZoneID(zoneID);
            waters.add(ws);
        }

        System.out.println("*rts*******");
        for (WaterSource ws : waters) {
            ws.toString();
        }
        System.out.println("*******RequestWawterSource---Parse Ends*******");
    }

    @Override
    public void doBusiness() throws Exception {
        System.out.println("At the beggining of doBusiness()");
        System.out.println("Username is:" + client.getPlayer().getUsername());

        if (client.getWorld() != null) {
            Environment currentEnv1 = client.getWorld().getEnvByUserID(client.getPlayer().getID());
            System.out.println("currentEnv1 is:");
            currentEnv1.toString();
        } else {
            System.out.println("client.getWorld() is null");
        }

        //Get the environment of this client.
        Environment currentEnv = client.getWorld().getEnvByUserID(client.getPlayer().getID());
        if (currentEnv != null) {
            System.out.println("Envrionment is not null");
            responseWaterSource.setStatus((short) 0);
            responseWaterSource.setWorld(client.getWorld());

            for (WaterSource ws : waters) {
                try {
                    WaterSourceDAO.createWaterSource(ws);
                } catch (SQLException ex) {
                    Logger.getLogger(RequestWaterSource.class.getName()).log(Level.SEVERE, null, ex);
                }

                //Get this WaterSource from database just for its id.
                try {
                    List<WaterSource> sameWSList = WaterSourceDAO.getByZoneID(ws.getZoneID());
                    if (sameWSList != null) {
                        WaterSource sameWS = sameWSList.get(0);//Each zone only has one water source.
                        if (sameWS != null) {
                            Zone zone = currentEnv.getZoneByID(sameWS.getZoneID());
                            if (zone != null) {
//                                zone.getWaters().add(sameWS);
                            }
                        }
                    }
                } catch (SQLException ex) {
                }
            }
        } else {
            System.out.println("The environment is null");
            responseWaterSource.setStatus((short) 1);
        }
    }
}
