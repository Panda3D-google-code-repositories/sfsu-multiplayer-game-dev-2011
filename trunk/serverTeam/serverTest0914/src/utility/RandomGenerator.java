package utility;

import java.util.UUID;

/**
 *
 * @author Xuyuan
 */
public class RandomGenerator {
    public static String generateRandomString32(){
        String randomString=UUID.randomUUID().toString();
        return randomString;
    }

}
