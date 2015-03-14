package model;

import dataAccessLayer.WorldDAO;

import java.lang.reflect.Field;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import worldManager.gameEngine.GameEngine;
import worldManager.gameEngine.Zone;

/**
 *
 * @author Xuyuan
 */
public class World {

    private int world_id;
    private int creatorPlayerID;
    private String gameName;
    private long seconds;
    private int year;
    private int month;
    private int days;
    private int maxPlayers;
    private String envType;
    private short accessType;
    private short gameMode;
    private String password;
    private List<Environment> environments;
    private boolean hasStarted;
    private List<Player> playerList;
    private HashMap<Integer, Boolean> readyList;
    private GameEngine gameEngine;
    private float time_rate;
    private long play_time;
    private String last_played;

    public World(int world_id) {
        this.world_id = world_id;

        seconds = 1;
        year = 1;
        month = 1;
        days = 1;
        password = "";

        time_rate = 1.0f;

        environments = new ArrayList<Environment>();
        playerList = new ArrayList<Player>();
        readyList = new HashMap<Integer, Boolean>();
    }

    public int getID() {
        return world_id;
    }

    public int setID(int world_id) {
        return this.world_id = world_id;
    }

    public float getTimeRate() {
        return time_rate;
    }

    public float setTimeRate(float time_rate) {
        return this.time_rate = time_rate;
    }

    /**
     * Remove an environment out of the world
     * 
     * @param row               The row of the environment
     * @param col               The col of the environment 
     * @return                  The environment which is removed
     */
    public Environment getEnvByRowAndCol(int row, int col) {
        for (Environment env : environments) {
            if (env.getRow() == row && env.getColumn() == col) {
                return env;
            }
        }
        return null;
    }

    /**
     * Get the environment of a client in this world.
     *
     * @param username              The username of this client.
     * @return                      The target environment.
     */
    public Environment getEnvByUserID(int player_id) {
        for (Environment env : environments) {
            if (env.getOwnerID() == player_id) {
                return env;
            }
        }

        return null;
    }

    public Environment getEnvByID(int env_id) {
        for (Environment env : environments) {
            if (env.getID() == env_id) {
                return env;
            }
        }

        return null;
    }

    /**
     * See if the world contains a user's environment
     */
    public boolean hasEnvironmentOfPlayer(int player_id) {
        for (Environment env : environments) {
            if (env.getOwnerID() == player_id) {
                return true;
            }
        }

        return false;
    }

    public int getCreatorID() {
        return creatorPlayerID;
    }

    public int setCreatorID(int creatorPlayerID) {
        return this.creatorPlayerID = creatorPlayerID;
    }

    public short getAccessType() {
        return accessType;
    }

    public short setAccessType(short accessType) {
        return this.accessType = accessType;
    }

    public int getDays() {
        return days;
    }

    public int setDays(int days) {
        return this.days = days;
    }

    public String getEnvType() {
        return envType;
    }

    public String setEnvType(String envType) {
        return this.envType = envType;
    }

    public List<Environment> getEnvironments() {
        return environments;
    }

    public void setEnvironments(List<Environment> environments) {
        for (Environment env : environments) {
            setEnvironment(env);
        }
    }

    public boolean setEnvironment(Environment environment) {
        for (Zone zone : environment.getZones()) {
            gameEngine.addZone(zone);
        }

        return environments.add(environment);
    }

    public short getGameMode() {
        return gameMode;
    }

    public short setGameMode(short gameMode) {
        return this.gameMode = gameMode;
    }

    public String getGameName() {
        return gameName;
    }

    public String setGameName(String gameName) {
        return this.gameName = gameName;
    }

    public int getMaxPlayers() {
        return maxPlayers;
    }

    public int setMaxPlayers(int maxPlayers) {
        return this.maxPlayers = maxPlayers;
    }

    public String getPassword() {
        return password;
    }

    public String setPassword(String password) {
        return this.password = password;
    }

    public long getPlayTime() {
        return play_time;
    }
    
    public long setPlayTime(long play_time) {
        return this.play_time = play_time;
    }

    public long getSeconds() {
        return seconds;
    }

    public long setSeconds(long seconds) {
        return this.seconds = seconds;
    }
    
    public int getYear() {
        return year;
    }
    
    public int setYear(int year) {
        return this.year = year;
    }

    public int getMonth() {
        return month;
    }

    public int setMonth(int month) {
        return this.month = month;
    }

    public String getLastPlayed() {
        return last_played;
    }

    public String setLastPlayed(String last_played) {
        return this.last_played = last_played;
    }

    public boolean isHasStarted() {
        return hasStarted;
    }

    public boolean setHasStarted(boolean hasStarted) {
        return this.hasStarted = hasStarted;
    }

    public List<Player> getPlayers() {
        return playerList;
    }

    public Player getPlayer(int player_id) {
        for (Player player : playerList) {
            if (player.getID() == player_id) {
                return player;
            }
        }

        return null;
    }

    public boolean hasPlayer(int player_id) {
        return getPlayer(player_id) != null;
    }

    public boolean setPlayer(Player player) {
        readyList.put(player.getID(), false);
        return playerList.add(player);
    }

    public void removePlayer(int player_id) {
        readyList.remove(player_id);
        for (Player player : playerList) {
            if (player.getID() == player_id) {
                playerList.remove(player);
                break;
            }
        }
    }

    public boolean isReady() {
        for (boolean status : readyList.values()) {
            if (!status) {
                return false;
            }
        }

        return true;
    }

    public boolean setReady(int player_id, boolean status) {
        return readyList.put(player_id, status);
    }

    public GameEngine getGameEngine() {
        return gameEngine;
    }

    public GameEngine setGameEngine(GameEngine gameEngine) {
        return this.gameEngine = gameEngine;
    }
    
    public void removeGameEngine() {
        gameEngine.end();
        gameEngine = null;
    }

    public void end() {
        try {
            removeGameEngine();
            WorldDAO.updateTime(this);
        } catch (SQLException ex) {
            System.err.println(ex.getMessage());
        }
    }

    @Override
    public String toString() {
        String str = "";

        str += "-----" + "\n";
        str += getClass().getName() + "\n";
        str += "\n";

        for (Field field : getClass().getDeclaredFields()) {
            try {
                str += field.getName() + " - " + field.get(this) + "\n";
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
            }
        }

        str += "-----";

        return str;
    }
}
