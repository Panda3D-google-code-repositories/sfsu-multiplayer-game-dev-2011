package utility;

import java.util.Comparator;

import worldManager.gameEngine.species.Organism;

/**
 *
 * @author Gary
 */
public class OrganismComparator {

    public static Comparator<Organism> GroupSizeComparatorASC = new GroupSizeComparatorASC();
    public static Comparator<Organism> GroupSizeComparatorDESC = new GroupSizeComparatorDESC();

    private static class GroupSizeComparatorASC implements Comparator<Organism> {

        @Override
        public int compare(Organism o1, Organism o2) {
            if (o1.getGroupSize() > o2.getGroupSize()) {
                return 1;
            } else if (o1.getGroupSize() < o2.getGroupSize()) {
                return -1;
            } else {
                return 0;
            }
        }
    }

    private static class GroupSizeComparatorDESC implements Comparator<Organism> {

        @Override
        public int compare(Organism o1, Organism o2) {
            if (o1.getGroupSize() > o2.getGroupSize()) {
                return -1;
            } else if (o1.getGroupSize() < o2.getGroupSize()) {
                return 1;
            } else {
                return 0;
            }
        }
    }
}
