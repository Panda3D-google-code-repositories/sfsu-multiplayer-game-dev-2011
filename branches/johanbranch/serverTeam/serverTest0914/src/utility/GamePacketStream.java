package utility;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Calendar;
import java.text.SimpleDateFormat;

/**
 * 
 * @author genki, Gary. Modified by Xuyuan.
 */
public class GamePacketStream extends ByteArrayOutputStream {
    GamePacketStream(short message_id) {
        /* Reserve the first two bytes for the packet length */
        super.write(0xff);
        super.write(0xff);

        /* Set message ID */
        add(message_id);
    }

    public void add(byte[] bytes) {
        super.write(bytes, 0, bytes.length);
    }

    /**
     *  Little Endian to Big Endian Conversion for adding a short.
     */
    public void add(short short_val) {
        try {
            byte[] bytes = new byte[2];

            bytes[0] = (byte) (short_val);      // Lo
            bytes[1] = (byte) (short_val >> 8); // Hi

            super.write(bytes);
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public void add(int int_val) {
        try {
            byte[] bytes = new byte[4];

            bytes[0] = (byte) (int_val);        // Lo 0
            bytes[1] = (byte) (int_val >> 8);   // Hi 0
            bytes[2] = (byte) (int_val >> 16);  // Lo 1
            bytes[3] = (byte) (int_val >> 24);  // Hi 1

            super.write(bytes);
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
    /* End Little Endian to Big Endian Conversion */

    @Override
    public byte[] toByteArray() {
        byte[] bytes = super.toByteArray();

        // Update the length of packet size without counting these two bytes.
        bytes[0] = (byte) ((this.size() - 2) & 0xff);
        bytes[1] = (byte) ((this.size() - 2) >> 8);

        return bytes;
    }

    public static String now() {
        Calendar cal = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        return sdf.format(cal.getTime());

    }

    public byte getChecksum() {//?
        byte[] bytes = super.toByteArray();
        Integer checksum = 0, sum = 0;

        for (int i = 0; i < bytes.length; i++) {
            sum += bytes[i];
        }

        // take the least significant byte of sum, and take the two's complement
        checksum = -(sum & 0xFF);

        if (((sum + checksum) & 0xFF) == 0x00) {
            return checksum.byteValue();
        } else {
            return 0;
        }
    }

    @Override
    public String toString() {
        String str = "";

        byte[] bytes = super.toByteArray();
        int messageID = (bytes[3] << 8) | bytes[2];//?

        str = String.format("[%s] messageID: %d with %d bytes.[0x%X]\n", now(), messageID, bytes.length, getChecksum());

        return str;
    }
}
