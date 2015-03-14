package metadata;

/**
 *
 * @author Xuyuan
 */
public class Constants {

    // Request + Response
    public final static short CMSG_AUTH = 101;
    public final static short SMSG_AUTH = 201;
    public final static short CMSG_REGISTER = 102;
    public final static short SMSG_REGISTER = 202;
    public final static short CMSG_SEARCH_PRIVATE_WORLD = 103;
    public final static short SMSG_SEARCH_PRIVATE_WORLD = 203;
    public final static short CMSG_JOIN_PVE_WORLD = 104;
    public final static short SMSG_JOIN_PVE_WORLD = 204;
    public final static short CMSG_JOIN_PVP_WORLD = 105;
    public final static short SMSG_JOIN_PVP_WORLD = 205;
    public final static short CMSG_CREATE_NEW_WORLD = 106;
    public final static short SMSG_CREATE_NEW_WORLD = 206;
    public final static short CMSG_SEE_PVE_ONLINE_PLAYERS = 107;
    public final static short SMSG_SEE_PVE_ONLINE_PLAYERS = 207;
    public final static short CMSG_SEE_PVP_ONLINE_PLAYERS = 108;
    public final static short SMSG_SEE_PVP_ONLINE_PLAYERS = 208;
    public final static short CMSG_CHANGE_AVATAR = 109;
    public final static short SMSG_CHANGE_AVATAR = 209;
    public final static short CMSG_PASSWORD_PRIVATE_WORLD = 110;
    public final static short SMSG_PASSWORD_PRIVATE_WORLD = 210;
    public final static short CMSG_START_GAME = 111;
    public final static short SMSG_START_GAME = 211;
    public final static short CMSG_CHAT = 112;
    public final static short SMSG_CHAT = 212;
    public final static short CMSG_HEARTBEAT = 113;
    public final static short SMSG_HEARTBEAT = 213;
    public final static short CMSG_BUY_ANIMAL = 114;
    public final static short SMSG_BUY_ANIMAL = 214;
    public final static short CMSG_BUY_PLANT = 115;
    public final static short SMSG_BUY_PLANT = 215;
    public final static short CMSG_MOVE_ANIMAL = 116;
    public final static short SMSG_MOVE_ANIMAL = 216;
    public final static short CMSG_RESEARCH_DISEASES = 117;
    public final static short SMSG_RESEARCH_DISEASES = 217;
    public final static short CMSG_RESEARCH_WEATHER = 118;
    public final static short SMSG_RESEARCH_WEATHER = 218;
    public final static short CMSG_SAVE_EXIT_GAME = 119;
    public final static short SMSG_SAVE_EXIT_GAME = 219;
    public final static short CMSG_VOTE_GAME_SCALE = 120;
    public final static short SMSG_VOTE_GAME_SCALE = 220;
    public final static short CMSG_KICK_PLAYER_PVP_LOBBY = 121;
    public final static short SMSG_KICK_PLAYER_PVP_LOBBY = 221;
    public final static short CMSG_ACCEPT_ANIMAL = 122;
    public final static short SMSG_ACCEPT_ANIMAL = 222;
    public final static short CMSG_START_TO_READY_GAME = 123;
    public final static short SMSG_START_TO_READY_GAME = 223;
    public final static short CMSG_READY = 124;
    public final static short SMSG_READY = 224;
    public final static short CMSG_CANCEL_TO_JOIN_GAME = 125;
    public final static short SMSG_CANCEL_TO_JOIN_GAME = 225;
    public final static short CMSG_CHANGE_TEAM_PVP = 126;
    public final static short SMSG_CHANGE_TEAM_PVP = 226;
    public final static short CMSG_GET_PVE_WORLDS = 127;
    public final static short SMSG_GET_PVE_WORLDS = 227;
    public final static short CMSG_GET_PVP_WORLDS = 128;
    public final static short SMSG_GET_PVP_WORLDS = 228;
    public final static short CMSG_SEEONLINEPLAYERS = 129;
    public final static short SMSG_SEEONLINEPLAYERS = 229;
    public final static short CMSG_UPDATE_ANIMAL_TARGET = 130;
    public final static short SMSG_UPDATE_ANIMAL_TARGET = 230;
    public final static short CMSG_UPDATE_ANIMAL_COORDINATE = 131;
    public final static short SMSG_UPDATE_ANIMAL_COORDINATE = 231;
    public final static short CMSG_UPDATE_ENVIRONMENT = 132;
    public final static short SMSG_UPDATE_ENVIRONMENT = 232;
    public final static short CMSG_REQUESTWATERSOURCES = 133;
    public final static short SMSG_REQUESTWATERSOURCES = 233;
    public final static short CSMG_SHOP_LIST_ANIMAL = 134;
    public final static short SMSG_SHOP_LIST_ANIMAL = 234;
    public final static short CSMG_SHOP_LIST_PLANT = 135;
    public final static short SMSG_SHOP_LIST_PLANT = 235;
    public final static short CMSG_ALL_AVATAR_INFO = 136;
    public final static short SMSG_ALL_AVATAR_INFO = 236;
    public final static short CMSG_GET_PLAYER_WORLDS = 137;
    public final static short SMSG_GET_PLAYER_WORLDS = 237;
    public static final short CMSG_PLACE_SPECIES = 138;
    public static final short SMSG_PLACE_SPECIES = 238;
    public final static short CMSG_CREATE_AVATAR = 139;
    public final static short SMSG_CREATE_AVATAR = 239;
    public final static short CMSG_REMOVE_AVATAR = 140;
    public final static short SMSG_REMOVE_AVATAR = 240;
    public final static short CMSG_CHANGE_PARAMETERS = 141;
    public final static short SMSG_CHANGE_PARAMETERS = 241;
    public final static short CMSG_LEAVE_WORLD = 142;
    public final static short SMSG_LEAVE_WORLD = 242;
    public final static short CMSG_STATISTICS = 143;
    public final static short SMSG_STATISTICS = 243;
    public final static short CMSG_PARAMS = 144;
    public final static short SMSG_PARAMS = 244;
    public final static short CMSG_RESTART = 145;
    public final static short SMSG_RESTART = 245;
    public final static short CMSG_GIVE_SPECIES = 146;
    public final static short SMSG_GIVE_SPECIES = 246;
    public final static short CMSG_CHANGE_FUNCTIONAL_PARAMETERS = 147;
    public final static short SMSG_CHANGE_FUNCTIONAL_PARAMETERS = 247;
    public final static short CMSG_HIGH_SCORE = 148;
    public final static short SMSG_HIGH_SCORE = 248;
    public final static short CMSG_GET_FUNCTIONAL_PARAMETERS = 149;
    public final static short SMSG_GET_FUNCTIONAL_PARAMETERS = 249;
    public final static short CMSG_CHART_BIOMASS = 150;
    public final static short SMSG_CHART_BIOMASS = 250;
    public final static short CMSG_DELETE_WORLD = 151;
    public final static short SMSG_DELETE_WORLD = 251;

