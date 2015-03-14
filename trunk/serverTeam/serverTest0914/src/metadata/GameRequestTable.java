package metadata;

import java.util.HashMap;
import networking.request.GameRequest;

/**
 * This class holds the request code number and the corresponding request class.
 *
 * @author
 */
public class GameRequestTable {

    private static HashMap<Short, Class> requestNames;

    /*
     * Initicate the request table.
     */
    public static void init() {
        requestNames = new HashMap<Short, Class>();

        try {
            add(Constants.CMSG_AUTH, "RequestLogin");
            add(Constants.CMSG_REGISTER, "RequestRegist");
            add(Constants.CMSG_GET_PVE_WORLDS, "RequestGetPvEWorlds");
            add(Constants.CMSG_GET_PVP_WORLDS, "RequestGetPvPWorlds");
            add(Constants.CMSG_SEEONLINEPLAYERS, "RequestSeeOnlinePlayers");
            add(Constants.CMSG_SEARCH_PRIVATE_WORLD, "RequestSearchPrivateWorld");
            add(Constants.CMSG_CREATE_NEW_WORLD, "RequestCreateNewWorld");
            add(Constants.CMSG_JOIN_PVE_WORLD, "RequestJoinPvEWorld");
            add(Constants.CMSG_JOIN_PVP_WORLD, "RequestJoinPvPWorld");
            add(Constants.CMSG_START_TO_READY_GAME, "RequestStartToReadyWorld");
            add(Constants.CMSG_READY, "RequestReady");
            add(Constants.CMSG_SEE_PVP_ONLINE_PLAYERS, "RequestSeePvPOnlinePlayers");
            add(Constants.CMSG_SEE_PVE_ONLINE_PLAYERS, "RequestSeePvEOnlinePlayers");
            add(Constants.CMSG_HEARTBEAT, "RequestHeartbeat");
            add(Constants.CMSG_CHANGE_TEAM_PVP, "RequestChangeTeamPVP");
            add(Constants.CMSG_START_GAME, "RequestStartWorld");
            add(Constants.CMSG_MOVE_ANIMAL, "RequestMoveAnimal");
            add(Constants.CMSG_UPDATE_ANIMAL_COORDINATE, "RequestUpdateAnimalCoordinate");
            add(Constants.CMSG_BUY_PLANT, "RequestBuyPlant");
            add(Constants.CMSG_BUY_ANIMAL, "RequestBuyAnimal");
            add(Constants.CMSG_VOTE_GAME_SCALE, "RequestUpdateGameScaleVote");
            add(Constants.CMSG_CHANGE_AVATAR, "RequestChangeAvatar");
            add(Constants.CMSG_REQUESTWATERSOURCES, "RequestWaterSource");
            add(Constants.CMSG_CHAT, "RequestChat");
            add(Constants.CSMG_SHOP_LIST_ANIMAL, "RequestShopListAnimal");
            add(Constants.CSMG_SHOP_LIST_PLANT, "RequestShopListPlant");
            add(Constants.CMSG_ALL_AVATAR_INFO, "RequestAllAvatarInfo");
            add(Constants.CMSG_PLACE_SPECIES, "RequestPlaceSpecies");
            add(Constants.CMSG_CANCEL_TO_JOIN_GAME, "RequestCancelToJoinGame");
            add(Constants.CMSG_SAVE_EXIT_GAME, "RequestExitGame");
            add(Constants.CMSG_GET_PLAYER_WORLDS, "RequestGetPlayerWorlds");
            add(Constants.CMSG_CHANGE_PARAMETERS, "RequestChangeParameters");
            add(Constants.CMSG_LEAVE_WORLD, "RequestLeaveWorld");
            add(Constants.CMSG_STATISTICS, "RequestStats");
            add(Constants.CMSG_PARAMS, "RequestParams");
            add(Constants.CMSG_RESTART, "RequestRestart");
            add(Constants.CMSG_GIVE_SPECIES, "RequestGiveSpecies");
            add(Constants.CMSG_CHANGE_FUNCTIONAL_PARAMETERS, "RequestChangeFunctionalParams");
            add(Constants.CMSG_HIGH_SCORE, "RequestHighScore");
            add(Constants.CMSG_GET_FUNCTIONAL_PARAMETERS, "RequestGetFunctionalParameters");
            add(Constants.CMSG_CHART_BIOMASS, "RequestChartBiomass");
            add(Constants.CMSG_DELETE_WORLD, "RequestDeleteWorld");
        } catch (ClassNotFoundException e) {
            System.err.println(e.getMessage());
        }
    }

    /*
     * Add a piece of record to the rueqest table.
     */
    public static void add(short code, String name) throws ClassNotFoundException {
        requestNames.put(code, Class.forName("networking.request." + name));
    }

    /*
     * Get the request class by the given request code.
     */
    public static GameRequest get(short requestID) {
        GameRequest request = null;

        try {
            Class name = requestNames.get(requestID);

            if (name != null) {
                request = (GameRequest) name.newInstance();
                request.setID(requestID);
            } else {
                System.err.println("Invalid Request Code: " + requestID);
            }
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }

        return request;
    }
}
