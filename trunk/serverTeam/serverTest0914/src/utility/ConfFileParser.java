package utility;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * This class will parse a text file with the given file name.
 *
 * @author , Xuyuan
 */
public class ConfFileParser {
    private String fileName;
    private FileInputStream fis=null;
    private BufferedReader bur=null;

    public ConfFileParser(String fileName){
        this.fileName=fileName;
    }

    /*
     * Open the file with the given name.
     */
    public void openFile(){
        try{
            fis=new FileInputStream(this.fileName);
            bur=new BufferedReader(new InputStreamReader(fis));
        }catch(FileNotFoundException e){
            System.out.println("[In ConfFileParser.java]---No such file, please check.");
        }
    }

    /*
     * Parse each line of the file.
     */
    public Map<String, String> parse(){
        Map<String, String> records=new HashMap<String, String>();
        String str = null;//Store one line of string, like "Port 9090".
        String key = null;//Store key, like "Port".
        String value = null;//Store value, like "9090".
        StringTokenizer st = null;

        this.openFile();

        try{
            while((str=this.bur.readLine())!=null){
                //Delete spaces at the beginning and end.
                str=str.trim();
                //If the line has no content or starts with "#", then go to the next line.
                if(str.length()==0||str.charAt(0)=='#'){continue;}

                st=new StringTokenizer(str);
                int i=0;
                while(st.hasMoreTokens()){
                    i++;
                    if(i==1){
                        key=st.nextToken();
                    }else if(i==2){
                        value=st.nextToken();
                    }else{
                        System.out.println("[In ConfFileParser.java]---There are more than 2 parts in a line in file: "+this.fileName+", please check.");
                    }
                }
                records.put(key, value);
            }
        }catch(IOException e){
            e.printStackTrace();
        }  
        return records;
    }    
}