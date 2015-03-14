/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package simulationEngine;



import core.GameServer;
import java.io.FileInputStream;
import java.io.*;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Properties;
import java.util.Date;
import java.util.*;

import org.datacontract.schemas._2004._07.LINQ2Entities.User;
import org.datacontract.schemas._2004._07.LINQ2Entities.Nodes;
import org.datacontract.schemas._2004._07.LINQ2Entities.NodeParameters;
import org.datacontract.schemas._2004._07.ManipulationParameter.ManipulatingNode;
import org.datacontract.schemas._2004._07.ManipulationParameter.ManipulatingNodeProperty;
import org.datacontract.schemas._2004._07.ManipulationParameter.ManipulatingParameter;
import org.datacontract.schemas._2004._07.ManipulationParameter.ModelParam;
import org.datacontract.schemas._2004._07.ManipulationParameter.NodeBiomass;
import org.datacontract.schemas._2004._07.WCFService_Portal.CreateFoodwebResponse;
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationInfo;
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationInfoRequest;
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationInfoResponse;
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationResponse;
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationTimestepInfo;
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationTimestepInfoRequest;
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationTimestepInfoResponse;
import org.datacontract.schemas._2004._07.WCFService_Portal.NetworkCreationRequest;
import org.datacontract.schemas._2004._07.WCFService_Portal.NetworkRemoveRequest;
import org.datacontract.schemas._2004._07.WCFService_Portal.NodeInfoRequest;
import org.datacontract.schemas._2004._07.WCFService_Portal.NodeInfoResponse;
import org.datacontract.schemas._2004._07.WCFService_Portal.NodeInfo;
import org.datacontract.schemas._2004._07.WCFService_Portal.NetworkInfo;
import org.datacontract.schemas._2004._07.WCFService_Portal.NetworkInfoRequest;
import org.datacontract.schemas._2004._07.WCFService_Portal.NetworkInfoResponse;
import org.datacontract.schemas._2004._07.WCFService_Portal.Response;
import org.datacontract.schemas._2004._07.WCFService_Portal.SimpleManipulationRequest;
import org.datacontract.schemas._2004._07.WCFService_Portal.*;
import org.foodwebs.www._2009._11.IN3DService;
import org.foodwebs.www._2009._11.IN3DServiceProxy;

import metadata.Constants;

import model.SpeciesType;

import simulationEngine.*;
import simulationEngine.SpeciesZoneType.SpeciesTypeEnum;
import simulationEngine.config.ManipulatingNodePropertyName;
import simulationEngine.config.ManipulatingParameterName;
import simulationEngine.config.ManipulationActionType;
import simulationEngine.config.ModelType;


/**
 *
 * @author Paul
 */
public class SimulationEngineTest {

    
    
    
        public String foodwebStabilityTest10_7(SimulationEngine se)
        {

            int nodeList[] = { 4, 5, 73 };            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            

            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
            
            
            se.run(2, 18, manpId, false);
          
            se.getBiomassInfo(manpId);
            
            return manpId;
        }                            
    
        
        public String foodwebStabilityTest_4species_x73_08(SimulationEngine se)
        {

            int nodeList[] = { 4, 5, 73 };            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            

            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);                        
//            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);            
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
            
            
            se.run(2, 18, manpId, false);
          
            se.getBiomassInfo(manpId);
            
            return manpId;
        }                     
    
        
        public String foodwebStabilityTest_4species_x73_80_08(SimulationEngine se)
        {

            int nodeList[] = { 4, 5, 73 };            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            

            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);                        
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);            
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
/*            
            nodes = new ArrayList<ManipulatingNode>();
            sParams = new ArrayList<ManipulatingParameter>();            
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);                        
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);            
            se.updateSystemParameters(2, false, manpId, sParams, nodes);            
  */        
            se.run(2, 18, manpId, false);
          
