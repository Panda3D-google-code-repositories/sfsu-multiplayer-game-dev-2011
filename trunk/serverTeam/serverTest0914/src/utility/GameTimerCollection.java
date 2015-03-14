package utility;

import core.GameServer;

import dataAccessLayer.PlayerDAO;

import java.sql.SQLException;
import java.util.TimerTask;

import model.Player;

import worldManager.gameEngine.Zone;

/**
 * 
 * @author Gary
 */
public class GameTimerCollection {

    public static class ZoneTimeTimer extends TimerTask {

        private Player player;
        private Zone zone;

        public ZoneTimeTimer(Player player, Zone zone) {
            this.player = player;
            this.zone = zone;
        }

        @Override
        public void run() {
            GameServer.getInstance().updateExperience(player, 100);
            GameServer.getInstance().updateCash(player, 75);
        }
    }

    public static class SaveTimer extends TimerTask {

        private Player player;

        public SaveTimer(Player player) {
            this.player = player;
        }

        @Override
        public void run() {
            long current = System.currentTimeMillis();
            long seconds = (current - player.getLastSaved()) / 1000;

            player.setPlayTime(player.getPlayTime() + seconds);
            player.setLastSaved(current);

            try {
                PlayerDAO.updatePlayTime(player.getID(), player.getPlayTime());
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }
        }
    }
}
