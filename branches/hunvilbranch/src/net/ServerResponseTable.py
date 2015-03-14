from common.Constants import Constants

from net.response.ResponseLogin import ResponseLogin
from net.response.ResponseRegister import ResponseRegister

from net.response.ResponseGetPvEWorlds import ResponseGetPvEWorlds
from net.response.ResponseGetPvPWorlds import ResponseGetPvPWorlds
from net.response.ResponseSeeOnlinePlayers import ResponseSeeOnlinePlayers
from net.response.ResponseSeePVEOnlinePlayers import ResponseSeePVEOnlinePlayers
from net.response.ResponseSeePVPOnlinePlayers import ResponseSeePVPOnlinePlayers
from net.response.ResponseUpdateEnvironment import ResponseUpdateEnvironment
from net.response.ResponseCreateNewWorld import ResponseCreateNewWorld
from net.response.ResponseSearchPrivateWorld import ResponseSearchPrivateWorld
from net.response.ResponseJoinPVEWorld import ResponseJoinPVEWorld
from net.response.ResponseJoinPVPWorld import ResponseJoinPVPWorld
from net.response.ResponseStartToReadyWorld import ResponseStartToReadyWorld
from net.response.ResponseReady import ResponseReady
from net.response.ResponseChangeAvatarType import ResponseChangeAvatarType
from net.response.ResponseChangeTeamPVP import ResponseChangeTeamPVP
from net.response.ResponseChat import ResponseChat
from net.response.ResponseBuyAnimal import ResponseBuyAnimal
from net.response.ResponseBuyPlant import ResponseBuyPlant
from net.response.ResponseMoveAnimal import ResponseMoveAnimal
from net.response.ResponseBirthAnimal import ResponseBirthAnimal
from net.response.ResponseRevealAnimalDisease import ResponseRevealAnimalDisease
from net.response.ResponseCureAnimalDisease import ResponseCureAnimalDisease
from net.response.ResponseUpdateAnimalTarget import ResponseUpdateAnimalTarget
from net.response.ResponseUpdateAnimalBiomass import ResponseUpdateAnimalBiomass
from net.response.ResponseUpdateAnimalNoWaterCount import ResponseUpdateAnimalNoWaterCount
from net.response.ResponseUpdateAnimalZone import ResponseUpdateAnimalZone
from net.response.ResponseUpdateAnimalOwner import ResponseUpdateAnimalOwner
from net.response.ResponseKillAnimal import ResponseKillAnimal
from net.response.ResponseBirthPlant import ResponseBirthPlant
from net.response.ResponseRevealPlantDisease import ResponseRevealPlantDisease
from net.response.ResponseCurePlantDisease import ResponseCurePlantDisease
from net.response.ResponseUpdatePlantBiomass import ResponseUpdatePlantBiomass
from net.response.ResponseUpdatePlantNoWaterCount import ResponseUpdatePlantNoWaterCount
from net.response.ResponseUpdatePlantNoLightCount import ResponseUpdatePlantNoLightCount
from net.response.ResponseKillPlant import ResponseKillPlant
from net.response.ResponseUpdateWaterSource import ResponseUpdateWaterSource
from net.response.ResponseCurrentDay import ResponseCurrentDay
from net.response.ResponseWeatherPrediction import ResponseWeatherPrediction
from net.response.ResponseUpdateAvgGameScale import ResponseUpdateAvgGameScale
from net.response.ResponseUpdateAvatarXP import ResponseUpdateAvatarXP
from net.response.ResponseUpdateAvatarCash import ResponseUpdateAvatarCash
from net.response.ResponseUpdateEnvScore import ResponseUpdateEnvScore
from net.response.ResponseSetUserPrimaryAvatar import ResponseSetUserPrimaryAvatar
from net.response.ResponseCancelToJoinGame import ResponseCancelToJoinGame
from net.response.ResponseStartSixtySecondsCounter import ResponseStartSixtySecondsCounter