//            se.getBiomassInfo(manpId);
            
            return manpId;
        }            
        
        
        public String foodwebStabilityTest_4species_x73_02_80_02(SimulationEngine se)
        {

            int nodeList[] = { 4, 5, 73 };            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            

            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.2, sParams);                        
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.2, sParams);            
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
   
          
            se.run(2, 18, manpId, false);
          
            se.getBiomassInfo(manpId);
            
            return manpId;
        }              
        
       public String foodwebStabilityTest_4species_4_R_08(SimulationEngine se)
        {

            int nodeList[] = { 4, 5};            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
/*            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            
*/
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
//            se.setNodeParameter(80, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.8, sParams);        

            se.setNodeParameter(4, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.2, sParams);                        
            se.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.5, sParams);            
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
/*            
            nodes = new ArrayList<ManipulatingNode>();
            sParams = new ArrayList<ManipulatingParameter>();            
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);                        
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.4, sParams);            
            se.updateSystemParameters(2, false, manpId, sParams, nodes);            
*/          
            se.run(2, 18, manpId, false);
          
            se.getBiomassInfo(manpId);
            
            return manpId;
        }                      
        
       
       
      public String foodwebStabilityTest_4species_x4_X02(SimulationEngine se)
        {

            int nodeList[] = { 4, 5};            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
/*            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            
*/
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
//            se.setNodeParameter(80, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.8, sParams);                        
            se.setNodeParameter(4, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.2, sParams);            
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
/*            
            nodes = new ArrayList<ManipulatingNode>();
            sParams = new ArrayList<ManipulatingParameter>();            
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);                        
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.4, sParams);            
            se.updateSystemParameters(2, false, manpId, sParams, nodes);            
*/          
            se.run(2, 18, manpId, false);
          
            se.getBiomassInfo(manpId);
            
            return manpId;
        }                       
       
      
      
      
     public String foodwebStabilityTest_4species_73_4_PD_05(SimulationEngine se)
        {

            int nodeList[] = { 4, 5, 73};            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(73, 4, ManipulatingParameterName.d.getManipulatingParameterIndex(), 0.5, sParams);
//            se.setNodeParameter(80, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.8, sParams);                        
//            se.setNodeParameter(4, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.2, sParams);            
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
/*            
            nodes = new ArrayList<ManipulatingNode>();
            sParams = new ArrayList<ManipulatingParameter>();            
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);                        
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.4, sParams);            
            se.updateSystemParameters(2, false, manpId, sParams, nodes);            
*/          
            se.run(2, 18, manpId, false);
          
            se.getBiomassInfo(manpId);
            
            return manpId;
        }                   
      
     
          public String foodwebStabilityTest_4species_73_5_PD_05(SimulationEngine se)
        {

            int nodeList[] = { 4, 5, 73};            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(73, 5, ManipulatingParameterName.d.getManipulatingParameterIndex(), 0.5, sParams);
//            se.setNodeParameter(80, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.8, sParams);                        
//            se.setNodeParameter(4, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.2, sParams);            
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
/*            
            nodes = new ArrayList<ManipulatingNode>();
            sParams = new ArrayList<ManipulatingParameter>();            
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);                        
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.4, sParams);            
            se.updateSystemParameters(2, false, manpId, sParams, nodes);            
*/          
            se.run(2, 18, manpId, false);
          
            se.getBiomassInfo(manpId);
            
            return manpId;
        }                   
      
          
         public String foodwebStabilityTest_4species_73_4_5_PD_05(SimulationEngine se)
        {

            int nodeList[] = { 4, 5, 73};            

            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2500);
            node.setHasLinks(false);
            nodes.add(node);
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);            
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId("74B9B375-1729-4516-A231-AE8A6114AACF");            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(73, 4, ManipulatingParameterName.d.getManipulatingParameterIndex(), 0.1, sParams);            
            se.setLinkParameter(73, 5, ManipulatingParameterName.d.getManipulatingParameterIndex(), 0.3, sParams);
//            se.setNodeParameter(80, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.8, sParams);                        
//            se.setNodeParameter(4, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.2, sParams);            
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
/*            
            nodes = new ArrayList<ManipulatingNode>();
            sParams = new ArrayList<ManipulatingParameter>();            
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);                        
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.4, sParams);            
            se.updateSystemParameters(2, false, manpId, sParams, nodes);            
*/          
            se.run(2, 18, manpId, false);
          
