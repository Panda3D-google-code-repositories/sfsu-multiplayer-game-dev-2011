package model;

public class Stat {
	private int activityDay;
	private String activityType;
	private int animalTypeId;
	private int count;
	private String activityMessage;
	private String speciesName;
	private int envScore;
	private int plantTypeId;
	private String plantName;
	
	public int getActivityDay() {
		return activityDay;
	}
	public void setActivityDay(int activityDay) {
		this.activityDay = activityDay;
	}
	public String getActivityType() {
		return activityType;
	}
	public void setActivityType(String activityType) {
		this.activityType = activityType;
	}
	public int getAnimalTypeId() {
		return animalTypeId;
	}
	public void setAnimalTypeId(int animalTypeId) {
		this.animalTypeId = animalTypeId;
	}
	public int getCount() {
		return count;
	}
	public void setCount(int count) {
		this.count = count;
	}
	public String getActivityMessage() {
		if(activityMessage == null)
			return "----";
		return activityMessage;
	}
	public void setActivityMessage(String activityMessage) {
		this.activityMessage = activityMessage;
	}
	public void setAnimalName(String speciesName) {
		this.speciesName =speciesName;
	}
	
	public String getAnimalName(){
		return this.speciesName;
	}
	public void setEnvironmentScore(int score) {
		this.envScore = score;
		
	}
	public int getEnvironmentScore() {
		return this.envScore;
	}
	public void setPlantTypeId(int plantTypeID) {
		this.plantTypeId = plantTypeID;
	}
	
	public int getPlantTypeId(){
		return this.plantTypeId;
	}
	public void setPlantName(String plantName) {
		this.plantName = plantName;
		
	}
	
	public String getPlantName(){
		return this.plantName;
	}
	
	
}
