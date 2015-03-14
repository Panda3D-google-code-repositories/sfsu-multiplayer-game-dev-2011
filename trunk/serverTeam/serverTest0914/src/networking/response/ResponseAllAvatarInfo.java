package networking.response;

import metadata.Constants;

/**
 *
 * @author Xuyuan
 */
public class ResponseAllAvatarInfo extends GameResponse {

    public ResponseAllAvatarInfo() {
        responseCode = Constants.SMSG_ALL_AVATAR_INFO;
    }

    @Override
    public byte[] constructResponseInBytes() {
        throw new UnsupportedOperationException("Not supported yet.");
    }
}