//            se.getBiomassInfo(manpId);
            
            return manpId;
        }                         
          
         
         public void testManipulationParameterInfoReqest(SimulationEngine se)
         {
             ManipulatingParameter[] params = se.getSystemParameterInfos("6A8C7654-EA53-415A-982F-00D7B208B906");
             for(ManipulatingParameter param : params)
             {
                 System.out.println("Name:" +param.getParamName() );                                                                    
                 System.out.println("Idx:" +param.getParamIdx() );                 
                 System.out.println("Type:" +param.getParamType() );                 
                 System.out.println("value:" +param.getParamValue() );                 
                 System.out.println("TsIdx:" +param.getTimestepIdx() );                                                   
                 System.out.println("nodeIdx:" +param.getNodeIdx() ); 
                 if(param.getPredIdx() != -1)
                    System.out.println("pred:" +param.getPredIdx() );                                  
                 if(param.getPreyIdx() != -1)                 
                    System.out.println("prey:" +param.getPreyIdx() );                                                   
                 System.out.println("=======================" );                                  
             }
         }
         
         
         
         public static boolean compareCSVFiles(String oldfileName, String newfileName)
         {
             
             BufferedReader oldreader = null;
             BufferedReader newreader = null;
             try
             {
                oldreader = new BufferedReader(new InputStreamReader(new FileInputStream(oldfileName),"US-ASCII"));
                newreader = new BufferedReader(new InputStreamReader(new FileInputStream(newfileName),"US-ASCII"));
                boolean firstline = true;
                
                while(true) 
                {
                    String reader1Line = oldreader.readLine();
                    String reader2Line = newreader.readLine();
                    if(reader1Line == null) 
                    {
                         if(reader2Line == null) 
                         {
                            break;
                         }
                         else 
                         {
                        //Error file 2 has more lines than file 1
                             oldreader.close();
                             newreader.close();            
                            return false;
                        }
                    }
                    else if(reader2Line == null && reader1Line != null) 
                    {
                        //Error file 1 has more lines than file 2                    
                         oldreader.close();
                         newreader.close();            
                        return false;
                    }

                    String[] line1Parts = reader1Line.split(",");
                    String[] line2Parts = reader2Line.split(",");
                    if(line1Parts.length != line2Parts.length)
                    {
                         oldreader.close();
                         newreader.close();            
                        return false;
                    }
                        //error different number of entries in the two rows

                    if(!firstline)
                    {
                        for(int i = 0; i < line1Parts.length;i++) 
                        {
                            if(line1Parts[i].length() == 0 && line2Parts[i].length() == 0)
                                continue;
                            double entry1 = Double.parseDouble(line1Parts[i]);
                            double entry2 = Double.parseDouble(line2Parts[i]);
                            double average = (entry1 + entry2) / 2;
                            if(Math.abs((entry1 - entry2) / average) > 0.03) 
                            {
                                oldreader.close();
                                newreader.close();            
                                return false;
                             //Entries are too close.
                            }
                        }
                    }
                    else
                    {
                        firstline = false;
                    }
                }
                 oldreader.close();
                 newreader.close();            
             }
            catch(Exception e)
            {
                System.err.println("Error while comparing two csv file:" +e.getMessage());
            }
            return true;
         }
         
         private boolean testManipulationFunctionResultFile(String dir, String normalFile, String testFile)
         {
             boolean passed;
              
             passed = compareCSVFiles(dir+normalFile+".csv", testFile);
             if(!passed)
             {
                System.out.println(normalFile+" test failed");
                return false;
             }
             else
                System.out.println("passed "+normalFile+" test");
             
             return true;
         }
                 
         
        public boolean masterTestFunction(String url)
        {
 
            boolean passed;
//	    SimulationEngine se = new SimulationEngine();                                         
            SimulationEngine se = new SimulationEngine(url);             
//            SimulationEngine se = new SimulationEngine("http://127.0.0.1:82/N3DWebService.svc?wsdl");                         
//	    SimulationEngine se = new SimulationEngine("http://localhost:41246/N3DWebService.svc?wsdl");                             
            String dir = "E:\\Project\\Beast\\data\\testData\\";
           
            // serengeti sub food web creation test
            int nodeList[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36};
            String serengetiFWName = "f1a55cx.8adfbbaav";
            String netId = se.createSeregenttiSubFoodweb(serengetiFWName, nodeList, true);
            if(netId == null)
            {
                System.out.println("error while creating food web");
                return false;
            }
            else
            {
                System.out.println("Serengeti sub foodweb creation passed");                
                se.deleteNetwork(netId);
            }
            
            serengetiFWName = "f2a55cx77.fdadaacdax";
            // simple manipulation creating and running test
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, serengetiFWName, 0, 10, true);
            if(netId == null)
            {
                System.out.println("error while creating manipulation");
                return false;
            }
            else
            {
                System.out.println("Simple manipulation creation passed");                
                se.deleteManipulation(manpId);
            }
            
