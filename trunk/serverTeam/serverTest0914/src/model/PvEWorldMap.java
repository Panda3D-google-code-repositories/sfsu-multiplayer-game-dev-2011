package model;

import java.util.HashMap;
import java.util.Map;

import utility.JSONHelper;

/**
 *
 * @author Xuyuan, idea from Hunvil.
 */
public class PvEWorldMap {

    private int table_id;//Primary key. -----[table_id]
    private int world_id;//Id of the pve world which the map belongs to.-----[worldID_fk]
    private String team0Map;//-----[team0_map]
    //For a pve world map, the team1Map is empty.
    private int squareSize = 0;//Squre size of the pve map. -----[square_size]
    //The following part has nothing to do with db.
    private Map<Integer, Integer> worldMap = new HashMap<Integer, Integer>();//This one is not for db.

    public PvEWorldMap(int world_id) {
        this.world_id = world_id;
        team0Map = "";
    }

    public int getTableId() {
        return table_id;
    }

    public int setTableId(int table_id) {
        return this.table_id = table_id;
    }

    public int getWorldID() {
        return world_id;
    }

    public int setWorldID(int world_id) {
        return this.world_id = world_id;
    }

    /** fine
     * Get the available position in the current square
     *
     * @return		 	the available position in the current square
     */
    private int getAvailablePosition() {
        for (Integer key : worldMap.keySet()) {
            if (worldMap.get(key) == 0) {
                worldMap.put(key, 1);
                return key;
            }
        }

        return -1;
    }

    /** fine
     * Get the assigned position of an environment in the world.
     *
     * @return		 	The assigned position of an environment
     */
    public int assignEnvironmentPosition() {
        int position = getAvailablePosition();

        if (position == -1) {//If the square is full, expand the squre.
            expandSquare();
            position = getAvailablePosition();
        }

        worldMap.put(position, 1);
        team0Map = JSONHelper.MapToJSON(worldMap);

        return position;
    }

    /**
     * Expand the square from this.squareSize to this.squareSize+1
     * 
     */
    private void expandSquare() {
        squareSize++;

        for (int i = 0; i < squareSize; i++) {
            for (int j = 0; j < squareSize; j++) {
                int mapIDForCurrentPosition = generateMapIDForEnv(i, j);

                if (!worldMap.containsKey(mapIDForCurrentPosition)) {
                    worldMap.put(mapIDForCurrentPosition, 0);
                }
            }
        }

    }

    /**
     * Generate the map id(position of the environment) from row(j) and column(i)
     * 
     * @param i         The column of the environment
     * @param j         The row of the environment
     * @return          The map id(position of the environment)
     */
    private int generateMapIDForEnv(int i, int j) {
        return (j * 10 + i + 1);
    }

    private void printMap() {
        System.out.println("--------------");
        for (int j = 0; j < this.squareSize; j++) {
            for (int i = 0; i < this.squareSize; i++) {
                System.out.print(this.worldMap.get(this.generateMapIDForEnv(i, j)));
            }
            System.out.println();
        }
    }

    /**
     * Get the row from the position.
     *
     * @param position      The position of the environment in this PvE world
     * @return              The row of the position
     */
    public int getRow(int position) {
        return (position / 10);
    }

    /**
     * Get the col from the position.
     *
     * @param position      The position of the environment in this PvE world
     * @return              The col of the position
     */
    public int getCol(int position) {
        return (position % 10 - 1);
    }

    /**
     * Quit the position on this PvE world map.
     *
     * @param position          The position of a player.
     */
    public void quitPosition(int position) {
        this.worldMap.put(position, 0);
    }

    public int getPositionBasingOnRowAndCol(int row, int col) {
        return (10 * row + col + 1);
    }

    public int getSquareSize() {
        return squareSize;
    }

    public void setSquareSize(int squareSize) {
        this.squareSize = squareSize;
    }

    public String getTeam0Map() {
        return team0Map;
    }

    public void setTeam0Map(String team0Map) {
        worldMap = JSONHelper.JSONTOMap(team0Map);
        this.team0Map = team0Map;
    }

    public Map<Integer, Integer> getWorldMap() {
        return worldMap;
    }

    public void setWorldMap(Map<Integer, Integer> worldMap) {
        this.worldMap = worldMap;
    }

    @Override
    public String toString() {
        String str = "";

        System.out.println("This is a PvEWorldMap object");
        System.out.println("tableId:" + this.table_id);
        System.out.println("worldIDFk:" + this.world_id);
        System.out.println("team0Map(JSON String):" + this.team0Map);
        System.out.println("squareSize:" + this.squareSize);

        System.out.println("-------PvE Map-------");
        for (int j = 0; j < this.squareSize; j++) {
            for (int i = 0; i < this.squareSize; i++) {
                System.out.print(this.worldMap.get(this.generateMapIDForEnv(i, j)));
            }
            System.out.println();
        }

        return str;
    }
}
