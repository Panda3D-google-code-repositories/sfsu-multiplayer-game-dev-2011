/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package dataAccessLayer;

import model.*;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Ashu
 */
public class AvatarDAOTest {
    private Player pl = new Player(1, "test", "testpass", "testpass@sfsu.edu", "testCharName");
    private Avatar avatar = new Avatar("testAvatar", 900, 1000, 3, 100, pl, 2, 5);
    
    
    public AvatarDAOTest() {
      }

    @BeforeClass
    public static void setUpClass() throws Exception {
    }

    @AfterClass
    public static void tearDownClass() throws Exception {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }

    /**
     * Test of saveAvatar method, of class AvatarDAO.
     */
    @Test
    public void testSaveAvatar() throws Exception {
        System.out.println("saveAvatar");
        AvatarDAO instance = new AvatarDAO();
        instance.saveAvatar(avatar);
//        instance. .viewAllAvatarRecords();
    }

    /**
     * Test of getAvatarByEnvironmentID method, of class AvatarDAO.
     */
    @Test
    public void testGetAvatarByEnvironmentID_int() throws Exception {
        System.out.println("getAvatarByEnvironmentIDint");
        int envID = 0;
        AvatarDAO instance = new AvatarDAO();
        Avatar result = instance.getAvatarByEnvironmentID(envID);
        int res = result.getAvatarIdPk();
        if(res == 0)
            System.out.println("test passed res"+res);
        else
            System.out.println("test failed res");
        envID = 2;
        result = instance.getAvatarByEnvironmentID(envID);
        int res1 = result.getAvatarIdPk();
        if (res1 == 2)
            System.out.println("test passed res1");
        else
            System.out.println("test failed res1");
        
    }

    /**
     * Test of getAvatarByEnvironmentID method, of class AvatarDAO.
     */
    @Test
    public void testGetAvatarByEnvironmentID_Environment() throws Exception {
        System.out.println("getAvatarByEnvironmentID_envi");
        Environment environment = new Environment(1);
        environment.setEnvIdPk(3);
        AvatarDAO instance = new AvatarDAO();
        Avatar result = instance.getAvatarByEnvironmentID(environment);
        if (result.getAvatarIdPk() == 30)
             System.out.println("test passed resEnvi");
        else
            System.out.println("test failed resEnvi"+ result.getAvatarIdPk());
    }

   
}