    // Response Only
    public final static short SMSG_BIRTH_ANIMAL = 301;
    public final static short SMSG_BIRTH_PLANT = 302;
    public final static short SMSG_GET_ENV = 303;
    public final static short SMSG_CURE_ANIMAL_DISEASE = 304;
    public final static short SMSG_CURE_PLANT_DISEASE = 305;
    public final static short SMSG_UPDATE_ANIMAL_BIOMASS = 306;
    public final static short SMSG_UPDATE_PLANT_BIOMASS = 307;
    public final static short SMSG_UPDATE_ANIMAL_NO_WATER_COUNT = 308;
    public final static short SMSG_UPDATE_PLANT_NO_WATER_COUNT = 309;
    public final static short SMSG_UPDATE_ANIMAL_ZONE = 310;
    public final static short SMSG_UPDATE_ANIMAL_OWNER = 311;
    public final static short SMSG_UPDATE_PLANT_NO_LIGHT_COUNT = 312;
    public final static short SMSG_KILL_ANIMAL = 313;
    public final static short SMSG_KILL_PLANT = 314;
    public final static short SMSG_UPDATE_WATER_SOURCE = 315;
    public final static short SMSG_UPDATE_TIME = 316;
    public final static short SMSG_WEATHER_PREDICTION = 317;
    public final static short SMSG_UPDATE_AVG_GAME_SCALE_VOTE = 318;
    public final static short SMSG_UPDATE_XP = 319;
    public final static short SMSG_UPDATE_CASH = 320;
    public final static short SMSG_UPDATE_ENV_SCORE = 321;
    public final static short SMSG_SET_USER_PRIMARY_AVATAR = 322;
    public final static short SMSG_REVEAL_ANIMAL_DISEASE = 323;
    public final static short SMSG_REVEAL_PLANT_DISEASE = 324;
    public final static short SMSG_UPDATE_GAME_SCALE_TIME = 325;
    public static final short SMSG_UPDATE_ONLINE_PLAYERS = 326;
    public final static short SMSG_UPDATE_LEVEL = 327;
    public final static short SMSG_DRINK_WATER = 328;
    public final static short SMSG_CREATE_ENV = 329;
    public final static short SMSG_TARGET_REWARD = 330;
    public final static short SMSG_SHOP_UNLOCK = 331;

