package utility;

import java.util.ArrayList;
import java.util.List;

import metadata.Constants;

/**
 *
 * @author Gary
 */
public abstract class ExpTable {

    private static List<Integer> expTable;

    public static void init() {
        expTable = new ArrayList<Integer>(Constants.MAX_LEVEL + 1);
        expTable.add(0);

        for (int i = 1; i <= Constants.MAX_LEVEL; i++) {
            expTable.add(expTable.get(i - 1) + (int) (Constants.STARTING_NEEDED_EXP * Math.pow(1.25f, (i - 1))));
        }
    }

    public static int getExp(int level) {
        return expTable.get(level);
    }

    public static int getExpToAdvance(int level) {
        return expTable.get(level) - expTable.get(level - 1);
    }

    public static int getLevel(int experience) {
        int level = 0;

        for (int i = 0; i < expTable.size(); i++) {
            if (experience >= expTable.get(i)) {
                level++;
            }
        }

        return level;
    }
}
