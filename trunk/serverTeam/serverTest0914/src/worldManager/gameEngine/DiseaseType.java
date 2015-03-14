package worldManager.gameEngine;

import dataAccessLayer.DiseaseTypeDAO;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Nathan Greco
 */
public class DiseaseType {

    private int diseaseTypeID;
    private String diseaseType;
    private String description;
    private float infectChance;
    private float spreadChance;
    private ArrayList<Integer> infectSpecies;
    private float deathRate;
    private float healChance;

    public DiseaseType(String disease) {
        //for given disease, gather info from DB:
        //diseaseType (name)
        //description
        //infectChance (0-1)
        //spreadChance (0-1)
        //infectSpecies (array of species that CAN be infected)
        //deathRate (0-1)
        //healChance (0-1)

        try {
            DiseaseTypeDAO.doBusiness(this);
        } catch (SQLException ex) {
            Logger.getLogger(DiseaseType.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void run() {
    }

    public int getDiseaseTypeID() {
        return this.diseaseTypeID;
    }

    public String getDiseaseType() {
        return this.diseaseType;
    }

    public String getDescription() {
        return this.description;
    }

    public float getInfectChance() {
        return this.infectChance;
    }

    public float getSpreadChance() {
        return this.spreadChance;
    }

    public ArrayList<Integer> getInfectSpecies() {
        return this.infectSpecies;
    }

    public float getDeathRate() {
        return this.deathRate;
    }

    public float getHealChance() {
        return this.healChance;
    }

    public void setDeathRate(float deathRate) {
        this.deathRate = deathRate;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setDiseaseType(String diseaseType) {
        this.diseaseType = diseaseType;
    }

    public void setHealChance(float healChance) {
        this.healChance = healChance;
    }

    public void setInfectChance(float infectChance) {
        this.infectChance = infectChance;
    }

    public void setInfectSpecies(ArrayList<Integer> infectSpecies) {
        this.infectSpecies = infectSpecies;
    }

    public void setSpreadChance(float spreadChance) {
        this.spreadChance = spreadChance;
    }
}
