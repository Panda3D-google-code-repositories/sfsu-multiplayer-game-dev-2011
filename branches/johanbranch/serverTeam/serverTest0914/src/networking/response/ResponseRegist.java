package networking.response;

import utility.GamePacket;
import metadata.Constances;

/**
 * This class extends GameResponse and is responsible for handle the regist response.
 *
 * @author , Xuyuan
 */
public class ResponseRegist extends GameResponse{
    private String notification;//"Success" or "Failure" to tell user if they are succeed the registration.

    public ResponseRegist(){
        this.responseCode=Constances.SMSG_REGISTER;
    }
    /*
     * Return the response in the format of bytes.
     */
    public void setNotification(String notification){
        this.notification=notification;
    }
    
    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet=new GamePacket(this.responseCode);
        if(this.notification.equals("success")){
            packet.addShort16((short)1);
            System.out.println(1);
        }else{
            packet.addShort16((short)0);
            System.out.println(0);
        }

        
        return packet.getBytes();
    }

    @Override
    public void printResponse() {
        System.out.println("=========In ResponseRegist==========");
        System.out.println("Notification:"+this.notification);
    }
}
