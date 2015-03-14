package model;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

/**
 *
 * @author Gary
 */
public abstract class SpeciesType {

    protected int species_id;
    protected String type;
    protected String species_name;
    protected int cost;
    protected String description;
    protected double biomass;
    protected int waterBiomassLoss;
    protected int waterNeedFrequency;
    protected float growthRate;
    protected float healChance;
    protected int model_id;
    protected float carrying_capacity;
    protected String category;
    protected int[] nodeList;
    protected float trophic_level;
    protected int group_type;
    protected int group_capacity;
    protected HashMap<Integer, HashMap<Integer, SpeciesType>> predatorList;
    protected HashMap<Integer, HashMap<Integer, SpeciesType>> preyList;
    protected HashMap<Integer, Integer> nodeAmountList;

    public SpeciesType() {
        group_type = -1;

        nodeList = new int[]{0};
        predatorList = new HashMap<Integer, HashMap<Integer, SpeciesType>>();
        preyList = new HashMap<Integer, HashMap<Integer, SpeciesType>>();
        nodeAmountList = new HashMap<Integer, Integer>();
    }

    public int getID() {
        return species_id;
    }

    public int setID(int species_id) {
        return this.species_id = species_id;
    }

    public String getType() {
        return species_name;
    }

    public String setType(String species_name) {
        return this.species_name = species_name;
    }

    public String getSpeciesName() {
        return species_name;
    }

    public String setSpeciesName(String speciesName) {
        return this.species_name = speciesName;
    }

    public int getCost() {
        return cost;
    }

    public int setCost(int cost) {
        return this.cost = cost;
    }

    public String getDescription() {
        return description;
    }

    public String setDescription(String description) {
        return this.description = description;
    }
    
    public String getCategory() {
        return category;
    }
    
    public String setCategory(String category) {
        return this.category = category;
    }

    public double getAvgBiomass() {
        return biomass;
    }

    public double setAvgBiomass(double biomass) {
        return this.biomass = biomass;
    }

    public int getWaterBiomassLoss() {
        return waterBiomassLoss;
    }

    public int setWaterBiomassLoss(int waterBiomassLoss) {
        return this.waterBiomassLoss = waterBiomassLoss;
    }

    public int getWaterNeedFrequency() {
        return waterNeedFrequency;
    }

    public int setWaterNeedFrequency(int waterNeedFrequency) {
        return this.waterNeedFrequency = waterNeedFrequency;
    }

    public float getGrowthRate() {
        return growthRate;
    }

    public float setGrowthRate(float growthRate) {
        return this.growthRate = growthRate;
    }

    public float getHealChance() {
        return healChance;
    }

    public float setHealChance(float healChance) {
        return this.healChance = healChance;
    }

    public int getModelID() {
        return model_id;
    }

    public int setModelID(int model_id) {
        return this.model_id = model_id;
    }

    public float getCarryingCapacity() {
        return carrying_capacity;
    }

    public float setCarryingCapacity(float carrying_capacity) {
        return this.carrying_capacity = carrying_capacity;
    }

    public int[] getNodeList() {
        return nodeList;
    }

    public boolean hasNodeID(int node_id) {
        return Arrays.binarySearch(nodeList, node_id) >= 0;
    }

    public boolean equalsNodeList(int[] nodeList) {
        Arrays.sort(nodeList);
        return Arrays.equals(nodeList, this.nodeList);
    }

    public int[] setNodeList(int[] nodeList) {
        Arrays.sort(nodeList);
        return this.nodeList = nodeList;
    }
    
    public int getNodeAmount(int node_id) {
        return nodeAmountList.get(node_id);
    }
    
    public HashMap<Integer, Integer> getNodeAmountList() {
        return nodeAmountList;
    }
    
    public HashMap<Integer, Integer> setNodeAmountList(HashMap<Integer, Integer> nodeAmountList) {
        return this.nodeAmountList = nodeAmountList;
    }

    public float getTrophicLevel() {
        return trophic_level;
    }