    // Game Types
    public static final short GAME_TYPE_PVE = 0;
    public static final short GAME_TYPE_PVP = 1;
    // Privacy Type
    public static final short PRIVACY_TYPE_PRIVATE = 0;
    public static final short PRIVACY_TYPE_PUBLIC = 1;
    // Diet Type
    public static final short DIET_TYPE_OMNIVORE = 0;
    public static final short DIET_TYPE_CARNIVORE = 1;
    public static final short DIET_TYPE_HERBIVORE = 2;
    // Avatar Type
    public static final short AVATAR_TYPE_PLANTER = 1;
    public static final short AVATAR_TYPE_BREEDER = 2;
    public static final short AVATAR_TYPE_WEATHER_MAN = 3;
    // Organism Type
    public static final short ORGANISM_TYPE_ANIMAL = 0;
    public static final short ORGANISM_TYPE_PLANT = 1;
    // Location
    public static final short LOCATION_MAIN_LOBBY = 0;
    public static final short LOCATION_PVP_G_LOBBY = 1;
    public static final short LOCATION_PVE_G_LOBBY = 2;
    public static final short LOCATION_PVP_W_LOBBY = 3;
    public static final short LOCATION_PVE_W_LOBBY = 4;
    // Reward Type
    public static final short REWARD_TYPE_XP = 0;
    public static final short REWARD_TYPE_MONEY = 1;
    // Parameter Type
    public static final short PARAMETER_K = 0;	//Plants Carrying capacity >0
    public static final short PARAMETER_R = 1;	//Plants Growth rate 0-1
    public static final short PARAMETER_X = 2;	//Plants Metabolic rate 0-1
    public static final short PARAMETER_X_A = 3;	//Animals
    public static final short PARAMETER_E = 4; //Animals assimilationEfficiency
    public static final short PARAMETER_D = 5; //Animals predatorInterference
    public static final short PARAMETER_Q = 6; //Animals functionalResponseControl
    public static final short PARAMETER_A = 7; //Animals relativeHalfSaturationDensity
    // Create Organism Status
    public static final short CREATE_STATUS_DEFAULT = 0;
    public static final short CREATE_STATUS_BIRTH = 1;
    public static final short CREATE_STATUS_PURCHASE = 2;
    // Remove Organism Status
    public static final short REMOVE_STATUS_DEFAULT = 0;
    public static final short REMOVE_STATUS_DEATH = 1;
    // Other
    public static final float TIME_MODIFIER = 1f;
    public static final int SAVE_INTERVAL = 60000;
    public static final float BIOMASS_SCALE = 100000;
    public static final String CLIENT_VERSION = "1.32";
    public static final int MODIFIER_PLANT = 1000;
    public static final int MODIFIER_ANIMAL = 2000;
    public static final int TIMEOUT_SECONDS = 30;
    public static final int INITIAL_GOLD = 1500;
    public static final int MAX_LEVEL = 10;
    public static final int MAX_GOLD = 1000000;
    public static final int STARTING_NEEDED_EXP = 1000;
    public static final int MONTH_DURATION = 300;
    public static final int MAX_SPECIES_SIZE = 10;
    public static final short CREATE_LOAD = 0;
    public static final short CREATE_USER = 1;
    public static final short CREATE_SYSTEM = 2;
    public static final float MULTIPLIER_EXP = 1f;
}