class ServerResponseTable:

    responseTable = {}

    @staticmethod
    def init():
        """Initialize the response table."""
        ServerResponseTable.add(Constants.SMSG_AUTH, 'ResponseLogin')
        ServerResponseTable.add(Constants.SMSG_REGISTER, 'ResponseRegister')
        ServerResponseTable.add(Constants.SMSG_GETPVEWORLDS, 'ResponseGetPvEWorlds')
        ServerResponseTable.add(Constants.SMSG_GETPVPWORLDS, 'ResponseGetPvPWorlds')
        ServerResponseTable.add(Constants.SMSG_SEEONLINEPLAYERS, 'ResponseSeeOnlinePlayers')
        ServerResponseTable.add(Constants.SMSG_SEE_PVE_ONLINE_PLAYERS, 'ResponseSeePVEOnlinePlayers')
        ServerResponseTable.add(Constants.SMSG_SEE_PVP_ONLINE_PLAYERS, 'ResponseSeePVPOnlinePlayers')
        ServerResponseTable.add(Constants.SMSG_UPDATEENVIRONMENT, 'ResponseUpdateEnvironment')
        ServerResponseTable.add(Constants.SMSG_CREATE_NEW_WORLD, 'ResponseCreateNewWorld')
        ServerResponseTable.add(Constants.SMSG_SEARCH_PRIVATE_WORLD, 'ResponseSearchPrivateWorld')
        ServerResponseTable.add(Constants.SMSG_JOIN_PVE_WORLD, 'ResponseJoinPVEWorld')
        ServerResponseTable.add(Constants.SMSG_JOIN_PVP_WORLD, 'ResponseJoinPVPWorld')
        ServerResponseTable.add(Constants.SMSG_START_TO_READY_GAME, 'ResponseStartToReadyWorld')
        ServerResponseTable.add(Constants.SMSG_READY, 'ResponseReady')
        ServerResponseTable.add(Constants.SMSG_CHANGE_AVATAR_TYPE, 'ResponseChangeAvatarType')
        ServerResponseTable.add(Constants.SMSG_CHAT, 'ResponseChat')
        ServerResponseTable.add(Constants.SMSG_CHANGE_TEAM_PVP, 'ResponseChangeTeamPVP')
        ServerResponseTable.add(Constants.SMSG_BUY_ANIMAL, 'ResponseBuyAnimal')
        ServerResponseTable.add(Constants.SMSG_BUY_PLANT, 'ResponseBuyPlant')
        ServerResponseTable.add(Constants.SMSG_MOVE_ANIMAL, 'ResponseMoveAnimal')
        ServerResponseTable.add(Constants.SMSG_BIRTH_ANIMAL, 'ResponseBirthAnimal')
        ServerResponseTable.add(Constants.SMSG_REVEAL_ANIMAL_DISEASE, 'ResponseRevealAnimalDisease')
        ServerResponseTable.add(Constants.SMSG_CURE_ANIMAL_DISEASE, 'ResponseCureAnimalDisease')
        ServerResponseTable.add(Constants.SMSG_UPDATE_ANIMAL_TARGET, 'ResponseUpdateAnimalTarget')
        ServerResponseTable.add(Constants.SMSG_UPDATE_ANIMAL_BIOMASS, 'ResponseUpdateAnimalBiomass')
        ServerResponseTable.add(Constants.SMSG_UPDATE_ANIMAL_NO_WATER_COUNT, 'ResponseUpdateAnimalNoWaterCount')
        ServerResponseTable.add(Constants.SMSG_UPDATE_ANIMAL_ZONE, 'ResponseUpdateAnimalZone')
        ServerResponseTable.add(Constants.SMSG_UPDATE_ANIMAL_OWNER, 'ResponseUpdateAnimalOwner')
        ServerResponseTable.add(Constants.SMSG_KILL_ANIMAL, 'ResponseKillAnimal')
        ServerResponseTable.add(Constants.SMSG_BIRTH_PLANT, 'ResponseBirthPlant')
        ServerResponseTable.add(Constants.SMSG_REVEAL_PLANT_DISEASE, 'ResponseRevealPlantDisease')
        ServerResponseTable.add(Constants.SMSG_CURE_PLANT_DISEASE, 'ResponseCurePlantDisease')
        ServerResponseTable.add(Constants.SMSG_UPDATE_PLANT_BIOMASS, 'ResponseUpdatePlantBiomass')
        ServerResponseTable.add(Constants.SMSG_UPDATE_PLANT_NO_WATER_COUNT, 'ResponseUpdatePlantNoWaterCount')
        ServerResponseTable.add(Constants.SMSG_UPDATE_PLANT_NO_LIGHT_COUNT, 'ResponseUpdatePlantNoLightCount')
        ServerResponseTable.add(Constants.SMSG_KILL_PLANT, 'ResponseKillPlant')
        ServerResponseTable.add(Constants.SMSG_UPDATE_WATER_SOURCE, 'ResponseUpdateWaterSource')
        ServerResponseTable.add(Constants.SMSG_CURRENT_DAY, 'ResponseCurrentDay')
        ServerResponseTable.add(Constants.SMSG_WEATHER_PREDICTION, 'ResponseWeatherPrediction')
        ServerResponseTable.add(Constants.SMSG_UPDATE_AVG_GAME_SCALE, 'ResponseUpdateAvgGameScale')
        ServerResponseTable.add(Constants.SMSG_UPDATE_AVATAR_XP, 'ResponseUpdateAvatarXP')
        ServerResponseTable.add(Constants.SMSG_UPDATE_AVATAR_CASH, 'ResponseUpdateAvatarCash')
        ServerResponseTable.add(Constants.SMSG_UPDATE_ENV_SCORE, 'ResponseUpdateEnvScore')
        ServerResponseTable.add(Constants.SMSG_SET_USER_PRIMARY_AVATAR, 'ResponseSetUserPrimaryAvatar')
        ServerResponseTable.add(Constants.SMSG_CANCEL_TO_JOIN_GAME, 'ResponseCancelToJoinGame')
        ServerResponseTable.add(Constants.SMSG_START_SIXTY_SECONDS_COUNTER, 'ResponseStartSixtySecondsCounter')

    @staticmethod
    def add(constant, name):
        """Map a numeric response code with the name of an existing response module."""
        if name in globals():
            ServerResponseTable.responseTable[constant] = name
        else:
            print 'Add Response Error: No module named ' + str(name)

    @staticmethod
    def get(responseCode):
        """Retrieve an instance of the corresponding response."""
        serverResponse = None

        if responseCode in ServerResponseTable.responseTable:
            serverResponse = globals()[ServerResponseTable.responseTable[responseCode]]()
        else:
            print 'Bad Response Code: ' + str(responseCode)

        return serverResponse
