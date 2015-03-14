package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Gary
 */
public class ResponseChartBiomass extends GameResponse {

    private short type;
    private String csv;

    public ResponseChartBiomass() {
        responseCode = Constants.SMSG_CHART_BIOMASS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(type);
        packet.addString(csv);

        return packet.getBytes();
    }

    public void setCSV(String csv) {
        this.csv = csv;
    }

    public void setType(short type) {
        this.type = type;
    }
}
