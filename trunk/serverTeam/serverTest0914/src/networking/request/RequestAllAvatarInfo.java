package networking.request;

import java.io.IOException;

import networking.response.ResponseAllAvatarInfo;
import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestAllAvatarInfo extends GameRequest {

    // Data
    private String worldName;
    // Responses
    private ResponseAllAvatarInfo responseAllAvatarInfo;

    public RequestAllAvatarInfo() {
        responses.add(responseAllAvatarInfo = new ResponseAllAvatarInfo());
    }

    @Override
    public void parse() throws IOException {
        worldName = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
    }
}
