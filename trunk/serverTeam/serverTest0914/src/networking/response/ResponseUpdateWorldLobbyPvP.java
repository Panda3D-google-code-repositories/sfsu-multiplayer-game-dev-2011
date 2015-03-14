package networking.response;

import model.World;

/**
 *  (This class is not in use.)
 * @author Xuyuan
 */
public class ResponseUpdateWorldLobbyPvP extends GameResponse {

    private World pvpWorld;

    public ResponseUpdateWorldLobbyPvP() {
    }

    @Override
    public byte[] constructResponseInBytes() {
        throw new UnsupportedOperationException("Not supported yet.");
    }
}
