/**
 * 
 */
package simulationEngine;

import core.GameServer;
import dataAccessLayer.UserActionsDAO;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Properties;

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
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationParameterInfoRequest;
import org.datacontract.schemas._2004._07.WCFService_Portal.ManipulationParameterInfoResponse;
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
import org.foodwebs.www._2009._11.IN3DService;
import org.foodwebs.www._2009._11.IN3DServiceProxy;

import metadata.Constants;

import model.AnimalType;
import model.SpeciesType;

import simulationEngine.SpeciesZoneType.SpeciesTypeEnum;
import simulationEngine.config.ManipulatingNodePropertyName;
import simulationEngine.config.ManipulatingParameterName;
import simulationEngine.config.ManipulationActionType;
import simulationEngine.config.ModelType;

/**
 * @author Sonal
 * 
 */
public class SimulationEngine {

    private IN3DService svc;
    private User user;
    private Properties propertiesConfig;
    private HashMap<Integer, SpeciesZoneType> mSpecies;

    public static final int SEARCH_MODE = 0;
    public static final int UPDATE_MODE = 1;
    public static final int REMOVE_MODE = 2;
    public static final int INSERT_MODE = 3;
    public static final int REMOVE_ALL_MODE = 6;    
    
    
    
    
    
    public SimulationEngine() {
        IN3DServiceProxy proxy = new IN3DServiceProxy();
        // Read properties file.
        Properties propertiesLogin = new Properties();
        propertiesConfig = new Properties();
        try {
            propertiesLogin.load(new FileInputStream("src/simulationEngine/config/webserviceLogin.properties"));
            user = new User();
            user.setUsername(propertiesLogin.getProperty("username"));
            propertiesConfig.load(new FileInputStream("src/simulationEngine/config/SimulationEngineConfig.properties"));
            proxy.setEndpoint(propertiesConfig.getProperty("wsdlurl"));
//            proxy.setEndpoint(propertiesConfig.getProperty("stagingurl"));            
//            proxy.setEndpoint(propertiesConfig.getProperty("devurl"));                        
            svc = proxy.getIN3DService();
        } catch (IOException e) {
            e.printStackTrace();
        }

        mSpecies = new HashMap<Integer, SpeciesZoneType>();
    }

    
   public SimulationEngine(String url) {
        IN3DServiceProxy proxy = new IN3DServiceProxy();
        // Read properties file.
        Properties propertiesLogin = new Properties();
        propertiesConfig = new Properties();
        try {
            propertiesLogin.load(new FileInputStream("src/simulationEngine/config/webserviceLogin.properties"));
            user = new User();
            user.setUsername(propertiesLogin.getProperty("username"));
            propertiesConfig.load(new FileInputStream("src/simulationEngine/config/SimulationEngineConfig.properties"));
            proxy.setEndpoint(url);
            System.err.println("web service url for SimulationEngine:"+url);
//            proxy.setEndpoint(propertiesConfig.getProperty("stagingurl"));            
//            proxy.setEndpoint(propertiesConfig.getProperty("devurl"));                        
            svc = proxy.getIN3DService();
        } catch (IOException e) {
            e.printStackTrace();
        }

        mSpecies = new HashMap<Integer, SpeciesZoneType>();
    }    
    
    public HashMap<Integer, SpeciesZoneType> getSpecies() {
        return mSpecies;
    }
    
    public void logTime(String string) {
        if (true) {
            System.out.println(string);
        }
    }

