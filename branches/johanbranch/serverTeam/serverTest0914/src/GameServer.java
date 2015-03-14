
import java.io.IOException;
import java.net.ServerSocket;
import utility.ConfFileParser;
import configuration.GameServerConf;
import java.net.Socket;
import metadata.GameRequestTable;

/**
 * This class is the entry of Beast Reality Game Server. It does configurations and then runs. 
 *
 * @author , Xuyuan
 */

public class GameServer {
    private GameServerConf configuration;
    private boolean ready=false;

    /*
     * Iniciate the game server.
     */
    public GameServer(){
        this.configuration=new GameServerConf();
        GameRequestTable.init();
    }

    /*
     * Configure the game server by reading from file conf/gameServer.conf.
     */
    private void configure(){
        ConfFileParser confFileParser=new ConfFileParser("conf/gameServer.conf");
        this.configuration.setConfRecords(confFileParser.parse());
    }

    /*
     * Get ready by starting the configuration process and setting ready flag.
     */
    private void getReady(){
        this.configure();
     
        this.ready=true;
     
    }

    private boolean isReady(){
        return this.ready;
    }

    /*
     * Run the game server.
     */
    private void run(){
        ServerSocket listenSocket;
        int serverPort=this.configuration.getPortNumber();

        try{
            //Start to listen on a certain port.
            listenSocket=new ServerSocket(serverPort);
            System.out.println("Server has started on port:"+listenSocket.getLocalPort());
            System.out.println("Waiting for clients...");

            while(true){
                try {
                    //A clientSocket will represent a connection between the client and this server.
                    Socket clientSocket = listenSocket.accept();
                    System.out.println("A Connection Established!");

                    //Create a client on a thread and pass the clientSocket to it. 
                    GameClient client=new GameClient(clientSocket);
                    client.start();

                    
                } catch (IOException e) {
                    System.out.println(e.getMessage());
                }
            }
                        
        }catch(IOException e){
            System.out.println(e.getMessage());
        }catch(Exception e){
            System.out.println(e.getMessage());
        }

      
    }

    public static void main(String args[]){
        GameServer gameServer=new GameServer();
        
        gameServer.getReady();

        if(gameServer.isReady()){
            gameServer.run();
        }
    }

}