/*            
          // test 'getBiomass' function
            passed = this.testGetBiomass(se, "testGetBiomass1");       
            if(passed)
            {
                System.out.println("getBiomass function test1 passed");                                
            }
            else
            {
                System.out.println("getBiomass function test1 failed");                                            
                return false;
            }
            this.testGetBiomass(se, "testGetBiomass2");       
            if(passed)
            {
                System.out.println("getBiomass function test2 passed");                                
            }
            else
            {
                System.out.println("getBiomass function test2 failed");                                            
                return false;
            }
            this.testGetBiomass(se, "testGetBiomass3");      
            if(passed)
            {
                System.out.println("getBiomass function test3 passed");                                
            }
            else
            {
                System.out.println("getBiomass function test3 failed");                                            
                return false;
            }            
*/            
            // adding 5 species (10, 11, 13, 14, 16 ) to manipulation in a row
            manpId = se.foodwebStabilityTest10_1_1();
            if(manpId == null)
            {
                System.out.println("error while adding species to manipulation");
                return false;
            }
            else
            {
                System.out.println("Adding 5 species to manipulation in a row passed");                
                se.deleteManipulation(manpId);
            }
            
            // adding 14 species to manipulation in a row            
            manpId = se.runningTest();
            if(manpId == null)
            {
                System.out.println("error while adding 14 species to manipulation");
                return false;
            }
            else
            {
                System.out.println("Adding 14 species to manipulation in a row passed");                
                se.deleteManipulation(manpId);
            }
            
            // test 'updateBiomass' function
            manpId = se.foodwebModelStabilityTest1();
            if(manpId == null)
            {
                System.out.println("error on testing updateBiomass");
                return false;
            }
            else
            {
                String normalFile = "updateBiomass";
                String testFile = dir+"test3.csv";
                se.saveBiomassCSVFile(manpId, testFile );
                se.deleteManipulation(manpId);                
//                passed = testManipulationFunctionResultFile(dir, normalFile, testFile);
//                if(!passed)
//                    return passed;
                
                System.out.println("updateBiomass function test passed");                
            }            
            
  
            
            
            // test 'updateSystemParameters' function
            manpId = se.foodwebStabilityTest10_4();
           if(manpId == null)
            {
                System.out.println("error on testing 'updateSystemParameters'");
                return false;
            }
            else
            {
                String normalFile = "updateSystemParameters";
//                String testFile = dir+"test3.csv";
//                se.saveBiomassCSVFile(manpId, testFile );
                se.deleteManipulation(manpId);                
//                passed = testManipulationFunctionResultFile(dir, normalFile, testFile);
//                if(!passed)
//                    return passed;
                
                System.out.println("'updateSystemParameters' function test passed");                
            }                        
            SimulationEngineTest test = new SimulationEngineTest();
            
            // this function tests if node parameters are manipulated successfully
            manpId = test.foodwebStabilityTest_4species_x73_80_08(se);
               
            String normalFile = "foodwebStabilityTest_4species_x73_80_08";
            String testFile = dir+"test1.csv";
            se.saveBiomassCSVFile(manpId, testFile );
            se.deleteManipulation(manpId);                
            passed = testManipulationFunctionResultFile(dir, normalFile, testFile);
            if(!passed)
                return passed;

            // this function tests if link parameters are manipulated successfully               
            manpId = test.foodwebStabilityTest_4species_73_4_5_PD_05(se);
            normalFile = "foodwebStabilityTest_4species_73_4_5_PD_05";
            testFile = dir+"test2.csv";
            se.saveBiomassCSVFile(manpId, testFile );
            se.deleteManipulation(manpId);                                
            passed = testManipulationFunctionResultFile(dir, normalFile, testFile);
            if(!passed)
                return passed;
            
            // tests if cocurrent 10 manipulations run smoothly without any error.
            se.testManpThread();
            
             return true;
         }
         
        public void testNode4Oribi(SimulationEngine se )
        {
            int nodeList[] = {4,5, 73};
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "testNode4and73", 0, 1, true);
                    
           List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(10000);
            node.setHasLinks(false);
            nodes.add(node);

            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(10000);
            node.setHasLinks(false);
            nodes.add(node);

            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(10);
            node.setHasLinks(false);
            nodes.add(node);
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
//            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
//            this.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
            se.run(2, 18, manpId, false);
          
            se.saveBiomassCSVFile(manpId); 
            se.getBiomassInfo(manpId);
            se.deleteManipulation(manpId);                                  
            
        }
        
        
      public void testInsectFoodweb(SimulationEngine se)
      {
            int nodeList[] = {1,8};
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "testInsectWeb", 0, 1, true);
                    
           List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(8);
            node.setBeginingBiomass(2);
            node.setHasLinks(false);
            nodes.add(node);

            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(1, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setNodeParameter(8, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.75, 1, sParams);            
//            this.setNodeParameter(12, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.9, sParams);                        
//            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 5000, sParams);            
//            this.setNodeParameter(4, ManipulatingParameterName.r.getManipulatingParameterIndex(), , sParams);
//            this.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.333, sParams);            

//            this.setLinkParameter(73, 4, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.6, 1, sParams);            
//            this.setLinkParameter(73, 5, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.4, 1, sParams);                        
            se.updateSystemParameters(1, false, manpId, sParams, nodes);

///            testParameters(manpId, sParams);
//            run(2, 8, manpId, false);                        

           
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(2);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(2);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(2, ManipulatingParameterName.k.getManipulatingParameterIndex(), 4000, 2, sParams);                                    
//            se.setNodeParameter(12, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.85, 2, sParams);                        
//            this.setLinkParameter(9, 1, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.05, 1, sParams);            
//            this.setLinkParameter(9, 9, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.3, 1, sParams);                        
//            this.setLinkParameter(9, 12, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.65, 1, sParams);                        
            
//            this.setLinkParameter(73, 4, ManipulatingParameterName.d.getManipulatingParameterIndex(), 1, 3, sParams);
//            this.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.9, sParams);
//            this.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.333, sParams);            
            se.updateSystemParameters(2, false, manpId, sParams, nodes);   
//            run(3, 27, manpId, false);                          

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(3);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(9);
            node.setBeginingBiomass(2);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(3, false, manpId, sParams, nodes);               

            
            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(4);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(12);
            node.setBeginingBiomass(1.5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(4, false, manpId, sParams, nodes);               

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(5);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 4000, 5, sParams);                                                
            se.updateSystemParameters(5, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(6);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(14);
            node.setBeginingBiomass(3);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(6, false, manpId, sParams, nodes);               

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(7);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(7);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(7, ManipulatingParameterName.k.getManipulatingParameterIndex(), 4000, 7, sParams);                                                            
            se.updateSystemParameters(7, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(8);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(16);
            node.setBeginingBiomass(1.3);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(8, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(9);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(20);
            node.setBeginingBiomass(1.2);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(9, false, manpId, sParams, nodes);               
            
            se.run(10, 20, manpId, false);

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(30);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(8000);
            node.setHasLinks(false);
            nodes.add(node);
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(30, false, manpId, sParams, nodes);               
            
             se.run(31, 20, manpId, false);
          
            se.saveBiomassCSVFile(manpId); 
            se.getBiomassInfo(manpId);
            se.deleteManipulation(manpId);                       
        }
        
      
      
      
      public void testInsectFoodweb2(SimulationEngine se)
      {
            int nodeList[] = {1,8};
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "testInsectWeb", 0, 1, true);
                    
           List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(1);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(8);
            node.setBeginingBiomass(0.001);
            node.setHasLinks(false);
            nodes.add(node);

            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(1, ManipulatingParameterName.k.getManipulatingParameterIndex(), 2, sParams);
            se.setNodeParameter(8, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.75, 1, sParams);            
//            this.setNodeParameter(12, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.9, sParams);                        
//            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 5000, sParams);            
//            this.setNodeParameter(4, ManipulatingParameterName.r.getManipulatingParameterIndex(), , sParams);
//            this.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.333, sParams);            

//            this.setLinkParameter(73, 4, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.6, 1, sParams);            
//            this.setLinkParameter(73, 5, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.4, 1, sParams);                        
            se.updateSystemParameters(1, false, manpId, sParams, nodes);

///            testParameters(manpId, sParams);
//            run(2, 8, manpId, false);                        

           
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(2);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(2);
            node.setBeginingBiomass(1);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(2, ManipulatingParameterName.k.getManipulatingParameterIndex(), 2, 2, sParams);                                    
//            se.setNodeParameter(12, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.85, 2, sParams);                        
//            this.setLinkParameter(9, 1, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.05, 1, sParams);            
//            this.setLinkParameter(9, 9, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.3, 1, sParams);                        
//            this.setLinkParameter(9, 12, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.65, 1, sParams);                        
            
//            this.setLinkParameter(73, 4, ManipulatingParameterName.d.getManipulatingParameterIndex(), 1, 3, sParams);
//            this.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.9, sParams);
//            this.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.333, sParams);            
            se.updateSystemParameters(2, false, manpId, sParams, nodes);   
//            run(3, 27, manpId, false);                          

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(3);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(9);
            node.setBeginingBiomass(0.001);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(3, false, manpId, sParams, nodes);               

            
            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(4);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(12);
            node.setBeginingBiomass(0.00075);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(4, false, manpId, sParams, nodes);               

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(5);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(1);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 2, 5, sParams);                                                
            se.updateSystemParameters(5, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(6);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(14);
            node.setBeginingBiomass(0.0015);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(6, false, manpId, sParams, nodes);               

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(7);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(7);
            node.setBeginingBiomass(1);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(7, ManipulatingParameterName.k.getManipulatingParameterIndex(), 2, 7, sParams);                                                            
            se.updateSystemParameters(7, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(8);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(16);
            node.setBeginingBiomass(0.00065);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(8, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(9);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(20);
            node.setBeginingBiomass(0.0006);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(9, false, manpId, sParams, nodes);               
            
            se.run(10, 240, manpId, false);

/*            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(30);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(8000);
            node.setHasLinks(false);
            nodes.add(node);
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(30, false, manpId, sParams, nodes);               
            
             se.run(31, 20, manpId, false);
*/          
            se.saveBiomassCSVFile(manpId); 
            se.getBiomassInfo(manpId);
            se.deleteManipulation(manpId);                       
        }
        

      
      public void testInsectFoodweb3(SimulationEngine se)
      {
            int nodeList[] = {1,8};
            int halfSDtoPlant = 200;
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "testInsectWeb", 0, 1, true);
                    
           List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(8);
            node.setBeginingBiomass(2);
            node.setHasLinks(false);
            nodes.add(node);

            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(1, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            se.setLinkParameter(8, 1, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 1, sParams);            

            se.updateSystemParameters(1, false, manpId, sParams, nodes);
           
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(2);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(2);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(2, ManipulatingParameterName.k.getManipulatingParameterIndex(), 4000, 2, sParams);                                    
            se.setLinkParameter(8, 2, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 2, sParams);                        
            se.updateSystemParameters(2, false, manpId, sParams, nodes);   

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(3);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(9);
            node.setBeginingBiomass(2);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(9, 1, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 3, sParams);                        
            se.updateSystemParameters(3, false, manpId, sParams, nodes);               

            
            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(4);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(12);
            node.setBeginingBiomass(1.5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(12, 1, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 4, sParams);            
            se.updateSystemParameters(4, false, manpId, sParams, nodes);               

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(5);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 4000, 5, sParams);                                                
            se.setLinkParameter(12, 5, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 5, sParams);                        
            se.updateSystemParameters(5, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(6);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(14);
            node.setBeginingBiomass(3);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(14, 1, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 6, sParams);            
            se.setLinkParameter(14, 2, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 6, sParams);            
            se.setLinkParameter(14, 5, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 6, sParams);                        
            se.updateSystemParameters(6, false, manpId, sParams, nodes);               

            
            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(7);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(7);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setNodeParameter(7, ManipulatingParameterName.k.getManipulatingParameterIndex(), 4000, 7, sParams);                                                            
            se.setLinkParameter(14, 7, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 7, sParams);                        
            se.updateSystemParameters(7, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(8);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(16);
            node.setBeginingBiomass(1.3);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(16, 1, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 8, sParams);                                    
            se.updateSystemParameters(8, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(9);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(20);
            node.setBeginingBiomass(1.2);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(9, false, manpId, sParams, nodes);               
            
            se.run(10, 20, manpId, false);

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(30);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(8000);
            node.setHasLinks(false);
            nodes.add(node);
            
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(30, false, manpId, sParams, nodes);               
            
             se.run(31, 20, manpId, false);
          
            se.saveBiomassCSVFile(manpId); 
            se.getBiomassInfo(manpId);
            se.deleteManipulation(manpId);                       
        }
            
      
     public void testInsectFoodweb4(SimulationEngine se)
      {
            int nodeList[] = {1,8};
            int halfSDtoPlant = 200;
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "testInsectWeb", 0, 1, true);
                    
           List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(8);
            node.setBeginingBiomass(0.02);
            node.setHasLinks(false);
            nodes.add(node);
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(1, false, manpId, sParams, nodes);

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(2);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(9);
            node.setBeginingBiomass(0.03);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(2, false, manpId, sParams, nodes);   

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(3);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(11);
            node.setBeginingBiomass(0.02);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(3, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(4);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(12);
            node.setBeginingBiomass(0.02);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(4, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(5);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(3);
            node.setBeginingBiomass(1);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(5, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(6);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(13);
            node.setBeginingBiomass(0.02);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(6, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(7);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(14);
            node.setBeginingBiomass(0.02);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(7, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(8);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(0.02);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(8, false, manpId, sParams, nodes);               

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(9);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(7);
            node.setBeginingBiomass(1);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            sParams = new ArrayList<ManipulatingParameter>();
            se.updateSystemParameters(9, false, manpId, sParams, nodes);               

            
            se.run(10, 30, manpId, false);
            se.saveBiomassCSVFile(manpId); 
            se.getBiomassInfo(manpId);
            se.deleteManipulation(manpId);                       
        }      

     public boolean testGetBiomass(SimulationEngine se ,String networkName) {
        int nodeList[] = {1, 8, 9};

        String man_id = se.createAndRunSeregenttiSubFoodweb(nodeList, networkName, 0, 0, true);

        List<NodeBiomass> lNodeBiomass = new ArrayList<NodeBiomass>();

        lNodeBiomass.add(new NodeBiomass(1000 * 10, 1));
        lNodeBiomass.add(new NodeBiomass(20 * 5, 8));
        lNodeBiomass.add(new NodeBiomass(20 * 5, 9));

        if (!lNodeBiomass.isEmpty()) {
            se.updateBiomass(man_id, lNodeBiomass, 0);
        }

        String errMsg = se.getBiomass(man_id, 0, 0);
        se.deleteManipulation(man_id);
        
        if(errMsg == null)
        {

            return true;
        }
        else
        {
            System.out.println("Error on getBiomass function:"+errMsg);            
            return false;
        }
    }

     
     
     public void createLevel1FW(SimulationEngine se)
     {
         String fwName = "Serengeti_level1_Foodweb";
         int nodeList[] = { 1,3,4,8,13,16,20, 21, 24, 31};
         se.createSeregenttiSubFoodweb(fwName, nodeList, true);
         
     }
     
     public void createLevel3FW_2(SimulationEngine se)
     {
         String fwName = "Serengeti_level3_Foodweb_2";
         int nodeList[] = { 1,2,3,4,5,8,13,14,15,16,17,20, 21, 24, 25,31,33,34,28,42,44};
         String networkId =  se.createSeregenttiSubFoodweb(fwName, nodeList, true);
         se.run(0, 300, networkId, true);
         
     }     
     
     
     public void nodeInfoTest(SimulationEngine se)
     {
         try
         {
            NetworkInfoRequest nir = new NetworkInfoRequest();
            String keyword = "Serengeti";
            nir.setTextSearch(true);
            nir.setTextSearchMode(0);
			
            Object[] sps = new Object[1];
            sps[0] = keyword;
//			nir.setWhereClause("name == @0");
//            nir.setSearchParameters(sps);
            nir.setWhereClause(keyword);
            
            
		
            NetworkInfoResponse ns = (NetworkInfoResponse)se.getN3DService().executeRequest(nir);         
			String errMsg = ns.getMessage();
			if(errMsg != null)
				System.out.print("msg:"+errMsg);
			NetworkInfo[] nets = ns.getNetworkInfo();
			for(NetworkInfo net : nets)
			{
				System.out.print("node:"+net.getNetworkName());
			}
//         NodeInfoRequest nir = new NodeInfoRequest();
         }
	catch(Exception e)
	{
            System.out.println("error:"+e.getMessage());			
	}       
         
     }
     
     public void testMay24_1(SimulationEngine se)
     {
           int nodeList[] = {4,73,80};
            int halfSDtoPlant = 200;
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "testMay24_1", 0, 1, true);
                    
           List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(1);
            node.setHasLinks(false);
            nodes.add(node);
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(0.5);
            node.setHasLinks(false);
            nodes.add(node);
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(0.01);
            node.setHasLinks(false);
            nodes.add(node);            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            
//            se.setNodeParameter(4, ManipulatingParameterName.x.getManipulatingParameterIndex(), 4000, 1, sParams);           
            se.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.01, 1, sParams);           
            se.setNodeParameter(80, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.01, 1, sParams);                       
            se.updateSystemParameters(1, false, manpId, sParams, nodes);
            se.run(2, 400, manpId);
            se.saveBiomassCSVFile(manpId);
            
       
     }
     
     
    public void testMay26_1(SimulationEngine se)
     {
           int nodeList[] = {34,10,11,13,14,15};
            int halfSDtoPlant = 200;
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "testMay26_1", 0, 1, true);
                    
           List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(15);
            node.setBeginingBiomass(1);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(se.getProperties().getProperty("serengetiNetworkId"));            
            nodes.add(node);             

            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(14, 1, ManipulatingParameterName.b0.getManipulatingParameterIndex(), halfSDtoPlant, 6, sParams);            
            se.updateSystemParameters(1, false, manpId, sParams, nodes);                          
            
//            se.setNodeParameter(4, ManipulatingParameterName.x.getManipulatingParameterIndex(), 4000, 1, sParams);           
//            se.setNodeParameter(14, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.91, 1, sParams);           
//            se.setNodeParameter(20, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.9, 1, sParams);                       
//            se.updateSystemParameters(1, false, manpId, sParams, nodes);
            se.run(2, 10, manpId);
            se.saveBiomassCSVFile(manpId);
            
       
     }     
     
    public void testJun3(SimulationEngine se)
     {
           int nodeList[] = {34,10,11,13,14,15};
            int halfSDtoPlant = 200;
            String manpId = se.createAndRunSeregenttiSubFoodweb(nodeList, "testJun3", 0, 1, true);
                    
           List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();

            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            se.setLinkParameter(34, 10, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.6, 6, sParams);            
            se.setLinkParameter(34, 11, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.1, 6, sParams);            
            se.setLinkParameter(34, 13, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.1, 6, sParams);            
            se.setLinkParameter(34, 14, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.1, 6, sParams);                        
            se.setLinkParameter(34, 15, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.1, 6, sParams);                        
            se.updateSystemParameters(1, false, manpId, sParams, nodes);                          
            
            se.run(2, 10, manpId);
            se.saveBiomassCSVFile(manpId);
            
       
     }     
     
     
     
	public static void main(String args[]) 
	{
            
                System.out.println("simulation engine starts");
                
//               SimulationEngine se = new SimulationEngine("http://54050601f7a9427285bd6fcfd56f8679.cloudapp.net/N3DWebService.svc?wsdl");       
//                SimulationEngine se = new SimulationEngine("http://127.0.0.1:81/N3DWebService.svc?wsdl");   
		SimulationEngine se = new SimulationEngine();
               
//                SimulationEngine se = new SimulationEngine("http://localhost:41246/N3DWebService.svc?wsdl");
                SimulationEngineTest ts =  new SimulationEngineTest();
                ts.testJun3(se);
//                ts.testMay26_1(se);
//                ts.createLevel3FW_2(se);
/*               
                ts.testGetBiomass(se, "WoB-BiomassT01");
                ts.testGetBiomass(se, "WoB-BiomassT02");
                ts.testGetBiomass(se, "WoB-BiomassT03");
                ts.testGetBiomass(se, "WoB-BiomassT04");
                ts.testGetBiomass(se, "WoB-BiomassT05");
*/ 
//                se.saveBiomassCSVFile("C5C142D1-F3CD-4A5C-9E98-A9B0BF7A04B1");
//		SimulationEngine se = new SimulationEngine("http://localhost:41246/N3DWebService.svc?wsdl");
//                SimulationEngine se = new SimulationEngine("http://127.0.0.1:81/N3DWebService.svc?wsdl");                
//                se.runManipulationTest("20a2ad49-11a4-49f2-91c8-41a5cfe764e4",3,5);
//                se.getBiomassInfo("e5ff191e-d8f8-4a87-b385-085812116724");
//                SimulationEngine se = new SimulationEngine();                

//                test.foodwebStabilityTest10_7(se);
                
                
                
//               SimulationEngineTest test = new SimulationEngineTest();                
//                test.testInsectFoodweb4(se);
//                test.testNode4Oribi(se);
//                ts.masterTestFunction("http://127.0.0.1:81/N3DWebService.svc?wsdl");                                
//                test.masterTestFunction("http://localhost:41246/N3DWebService.svc?wsdl");
//                ts.masterTestFunction("http://54050601f7a9427285bd6fcfd56f8679.cloudapp.net/N3DWebService.svc?wsdl");
//                test.masterTestFunction("http://54050601f7a9427285bd6fcfd56f8679.cloudapp.net/N3DWebService.svc?wsdl");
//                ts.masterTestFunction("http://n3dwebservice.cloudapp.net/N3DWebService.svc?wsdl");                
                
//                String manpl = test.foodwebStabilityTest10_7(se);
//                String manpl = test.foodwebStabilityTest_4species_x73_08(se);
//                String manpl = test.foodwebStabilityTest_4species_x73_80_08(se);
//                String manpl = test.foodwebStabilityTest_4species_x73_02_80_02(se);
//                String manpl = test.foodwebStabilityTest_4species_4_R_08(se);
//                String manpl = test.foodwebStabilityTest_4species_73_4_5_PD_05(se);
//                test.testManipulationParameterInfoReqest(se);
//                se.saveBiomassCSVFile(manpl);
//                se.deleteManipulation(manpl);

        
        }
    
}