    public float setTrophicLevel(float trophic_level) {
        return this.trophic_level = trophic_level;
    }

    public int getGroupType() {
        return group_type;
    }

    public int setGroupType(int group_type) {
        return this.group_type = group_type;
    }
    
    public int getGroupCapacity() {
        return group_capacity;
    }
    
    public int setGroupCapacity(int group_capacity) {
        return this.group_capacity = group_capacity;
    }

    public List<Integer> getPredatorIDs(int group_type) {
        List<Integer> idList = new ArrayList<Integer>();
        HashMap<Integer, SpeciesType> subPredatorList = predatorList.get(group_type);

        if (subPredatorList != null) {
            idList.addAll(subPredatorList.keySet());
        }

        return idList;
    }

    public void addPredatorID(int predator_id, int group_type) {
        HashMap<Integer, SpeciesType> subPredatorList = predatorList.get(group_type);

        if (subPredatorList == null) {
            subPredatorList = new HashMap<Integer, SpeciesType>();
            predatorList.put(group_type, subPredatorList);
        }

        subPredatorList.put(predator_id, null);
    }
    public List<Integer> getPredatorIndex() {
        List<Integer> typeList = new ArrayList<Integer>();
//        for (HashMap<Integer, SpeciesType> subPredatorList : predatorList.values()) {
//        	for(SpeciesType predator :subPredatorList.values()){
//        		int[] nodeList = predator.getNodeList();  
//        		System.out.print(nodeList[0] + " ");
//        	}
//        }
        return typeList;
    }

    public List<Integer> getPreyIndex() {
        List<Integer> typeList = new ArrayList<Integer>();
//        for (HashMap<Integer, SpeciesType> subPreyList : preyList.values()) {
//        	for(SpeciesType predator :subPreyList.values()){
//        		int[] nodeList = predator.getNodeList();  
//        		System.out.print(nodeList[0] + " ");
//        	}
//        }
        return typeList;
    } 
    public List<SpeciesType> getPredatorList(int group_type) {
        List<SpeciesType> typeList = new ArrayList<SpeciesType>();
        HashMap<Integer, SpeciesType> subPredatorList = predatorList.get(group_type);

        if (subPredatorList != null) {
            for (SpeciesType predator : subPredatorList.values()) {
                if (predator != null) {
                    typeList.add(predator);
                }
            }
        }

        return typeList;
    }

    public void resolvePredator(SpeciesType predator) {
        HashMap<Integer, SpeciesType> subPredatorList = predatorList.get(predator.getGroupType());

        if (subPredatorList != null) {
            subPredatorList.put(predator.getID(), predator);
        }
    }

    public List<Integer> getPreyIDs(int group_type) {
        List<Integer> idList = new ArrayList<Integer>();
        HashMap<Integer, SpeciesType> subPreyList = preyList.get(group_type);

        if (subPreyList != null) {
            idList.addAll(subPreyList.keySet());
        }

        return idList;
    }

    public void addPreyID(int prey_id, int group_type) {
        HashMap<Integer, SpeciesType> subPreyList = preyList.get(group_type);

        if (subPreyList == null) {
            subPreyList = new HashMap<Integer, SpeciesType>();
            preyList.put(group_type, subPreyList);
        }

        subPreyList.put(prey_id, null);
    }

    public List<SpeciesType> getPreyList(int group_type) {
        List<SpeciesType> typeList = new ArrayList<SpeciesType>();
        HashMap<Integer, SpeciesType> subPreyList = preyList.get(group_type);

        if (subPreyList != null) {
            for (SpeciesType species : subPreyList.values()) {
                if (species != null) {
                    typeList.add(species);
                }
            }
        }

        return typeList;
    }

    public void resolvePrey(SpeciesType prey) {
        HashMap<Integer, SpeciesType> subPreyList = preyList.get(prey.getGroupType());

        if (subPreyList != null) {
            subPreyList.put(prey.getID(), prey);
        }
    }
}
