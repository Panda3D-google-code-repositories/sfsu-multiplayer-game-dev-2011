package networking.response;

import metadata.Constants;
import utility.GamePacket;

/**
 *
 * @author Xuyuan
 */
public class ResponseUpdateWeatherPrediction extends GameResponse {

    private short day;
    private short lightOutput;
    private short rainOutput;

    public ResponseUpdateWeatherPrediction() {
        responseCode = Constants.SMSG_WEATHER_PREDICTION;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addShort16(day);
        packet.addShort16(lightOutput);
        packet.addShort16(rainOutput);
        return packet.getBytes();
    }

    public void setDay(short day) {
        this.day = day;
    }

    public void setLightOutput(short lightOutput) {
        this.lightOutput = lightOutput;
    }

    public void setRainOutput(short rainOutput) {
        this.rainOutput = rainOutput;
    }
}
