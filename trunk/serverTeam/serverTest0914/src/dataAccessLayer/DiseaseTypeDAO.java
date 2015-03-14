package dataAccessLayer;

import java.sql.SQLException;
import java.util.ArrayList;

import worldManager.gameEngine.Disease;
import worldManager.gameEngine.DiseaseType;

/**
 *
 * @author Partap Aujla
 */
public final class DiseaseTypeDAO {

    private DiseaseTypeDAO() {
    }

    /**
     * IMPLEMENTATION STILL INCOMPLETE.  Need to figure out DAO object will come
     * from which needs to be passed through the DAO constructors.  The function
     * does the business related to game logic.
     * @param passedDiseaseType
     * @throws SQLException 
     */
    public static void doBusiness(DiseaseType passedDiseaseType) throws SQLException {
        int disease_id = passedDiseaseType.getDiseaseTypeID();
        Disease holdDisease = new Disease(disease_id);
        //DiseaseDAO dd = new DiseaseDAO();
        //holdDisease = dd.getByDiseaseID(disease_id_pk);
        String diseaseType = holdDisease.getName();
        String description = holdDisease.getDescription();
        float infectChance = holdDisease.getInfectChance();
        float spreadChance = holdDisease.getSpreadChance();
        ArrayList<Integer> infectSpeciesList = new ArrayList<Integer>();
        //DiseaseInfectsAnimalDAO dia = new DiseaseInfectsAnimalDAO();
        //infectSpeciesList = (ArrayList)dia.getAnimalIDByDiseaseID(disease_id_pk);
        float deathRate = holdDisease.getDeathRate();
        float healChance = holdDisease.getHealChance();
        passedDiseaseType.setDiseaseType(diseaseType);
        passedDiseaseType.setDescription(description);
        passedDiseaseType.setInfectChance(infectChance);
        passedDiseaseType.setSpreadChance(spreadChance);
        passedDiseaseType.setInfectSpecies(infectSpeciesList);
        passedDiseaseType.setDeathRate(deathRate);
        passedDiseaseType.setHealChance(healChance);
    }
}
