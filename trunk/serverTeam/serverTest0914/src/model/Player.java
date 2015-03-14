package model;

import core.GameClient;

import java.lang.reflect.Field;

import metadata.Constants;

import utility.GameTimer;
import utility.GameTimerCollection;

/**
 * This is User entity class.
 * @author Xuyuan
 */
public class Player {

    private int player_id;
    private String username;
    private String password;
    private String email;
    private String first_name;
    private String last_name;
    private GameClient client;
    private Avatar avatar;
    private long play_time;
    private long last_saved;
    private GameTimer saveTimer;
    private String last_logout;

    public Player(int player_id) {
        this.player_id = player_id;

        last_saved = System.currentTimeMillis();
        saveTimer = new GameTimer();
    }

    public int getID() {
        return player_id;
    }

    public int setID(int player_id) {
        return this.player_id = player_id;
    }

    public String getEmail() {
        return email;
    }

    public String setEmail(String email) {
        return this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public String setPassword(String password) {
        return this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public String setUsername(String username) {
        return this.username = username;
    }

    public String getFirstName() {
        return first_name;
    }

    public String setFirstName(String first_name) {
        return this.first_name = first_name;
    }

    public String getLastName() {
        return last_name;
    }

    public String setLastName(String last_name) {
        return this.last_name = last_name;
    }

    public GameClient getClient() {
        return client;
    }

    public GameClient setClient(GameClient client) {
        return this.client = client;
    }

    public Avatar getAvatar() {
        return avatar;
    }

    public Avatar setAvatar(Avatar avatar) {
        return this.avatar = avatar;
    }

    public long getPlayTime() {
        return play_time;
    }
    
    public long setPlayTime(long play_time) {
        return this.play_time = play_time;
    }
    
    public long getLastSaved() {
        return last_saved;
    }

    public long setLastSaved(long last_saved) {
        return this.last_saved = last_saved;
    }

    public void startSaveTimer() {
        saveTimer.schedule(new GameTimerCollection.SaveTimer(this), Constants.SAVE_INTERVAL, Constants.SAVE_INTERVAL);
    }

    public boolean stopSaveTimer() {
        return saveTimer.end();
    }

    public String getLastLogout() {
        return last_logout;
    }

    public String setLastLogout(String last_logout) {
        return this.last_logout = last_logout;
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
