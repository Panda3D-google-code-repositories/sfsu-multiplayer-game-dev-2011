package core;

import dataAccessLayer.PlayerDAO;
import dataAccessLayer.WorldDAO;
import java.io.ByteArrayInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.lang.reflect.Field;
import java.net.Socket;
import java.sql.SQLException;
import java.util.LinkedList;
import java.util.Queue;

import metadata.Constants;
import metadata.GameRequestTable;

import model.Avatar;
import model.Player;
import model.World;

import networking.request.GameRequest;
import networking.response.GameResponse;

import networking.response.ResponseChat;
import networking.response.ResponseSeeOnlinePlayers;
import utility.DataReader;

/**
 * This class represents each client on a thread and holds the client's state.
 *
 * @author Xuyuan
 */
public class GameClient extends Thread {

    private GameServer server;
    private Socket mySocket;
    private InputStream inputStream;
    private OutputStream outputStream;
    private DataInputStream dataInputStream;
    private DataInputStream dataInput;
    private Player player;
    private boolean isPlaying;
    private Avatar avatar;
    private World world;
    private Queue<GameResponse> updates;

    /*
     * Inicate the game client by getting the clientSocket and create inputStream&outputStream.
     */
    public GameClient(Socket clientSocket, GameServer server) throws IOException {
        mySocket = clientSocket;
        this.server = server;
        updates = new LinkedList<GameResponse>();

        inputStream = mySocket.getInputStream();
        outputStream = mySocket.getOutputStream();
        dataInputStream = new DataInputStream(inputStream);
    }

    /*
     * This method overrides the run() from Thread class. So we can customize the client's behaviour here.
     */
    @Override
    public void run() {
        isPlaying = true;
        long lastActivity = System.currentTimeMillis();
        short requestCode = -1;

        while (isPlaying) {
            try {
                //"In pydatagram, the first short is always size of package."
                short requestLength = DataReader.readShort(dataInputStream);

                if (requestLength > 0) {
                    lastActivity = System.currentTimeMillis();

                    byte[] buffer = new byte[requestLength];
                    inputStream.read(buffer, 0, requestLength);
                    dataInput = new DataInputStream(new ByteArrayInputStream(buffer));

                    requestCode = DataReader.readShort(dataInput);

//                    if (requestCode != Constants.CMSG_HEARTBEAT) {
//                        System.out.println("Request code is : " + requestCode);
//                    }

                    GameRequest request = GameRequestTable.get(requestCode);

                    //If the request if valid, process like following:
                    if (request != null) {
                        request.setGameClient(this);
                        //Pass the realInputStream to the request object.
                        request.setDataInputStream(dataInput);
                        //The request object parses the realInputStream.
                        request.parse();
                        //The request object process business.
                        request.doBusiness();
                        //Get the response created by the request object.
                        for (GameResponse response : request.getResponses()) {
                            //Construct the response from an object to an outputStream.
                            outputStream.write(response.constructResponseInBytes());
                        }

//                        response.printResponse();
                    }
                } else {
                    // Check if GameClient has been waiting for client's request at least 1 minute
                    if ((System.currentTimeMillis() - lastActivity) / 1000 >= Constants.TIMEOUT_SECONDS) {
                        isPlaying = false;
                    }
                }
            } catch (Exception e) {
                System.err.println("Request [" + requestCode + "] Error:");
                System.err.println(e.getMessage());
                System.err.println("---");
                e.printStackTrace();
            }
        }

        System.out.println("The client stops playing.");

        if (player != null) {
            //Delete this client out of the playerPositionTracker in GameServer.java
            server.deletePlayerOutOfPositionTracker(player.getID());

            player.stopSaveTimer();

            if (world != null) {
                world.removePlayer(player.getID());

                if (world.getPlayers().isEmpty()) {
                    world.end();
                    server.removeWorldAndWorldMapFromBuffer(world.getID(), world.getGameMode());
                }
            }

            try {
                WorldDAO.updateLastPlayed(world.getID());

                long seconds = (System.currentTimeMillis() - player.getLastSaved()) / 1000;
                player.setPlayTime(player.getPlayTime() + seconds);

                PlayerDAO.updateLogout(player.getID(), player.getPlayTime());
            } catch (SQLException ex) {
                System.err.println(ex.getMessage());
            }

            GameServer.getInstance().removeActivePlayer(player.getID());

            ResponseChat responseChat = new ResponseChat();
            responseChat.setMessage("[" + player.getUsername() + "] has logged off.");
            responseChat.setType((short) 1);

            GameServer.getInstance().addResponseForAllOnlinePlayers(this.getId(), responseChat);

            ResponseSeeOnlinePlayers responsePlayers = new ResponseSeeOnlinePlayers();
            responsePlayers.setOnlinePlayers(GameServer.getInstance().getActivePlayers());

            GameServer.getInstance().addResponseForAllOnlinePlayers(this.getId(), responsePlayers);
        }

        //Delete this client out of the activeThreads
        server.deletePlayerThreadOutOfActiveThreads(getId());
    }
    
    public void stopClient() {
        isPlaying = false;
    }

    public GameServer getServer() {
        return server;
    }

    public Player getPlayer() {
        return player;
    }

    public Player setPlayer(Player player) {
        return this.player = player;
    }

    public boolean addResponseForUpdate(GameResponse response) {
        return updates.add(response);
    }

    public Queue<GameResponse> getUpdates() {
        Queue<GameResponse> responseList = null;

        synchronized (this) {
            responseList = updates;
            updates = new LinkedList<GameResponse>();
        }

        return responseList;
    }

    public OutputStream getOutputStream() {
        return outputStream;
    }

    public World getWorld() {
        return world;
    }

    public World setWorld(World world) {
        return this.world = world;
    }

    public Avatar getAvatar() {
        return avatar;
    }

    public Avatar setAvatar(Avatar avatar) {
        return this.avatar = avatar;
    }

    /**
     * Clear the update buffer of this client thread. 
     */
    public void clearUpdateBuffer() {
        updates.clear();
    }

    public String getIP() {
        return mySocket.getInetAddress().getHostAddress();
    }

    /**
     * Print part information of a GameClient object.
     *
     */
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
