import java.io.ByteArrayInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import metadata.GameRequestTable;
import networking.request.GameRequest;
import networking.response.GameResponse;
import utility.DataReader;


/**
 * This class represents each client on a thread and holds the client's state.
 *
 * @author , Xuyuan
 */

public class GameClient extends Thread{
    private Socket mySocket;
    private InputStream inputStream;
    private OutputStream outputStream;
    private DataInputStream dataInputStream;
    private DataInputStream dataInput;
    private boolean isPlaying;

    /*
     * Inicate the game client by getting the clientSocket and create inputStream&outputStream.
     */
    public GameClient(Socket clientSocket){
        this.mySocket = clientSocket;

        try {
            this.inputStream = this.mySocket.getInputStream();
            this.outputStream = this.mySocket.getOutputStream();
            this.dataInputStream=new DataInputStream(this.inputStream);
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    /*
     * This method overrides the run() from Thread class. So we can customize the client's behaviour here.
     */
    @Override
    public void run(){
         this.isPlaying=true;
         int number_of_sleep_cycles=0;

         while(this.isPlaying){
            try{
               //"In pydatagram, the first short is always size of package."
               short requestLength=DataReader.readShort(dataInputStream);
            
               if(requestLength>0){
                   //"If request erceived, reset number_of_sleep_cycles"
                   number_of_sleep_cycles=0;

                   byte[] buffer = new byte[requestLength];
                   this.inputStream.read(buffer, 0, requestLength);
                   this.dataInput=new DataInputStream(new ByteArrayInputStream(buffer));
                 
                   short requestCode = DataReader.readShort(dataInput);

                   GameRequest request=GameRequestTable.get(requestCode);

                   System.out.println("Request code is : "+requestCode);


                   //If the request if valid, process like following:
                   if(request!=null){
                      //Pass the realInputStream to the request object.
                      request.setDataInputStream(this.dataInput);
                      //The request object parses the realInputStream.
                      request.parse();
                      //The request object process business.
                      request.doBusiness();
                      //Get the response created by the request object.
                      GameResponse response=request.getResponse();
                      //Construct the response from an object to an outputStream.
                      this.outputStream.write(response.constructResponseInBytes());
                   }
                   
               }else{
                   //"If size of package is <=0 (no valid request), 
                   //put thread to sleep for 20 milliseconds each time,
                   //for as long as client sends no requests."
                   Thread.sleep(20);
                   number_of_sleep_cycles++;

                   //"Check if GameClient has been waiting for client's request at least 1 minute
                   //(1 minute=3000 sleeping cycles)"
                   if(number_of_sleep_cycles>=3000){
                       this.isPlaying=false;
                   }
               }
            }catch(IOException e) {
               System.out.println(e.getMessage());
            }catch(InterruptedException e){
               System.out.println(e.getMessage());
            }
         }

         System.out.println("The client stops playing.");
    }

}
