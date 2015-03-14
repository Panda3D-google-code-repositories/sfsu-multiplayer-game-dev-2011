package networking.request;

import core.GameServer;

import dataAccessLayer.ChatLogDAO;

import java.io.IOException;

import networking.response.ResponseChat;

import utility.DataReader;

/**
 *
 * @author Xuyuan
 */
public class RequestChat extends GameRequest {

    // Data
    private short type;
    private String message;
    // Responses
    private ResponseChat responseChat;

    public RequestChat() {
        responses.add(responseChat = new ResponseChat());
    }

    @Override
    public void parse() throws IOException {
        type = DataReader.readShort(dataInput);
        message = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        ChatLogDAO.createMessage(client.getPlayer().getID(), message);

        responseChat.setMessage(message);
        responseChat.setName(client.getPlayer().getUsername());
        responseChat.setType(type);

        GameServer.getInstance().addResponseForAllOnlinePlayers(client.getId(), responseChat);
    }
}
