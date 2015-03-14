package model;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import utility.JSONHelper;

/**
 *
 * @author Xuyuan
 */
public class PvPWorldMap {

    private int table_id;
    private int world_id;
    private String team0Map;
    private String team1Map;
    //For pvp world map, the [square_size] is empty.
    //The following part has nothing to do with db.
    private int teamNo;
    private int positionInTeam;
    private int worldSize;
    private Map<Integer, Integer> team0;
    private Map<Integer, Integer> team1;

    public PvPWorldMap(int world_id, int worldSize) {
        this.world_id = world_id;
        this.worldSize = worldSize;

        team0 = new HashMap<Integer, Integer>();
        team1 = new HashMap<Integer, Integer>();

        for (int i = 0; i < worldSize / 2; i++) {
            team0.put(i, 0);
            team1.put(i, 0);
        }
    }

    /**
     * Default Constructor.
     */
    public PvPWorldMap() {
    }

    public void setTableID(int table_id) {
        this.table_id = table_id;
    }

    public int getTableID() {
        return this.table_id;
    }

    public void setWorldID(int world_id) {
        this.world_id = world_id;
    }

    public int getWorldID() {
        return this.world_id;
    }

    /** fine
     * Assign a new environment a position in this world
     *
     */
    public void assignEnvironmentPosition() {
        int team0Size = getPlayerNumInTeam0();
        int team1Size = getPlayerNumInTeam1();
        if (team0Size <= team1Size) {//Put the environment in team 0
            teamNo = 0;
            positionInTeam = getAvailablePositionInTeam0();
            team0.put(positionInTeam, 1);
            team0Map = JSONHelper.MapToJSON(team0);
        } else {
            teamNo = 1;
            positionInTeam = getAvailablePositionInTeam1();
            team1.put(positionInTeam, 1);
            team1Map = JSONHelper.MapToJSON(team1);
        }
    }

    /**
     * Quit the team and position.
     *
     * @param team              Team number of the player.
     * @param position          Position of the player in that team.
     */
    public void quitOldTeamAndPosition(int team, int position) {
        if (team == 0) {
            team0.put(position, 0);
            team0Map = JSONHelper.MapToJSON(team0);
        } else if (team == 1) {
            team1.put(position, 0);
            team1Map = JSONHelper.MapToJSON(team1);
        }
    }

    /**
     * Remove the last player out of team with the number of teamNO
     *
     * @param teamNO            The target team
     * @return                  The position of the player who is removed.
     */
    public int removeLastOnePlayerFromTeamN(int teamNO) {
        Map<Integer, Integer> map = null;
        int lastPlayerPosition = -1;

        if (teamNO == 0) {
            map = team0;
        } else if (teamNO == 1) {
            map = team1;
        } else {
            System.out.println("Wrong map number---the number of the map is neither 0 nor 1.");
        }

        if (map != null) {
            Set<Integer> keySet = map.keySet();
            for (int i = 0; i < worldSize / 2; i++) {
                if (map.get(i) == 1) {
                    lastPlayerPosition = i;
                }
            }

            quitOldTeamAndPosition(teamNO, lastPlayerPosition);
        }

        return lastPlayerPosition;
    }

    /**
     * Get a position in team with the team number of teamNO
     *
     * @param teamNO            The number of the team
     * @return                  The position of in the team
     */
    public int getPositionInNewTeam(int teamNo) {
        int position = -2;
        if (teamNo == 0) {
            position = getAvailablePositionInTeam0();
            if (position != -1) {
                team0.put(position, 1);
                team0Map = JSONHelper.MapToJSON(team0);
            }
        } else if (teamNo == 1) {
            position = getAvailablePositionInTeam1();
            if (position != -1) {
                team1.put(position, 1);
                team1Map = JSONHelper.MapToJSON(team1);
            }

        } else {
            position = -1;
        }
        return position;
    }

    /** fine
     * Get the number of players in team 0
     *
     * @return              The number of players in team 0
     */
    private int getPlayerNumInTeam0() {
        int num = 0;
        Set<Integer> keySet = team0.keySet();
        for (Integer key : keySet) {
            if (team0.get(key) == 1) {
                num++;
            }
        }

        return num;
    }

    /** fine
     * Get the number of players in team 1
     *
     * @return              The number of players in team 1
     */
    private int getPlayerNumInTeam1() {
        int num = 0;
        Set<Integer> keySet = team1.keySet();
        for (Integer key : keySet) {
            if (team1.get(key) == 1) {
                num++;
            }
        }

        return num;
    }

    /** fine
     * Get the available position in team 0
     *
     * @return              The available position in team 0
     */
    private int getAvailablePositionInTeam0() {
        Set<Integer> keySet = team0.keySet();
        for (Integer key : keySet) {
            if (team0.get(key) == 0) {
                return key;
            }
        }
        return -1;
    }

    /** fine
     * Get the available position in team 1
     *
     * @return              The available position in team 1
     */
    private int getAvailablePositionInTeam1() {
        Set<Integer> keySet = team1.keySet();
        for (Integer key : keySet) {
            if (team1.get(key) == 0) {
                return key;
            }
        }
        return -1;
    }

    /** fine
     * Get the team number
     *
     * @return              The team number
     */
    public int getRow() {
        return teamNo;
    }

    /** fine
     * Get the position in team
     *
     * @return              The position in team.
     */
    public int getCol() {
        return positionInTeam;
    }

    public void printObject() {
        System.out.println("This is a PvPWorldMap object");
        System.out.println("tableId:" + table_id);
        System.out.println("worldIDFk:" + world_id);
        System.out.println("team0Map(JSON String):" + team0Map);
        System.out.println("team1Map(JSON String):" + team1Map);
        System.out.println("worldSize:" + worldSize);

        System.out.println("Team 0:");
        for (int i = 0; i < worldSize / 2; i++) {
            System.out.print(team0.get(i));
            System.out.print(" | ");
        }

        System.out.println("Team 1:");
        for (int i = 0; i < worldSize / 2; i++) {
            System.out.print(team1.get(i));
            System.out.print(" | ");
        }
    }

    public int getPositionInTeam() {
        return positionInTeam;
    }

    public void setPositionInTeam(int positionInTeam) {
        this.positionInTeam = positionInTeam;
    }

    public Map<Integer, Integer> getTeam0() {
        return team0;
    }

    public void setTeam0(Map<Integer, Integer> team0) {
        this.team0 = team0;
    }

    public String getTeam0Map() {
        return team0Map;
    }

    public void setTeam0Map(String team0Map) {
        this.team0Map = team0Map;
    }

    public Map<Integer, Integer> getTeam1() {
        return team1;
    }

    public void setTeam1(Map<Integer, Integer> team1) {
        this.team1 = team1;
    }

    public String getTeam1Map() {
        return team1Map;
    }

    public void setTeam1Map(String team1Map) {
        this.team1Map = team1Map;
    }

    public int getTeamNo() {
        return teamNo;
    }

    public void setTeamNo(int teamNo) {
        this.teamNo = teamNo;
    }
//    public void printMap() {
//        System.out.println("==============");
//        System.out.println("Team 0:");
//        System.out.println(this.team0);
//
//        System.out.println("Team 1:");
//        System.out.println(this.team1);
//    }
//    public static void main(String[] args) {
//        PvPWorldMap map = new PvPWorldMap(1, 10);
//
//        for (int i = 0; i < 10; i++) {
//            map.assignEnvironmentPosition();
//            map.printMap();
//        }
//    }
}
