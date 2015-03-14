package networking.request;

import java.io.IOException;

import metadata.Constants;

import model.World;

import networking.response.ResponseReady;
import networking.response.ResponseStartWorld;
import networking.response.ResponseUpdateTime;

import utility.DataReader;

import worldManager.gameEngine.Zone;

/**
 *
 * @author Xuyuan
 */
public class RequestReady extends GameRequest {

    // Data
    private boolean status;
    // Responses
    private ResponseReady responseReady;
    private ResponseStartWorld responseStartWorld;
    private ResponseUpdateTime responseUpdateTime;

    public RequestReady() {
        responses.add(responseReady = new ResponseReady());
    }

    @Override
    public void parse() throws IOException {
        status = true;
    }

    @Override
    public void doBusiness() throws Exception {
        World world = client.getWorld();

        if (world != null) {
            world.setReady(client.getPlayer().getID(), status);

            responseReady.setStatus(status);
            responseReady.setUsername(client.getPlayer().getUsername());
//            client.getServer().addResponseToOtherPeopleInTheSameWorld(client.getId(), world.getID(), responseReady);

            if (world.isReady()) {
                for (Zone zone : world.getGameEngine().getZoneList()) {
                    if (zone.isEnable()) {
                        zone.startTimeActiveTimer();
                    }
                }

                responses.add(responseStartWorld = new ResponseStartWorld());

                responseStartWorld.setStatus(true);

                responses.add(responseUpdateTime = new ResponseUpdateTime());

                responseUpdateTime.setMonth(world.getMonth());
                responseUpdateTime.setYear(world.getYear());
                responseUpdateTime.setDuration(Constants.MONTH_DURATION);
                responseUpdateTime.setCurrent((int) world.getSeconds());
                responseUpdateTime.setRate(world.getGameEngine().getGameScale());
            }
        }
    }
}
