package networking.request;

import java.io.IOException;

import model.World;
import networking.response.ResponseStartToReadyWorld;
import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestStartToReadyWorld extends GameRequest {

    // Data
    private String worldName;
    // Responses
    private ResponseStartToReadyWorld responseStartToReadyWorld;

    public RequestStartToReadyWorld() {
        responses.add(responseStartToReadyWorld = new ResponseStartToReadyWorld());
    }

    @Override
    public void parse() throws IOException {
        worldName = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        World currentWorld = client.getServer().getOnlineActiveWorld(worldName);

        if (currentWorld != null) {
            responseStartToReadyWorld.setStatus((short) 0);
            client.getServer().addResponseToOtherPeopleInTheSameWorld(client.getId(), currentWorld.getID(), responseStartToReadyWorld);

        } else {
            responseStartToReadyWorld.setStatus((short) 1);
            System.out.println("The world does not exist");
        }

    }
}
