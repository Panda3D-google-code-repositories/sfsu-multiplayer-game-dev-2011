/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package dataAccessLayer;

import java.util.List;
import model.Environment;
import model.World;
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
public class EnvironmentDAOTest {
    
    public EnvironmentDAOTest() {
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
     * Test of saveEnvironment method, of class EnvironmentDAO.
     */
    @Test
    public void testSaveEnvironment() throws Exception {
        System.out.println("saveEnvironment");
        Environment environment = null;
        EnvironmentDAO instance = new EnvironmentDAO();
        instance.saveEnvironment(environment);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of getEnvironmentByWorldIDAndRowAndCol method, of class EnvironmentDAO.
     */
    @Test
    public void testGetEnvironmentByWorldIDAndRowAndCol() throws Exception {
        System.out.println("getEnvironmentByWorldIDAndRowAndCol");
        Environment environment = null;
        EnvironmentDAO instance = new EnvironmentDAO();
        Environment expResult = null;
        Environment result = instance.getEnvironmentByWorldIDAndRowAndCol(environment);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of getEnvironmentByWorldID method, of class EnvironmentDAO.
     */
    @Test
    public void testGetEnvironmentByWorldID_int() throws Exception {
        System.out.println("getEnvironmentByWorldID");
        int worldIdPk = 0;
        EnvironmentDAO instance = new EnvironmentDAO();
        List expResult = null;
        List result = instance.getEnvironmentByWorldID(worldIdPk);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of getEnvironmentByWorldID method, of class EnvironmentDAO.
     */
    @Test
    public void testGetEnvironmentByWorldID_World() throws Exception {
        System.out.println("getEnvironmentByWorldID");
        World world = null;
        EnvironmentDAO instance = new EnvironmentDAO();
        List expResult = null;
        List result = instance.getEnvironmentByWorldID(world);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of main method, of class EnvironmentDAO.
     */
    @Test
    public void testMain() {
        System.out.println("main");
        String[] args = null;
        try
        {
            EnvironmentDAO.main(args);
        }
        catch(Exception e)
        {
            
        }
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
}
