package networking.request;

import dataAccessLayer.WorldDAO;
import java.io.IOException;

import networking.response.ResponseDeleteWorld;
import utility.DataReader;

/**
 *
 * @author Gary
 */
public class RequestDeleteWorld extends GameRequest {

    // Data
    private int world_id;
    // Responses
    private ResponseDeleteWorld responseDeleteWorld;

    public RequestDeleteWorld() {
        responses.add(responseDeleteWorld = new ResponseDeleteWorld());
    }

    @Override
    public void parse() throws IOException {
        world_id = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        WorldDAO.removeWorld(world_id);

        responseDeleteWorld.setStatus((short) 0);
        responseDeleteWorld.setWorldID(world_id);
    }
}