    public String createSeregenttiSubFoodweb(String networkName, int nodeList[], boolean overwrite)
    {
        String netId = null;
        
        ModelParam[] networkParams = new ModelParam[2];
        networkParams[0] = new ModelParam();
        networkParams[0].setParamName(ManipulatingNodePropertyName.Connectance.name());
        networkParams[0].setParamValue(Double.valueOf(propertiesConfig.getProperty("connectanceDefault")));
        networkParams[1] = new ModelParam();
        networkParams[1].setParamName(ManipulatingNodePropertyName.SpeciesCount.name());
        networkParams[1].setParamValue(Integer.valueOf(propertiesConfig.getProperty("speciesCountDefault")));

        NetworkCreationRequest req = new NetworkCreationRequest();
        req.setUser(user); // Owner of network
        req.setNetworkName(networkName); // Name of network -> username_worldname_zoneid
        req.setModelType(ModelType.CASCADE_MODEL.getModelType());
        req.setModelParams(networkParams);
        req.setCreationType(1); // sub food web
        req.setOriginFoodweb(propertiesConfig.getProperty("serengetiNetworkId")); // Serengeti
        req.setNodeList(nodeList);
        req.setOverwrite(overwrite);
        
        CreateFoodwebResponse response = null;
        try {
            response = (CreateFoodwebResponse) svc.executeNetworkCreationRequest(req);
            netId = response.getNetworkId();
            //TODO: Write web service call to database
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        
        String errorMsg = response.getMessage();
        if (errorMsg != null)
        {
            System.err.println("Error type: " + response.getErrorType() + "  error msg:" + errorMsg);
            return null;
        }
        
        return netId;
    }

    public Properties getProperties()
    {
        return propertiesConfig;
    }
    public ManipulationResponse createDefaultSubFoodweb(String networkName) {
        ModelParam[] networkParams = new ModelParam[2];
        networkParams[0] = new ModelParam();
        networkParams[0].setParamName(ManipulatingNodePropertyName.Connectance.name());
        networkParams[0].setParamValue(Double.valueOf(propertiesConfig.getProperty("connectanceDefault")));
        networkParams[1] = new ModelParam();
        networkParams[1].setParamName(ManipulatingNodePropertyName.SpeciesCount.name());
        networkParams[1].setParamValue(Integer.valueOf(propertiesConfig.getProperty("speciesCountDefault")));

        NetworkCreationRequest req = new NetworkCreationRequest();
        req.setUser(user); // Owner of network
        req.setNetworkName(networkName); // Name of network -> username_worldname_zoneid
        req.setModelType(ModelType.CASCADE_MODEL.getModelType());
        req.setModelParams(networkParams);
        req.setCreationType(1); // sub food web
        req.setOriginFoodweb(propertiesConfig.getProperty("serengetiNetworkId")); // Serengeti
        int nodeList[] = {Integer.valueOf(propertiesConfig.getProperty("defaultSpecies1Id")), Integer.valueOf(propertiesConfig.getProperty("defaultSpecies2Id"))}; // Grass & buffalo
        req.setNodeList(nodeList);

        CreateFoodwebResponse response = null;
        try {
            response = (CreateFoodwebResponse) svc.executeNetworkCreationRequest(req);
            //TODO: Write web service call to database
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        
        String errorMsg = response.getMessage();
        if (errorMsg != null) {
            System.err.println("Error type: " + response.getErrorType() + "  error msg:" + errorMsg);
            return null;
        } else {
            int timestepIdx = 0;
            List<Integer> lPrey = new ArrayList<Integer>();
            List<Integer> lPredator = new ArrayList<Integer>();
            List<SpeciesZoneType> speciesList = new ArrayList<SpeciesZoneType>();
            SpeciesZoneType szt1 = new SpeciesZoneType(propertiesConfig.getProperty("defaultSpecies1Name"), 5, Integer.valueOf(propertiesConfig.getProperty("defaultSpecies1SpeciesCount")), Double.valueOf(propertiesConfig.getProperty("defaultSpecies1PerSpeciesBiomass")), 0.0, SpeciesTypeEnum.PLANT);
            SpeciesZoneType szt2 = new SpeciesZoneType(propertiesConfig.getProperty("defaultSpecies2Name"), 88, Integer.valueOf(propertiesConfig.getProperty("defaultSpecies2SpeciesCount")), Double.valueOf(propertiesConfig.getProperty("defaultSpecies2PerSpeciesBiomass")), 0.0, SpeciesTypeEnum.ANIMAL);
            speciesList.add(szt1);
            speciesList.add(szt2);            
            //Increasing carrying capacity of grass
            ManipulationResponse mResponse = modifyManipulatingParameters(speciesList, timestepIdx , true, response.getNetworkId());
            
            if(mResponse == null)
                return null;
            String manipulationId = mResponse.getManipulationId();
            String oldNetworkId = mResponse.getNetworksId();
//            deleteNetwork(response.getNetworkId()); // deleting old network made by NetworkCreationRequest 
            //Increasing carrying capacity of buffalo
//            mResponse = modifyManipulatingParameters(szt2, timestepIdx, false, manipulationId);
//            deleteNetwork(oldNetworkId);  // deleting old network made by previous manipulation            
            
//            if(mResponse == null)
//                return null;
            
            return mResponse;
        }
    }
    
    
    public void deleteManipulation(String manpId)
    {
        ManipulationDeletion md = new ManipulationDeletion(manpId);  
        md.run();        
    }    
    
    public void deleteNetwork(String networkId)
    {
        NetworkDeletion nd = new NetworkDeletion(networkId);  
        nd.run();        
    }
    
    public class NetworkDeletion implements Runnable
    {

        String _netId;

        public NetworkDeletion(String netId)
        {
            _netId = netId;
        }

        
	public void run()
	{
            try
            {
                NetworkRemoveRequest request = new NetworkRemoveRequest();
                request.setUser(user);
                request.setNetworksIdx(_netId);
                svc.executeRequest(request);
            }
            catch(Exception e)
            {
            
            }
        }        
    }
    
    
    
    public class ManipulationDeletion implements Runnable
    {

        String _manpId;

        public ManipulationDeletion(String manpId)
        {
            _manpId = manpId;
        }

        
	public void run()
	{
            try
            {
                ManipulationInfoRequest request = new ManipulationInfoRequest();
                request.setUser(user);
                request.setManipulationId(_manpId);
                request.setMode(SimulationEngine.REMOVE_ALL_MODE);
                svc.executeRequest(request);            
            }
            catch(Exception e)
            {
                
            }
        }        
    }
    
    
    public ManipulatingParameter[] getSystemParameterInfos(String manpId)
    {
        ManipulationParameterInfoRequest request = new ManipulationParameterInfoRequest();
        request.setUser(user);
        request.setManipulationId((manpId));
        request.setMode(SEARCH_MODE);
        

        ManipulationParameterInfoResponse response = new ManipulationParameterInfoResponse();
        try {
//            response = (ManipulationTimestepInfoResponse) svc.executeRequest(req);
            response = (ManipulationParameterInfoResponse) svc.executeRequest(request);
            //TODO: Write web service call to database
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        String errMsg = response.getMessage();
        if (errMsg != null) {
            System.err.println("Error:" + errMsg);
            return null;
        }
        return response.getManipulationInfos();        
    }
    
    
   public String setNodeParameter(int nodeIdx, int paramIdx, double paramValue, int timestep, List<ManipulatingParameter> sParams )
    {
        ManipulatingParameter param = new ManipulatingParameter();        
        
        if(paramIdx == ManipulatingParameterName.k.getManipulatingParameterIndex())
        {
            if(paramValue <= 0)
                return "Carrying capacity should be bigger than 0";
            param.setParamType(ManipulatingParameterName.k.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.k.name());
            param.setParamIdx(ManipulatingParameterName.k.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setTimestepIdx(timestep);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.x.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Metabolic rate should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.x.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.x.name());
            param.setParamIdx(ManipulatingParameterName.x.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setTimestepIdx(timestep);            
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.r.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Plant growth rate should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.r.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.r.name());
            param.setParamIdx(ManipulatingParameterName.r.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setTimestepIdx(timestep);            
            param.setParamValue(paramValue);            
        }
        else
        {
            return "that type of node parameter is not supported yet";
        }
        
        sParams.add(param);
        
        return null;
    }        
    
    public String setNodeParameter(int nodeIdx, int paramIdx, double paramValue, List<ManipulatingParameter> sParams )
    {
    	System.out.println("SetNodeParameter [nodeIdx]-"+nodeIdx);
        ManipulatingParameter param = new ManipulatingParameter();        
        
        if(paramIdx == ManipulatingParameterName.k.getManipulatingParameterIndex())
        {
            if(paramValue <= 0)
                return "Carrying capacity should be bigger than 0";
            param.setParamType(ManipulatingParameterName.k.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.k.name());
            param.setParamIdx(ManipulatingParameterName.k.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.x.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Metabolic rate should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.x.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.x.name());
            param.setParamIdx(ManipulatingParameterName.x.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.r.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Plant growth rate should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.r.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.r.name());
            param.setParamIdx(ManipulatingParameterName.r.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }
        else
        {
            return "that type of node parameter is not supported yet";
        }
        
        sParams.add(param);
        
        return null;
    }
    

//HJR
    public String setFunctionalNodeParameter(int nodeIdx, int preyIdx, int paramIdx, double paramValue, List<ManipulatingParameter> sParams ,SpeciesZoneType szt)
    {
        ManipulatingParameter param = new ManipulatingParameter();        
        List<Integer> predatorIndex = szt.getlPredatorIndex();
        List<Integer> preyIndex = szt.getlPreyIndex();
        if(paramIdx == ManipulatingParameterName.x.getManipulatingParameterIndex())
        {
            if(paramValue <= 0)
                return "Metabolic Rate for Plants should be bigger than 0";
            param.setParamType(ManipulatingParameterName.x.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.x.name());
            param.setParamIdx(ManipulatingParameterName.x.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.ax.getManipulatingParameterIndex())
        {
            if(paramValue <= 0)
                return "Metabolic Rate for Animals should be bigger than 0";
            param.setParamType(ManipulatingParameterName.ax.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.ax.name());
            param.setParamIdx(ManipulatingParameterName.ax.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.e.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Assimilation Efficiency should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.e.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.e.name());
            param.setParamIdx(ManipulatingParameterName.e.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setPreyIdx(preyIdx);
            param.setPredIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.d.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Predator Interference should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.d.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.d.name());
            param.setParamIdx(ManipulatingParameterName.d.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setPreyIdx(preyIdx);
            param.setPredIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.q.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Functional Response Control should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.q.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.q.name());
            param.setParamIdx(ManipulatingParameterName.q.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setPreyIdx(preyIdx);
            param.setPredIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.a.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Relative Half Saturation Density should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.a.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.a.name());
            param.setParamIdx(ManipulatingParameterName.a.getManipulatingParameterIndex());            
            param.setNodeIdx(nodeIdx);
            param.setPreyIdx(preyIdx);
            param.setPredIdx(nodeIdx);
            param.setParamValue(paramValue);            
        }        
        else
        {
            return "that type of node parameter is not supported yet";
        }
        
        sParams.add(param);
        
        return null;
    }
    public String setLinkParameter(int predIdx, int preyIdx, int paramIdx, double paramValue, List<ManipulatingParameter> sParams )
    {
        ManipulatingParameter param = new ManipulatingParameter();        
        
        if(paramIdx == ManipulatingParameterName.e.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Assimilation efficiency rate should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.e.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.e.name());
            param.setParamIdx(ManipulatingParameterName.e.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.a.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Relative Half Saturation Density should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.a.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.a.name());
            param.setParamIdx(ManipulatingParameterName.a.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
        }
       else if(paramIdx == ManipulatingParameterName.q.getManipulatingParameterIndex())
        {
            param.setParamType(ManipulatingParameterName.q.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.q.name());
            param.setParamIdx(ManipulatingParameterName.q.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.d.getManipulatingParameterIndex())
        {
            param.setParamType(ManipulatingParameterName.d.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.d.name());
            param.setParamIdx(ManipulatingParameterName.d.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.b0.getManipulatingParameterIndex())
        {
            param.setParamType(ManipulatingParameterName.b0.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.b0.name());
            param.setParamIdx(ManipulatingParameterName.b0.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
        }        
        
        else
        {
            return "that type of link parameter is not supported yet";
        }
        
        sParams.add(param);
        
        return null;
    }    
    
   public String setLinkParameter(int predIdx, int preyIdx, int paramIdx, double paramValue, int tsIdx, List<ManipulatingParameter> sParams )
    {
        ManipulatingParameter param = new ManipulatingParameter();        
        
        if(paramIdx == ManipulatingParameterName.e.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Assimilation efficiency rate should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.e.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.e.name());
            param.setParamIdx(ManipulatingParameterName.e.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setTimestepIdx(tsIdx);
            param.setParamValue(paramValue);            
        }
        else if(paramIdx == ManipulatingParameterName.a.getManipulatingParameterIndex())
        {
            if(paramValue < 0 || paramValue > 1)
                return "Relative Half Saturation Density should be between 0 and 1";
            param.setParamType(ManipulatingParameterName.a.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.a.name());
            param.setParamIdx(ManipulatingParameterName.a.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
            param.setTimestepIdx(tsIdx);            
        }
        else if(paramIdx == ManipulatingParameterName.q.getManipulatingParameterIndex())
        {
            param.setParamType(ManipulatingParameterName.q.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.q.name());
            param.setParamIdx(ManipulatingParameterName.q.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
            param.setTimestepIdx(tsIdx);            
        }
        else if(paramIdx == ManipulatingParameterName.d.getManipulatingParameterIndex())
        {
            param.setParamType(ManipulatingParameterName.d.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.d.name());
            param.setParamIdx(ManipulatingParameterName.d.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
            param.setTimestepIdx(tsIdx);
        }
        else if(paramIdx == ManipulatingParameterName.b0.getManipulatingParameterIndex())
        {
            param.setParamType(ManipulatingParameterName.b0.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.b0.name());
            param.setParamIdx(ManipulatingParameterName.b0.getManipulatingParameterIndex());            
            param.setPredIdx(predIdx);
            param.setPreyIdx(preyIdx);
            param.setParamValue(paramValue);            
            param.setTimestepIdx(tsIdx);
        }        
        
        else
        {
            return "that type of link parameter is not supported yet";
        }
        
        sParams.add(param);
        
        return null;
    }        
    
    
    private List<ManipulatingParameter> getSystemParameter(SpeciesZoneType species, int timestepIdx)
    {
        
        SpeciesTypeEnum type = species.getType();
        int nodeIdx = species.getNodeIndex();
        
        List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
                
        if(type == SpeciesTypeEnum.PLANT)
        {
            // Carrying capacity(k) and GrowthRate(r) are only effective when species is plant
            // Higher Carrying capacity means higher biomass
            // for example, if carrying capacity is 10, maximum biomass of species is 10.
            // Higher growth rate means that species with higher growth rate will gain biomass faster.
            // Metabolic rate (x) are effective for both animals and plants
            // higher metabolic rate means that biomass of species will decrease compared to other species

            ManipulatingParameter param = new ManipulatingParameter();
            param.setParamType(ManipulatingParameterName.k.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.k.name());
            param.setNodeIdx(nodeIdx);
            param.setParamIdx(ManipulatingParameterName.k.getManipulatingParameterIndex());
               // parameter k, r, x can't have negative value. if they have negative value, it means that data is not assigned yet.)
            double paramKVal = species.getParamK();
            if(paramKVal < 0)
                param.setParamValue(Double.valueOf(propertiesConfig.getProperty("carryingCapacityDefault")));
            else
                param.setParamValue(paramKVal);            

            param.setTimestepIdx(timestepIdx);                    
            sParams.add(param);

            param = new ManipulatingParameter();
            param.setParamType(ManipulatingParameterName.r.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.r.name());
            param.setNodeIdx(nodeIdx);
            param.setParamIdx(ManipulatingParameterName.r.getManipulatingParameterIndex());
            double paramRVal = species.getParamR();
            if(paramRVal < 0)
                param.setParamValue(Double.valueOf(propertiesConfig.getProperty("growthRateDefault")));
            else
                param.setParamValue(paramRVal);                        
            param.setTimestepIdx(timestepIdx);                    
            sParams.add(param);
            
            param = new ManipulatingParameter();
            param.setParamType(ManipulatingParameterName.x.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.x.name());
            param.setNodeIdx(nodeIdx);
            param.setParamIdx(ManipulatingParameterName.x.getManipulatingParameterIndex());
            double paramXVal = species.getParamR();
            if(paramXVal < 0)
                param.setParamValue(Double.valueOf(propertiesConfig.getProperty("metabolicRateDefault")));
            else
                param.setParamValue(paramXVal);            
            param.setTimestepIdx(timestepIdx);                    
            sParams.add(param);            
        }
        else if(type == SpeciesTypeEnum.ANIMAL)
        {

            // Metabolic rate (x) are effective for both animals and plants            
            // higher metabolic rate means that biomass of species will decrease compared to other species            
            // Assimilation efficiency (e) is only available for animals.
            // higher assimilation efficiency means that biomass of species will increase.
            
            ManipulatingParameter param = new ManipulatingParameter();
            param.setParamType(ManipulatingParameterName.x.getManipulatingParameterType());
            param.setParamName(ManipulatingParameterName.x.name());
            param.setNodeIdx(nodeIdx);
            param.setParamIdx(ManipulatingParameterName.x.getManipulatingParameterIndex());
            double paramXVal = species.getParamR();
            if(paramXVal < 0)
                param.setParamValue(Double.valueOf(propertiesConfig.getProperty("metabolicRateDefault")));
            else
                param.setParamValue(paramXVal);            
            param.setTimestepIdx(timestepIdx);                    
            sParams.add(param);
            
            List<Integer> preys = species.getlPreyIndex();
            if(preys != null)
            {
                for(Integer prey: preys)
                {
                    param = new ManipulatingParameter();
                    param.setParamType(ManipulatingParameterName.e.getManipulatingParameterType());
                    param.setParamName(ManipulatingParameterName.e.name());
                    param.setPredIdx(nodeIdx);
                    param.setPreyIdx(prey);
                    param.setParamIdx(ManipulatingParameterName.e.getManipulatingParameterIndex());
                    if(species.getParamE() != null && species.getParamE(prey) != null)
                        param.setParamValue(species.getParamE(prey).getParamValue());                            
                    else
                        param.setParamValue(Double.valueOf(propertiesConfig.getProperty("assimilationEfficiencyDefault")));
                    param.setTimestepIdx(timestepIdx);                    
                    sParams.add(param);
                }

                for(Integer prey: preys)
                {
                    param = new ManipulatingParameter();
                    param.setParamType(ManipulatingParameterName.a.getManipulatingParameterType());
                    param.setParamName(ManipulatingParameterName.a.name());
                    param.setPredIdx(nodeIdx);
                    param.setPreyIdx(prey);
                    param.setParamIdx(ManipulatingParameterName.a.getManipulatingParameterIndex());
                    if(species.getParamA() != null && species.getParamA(prey) != null)
                        param.setParamValue(species.getParamA(prey).getParamValue());                            
                    else
                        param.setParamValue(Double.valueOf(propertiesConfig.getProperty("relativeHalfSaturationDensityDefault")));
                    param.setTimestepIdx(timestepIdx);                    
                    sParams.add(param);
                }
            
                for(Integer prey: preys)
                {
                    param = new ManipulatingParameter();
                    param.setParamType(ManipulatingParameterName.q.getManipulatingParameterType());
                    param.setParamName(ManipulatingParameterName.q.name());
                    param.setPredIdx(nodeIdx);
                    param.setPreyIdx(prey);
                    param.setParamIdx(ManipulatingParameterName.q.getManipulatingParameterIndex());
                    if(species.getParamQ() != null && species.getParamQ(prey) != null)
                        param.setParamValue(species.getParamQ(prey).getParamValue());                            
                    else
                        param.setParamValue(Double.valueOf(propertiesConfig.getProperty("functionalResponseControlParameterDefault")));
                    param.setTimestepIdx(timestepIdx);                    
                    sParams.add(param);
                }            
            
                for(Integer prey: preys)
                {
                    param = new ManipulatingParameter();
                    param.setParamType(ManipulatingParameterName.d.getManipulatingParameterType());
                    param.setParamName(ManipulatingParameterName.d.name());
                    param.setPredIdx(nodeIdx);
                    param.setPreyIdx(prey);
                    param.setParamIdx(ManipulatingParameterName.d.getManipulatingParameterIndex());
                    if(species.getParamD() != null && species.getParamD(prey) != null)
                        param.setParamValue(species.getParamD(prey).getParamValue());                            
                    else
                        param.setParamValue(Double.valueOf(propertiesConfig.getProperty("predatorInterferenceDefault")));
                    param.setTimestepIdx(timestepIdx);                    
                    sParams.add(param);
                }
            }
        }        
        
        return sParams;
    }
    
 
    
    public ManipulatingParameter[] CopySystemParameter(List<ManipulatingParameter> params )
    {
        if(params == null)
            return null;

        ManipulatingParameter[] sysParams = new ManipulatingParameter[params.size()];             
        int idx = 0;
        for(ManipulatingParameter param : params)
        {
            sysParams[idx] = param;
            idx++;
        }
        return sysParams;
    }

    
    public String addMultipleSpeciesType(List<SpeciesZoneType> speciesList, int timestep, boolean isFirstManipulation, String networkOrManipulationId) throws SimulationException {
        long milliseconds = System.currentTimeMillis();
        List<ManipulatingParameter> sysParamList = new ArrayList<ManipulatingParameter>();
        List<ManipulatingNodeProperty> lManipulatingNodeProperty = new ArrayList<ManipulatingNodeProperty>();        
        ManipulatingNode[] nodes = new ManipulatingNode[speciesList.size()];
        int i = 0;
        for(SpeciesZoneType species : speciesList)
        {
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(timestep);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(species.getNodeIndex());
            node.setBeginingBiomass(species.getCurrentBiomass() / Constants.BIOMASS_SCALE);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setNodeName(species.getName()); // set node name            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes[i++] = node;
            
            //Connectance
            ManipulatingNodeProperty mnp = new ManipulatingNodeProperty();
            mnp.setNodeIdx(species.getNodeIndex());            
            mnp.setNodePropertyName(ManipulatingNodePropertyName.Connectance.name());
            mnp.setNodePropertyValue(Double.valueOf(propertiesConfig.getProperty("connectanceDefault")));
            lManipulatingNodeProperty.add(mnp);
            //Probability
            mnp = new ManipulatingNodeProperty();
            mnp.setNodeIdx(species.getNodeIndex());            
            mnp.setNodePropertyName(ManipulatingNodePropertyName.Probability.name());
            mnp.setNodePropertyValue(Double.valueOf(propertiesConfig.getProperty("probabilityDefault"))); // if this value is low, invasion may fail.
            lManipulatingNodeProperty.add(mnp);
            //SpeciesZoneType count
            mnp = new ManipulatingNodeProperty();
            mnp.setNodeIdx(species.getNodeIndex());            
            mnp.setNodePropertyName(ManipulatingNodePropertyName.SpeciesCount.name());
            mnp.setNodePropertyValue(species.getSpeciesCount());
            lManipulatingNodeProperty.add(mnp);
            
            List<ManipulatingParameter> params = this.getSystemParameter(species, timestep);            
            sysParamList.addAll(params);

            System.out.println("Adding: [" + species.getNodeIndex() + "] " + species.getName() + " " + species.getCurrentBiomass() / Constants.BIOMASS_SCALE);
        }
        
        ManipulatingNodeProperty[] nps = (ManipulatingNodeProperty[]) lManipulatingNodeProperty.toArray(new ManipulatingNodeProperty[0]);        
        ManipulatingParameter[] sysParams = CopySystemParameter(sysParamList);        
        
        SimpleManipulationRequest smr = new SimpleManipulationRequest();
        smr.setUser(user);
        smr.setBeginingTimestepIdx(timestep);
        if (isFirstManipulation) {
            smr.setNetworkId(networkOrManipulationId);
        } else {
            smr.setManipulationId(networkOrManipulationId);
        }
        smr.setTimestepsToRun(Integer.valueOf(propertiesConfig.getProperty("timestepsToRunDefault")));
        smr.setManipulationModelNodes(nodes);
        smr.setNodeProperties(nps);
        smr.setSysParams(sysParams);
        smr.setDescription(" " + propertiesConfig.getProperty("addNewSpeciesTypeDescription"));
        smr.setSaveLastTimestepOnly(false);

        ManipulationResponse response = new ManipulationResponse();
        try {
            response = (ManipulationResponse) svc.executeManipulationRequest(smr);
            //TODO: Write web service call to database
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        logTime("Total Time (Add Multiple Species Type): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");
        String errMsg = response.getMessage();
        if (errMsg != null) {
            throw new SimulationException("Error (addMultipleSpeciesType): " + errMsg);
        }
        return response.getManipulationId();
    }    
    
    
    public String addNewSpeciesType(SpeciesZoneType species, int timestep, boolean isFirstManipulation, String networkOrManipulationId) {
        long milliseconds = System.currentTimeMillis();        

        ManipulatingNode node = new ManipulatingNode();
        node.setTimestepIdx(timestep);
        node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
        node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
        node.setNodeIdx(species.getNodeIndex());
        node.setBeginingBiomass(species.getSpeciesCount() * species.getPerSpeciesBiomass()); // biomass = species count * per species biomass
        node.setGameMode(true);
        node.setNodeName(species.getName()); // set node name
        node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));
        ManipulatingNode[] nodes = new ManipulatingNode[1];
        nodes[0] = node;                


        List<ManipulatingNodeProperty> lManipulatingNodeProperty = new ArrayList<ManipulatingNodeProperty>();
        //Connectance
        ManipulatingNodeProperty mnp = new ManipulatingNodeProperty();
        mnp.setNodePropertyName(ManipulatingNodePropertyName.Connectance.name());
        mnp.setNodePropertyValue(Double.valueOf(propertiesConfig.getProperty("connectanceDefault")));
        lManipulatingNodeProperty.add(mnp);
        //Probability
        mnp = new ManipulatingNodeProperty();
        mnp.setNodePropertyName(ManipulatingNodePropertyName.Probability.name());
        mnp.setNodePropertyValue(Double.valueOf(propertiesConfig.getProperty("probabilityDefault"))); // if this value is low, invasion may fail.
        lManipulatingNodeProperty.add(mnp);
        //SpeciesZoneType count
        mnp = new ManipulatingNodeProperty();
        mnp.setNodePropertyName(ManipulatingNodePropertyName.SpeciesCount.name());
        mnp.setNodePropertyValue(species.getSpeciesCount());
        lManipulatingNodeProperty.add(mnp);

        List<ManipulatingParameter> params = this.getSystemParameter(species, timestep);
        
        ManipulatingNodeProperty[] nps = (ManipulatingNodeProperty[]) lManipulatingNodeProperty.toArray(new ManipulatingNodeProperty[0]);        
        ManipulatingParameter[] sysParams = CopySystemParameter(params);        
        
        SimpleManipulationRequest smr = new SimpleManipulationRequest();
        smr.setSaveLastTimestepOnly(true);        
        smr.setUser(user);
        smr.setBeginingTimestepIdx(timestep);
        if (isFirstManipulation) {
            smr.setNetworkId(networkOrManipulationId);
        } else {
            smr.setManipulationId(networkOrManipulationId);
        }
        smr.setTimestepsToRun(Integer.valueOf(propertiesConfig.getProperty("timestepsToRunDefault")));
        smr.setManipulationModelNodes(nodes);
        smr.setNodeProperties(nps);
        smr.setSysParams(sysParams);
        smr.setDescription(species.getName() + " " + propertiesConfig.getProperty("addNewSpeciesTypeDescription"));
        smr.setSaveLastTimestepOnly(false);

        ManipulationResponse response = new ManipulationResponse();
        try {
            response = (ManipulationResponse) svc.executeManipulationRequest(smr);
            //TODO: Write web service call to database
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        String errMsg = response.getMessage();
        if (errMsg != null) {
            System.out.println("Error (addNewSpeciesType): " + errMsg);
            return null;
        } else {
            logTime("Total Time (Add New Species Type): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");
            System.out.println("Adding: [" + species.getNodeIndex() + "] " + species.getName() + " " + species.getCurrentBiomass());
        }
        return response.getManipulationId();
    }

	String addMoreSpeciesOfExistingType(SpeciesZoneType species, int timestep, boolean isFirstManipulation, String networkOrManipulationId)
	{
		ManipulatingNode node = new ManipulatingNode();
		node.setTimestepIdx(timestep); 
		node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
		node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
		node.setNodeIdx(species.getNodeIndex());
		node.setBeginingBiomass(species.getSpeciesCount() * species.getPerSpeciesBiomass()); // biomass = species count * per species biomass
                node.setGameMode(true);
                node.setNodeName(species.getName()); // set node name
                node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));                
                ManipulatingNode[] nodes = new ManipulatingNode[1];
                nodes[0] = node;                

                
		SimpleManipulationRequest smr = new SimpleManipulationRequest();
                smr.setSaveLastTimestepOnly(true);
		smr.setUser(user);
		smr.setBeginingTimestepIdx(timestep);
		if(isFirstManipulation)
			smr.setNetworkId(networkOrManipulationId);
		else
			smr.setManipulationId(networkOrManipulationId);			
		smr.setTimestepsToRun(Integer.valueOf(propertiesConfig.getProperty("timestepsToRunDefault")));
		smr.setManipulationModelNodes(nodes);
		smr.setDescription(species.getSpeciesCount() + " " + propertiesConfig.getProperty("addMoreSpeciesToExistingTypeDescription") + " " + species.getName());

		ManipulationResponse response = null;
		try
		{
			response = (ManipulationResponse) svc.executeManipulationRequest(smr);
			//TODO: Write web service call to database
		}
		catch (RemoteException e)
		{
			e.printStackTrace();
		}
		String errMsg = response.getMessage();
		if (errMsg != null)
		{
			System.err.println("Error:" + errMsg);
			return null;
		}
                
		return response.getManipulationId();
	}

	String reduceSpeciesOfExistingType(SpeciesZoneType species, int timestep, boolean isFirstManipulation, String networkOrManipulationId)
	{
		ManipulatingNode node = new ManipulatingNode();
		node.setTimestepIdx(timestep); 
		node.setManipulationActionType(ManipulationActionType.SPECIES_EXPLOIT.getManipulationActionType()); // exploit
		node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
		node.setNodeIdx(species.getNodeIndex());
		node.setBeginingBiomass(species.getSpeciesCount() * species.getPerSpeciesBiomass()); // biomass = species count * per species biomass
		node.setHasLinks(false);
                ManipulatingNode[] nodes = new ManipulatingNode[1];
                nodes[0] = node;                
                
                
		SimpleManipulationRequest smr = new SimpleManipulationRequest();
                smr.setSaveLastTimestepOnly(true);
		smr.setUser(user);
		smr.setBeginingTimestepIdx(timestep);
		if(isFirstManipulation)
			smr.setNetworkId(networkOrManipulationId);
		else
			smr.setManipulationId(networkOrManipulationId);			
		smr.setTimestepsToRun(Integer.valueOf(propertiesConfig.getProperty("timestepsToRunDefault")));
		smr.setManipulationModelNodes(nodes);
		smr.setDescription(species.getSpeciesCount() + " " + propertiesConfig.getProperty("reduceSpeciesOfExistingTypeDescription") + " " + species.getName());

		ManipulationResponse response = null;
		try
		{
			response = (ManipulationResponse) svc.executeManipulationRequest(smr);
			//TODO: Write web service call to database
		}
		catch (RemoteException e)
		{
			e.printStackTrace();
		}
		String errMsg = response.getMessage();
		if (errMsg != null)
		{
			System.err.println("Error:" + errMsg);
			return null;
		}
		return response.getManipulationId();
	}

	String removeSpeciesType(SpeciesZoneType species, int timestep, boolean isFirstManipulation, String networkOrManipulationId)
	{
		ManipulatingNode node = new ManipulatingNode();
		node.setTimestepIdx(timestep); 
		node.setManipulationActionType(ManipulationActionType.SPECIES_REMOVAL.getManipulationActionType()); // removal
		node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
		node.setNodeIdx(species.getNodeIndex());
		node.setHasLinks(false);
                ManipulatingNode[] nodes = new ManipulatingNode[1];
                nodes[0] = node;                

		SimpleManipulationRequest smr = new SimpleManipulationRequest();
                smr.setSaveLastTimestepOnly(true);
		smr.setUser(user);
		smr.setBeginingTimestepIdx(timestep);
		if(isFirstManipulation)
			smr.setNetworkId(networkOrManipulationId);
		else
			smr.setManipulationId(networkOrManipulationId);			
		smr.setTimestepsToRun(Integer.valueOf(propertiesConfig.getProperty("timestepsToRunDefault")));
		smr.setManipulationModelNodes(nodes);
		smr.setDescription(species.getName() + " " + propertiesConfig.getProperty("removeSpeciesTypeDescription"));

		ManipulationResponse response = null;
		try
		{
			response = (ManipulationResponse) svc.executeManipulationRequest(smr);
			//TODO: Write web service call to database
		}
		catch (RemoteException e)
		{
			e.printStackTrace();
		}
		String errMsg = response.getMessage();
		if (errMsg != null)
		{
			System.err.println("Error:" + errMsg);
			return null;
		}
		return response.getManipulationId();
	}

    public void getBiomass(String manipulationId, int nodeIndex, int timestep) throws SimulationException {
        long milliseconds = System.currentTimeMillis();
        
        if(timestep >= 0)
        {
            ManipulationTimestepInfoRequest req = new ManipulationTimestepInfoRequest();
            req.setManipulationId(manipulationId);
            req.setIsNodeTimestep(true);
            req.setNodeIdx(nodeIndex);
            req.setTimestep(timestep);

            ManipulationTimestepInfoResponse response = null;
            try {
                response = (ManipulationTimestepInfoResponse) svc.executeRequest(req);
            } catch (RemoteException e) {
                throw new SimulationException("Error on running ManipulationTimestepInfoRequest: " + e.getMessage());
            }
            ManipulationTimestepInfo[] infos = response.getManipulationTimestepInfos();
            //TODO: Write web service call to database

            if (infos.length > 0) {
                SpeciesZoneType szt = null;

                for (ManipulationTimestepInfo speciesInfo : infos) {
                    if (speciesInfo.getTimestepIdx() == timestep) {
                        //add new species if not existing
                        SpeciesType speciesType = GameServer.getInstance().getSpeciesTypeByNodeID(speciesInfo.getNodeIdx());

                        double biomass = speciesInfo.getBiomass() * Constants.BIOMASS_SCALE;
                        int count = biomass < 1 ? 0 : (int) Math.ceil(biomass / speciesType.getAvgBiomass());

                        if (!mSpecies.containsKey(speciesInfo.getNodeIdx())) {
                            SpeciesTypeEnum group_type = SpeciesTypeEnum.ANIMAL;
                            if (speciesType.getGroupType() == Constants.ORGANISM_TYPE_PLANT) {
                                group_type = SpeciesTypeEnum.PLANT;
                            }

                            szt = new SpeciesZoneType(speciesInfo.getNodeName(), speciesInfo.getNodeIdx(), count, speciesType.getAvgBiomass(), biomass, group_type);
                            szt.setTrophicLevel(speciesType.getTrophicLevel());

                            //HJR
                            //Added these two lines to pass the prey and predator index to web services
                            szt.setlPredatorIndex(speciesType.getPredatorIndex());
                            szt.setlPreyIndex(speciesType.getPreyIndex());
                            
                            if (group_type == SpeciesTypeEnum.ANIMAL) {
                                szt.setParamX(((AnimalType) speciesType).getMetabolism());
                            }

                            mSpecies.put(speciesInfo.getNodeIdx(), szt);
                        } else { //update existing species current biomass
                            szt = mSpecies.get(speciesInfo.getNodeIdx());

                            szt.setCurrentBiomass(biomass);
                            szt.setSpeciesCount(count);
                        }
                    }
                }
            } else {
                throw new SimulationException("No Species Found!");
            }
        } else {
            throw new SimulationException("Error: Timestep is below 0");
        }

        logTime("Total Time (Get Biomass): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");
    }

 /*   
    public boolean isBiomassConditionOk(NodeBiomass nbs[])
    {
        boolean allzero = true;
        if(nbs == null)
            return false;
        
        for(NodeBiomass nb: nbs)
        {
            if(nb.getBiomass() != 0)
                allzero = false;
        }
    }
   */ 
    public void updateBiomass(String manipulationId, List<NodeBiomass> lNodeBiomass, int timestep) throws SimulationException {
        long milliseconds = System.currentTimeMillis();

        ManipulatingNode node = new ManipulatingNode();
        node.setTimestepIdx(timestep);
        node.setManipulationActionType(ManipulationActionType.MULTIPLE_BIOMASS_UPDATE.getManipulationActionType());
        ManipulatingNode[] nodes = new ManipulatingNode[1];
        nodes[0] = node;
        
        SimpleManipulationRequest smr = new SimpleManipulationRequest();
        smr.setUser(user);
        smr.setBeginingTimestepIdx(timestep);
        smr.setManipulationId(manipulationId);
        smr.setTimestepsToRun(Integer.valueOf(propertiesConfig.getProperty("timestepsToRunDefault")));
        smr.setManipulationModelNodes(nodes);
        NodeBiomass nba[] = (NodeBiomass[]) lNodeBiomass.toArray(new NodeBiomass[0]);
        smr.setNodeBiomasses(nba);
        smr.setDescription(propertiesConfig.getProperty("updateBiomassDescription"));
        smr.setSaveLastTimestepOnly(false);

        ManipulationResponse response = null;
        try {
            response = (ManipulationResponse) svc.executeManipulationRequest(smr);
            //TODO: Write web service call to database
        } catch (Exception e) {
            e.printStackTrace();
        }

        logTime("Total Time (Update Biomass): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");
        String errMsg = response.getMessage();
        if (errMsg != null) {
            throw new SimulationException("Error (updateBiomass): " + errMsg);
        }
    }

    public HashMap<Integer, SpeciesZoneType> getPrediction(HashMap<Integer, Integer> nodeList, String networkOrManipulationId, int currentTimestep) {
        long milliseconds = System.currentTimeMillis();

        System.out.println("Prediction at " + currentTimestep);

        //Get previous timestep biomass for all species from web service
        if (mSpecies.isEmpty()) {
            try {
                getBiomass(networkOrManipulationId, 0, currentTimestep);
            } catch (SimulationException ex) {
                System.out.println(ex.getMessage());
                return null;
            }
        }

        HashMap<Integer, SpeciesZoneType> mNewSpecies = new HashMap<Integer, SpeciesZoneType>();
        HashMap<Integer, SpeciesZoneType> mExistingSpecies = new HashMap<Integer, SpeciesZoneType>();
        HashMap<Integer, SpeciesZoneType> mUpdateSpecies = new HashMap<Integer, SpeciesZoneType>();

        SpeciesZoneType szt = null;

        for (int node_id : nodeList.keySet()) {
            SpeciesType speciesType = GameServer.getInstance().getSpeciesTypeByNodeID(node_id);
            int count = nodeList.get(node_id);

            //NEW SPECIES
            if (!mSpecies.containsKey(node_id)) {
                SpeciesTypeEnum group_type = SpeciesTypeEnum.ANIMAL;
                if (speciesType.getGroupType() == Constants.ORGANISM_TYPE_PLANT) {
                    group_type = SpeciesTypeEnum.PLANT;
                }

                szt = new SpeciesZoneType(speciesType.getType(), node_id, count, speciesType.getAvgBiomass(), speciesType.getAvgBiomass() * count, group_type);
                szt.setTrophicLevel(speciesType.getTrophicLevel());
                //HJR Added these two lines to pass the prey and predator index to web services
                szt.setlPredatorIndex(speciesType.getPredatorIndex());
                szt.setlPreyIndex(speciesType.getPreyIndex());
                
                if (group_type == SpeciesTypeEnum.ANIMAL) {
                    szt.setParamX(((AnimalType) speciesType).getMetabolism());
                }

                mNewSpecies.put(node_id, szt);
            } else {
                szt = mSpecies.get(node_id);
                mExistingSpecies.put(node_id, szt);

                szt.setSpeciesCount(Math.max(0, szt.getSpeciesCount() + count));
                szt.setCurrentBiomass(Math.max(0, szt.getCurrentBiomass() + szt.getPerSpeciesBiomass() * count));

                mUpdateSpecies.put(node_id, szt);
            }
        }
/*
        //Check for species moved from one zone to another
        if (mSpecies.size() > mExistingSpecies.size()) {
            for (int node_id : mSpecies.keySet()) {
                //Species moved from one zone to another
                if (!mExistingSpecies.containsKey(node_id)) {
                    szt = mSpecies.get(node_id);
                    szt.setCurrentBiomass(0);
                    szt.setSpeciesCount(0);

                    mUpdateSpecies.put(node_id, szt);
                }
            }
        }
*/
        for (SpeciesZoneType species : mNewSpecies.values()) {
            List<Integer> lPreyIndex = species.getlPreyIndex();
            List<Integer> lPredatorIndex = species.getlPredatorIndex();

            if (species.getlPrey() != null) {
                //Convert generic prey and predator list fetched to customized prey and predator list with local food web node indexes
                for (SpeciesType st : species.getlPrey()) {
                    for (int node_id : st.getNodeList()) {
                        if (mSpecies.containsKey(node_id) || mNewSpecies.containsKey(node_id)) {
                            lPreyIndex.add(node_id);
                        }
                    }
                }
            }

            if (species.getlPredator() != null) {
                for (SpeciesType st : species.getlPredator()) {
                    for (int node_id : st.getNodeList()) {
                        if (mSpecies.containsKey(node_id) || mNewSpecies.containsKey(node_id)) {
                            lPredatorIndex.add(node_id);
                        }
                    }
                }
            }

            mSpecies.put(species.getNodeIndex(), species);
        }

        if (!mNewSpecies.isEmpty()) {
            try {
                addMultipleSpeciesType(new ArrayList<SpeciesZoneType>(mNewSpecies.values()), currentTimestep, false, networkOrManipulationId);

                for (SpeciesZoneType species : mNewSpecies.values()) {
                    if (species.getType() == SpeciesTypeEnum.ANIMAL) {
                        this.setParameter(currentTimestep, species, networkOrManipulationId, Constants.PARAMETER_X, species.getParamX());
                    }
                }
            } catch (SimulationException ex) {
                System.out.println(ex.getMessage());
            }
        }

        if (!mUpdateSpecies.isEmpty()) {
            List<NodeBiomass> lNodeBiomass = new ArrayList<NodeBiomass>();

            for (SpeciesZoneType s : mUpdateSpecies.values()) {
                System.out.println("Updating Biomass: [" + s.getNodeIndex() + "] " + s.getName() + " " + s.getCurrentBiomass() / Constants.BIOMASS_SCALE);
                lNodeBiomass.add(new NodeBiomass(s.getCurrentBiomass() / Constants.BIOMASS_SCALE, s.getNodeIndex()));
            }

            if (!lNodeBiomass.isEmpty()) {
                try {
                    updateBiomass(networkOrManipulationId, lNodeBiomass, currentTimestep);
                } catch (SimulationException ex) {
                    System.out.println(ex.getMessage());
                }
            }
        }

        run(currentTimestep, 1, networkOrManipulationId);

        // get new predicted biomass
        try {
            getBiomass(networkOrManipulationId, 0, currentTimestep + 1);
        } catch (SimulationException ex) {
            System.out.println(ex.getMessage());
            return null;
        }
//        getBiomassInfo(networkOrManipulationId);

        logTime("Total Time (Get Prediction): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");

        return mSpecies;
    }

    public ManipulationResponse updateSystemParameters(int timestep, boolean isFirstManipulation, String networkOrManipulationId, List<ManipulatingParameter> sysParamList, List<ManipulatingNode> nodes) {
        long milliseconds = System.currentTimeMillis();
        
        SimpleManipulationRequest smr = new SimpleManipulationRequest();
        smr.setUser(user);
        smr.setBeginingTimestepIdx(timestep);
        if (isFirstManipulation) {
            smr.setNetworkId(networkOrManipulationId);
        } else {
            smr.setManipulationId(networkOrManipulationId);
        }
        smr.setTimestepsToRun(Integer.valueOf(propertiesConfig.getProperty("timestepsToRunDefault")));
        if(sysParamList != null)
            smr.setSysParams(CopySystemParameter(sysParamList));                
        else {
            System.out.println("Error (updateSystemParameters): " + "System parameter is null.");
        }
        smr.setDescription( "updateSystemParameters");
        smr.setSaveLastTimestepOnly(false);
        if(nodes != null)
            smr.setManipulationModelNodes(nodes.toArray(new ManipulatingNode[]{} ));

        ManipulationResponse response = null;
        try {
            response = (ManipulationResponse) svc.executeManipulationRequest(smr);
            //TODO: Write web service call to database
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        String errMsg = response.getMessage();
        if (errMsg != null) {
            System.out.println("Error (updateSystemParameters): " + errMsg);
            return null;
        }
        
        System.out.println("Total Time (updateSystemParameters): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");        
        return response;
    }    
    
    
    
    public ManipulationResponse modifyManipulatingParameters(List<SpeciesZoneType> speciesList, int timestep, boolean isFirstManipulation, String networkOrManipulationId) {
        
        List<ManipulatingParameter> sysParamList = new ArrayList<ManipulatingParameter>();
        ManipulatingNode[] nodes = new ManipulatingNode[speciesList.size()];
        int i = 0;
        for(SpeciesZoneType species : speciesList)
        {
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(timestep);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(species.getNodeIndex());
            node.setBeginingBiomass(species.getPerSpeciesBiomass() * species.getSpeciesCount());
            node.setHasLinks(false);
            nodes[i++] = node;
            
            List<ManipulatingParameter> params = this.getSystemParameter(species, timestep);            
            sysParamList.addAll(params);
        }
        
/*        
        //carrying capacity
        ManipulatingParameter[] sysParams = new ManipulatingParameter[1];
        sysParams[0] = new ManipulatingParameter();
        sysParams[0].setParamType(ManipulatingParameterName.k.getManipulatingParameterType());
        sysParams[0].setParamName(ManipulatingParameterName.k.name());
        sysParams[0].setNodeIdx(species.getNodeIndex());
        sysParams[0].setParamIdx(ManipulatingParameterName.k.getManipulatingParameterIndex());
        sysParams[0].setParamValue(Double.valueOf(propertiesConfig.getProperty("carryingCapacityDefault")));
        sysParams[0].setTimestepIdx(timestep);
*/
        

        ManipulatingParameter[] sysParams = CopySystemParameter(sysParamList);                
        
        
        
        
        SimpleManipulationRequest smr = new SimpleManipulationRequest();
        smr.setSaveLastTimestepOnly(true);
        smr.setUser(user);
        smr.setBeginingTimestepIdx(timestep);
        if (isFirstManipulation) {
            smr.setNetworkId(networkOrManipulationId);
        } else {
            smr.setManipulationId(networkOrManipulationId);
        }
        smr.setTimestepsToRun(Integer.valueOf(propertiesConfig.getProperty("timestepsToRunDefault")));
        smr.setManipulationModelNodes(nodes);
        
        smr.setSysParams(sysParams);                
//        smr.setSysParams(this.CopySystemParameter(sParams));        
//        smr.setSysParams((ManipulatingParameter[])sParams.toArray());
        smr.setDescription( " " + propertiesConfig.getProperty("increaseCarryingCapacityDescription") + " " + propertiesConfig.getProperty("carryingCapacityDefault"));
        smr.setSaveLastTimestepOnly(false);

        ManipulationResponse response = null;
        try {
            response = (ManipulationResponse) svc.executeManipulationRequest(smr);
            //TODO: Write web service call to database
        } catch (RemoteException e) {
            e.printStackTrace();
        }
        String errMsg = response.getMessage();
        if (errMsg != null) {
            System.out.println("Error (modifyingManipulatingParameters): " + errMsg);
            return null;
        }
        return response;
    }

    public void setCarryingCapacity(int timestep, int node_id, String manipulation_id, int value) {
        List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
        ManipulatingNode node = new ManipulatingNode();
        node.setTimestepIdx(timestep);
        node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
        node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
        node.setNodeIdx(node_id);
        node.setBeginingBiomass(2000);
        node.setHasLinks(false);
        nodes.add(node);

        List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
        setNodeParameter(node_id, ManipulatingParameterName.k.getManipulatingParameterIndex(), value, sParams);

        updateSystemParameters(timestep, false, manipulation_id, sParams, nodes);
    }
    
    public void setParameter(int timestep, SpeciesZoneType species, String manipulation_id, short parameter, double value) {
        List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
        ManipulatingNode node = new ManipulatingNode();
        node.setTimestepIdx(timestep);
        node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
        node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
        node.setNodeIdx(species.getNodeIndex());
        node.setBeginingBiomass(species.getCurrentBiomass() / Constants.BIOMASS_SCALE);
        node.setHasLinks(false);
        nodes.add(node);

        List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();

        if (parameter == Constants.PARAMETER_X) {
            setNodeParameter(species.getNodeIndex(), ManipulatingParameterName.x.getManipulatingParameterIndex(), value, sParams);
        }else if(parameter == Constants.PARAMETER_X_A){
        	setNodeParameter(species.getNodeIndex(), ManipulatingParameterName.ax.getManipulatingParameterIndex(), value, sParams);
        }

        updateSystemParameters(timestep, false, manipulation_id, sParams, nodes);
    }

    public void setParameters(int timestep, String manipulation_id, HashMap<Short, Float> parameterList) {
        for (SpeciesZoneType szt : mSpecies.values()) {
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(timestep);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(szt.getNodeIndex());
            node.setBeginingBiomass(szt.getCurrentBiomass());
            node.setHasLinks(false);
            nodes.add(node);

            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();

            if (szt.getType() == SpeciesTypeEnum.PLANT) {
                setNodeParameter(szt.getNodeIndex(), ManipulatingParameterName.k.getManipulatingParameterIndex(), parameterList.get(Constants.PARAMETER_K), sParams);
                System.out.println("Updating Plant Parameter: [K] " + szt.getName() + parameterList.get(Constants.PARAMETER_K));
                setNodeParameter(szt.getNodeIndex(), ManipulatingParameterName.r.getManipulatingParameterIndex(), parameterList.get(Constants.PARAMETER_R), sParams);
                System.out.println("Updating Plant Parameter: [R] " + szt.getName() + parameterList.get(Constants.PARAMETER_R));
//                setNodeParameter(szt.getNodeIndex(), ManipulatingParameterName.x.getManipulatingParameterIndex(), parameterList.get(Constants.PARAMETER_X), sParams);
//                System.out.println("Updating Plant Parameter: [X] " + parameterList.get(Constants.PARAMETER_X));
            } else if (szt.getType() == SpeciesTypeEnum.ANIMAL) {
//                setNodeParameter(szt.getNodeIndex(), ManipulatingParameterName.x.getManipulatingParameterIndex(), parameterList.get(Constants.PARAMETER_X_A), sParams);
//                System.out.println("Updating Animal Parameter: [X] " + parameterList.get(Constants.PARAMETER_X_A));
            }

            updateSystemParameters(timestep, false, manipulation_id, sParams, nodes);
        }
    }
//HJR
    public void setFunctionalParameters(int timestep, String manipulation_id, HashMap<Short, Float> parametersList, int parameterType, int predatorId) {
    	for (SpeciesZoneType szt : mSpecies.values()) {
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(timestep);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(szt.getNodeIndex());
            node.setBeginingBiomass(szt.getCurrentBiomass());
            node.setHasLinks(false);
            nodes.add(node);

            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            if (szt.getType() == SpeciesTypeEnum.PLANT) {
            	if(parameterType == Constants.PARAMETER_X){
            		Float paramValue = (float) 0;
            		Short nodeIdx = (short) szt.getNodeIndex();
            		if(nodeIdx != 0){
            			paramValue = parametersList.get(nodeIdx);
            			if(paramValue!=0){
            				paramValue = paramValue/100;
            			}
            		}
            		setFunctionalNodeParameter(szt.getNodeIndex(), 0,ManipulatingParameterName.x.getManipulatingParameterIndex(), paramValue, sParams,szt);
	                System.out.println("Updating Plant Parameter: [X] " +  szt.getName() + " NI " + szt.getNodeIndex() + " PV " + paramValue + " PT " + Constants.PARAMETER_X);
            	}
            }
            if (szt.getType() == SpeciesTypeEnum.ANIMAL) {
            	List<Integer> preys = szt.getlPreyIndex();
            	if(preys!=null){
            		if(parameterType == Constants.PARAMETER_X_A){
                		Float paramValue = (float) 0;
                		Short nodeIdx = (short) szt.getNodeIndex();
                		if(nodeIdx != 0){
                			paramValue = parametersList.get(nodeIdx);
                			if(paramValue!=0){
                				paramValue = paramValue/100;
                			}
                		}
			            setFunctionalNodeParameter(szt.getNodeIndex(), 0, ManipulatingParameterName.ax.getManipulatingParameterIndex(), paramValue, sParams,szt);
			            System.out.println("Updating Animal Parameter: [X_A] " +  szt.getName() + " NI " + szt.getNodeIndex() + " PV " + paramValue + " PT " +  Constants.PARAMETER_X_A);
            		}else if(parameterType == Constants.PARAMETER_E){
	            		for(Integer prey: preys){
			                setFunctionalNodeParameter(szt.getNodeIndex(), prey, ManipulatingParameterName.e.getManipulatingParameterIndex(), Constants.PARAMETER_E, sParams,szt);
			                System.out.println("Updating Animal Parameter: [E] " +   szt.getName() + Constants.PARAMETER_E);
	            		}
            		}else if(parameterType == Constants.PARAMETER_D){
	            		for(Integer prey: preys){
			                setFunctionalNodeParameter(szt.getNodeIndex(), prey, ManipulatingParameterName.d.getManipulatingParameterIndex(), Constants.PARAMETER_D, sParams,szt);
			                System.out.println("Updating Animal Parameter: [D] " +   szt.getName() + Constants.PARAMETER_D);
	            		}
            		}else if(parameterType == Constants.PARAMETER_Q){
	            		for(Integer prey: preys){
			                setFunctionalNodeParameter(szt.getNodeIndex(), prey, ManipulatingParameterName.q.getManipulatingParameterIndex(), Constants.PARAMETER_Q, sParams,szt);
			                System.out.println("Updating Animal Parameter: [Q] " +   szt.getName() +  Constants.PARAMETER_Q);
		            	}
            		}else if(parameterType == Constants.PARAMETER_A){
	            		for(Integer prey: preys){
			                setFunctionalNodeParameter(szt.getNodeIndex(), prey, ManipulatingParameterName.a.getManipulatingParameterIndex(), Constants.PARAMETER_A, sParams,szt);
			                System.out.println("Updating Animal Parameter: [A] " +   szt.getName() + Constants.PARAMETER_A);
		            	}
            		}
            	}
            }

            updateSystemParameters(timestep, false, manipulation_id, sParams, nodes);
        }
    }

//    //HJR This is the actual function to be used
//    public void setFunctionalParameters(int timestep, String manipulation_id, HashMap<Short, Float> parametersList, int parameterType, int predatorId) {
//    	for (SpeciesZoneType szt : mSpecies.values()) {
//            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
//            ManipulatingNode node = new ManipulatingNode();
//            node.setTimestepIdx(timestep);
//            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
//            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
//            node.setNodeIdx(szt.getNodeIndex());
//            node.setBeginingBiomass(szt.getCurrentBiomass());
//            node.setHasLinks(false);
//            nodes.add(node);
//
//            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
//            if (szt.getType() == SpeciesTypeEnum.PLANT) {
//            	if(parameterType == Constants.PARAMETER_X){
//            		Float paramValue = (float) 0;
//            		Short nodeIdx = (short) szt.getNodeIndex();
//            		if(nodeIdx != 0){
//            			paramValue = parametersList.get(nodeIdx);
//            			if(paramValue!=0){
//            				paramValue = paramValue/100;
//            			}
//            		}
//            		setFunctionalNodeParameter(szt.getNodeIndex(), 0,ManipulatingParameterName.x.getManipulatingParameterIndex(), paramValue, sParams,szt);
//	                System.out.println("Updating Plant Parameter: [X] " +  szt.getName() + " NI " + szt.getNodeIndex() + " PV " + paramValue + " PT " + Constants.PARAMETER_X);
//            	}
//            }
//            if (szt.getType() == SpeciesTypeEnum.ANIMAL) {
//            		if(parameterType == Constants.PARAMETER_X_A){
//                		Float paramValue = (float) 0;
//                		Short nodeIdx = (short) szt.getNodeIndex();
//                		if(nodeIdx != 0){
//                			paramValue = parametersList.get(nodeIdx);
//                			if(paramValue!=0){
//                				paramValue = paramValue/100;
//                			}
//                		}
//			            setFunctionalNodeParameter(szt.getNodeIndex(), 0, ManipulatingParameterName.ax.getManipulatingParameterIndex(), paramValue, sParams,szt);
//			            System.out.println("Updating Animal Parameter: [X_A] " +  szt.getName() + " NI " + szt.getNodeIndex() + " PV " + paramValue + " PT " +  Constants.PARAMETER_X_A);
//            		}else if(parameterType == Constants.PARAMETER_E){
//            			if( predatorId == szt.getNodeIndex()){
//		            		for(Short prey: parametersList.keySet()){
//		            			Short preyIdx = prey;
//		            			Float paramValue = parametersList.get(preyIdx);
//		            			if(paramValue!=0){
//	                				paramValue = paramValue/100;
//	                			}
//		            			//(int predIdx, int preyIdx, int paramIdx, double paramValue, List<ManipulatingParameter> sParams )
//		            			setLinkParameter(szt.getNodeIndex(), preyIdx, ManipulatingParameterName.e.getManipulatingParameterIndex(), paramValue, sParams);
//				                System.out.println("Updating Animal Parameter: [E] " +  " NI " + szt.getNodeIndex() + " PI " + preyIdx +  " PV " + paramValue + " PT " +  Constants.PARAMETER_E);
//		            		}
//            			}
//            		}else if(parameterType == Constants.PARAMETER_D){
//            			if( predatorId == szt.getNodeIndex()){
//		            		for(Short prey: parametersList.keySet()){
//		            			Short preyIdx = prey;
//		            			Float paramValue = parametersList.get(preyIdx);
//		            			if(paramValue!=0){
//	                				paramValue = paramValue/100;
//	                			}
//		            			setLinkParameter(szt.getNodeIndex(), preyIdx, ManipulatingParameterName.d.getManipulatingParameterIndex(), paramValue, sParams);
//				                System.out.println("Updating Animal Parameter: [D] " +  szt.getName() + " NI " + szt.getNodeIndex() + " PI " + preyIdx +  " PV " + paramValue + " PT " +   Constants.PARAMETER_D);
//		            		}
//            			}
//            		}else if(parameterType == Constants.PARAMETER_Q){
//            			if( predatorId == szt.getNodeIndex()){
//		            		for(Short prey: parametersList.keySet()){
//		            			Short preyIdx = prey;
//		            			Float paramValue = parametersList.get(preyIdx);
//		            			if(paramValue!=0){
//	                				paramValue = paramValue/100;
//	                			}
//		            			setLinkParameter(szt.getNodeIndex(), preyIdx, ManipulatingParameterName.q.getManipulatingParameterIndex(), paramValue, sParams);
//				                System.out.println("Updating Animal Parameter: [Q] " +  szt.getName() + " NI " + szt.getNodeIndex() + " PI " + preyIdx +  " PV " + paramValue + " PT " +   Constants.PARAMETER_Q);
//			            	}
//            			}
//            		}else if(parameterType == Constants.PARAMETER_A){
//            			if( predatorId == szt.getNodeIndex()){
//		            		for(Short prey: parametersList.keySet()){
//		            			Short preyIdx = prey;
//		            			Float paramValue = parametersList.get(preyIdx);
//		            			if(paramValue!=0){
//	                				paramValue = paramValue/100;
//	                			}
//		            			setLinkParameter(szt.getNodeIndex(), prey, ManipulatingParameterName.a.getManipulatingParameterIndex(), paramValue, sParams);
//				                System.out.println("Updating Animal Parameter: [A] " +  szt.getName() + " NI " + szt.getNodeIndex() + " PI " + preyIdx +  " PV " + paramValue + " PT " +   Constants.PARAMETER_A);
//			            	}
//            			}
//            		}
//            	}
//
//            updateSystemParameters(timestep, false, manipulation_id, sParams, nodes);
//        }
//    }
    
    public void getNetworkInfo() {
        try {
            NetworkInfoRequest request = new NetworkInfoRequest();
            request.setUser(user);

            NetworkInfoResponse response = (NetworkInfoResponse) svc.executeRequest(request);
            //TODO: Write web service call to database
            if (response.getMessage() == null) {
                System.out.println("\nNetwork info:");
                NetworkInfo info[] = response.getNetworkInfo();
                for (int i = 0; i < info.length; i++) {
                    System.out.println(info[i].getNetworkName() + " = " + info[i].getNetworkId());
                }
            } else {
                System.out.println("Error: " + response.getMessage());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void getUserManipulations() {
        // list manipulations of user
        try {
            ManipulationInfoRequest req = new ManipulationInfoRequest();
            req.setUser(user);

            ManipulationInfoResponse res = (ManipulationInfoResponse) svc.executeRequest(req);
            //TODO: Write web service call to database
            ManipulationInfo[] infos = res.getManipulationInfos();
            for (int i = 0; i < infos.length; i++) {
                System.out.println("\n\nManipulated network: " + infos[i].getNetworkName() + "\nManipulation id: " + infos[i].getManipulationId());
            }
        } catch (Exception e) {
            System.err.println("Error:" + e.getMessage());
        }
    }

    public void getBiomassInfo(String MANIPULATION_ID) {
        long milliseconds = System.currentTimeMillis();
        
        boolean finished = false;
        int curPage = 1;
        int curTimestep = -1;

        try {
            while (!finished) {
                ManipulationTimestepInfoRequest req = new ManipulationTimestepInfoRequest();
                req.setManipulationId(MANIPULATION_ID);
                req.setIsNodeTimestep(true); // getting node time step
                req.setNodeIdx(0); // set node index to 3
                req.setTimestep(0); // set time step to 5
//                req.setPage(curPage);

                ManipulationTimestepInfoResponse response = (ManipulationTimestepInfoResponse) svc.executeRequest(req);
                ManipulationTimestepInfo[] infos = response.getManipulationTimestepInfos();

                curPage = response.getCurPage();
                if (curPage >= response.getPageAvailable()) {
                    finished = true;
                } else {
                    curPage++;
                }

                for (int i = 0; i < infos.length; i++) {
                    if (infos[i].getTimestepIdx() != curTimestep) {
                        System.out.println("--[" + infos[i].getTimestepIdx() + "]--");
                        curTimestep = infos[i].getTimestepIdx();
                    }

                    System.out.println("Node[" + infos[i].getNodeIdx()
                            + "] + Node name[" + infos[i].getNodeName() + "]:"
                            + infos[i].getBiomass());
                }
            }
        } catch (Exception e) {
            System.out.println("Error (getBiomassInfo): " + e.getMessage());
        }
        
        logTime("Total Time (Get Biomass Info): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");
    }
    
    public void saveBiomassCSVFile(String manipulation_id) {
        String filename = "WoB_Data_" + manipulation_id + ".csv";

        try {
            String biomassCSV = getBiomassCSVString(manipulation_id);

            if (!biomassCSV.isEmpty()) {
                PrintStream p = new PrintStream(new FileOutputStream("E:\\Project\\Beast\\data\\" + filename));
                p.println(biomassCSV);
                p.close();

                System.out.println("Saved CSV to: " + "src/log/" + filename);
            }
        } catch (FileNotFoundException e) {
            System.err.println("Failed to save CSV to: " + "src/log/" + filename);
        }
    }
    
   public void saveBiomassCSVFile(String manipulation_id, String filename) {
        

        try {
            String biomassCSV = getBiomassCSVString(manipulation_id);

            if (!biomassCSV.isEmpty()) {
                PrintStream p = new PrintStream(new FileOutputStream(filename));
                p.println(biomassCSV);
                p.flush();
                p.close();


                System.out.println("Saved CSV to: " + "src/log/" + filename);
            }
        } catch (FileNotFoundException e) {
            System.err.println("Failed to save CSV to: " + "src/log/" + filename);
        }
    }    
    

    public String getBiomassCSVString(String manipulation_id) {
        String biomassCSV = "";
        boolean finished = false;
        int curPage = 1;
        int curTimestep = -1;
        HashMap<String, List<Double>> biomassData = new HashMap<String, List<Double>>();
        int currentDay = 0;

        try {
            while (!finished) {
                ManipulationTimestepInfoRequest req = new ManipulationTimestepInfoRequest();
                req.setManipulationId(manipulation_id);
                req.setIsNodeTimestep(true); // getting node time step
                req.setNodeIdx(0); // set node index to 3
                req.setTimestep(0); // set time step to 5
                req.setPage(curPage);
                
                ManipulationTimestepInfoResponse response = (ManipulationTimestepInfoResponse) svc.executeRequest(req);
                ManipulationTimestepInfo[] infos = response.getManipulationTimestepInfos();
                
                curPage = response.getCurPage();
                if (curPage >= response.getPageAvailable()) {
                    finished = true;
                } else {
                    curPage++;
                }

                for (int i = 0; i < infos.length; i++) {
                    if (infos[i].getTimestepIdx() != curTimestep) {
                        curTimestep = infos[i].getTimestepIdx();
                        currentDay++;
                    }

                    String name = "\"" + infos[i].getNodeName() + " [" + infos[i].getNodeIdx() + "]" + "\"";
                    double biomass = infos[i].getBiomass();
                    
                    if (!biomassData.containsKey(name)) {
                        List<Double> biomassList = new ArrayList<Double>();
                        
                        for (int day = 0; day < curTimestep; day++) {
                            biomassList.add(0.0);
                        }
                        
                        biomassData.put(name, biomassList);
                    }
                    
                    List<Double> biomassList = biomassData.get(name);
                    biomassList.add(biomass);
                }
            }
            
            for (String n : biomassData.keySet()) {
                biomassCSV += "," + n;
            }

            for (int i = 0; i < currentDay; i++) {
                String tempStr = "" + (i + 1);

                for (String name : biomassData.keySet()) {
                    List<Double> biomassList = biomassData.get(name);
                    double biomass = biomassList.get(i);

                    if (i > 0 && biomassList.get(i - 1) > 1.E-15 && biomass <= 1.E-15) {
                        tempStr += ",0";
                    } else if ((i == 0 || (i > 0 && biomassList.get(i - 1) <= 1.E-15)) && biomass <= 1.E-15) {
                        tempStr += ",";
                    } else {
                        tempStr += "," + biomass;
                    }
                }

                biomassCSV += "\n" + tempStr;
            }
        } catch (Exception e) {
            System.out.println("Error (getBiomassCSVString): " + e.getMessage());
        }
        
        return biomassCSV;
    }

    public ManipulationResponse run(int beginingTimestep, int timestepsToRun, String netId, boolean isNetwork) {
        long milliseconds = System.currentTimeMillis();

        SimpleManipulationRequest smr = new SimpleManipulationRequest();
        smr.setUser(user);
        smr.setBeginingTimestepIdx(beginingTimestep);
        if (isNetwork) {
            smr.setNetworkId(netId);
        } else {
            smr.setManipulationId(netId);
        }

//        smr.setManipulationModelNodes(nodes);
        smr.setTimestepsToRun(timestepsToRun);
        smr.setDescription("Serengetti sub foodweb stability test - netId:" + netId);
        smr.setSaveLastTimestepOnly(false);
//        smr.setSysParams(sysParams);

        ManipulationResponse response = null;
        try {
            response = (ManipulationResponse) svc.executeManipulationRequest(smr);
        } catch (RemoteException e) {
            e.printStackTrace();
        }

        logTime("Total Time (Run): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");

        String errMsg = response.getMessage();
        if (errMsg != null) {
            System.out.println("Error (run): " + errMsg);
            return null;
        } else {
            System.out.println("manpId:" + response.getManipulationId());
        }

        return response;
    }

    public void run(int startTimestep, int runTimestep, String manipulationId) {
        long milliseconds = System.currentTimeMillis();
        
        try {
            SimpleManipulationRequest smr = new SimpleManipulationRequest();
            smr.setSaveLastTimestepOnly(true);
            User user = new User();
            user.setUsername("beast");
            smr.setUser(user);
            smr.setBeginingTimestepIdx(startTimestep);
            smr.setTimestepsToRun(runTimestep);
            smr.setManipulationId(manipulationId);
            smr.setSaveLastTimestepOnly(false);

            ManipulationResponse response = (ManipulationResponse) svc.executeManipulationRequest(smr);
            String errMsg = response.getMessage();
            if (errMsg != null) {
                System.out.println("Error (run): " + errMsg);
            } else {
                System.out.println("Manipulation was successfully operated with manipulation id " + response.getManipulationId());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        logTime("Total Time (Run): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");
    }


        
   public HashMap<Integer, SpeciesZoneType> getPredictionTest(SpeciesZoneType species, String networkOrManipulationId, int currentTimestep) {
        //Get previous timestep biomass for all species from web service

        if(species != null)
        {
            String errMsg = addNewSpeciesType(species, currentTimestep, false, networkOrManipulationId);
            if(errMsg == null)
                mSpecies.put(species.getNodeIndex(), species);
        }
        else
            this.run(currentTimestep, 1, networkOrManipulationId, false);
        
//        if (mSpecies.isEmpty()) {
            try {
                getBiomass(networkOrManipulationId, 0, currentTimestep);
            } catch (SimulationException ex) {
                System.out.println(ex.getMessage());
            }
//        }
        
        
        List<NodeBiomass> lNodeBiomass = new ArrayList<NodeBiomass>();


        for (SpeciesZoneType s : mSpecies.values()) {
            s.setBiomassUpdate(false);
            lNodeBiomass.add(new NodeBiomass(s.getCurrentBiomass(), s.getNodeIndex()));
        }
        
        if (!lNodeBiomass.isEmpty()) {
            try {
                updateBiomass(networkOrManipulationId, lNodeBiomass, currentTimestep);
            } catch (SimulationException ex) {
                System.out.println(ex.getMessage());
            }
        }

        // get new predicted biomass
//        getBiomass(networkOrManipulationId, 0, currentTimestep);

        return mSpecies;
    }        
                
        public void getPredictionTest(String foodwebName)
        {
            ManipulationResponse response = this.createDefaultSubFoodweb(foodwebName);            
            String manipulationId = response.getManipulationId();
            String netId = response.getNetworksId();
            
            this.getPredictionTest(null, manipulationId, 1);
            
            SpeciesZoneType szt3 = new SpeciesZoneType("test6", 8, 3, 20, 8.0, SpeciesTypeEnum.ANIMAL);   
            this.getPredictionTest(szt3, manipulationId, 2);            
            
            this.getPredictionTest(null, manipulationId, 3);                        
            
            SpeciesZoneType s = mSpecies.get(5);
            s.setCurrentBiomass(1000.0);
            s = mSpecies.get(88);
            s.setCurrentBiomass(1.0);
            
            SpeciesZoneType szt4 = new SpeciesZoneType("test7", 11, 3, 20, 8.0, SpeciesTypeEnum.ANIMAL);               
            this.getPredictionTest(szt4, manipulationId, 4);                  
            
            getBiomassInfo(manipulationId);
            deleteManipulation(manipulationId);            
            
        }
   
 
        
        public void nodeInfoTest()
        {
            
        	NodeInfoRequest nir = new NodeInfoRequest();
                nir.setUser(user);
                nir.setNetworkId(propertiesConfig.getProperty("serengetiNetworkId"));
                        
            try
            {
		NodeInfoResponse rsps = (NodeInfoResponse)svc.executeRequest(nir);
		
		if(rsps != null)
		{
			NodeInfo[] nodes = rsps.getNodes();
			for(NodeInfo node : nodes)
			{
				System.out.print("node name:"+node.getNodeName());
				System.out.print("  idx:"+node.getNodeIdx());					
				System.out.println("  TL:"+node.getTrophicLevel());					
			}
		}            
           }
           catch(Exception e)
           {
               System.out.println("error:"+ e.getMessage());
           }
        }
	
        
        public String createAndRunSeregenttiSubFoodweb(int nodeList[], String foodwebName, int beginingTimestep,  int timestepsToRun, boolean overwrite)
        {
            long milliseconds = System.currentTimeMillis();

            if(nodeList == null)
                return "nodeList is null";
            String netId = createSeregenttiSubFoodweb(foodwebName, nodeList, overwrite);
            System.out.println("netId:"+ netId);
            ManipulationResponse mr= this.run(beginingTimestep, timestepsToRun, netId, true);
            
//            getBiomassInfo(mr.getManipulationId());
//            deleteManipulation(mr.getManipulationId()); 
            if(mr == null || mr.getMessage() != null)
                return null;
            logTime("Total Time (Create and Run Serengeti Sub-Food Web): " + Math.round((System.currentTimeMillis() - milliseconds) / 10.0) / 100.0 + " seconds");
            return mr.getManipulationId();
        }
        
        public String foodwebStabilityTest10_1_1()
        {
            int nodeList[] = {1,2,3,5,8,9,12,15,20,26};
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test1_2111", 0, 5, true);
            
            
            SpeciesZoneType szt1 = new SpeciesZoneType("", 10, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);
            manpId = this.addNewSpeciesType(szt1, 6, false, manpId);
            if(manpId == null)
                return null;
            szt1 = new SpeciesZoneType("", 11, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);            
            manpId = this.addNewSpeciesType(szt1, 7, false, manpId);            
            if(manpId == null)
                return null;
            szt1 = new SpeciesZoneType("", 13, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);            
            manpId = this.addNewSpeciesType(szt1, 8, false, manpId);            
            if(manpId == null)
                return null;
            szt1 = new SpeciesZoneType("", 14, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);            
            manpId = this.addNewSpeciesType(szt1, 9, false, manpId);            
            if(manpId == null)
                return null;
            szt1 = new SpeciesZoneType("", 16, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);            
            manpId = this.addNewSpeciesType(szt1, 10, false, manpId);            
            if(manpId == null)
                return null;
            
//            getBiomassInfo(manpId);
            return manpId;      
        }
        
        public String foodwebStabilityTest3(String fwname)
        {
            int nodeList[] = {7,33};
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, fwname, 0, 3, true);
            
            List<SpeciesZoneType> spList = new ArrayList<SpeciesZoneType>();
            SpeciesZoneType szt1 = new SpeciesZoneType("", 10, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);
            spList.add(szt1);
            szt1 = new SpeciesZoneType("", 11, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);
            spList.add(szt1);
            szt1 = new SpeciesZoneType("", 12, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);
            spList.add(szt1);

            try {
                this.addMultipleSpeciesType(spList, 3, false, manpId);
            } catch (SimulationException ex) {
                deleteManipulation(manpId);                      
                return "addMultipleSpeciesType failed";
            }

            getBiomassInfo(manpId);
            deleteManipulation(manpId);      
            return null;

          // ran 30 timesteps without any exinction
        }
        
        public void foodwebStabilityTest10_1()
        {
            int nodeList[] = {3, 4, 5, 7, 86, 87, 88, 89, 91, 93};
            // Fruits and nectar, Grains and seeds, Grass and herbs,  Trees and shrubs, Lion, Topi, Buffalo, Southern eland, Nile crocodile, Black Rhinoceros
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test1", 0,  100, true);

            getBiomassInfo(manpId);
            deleteManipulation(manpId);      

            /*
                Node[3] + Node name[Fruits and nectar] +Timestep [98]:0.01977582462131977
                Node[4] + Node name[Grains, seeds] +Timestep [98]:0.01977582462131977
                Node[5] + Node name[Grass and herbs] +Timestep [98]:1.8838178948499262E-4
                Node[7] + Node name[Trees and shrubs] +Timestep [98]:3.52768343873322E-4
                Node[86] + Node name[Lion] +Timestep [98]:0.22752830386161804
                Node[87] + Node name[Topi] +Timestep [98]:3.082611943483471E-11
                Node[88] + Node name[Buffalo] +Timestep [98]:1.1597672822105665E-10
                Node[89] + Node name[Southern eland] +Timestep [98]:0.666655957698822
                Node[91] + Node name[Nile crocodile] +Timestep [98]:9.649700950831175E-5
                Node[93] + Node name[Black rhinoceros] +Timestep [98]:0.17299097776412964            
             */ 
             
          // ran 100 timesteps without any exinction
        }
        
        public void foodwebStabilityTest10_2()
        {
            int nodeList[] = {3, 4, 5, 7, 86, 87, 88, 89, 91, 92};
            // Fruits and nectar, Grains and seeds, Grass and herbs,  Trees and shrubs, Lion, Topi, Buffalo, Southern eland, Nile crocodile, Maasai Giraffe            
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test8", 0, 1, true);
            System.out.println("manpId:"+manpId);
            getBiomassInfo(manpId);
            deleteManipulation(manpId);      
            
          // ran 50 timesteps without any exinction
          /*
            Node[3] + Node name[Fruits and nectar] +Timestep [98]:0.04633544012904167
            Node[4] + Node name[Grains, seeds] +Timestep [98]:0.04633544012904167
            Node[5] + Node name[Grass and herbs] +Timestep [98]:0.008385155349969864
            Node[7] + Node name[Trees and shrubs] +Timestep [98]:1.3869999384041876E-4
            Node[86] + Node name[Lion] +Timestep [98]:0.47203147411346436
            Node[87] + Node name[Topi] +Timestep [98]:2.495455575513006E-8
            Node[88] + Node name[Buffalo] +Timestep [98]:0.004852019250392914
            Node[89] + Node name[Southern eland] +Timestep [98]:0.08423218131065369
            Node[91] + Node name[Nile crocodile] +Timestep [98]:9.602162754163146E-5
            Node[92] + Node name[Maasai giraffe] +Timestep [98]:1.0182245023315772E-4
           */
        }        

        
        public void foodwebStabilityTest10_3()
        {
            int nodeList[] = {3, 4, 5, 7, 86, 87, 88, 89, 91, 94};
            // Fruits and nectar, Grains and seeds, Grass and herbs,  Trees and shrubs, Lion, Topi, Buffalo, Southern eland, Nile crocodile, Hippopotamus      
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test3",0, 1, true);
            
            
            this.getPredictionTest(null, manpId, 1);
            
            
            SpeciesZoneType s = mSpecies.get("Fruits and nectar");
            s.setCurrentBiomass(1000.0);
            s = mSpecies.get("Grains, seeds");
            s.setCurrentBiomass(1000.0);
            s = mSpecies.get("Grass and herbs");            
            s.setCurrentBiomass(1000.0);            
            s = mSpecies.get("Trees and shrubs");            
            s.setCurrentBiomass(1000.0);            
            s = mSpecies.get("Lion");            
            s.setCurrentBiomass(1.0);            
            s = mSpecies.get("Topi");            
            s.setCurrentBiomass(3.0);            
            s = mSpecies.get("Buffalo");            
            s.setCurrentBiomass(30.0);            
            s = mSpecies.get("Southern eland");            
            s.setCurrentBiomass(20.0);            
            s = mSpecies.get("Nile crocodile");            
            s.setCurrentBiomass(2.0);            
            s = mSpecies.get("Hippopotamus");            
            s.setCurrentBiomass(3.0);            
            this.getPredictionTest(null, manpId, 2);          
            this.run(3, 97, manpId, false);
            
            getBiomassInfo(manpId);
            deleteManipulation(manpId);                  
            

            
          // ran 100 timesteps without any exinction
           /*            
            Node[3] + Node name[Fruits and nectar] +Timestep [98]:0.10086638480424881
            Node[4] + Node name[Grains, seeds] +Timestep [98]:0.10086638480424881
            Node[5] + Node name[Grass and herbs] +Timestep [98]:9.615123417461291E-5
            Node[7] + Node name[Trees and shrubs] +Timestep [98]:0.10084232687950134
            Node[86] + Node name[Lion] +Timestep [98]:0.3669547438621521
            Node[87] + Node name[Topi] +Timestep [98]:3.273458730745915E-7
            Node[88] + Node name[Buffalo] +Timestep [98]:1.2872754077963844E-13
            Node[89] + Node name[Southern eland] +Timestep [98]:0.021927716210484505
            Node[91] + Node name[Nile crocodile] +Timestep [98]:9.950158710125834E-5
            Node[94] + Node name[Hippopotamus] +Timestep [98]:8.20449786260724E-5            
           */ 
 
        }        
        
        
 

    public SpeciesZoneType createSpecies(int node_id) {
        SpeciesZoneType szt = null;
        SpeciesType speciesType = GameServer.getInstance().getSpeciesTypeByNodeID(node_id);

        SpeciesTypeEnum group_type = SpeciesTypeEnum.ANIMAL;
        if (speciesType.getGroupType() == Constants.ORGANISM_TYPE_PLANT) {
            group_type = SpeciesTypeEnum.PLANT;
        }

        szt = new SpeciesZoneType(speciesType.getSpeciesName(), node_id, 1, speciesType.getAvgBiomass(), speciesType.getAvgBiomass(), group_type);
        szt.setTrophicLevel(speciesType.getTrophicLevel());

        return szt;
    }

       public String foodwebModelStabilityTest1()
       {
            int nodeList[] = {5, 7, 33, 52, 80, 82, 86, 92, 95};
            // Fruits and nectar, Grains and seeds, Grass and herbs,  Trees and shrubs, Leopard, Lion, Topi, Buffalo, Southern eland, Nile crocodile
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sgModelTest4", 0, 5, true);
            
            List<NodeBiomass> lNodeBiomass = new ArrayList<NodeBiomass>();
            NodeBiomass nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(5);
            lNodeBiomass.add(nb);
            nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(7);
            lNodeBiomass.add(nb);
            nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(33);
            lNodeBiomass.add(nb);
            nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(52);
            lNodeBiomass.add(nb);
            nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(80);
            lNodeBiomass.add(nb);
            nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(82);
            lNodeBiomass.add(nb);
            nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(86);
            lNodeBiomass.add(nb);
            nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(92);
            lNodeBiomass.add(nb);
            nb = new NodeBiomass();
            nb.setBiomass(0);
            nb.setNodeIdx(95);
            lNodeBiomass.add(nb);

            try {
                this.updateBiomass(manpId,lNodeBiomass, 6);
            } catch (SimulationException ex) {
                return null;
            }

            return manpId;
        }        
        
       public String foodwebStabilityTest10_4()
        {
            try
            {
            int nodeList[] = {3, 4, 5, 7, 80, 86, 87, 88, 89, 91};
            // Fruits and nectar, Grains and seeds, Grass and herbs,  Trees and shrubs, Leopard, Lion, Topi, Buffalo, Southern eland, Nile crocodile
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test4",0, 1, true);
            
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(500);
            node.setHasLinks(false);
            nodes.add(node);

            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 1000, sParams);
            this.setLinkParameter(88, 5, ManipulatingParameterName.e.getManipulatingParameterIndex(), 0.8, sParams);
            
            this.updateSystemParameters(1, false, manpId, sParams, nodes);
            
            this.run(2, 5, manpId, false);
            
            return manpId;
            }
            catch(Exception e)
            {
                return null;
            }
        }                
 
       
       public void testManpThread()
       {
           String fwName = "fwManpConcurrentTest";
           int i = 0;
           for(i=0; i<20; i++)
           {
               (new ManplTheadTest(fwName+(i++))).run();
           }
       }
       
      public class ManplTheadTest implements Runnable
       {
           String name = null;
          
           ManplTheadTest(String fwName)
           {
               name = fwName;
           }
       
           public void run()
           {
                try
                {
                    String msg = foodwebStabilityTest3(name);
                    if(msg != null)
                        System.out.println("Concurrent manipulation ["+name+"] failed");
                }
		catch(Exception e)
		{
			System.err.println("Error:"+e.getMessage());
		}		               
               
           }
       
       }       
       
             public void foodwebStabilityTest10_5()
        {
//            int nodeList[] = {3, 4, 5, 7, 80, 86, 87, 88, 89, 91};
            int nodeList[] = { 4, 5, 73 };            
            // Fruits and nectar, Grains and seeds, Grass and herbs,  Trees and shrubs, Leopard, Lion, Topi, Buffalo, Southern eland, Nile crocodile
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(500);
            node.setHasLinks(false);
            nodes.add(node);
            
            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(73);
            node.setBeginingBiomass(80);
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
            node.setBeginingBiomass(30);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 1000, sParams);
            this.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 1000, sParams);            
//            this.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 2, sParams);                        
//            this.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 8, sParams);            
//            this.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.8, sParams);            
//            this.setLinkParameter(88, 5, ManipulatingParameterName.e.getManipulatingParameterIndex(), 0.8, sParams);
            
            this.updateSystemParameters(1, false, manpId, sParams, nodes);
            
//            nodes = new ArrayList<ManipulatingNode>();
//            sParams = new ArrayList<ManipulatingParameter>();
//            this.updateSystemParameters(4, 1, false, manpId, sParams, nodes);            
            
            
            
            
            
            this.run(2, 18, manpId, false);
            
/*            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(11);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(100);
            node.setHasLinks(false);
            nodes.add(node);
            sParams = new ArrayList<ManipulatingParameter>();
  
            this.updateSystemParameters(10, false, manpId, sParams, nodes);            

            this.run(11, 3, manpId, false);
//            sParams = new ArrayList<ManipulatingParameter>();
//            this.setNodeParameter(7, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
//            this.updateSystemParameters(6, false, manpId, sParams, nodes);            
            
            
*/              
            
//          this.run(7, 10, manpId, false);
            
          
            getBiomassInfo(manpId);
            deleteManipulation(manpId);              
          // ran 100 timesteps without any exinction
           /*            
            Node[3] + Node name[Fruits and nectar] +Timestep [98]:0.10086638480424881
            Node[4] + Node name[Grains, seeds] +Timestep [98]:0.10086638480424881
            Node[5] + Node name[Grass and herbs] +Timestep [98]:9.615123417461291E-5
            Node[7] + Node name[Trees and shrubs] +Timestep [98]:0.10084232687950134
            Node[86] + Node name[Lion] +Timestep [98]:0.3669547438621521
            Node[87] + Node name[Topi] +Timestep [98]:3.273458730745915E-7
            Node[88] + Node name[Buffalo] +Timestep [98]:1.2872754077963844E-13
            Node[89] + Node name[Southern eland] +Timestep [98]:0.021927716210484505
            Node[91] + Node name[Nile crocodile] +Timestep [98]:9.950158710125834E-5
            Node[94] + Node name[Hippopotamus] +Timestep [98]:8.20449786260724E-5            
           */ 
 
        }                
             
        public String runningTest()
        {
           int nodeList[] = { 4, 5, 73 };            
            // Fruits and nectar, Grains and seeds, Grass and herbs,  Trees and shrubs, Leopard, Lion, Topi, Buffalo, Southern eland, Nile crocodile
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27111121",0, 1, true);
            for(int i=1; i<15; i++)
            {
                SpeciesZoneType szt = new SpeciesZoneType("", i+7, 1, 1, 1.0, SpeciesTypeEnum.ANIMAL);
                String result  = this.addNewSpeciesType(szt, i, false, manpId);
                if(result == null)
                    return null;
//                this.run(i, 1, manpId);
            }
            return manpId;

        }
 
        public void foodwebStabilityTest10_6()
        {
//            int nodeList[] = {3, 4, 5, 7, 80, 86, 87, 88, 89, 91};
            int nodeList[] = { 4, 5};            
            // Fruits and nectar, Grains and seeds, Grass and herbs,  Trees and shrubs, Leopard, Lion, Topi, Buffalo, Southern eland, Nile crocodile
            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
            System.out.println("manpId:"+manpId);
            
            List<ManipulatingNode> nodes = new ArrayList<ManipulatingNode>();
            ManipulatingNode node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(4);
            node.setBeginingBiomass(500);
            node.setHasLinks(false);
            nodes.add(node);


            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(500);
            node.setHasLinks(false);
            nodes.add(node);
            

            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(30);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);                   
            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 1000, sParams);
            this.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 1000, sParams);            
            
            this.updateSystemParameters(1, false, manpId, sParams, nodes);
            
            this.run(2, 18, manpId, false);
            
          
            getBiomassInfo(manpId);
            deleteManipulation(manpId);              
        }                

        
        
             public void foodwebStabilityTest10_7()
        {

            int nodeList[] = { 4, 5, 73 };            

            String manpId = this.createAndRunSeregenttiSubFoodweb(nodeList, "sg10Test27",0, 1, true);
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
            node.setBeginingBiomass(80);
            node.setHasLinks(false);
            nodes.add(node);            

/*            
            node = new ManipulatingNode();
            node.setTimestepIdx(1);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(80);
            node.setBeginingBiomass(30);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);                   
*/            
            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);
            this.setNodeParameter(4, ManipulatingParameterName.k.getManipulatingParameterIndex(), 8000, sParams);            
            
            this.updateSystemParameters(1, false, manpId, sParams, nodes);
            
            
            this.run(2, 18, manpId, false);
          
            getBiomassInfo(manpId);
            deleteManipulation(manpId);              
 
        }                        
             
             public void runManipulationTest(String manpId, int startTS, int tsToRun)
        {
            this.run(startTS, tsToRun, manpId, false);
            
          
            getBiomassInfo(manpId);
//            deleteManipulation(manpId);              
 
        }                
              
       
   public String getBiomassTest(String manipulationId, int nodeIndex, int timestep) {
       
        if(timestep >= 0)
        {
            ManipulationTimestepInfoRequest req = new ManipulationTimestepInfoRequest();
            req.setManipulationId(manipulationId);
            req.setIsNodeTimestep(true);
            req.setNodeIdx(nodeIndex);
            req.setTimestep(timestep);

            ManipulationTimestepInfoResponse response = null;
            try {
                response = (ManipulationTimestepInfoResponse) svc.executeRequest(req);
            } catch (RemoteException e) {
                e.printStackTrace();
                return "error on running ManipulationTimestepInfoRequest:"+e.getMessage();
            }
            ManipulationTimestepInfo[] infos = response.getManipulationTimestepInfos();
            //TODO: Write web service call to database

            if (infos.length > 0) {
                
                try
                {
                    for(ManipulationTimestepInfo info : infos)
                    {
                        System.out.println( "Node["+info.getNodeIdx()+"]["+info.getNodeName()+"]["+info.getTimestepIdx()+"]:" +info.getBiomass());                        
                    }
  
                }
                catch(Exception e)
                {
                    return "Error on getBiomass :" +e.getMessage();
                }
            } else {
                mSpecies.clear();
            }
        } else {
            return "Error : timestep is below 0";
        }


        return null;
      }       
       
       
       public void testGetBiomass()
       {
           
           
          System.out.println( getBiomassTest("2c13f25d-3733-49a3-bfbf-503f83094778", 0, 37 ));
                
           
       }
       
       public boolean isSameParameter(ManipulatingParameter oParam, ManipulatingParameter dParam)
       {
           if( (oParam.getNodeIdx() == dParam.getNodeIdx() && oParam.getTimestepIdx() == dParam.getTimestepIdx() || 
                   (oParam.getPredIdx() == dParam.getPredIdx() && oParam.getPreyIdx() == dParam.getPreyIdx() ) && oParam.getTimestepIdx() == dParam.getTimestepIdx()  ) )
               
           {
               if(oParam.getParamIdx() == dParam.getParamIdx() && oParam.getParamType() == dParam.getParamType() && oParam.getParamValue() == dParam.getParamValue())
                   return true;
           }
           
           return false;
       }
       
       public boolean testParameters(String manpId, List<ManipulatingParameter> sParams)
       {
           int count = sParams.size();
           int matchCount = 0;
           ManipulatingParameter[] params = this.getSystemParameterInfos(manpId);
//           if(sParams.size() != params.length)
           for( ManipulatingParameter sParam : sParams)
               for(ManipulatingParameter dParam : params)
                   if(this.isSameParameter(sParam, dParam))
                       matchCount++;
           if(matchCount == count)
               return true;
           else
               return false;
       }
       
       public void testNode4Oribi()
        {
            int nodeList[] = {1,9};
            String manpId = createAndRunSeregenttiSubFoodweb(nodeList, "testNode4and73", 0, 1, true);
                    
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
            node.setNodeIdx(9);
            node.setBeginingBiomass(10);
            node.setHasLinks(false);
            nodes.add(node);

            
            List<ManipulatingParameter> sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(1, ManipulatingParameterName.k.getManipulatingParameterIndex(), 4000, sParams);
            this.setNodeParameter(9, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.75, 1, sParams);            
//            this.setNodeParameter(12, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.9, sParams);                        
//            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 5000, sParams);            
//            this.setNodeParameter(4, ManipulatingParameterName.r.getManipulatingParameterIndex(), , sParams);
//            this.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.333, sParams);            

//            this.setLinkParameter(73, 4, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.6, 1, sParams);            
//            this.setLinkParameter(73, 5, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.4, 1, sParams);                        
            updateSystemParameters(1, false, manpId, sParams, nodes);

///            testParameters(manpId, sParams);
//            run(2, 8, manpId, false);                        

           
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(2);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(12);
            node.setBeginingBiomass(10);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(12, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.85, 2, sParams);                        
//            this.setLinkParameter(9, 1, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.05, 1, sParams);            
//            this.setLinkParameter(9, 9, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.3, 1, sParams);                        
//            this.setLinkParameter(9, 12, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.65, 1, sParams);                        
            
//            this.setLinkParameter(73, 4, ManipulatingParameterName.d.getManipulatingParameterIndex(), 1, 3, sParams);
//            this.setNodeParameter(73, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.9, sParams);
//            this.setNodeParameter(5, ManipulatingParameterName.r.getManipulatingParameterIndex(), 0.333, sParams);            
            updateSystemParameters(2, false, manpId, sParams, nodes);   
//            run(3, 27, manpId, false);                          
            

            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(3);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(20);
            node.setBeginingBiomass(4);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             

            node = new ManipulatingNode();
            node.setTimestepIdx(3);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(25);
            node.setBeginingBiomass(5);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            node = new ManipulatingNode();
            node.setTimestepIdx(3);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);            
            
            sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(20, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.65, 3, sParams);              
//            this.setLinkParameter(73, 4, ManipulatingParameterName.a.getManipulatingParameterIndex(), 0.6, 1, sParams);            
            
            updateSystemParameters(3, false, manpId, sParams, nodes);   
//            run(4, 22, manpId, false);                        
            
            
           
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(4);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(75);
            node.setBeginingBiomass(10);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             

            
            node = new ManipulatingNode();
            node.setTimestepIdx(4);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(3000);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            
            
            sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(5, ManipulatingParameterName.k.getManipulatingParameterIndex(), 4000, sParams);            
            this.setNodeParameter(75, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.4, 4, sParams);              
            updateSystemParameters(4, false, manpId, sParams, nodes);   
            

            
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(5);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(57);
            node.setBeginingBiomass(10);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            node = new ManipulatingNode();
            node.setTimestepIdx(5);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);            
            node = new ManipulatingNode();
            node.setTimestepIdx(5);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             

            
            
            sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(57, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.35, 5, sParams);              
            updateSystemParameters(5, false, manpId, sParams, nodes);   
            

            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(6);
            node.setManipulationActionType(ManipulationActionType.SPECIES_INVASION.getManipulationActionType()); // invasion
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(49);
            node.setBeginingBiomass(10);
            node.setHasLinks(false);
            node.setGameMode(true);            
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             

            sParams = new ArrayList<ManipulatingParameter>();
            this.setNodeParameter(49, ManipulatingParameterName.x.getManipulatingParameterIndex(), 0.3, 6, sParams);              
            updateSystemParameters(6, false, manpId, sParams, nodes);   
            
            

            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(7);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);            
            sParams = new ArrayList<ManipulatingParameter>();
            node = new ManipulatingNode();
            node.setTimestepIdx(7);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            
            updateSystemParameters(7, false, manpId, sParams, nodes);   
            

            run(8, 1, manpId, false);
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(9);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);     
            node = new ManipulatingNode();
            node.setTimestepIdx(9);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            updateSystemParameters(9, false, manpId, sParams, nodes);   
            
            
            run(10, 1, manpId, false);
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(11);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);     
            node = new ManipulatingNode();
            node.setTimestepIdx(11);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            updateSystemParameters(11, false, manpId, sParams, nodes);   
            
            
            run(12, 1, manpId, false);
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(13);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);      
            node = new ManipulatingNode();
            node.setTimestepIdx(13);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            updateSystemParameters(13, false, manpId, sParams, nodes);               

            
            run(14, 1, manpId, false);
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(15);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);      
            node = new ManipulatingNode();
            node.setTimestepIdx(15);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            updateSystemParameters(15, false, manpId, sParams, nodes);               

            run(16, 1, manpId, false);
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(17);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);     
            node = new ManipulatingNode();
            node.setTimestepIdx(17);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            updateSystemParameters(17, false, manpId, sParams, nodes);               

            run(18, 1, manpId, false);
            nodes = new ArrayList<ManipulatingNode>();
            node = new ManipulatingNode();
            node.setTimestepIdx(19);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(1);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            nodes.add(node);      
            node = new ManipulatingNode();
            node.setTimestepIdx(19);
            node.setManipulationActionType(ManipulationActionType.SPECIES_PROLIFERATION.getManipulationActionType()); // proliferation
            node.setModelType(ModelType.CASCADE_MODEL.getModelType()); // cascading model
            node.setNodeIdx(5);
            node.setBeginingBiomass(2000);
            node.setHasLinks(false);
            node.setOriginFoodwebId(propertiesConfig.getProperty("serengetiNetworkId"));            
            nodes.add(node);             
            
            sParams = new ArrayList<ManipulatingParameter>();
            updateSystemParameters(19, false, manpId, sParams, nodes);               

            
            
            saveBiomassCSVFile(manpId); 
            getBiomassInfo(manpId);
            deleteManipulation(manpId);                                  
            
        }
               
       
	public static void main(String args[]) throws FileNotFoundException, IOException
	{
            
                System.out.println("simulation engine starts");
                
                
//		SimulationEngine se = new SimulationEngine();
//                SimulationEngine se = new SimulationEngine("http://n3d.cloudapp.net/N3DWebService.svc?wsdl");             
//	    SimulationEngine se = new SimulationEngine("http://localhost:41246/N3DWebService.svc?wsdl");                             
//	    SimulationEngine se = new SimulationEngine("http://127.0.0.1:81/N3DWebService.svc?wsdl");                                         
	    SimulationEngine se = new SimulationEngine("http://54050601f7a9427285bd6fcfd56f8679.cloudapp.net/N3DWebService.svc?wsdl");                                         

                
                se.testNode4Oribi();
//                String manpl = se.foodwebStabilityTest10_1_1();
//                se.deleteManipulation(manpl);                
//                 se.foodwebStabilityTest10_5();
/*                
            String manpId = se.runningTest();
            if(manpId != null)
            {
                se.getBiomassInfo(manpId);
                se.saveBiomassCSVFile(manpId);
                se.deleteManipulation(manpId);
            }
 * 
 */
//                se.getBiomassInfo("BC043271-726E-44D1-AA6A-8BD787002AFD"); 
//                se.SixSpeciesFoodwebTest("aFW105");
//                se.getPredictionTest("abc3");
//                se.foodwebStabilityTest3();
//                se.foodwebStabilityTest10_5();
//                se.foodwebStabilityTest10_7();                
//                se.runManipulationTest("20a2ad49-11a4-49f2-91c8-41a5cfe764e4",3,5);
//                se.testGetBiomass();
//                se.foodwebStabilityTest10_5();
//                se.nodeInfoTest();
//                se.SixSpeciesFoodwebTest("aFoodWeb1000");
	}
}
