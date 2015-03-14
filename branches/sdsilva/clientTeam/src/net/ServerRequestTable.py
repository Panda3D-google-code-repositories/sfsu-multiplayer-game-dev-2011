from common.Constants import Constants

from net.request.RequestLogin import RequestLogin
from net.request.RequestRegister import RequestRegister
from net.request.RequestSendPasswordForPrivateWorld import RequestSendPasswordForPrivateWorld
from net.request.RequestCurrentGames import RequestCurrentGames
from net.request.RequestSearchPrivateWorld import RequestSearchPrivateWorld
from net.request.RequestStartGame import RequestStartGame
from net.request.RequestJoinPVPWorld import RequestJoinPVPWorld
from net.request.RequestJoinPVEWorld import RequestJoinPVEWorld
from net.request.RequestCreateNewWorld import RequestCreateNewWorld
from net.request.RequestUniversalChat import RequestUniversalChat
from net.request.RequestPVEModeChat import RequestPVEModeChat
from net.request.RequestPVPModeChat import RequestPVPModeChat
from net.request.RequestWorldChat import RequestWorldChat
from net.request.RequestWhisperingChat import RequestWhisperingChat
from net.request.RequestKickPlayerOut import RequestKickPlayerOut
from net.request.RequestMoveAnimal import RequestMoveAnimal
from net.request.RequestAnimalInfo import RequestAnimalInfo
from net.request.RequestAddAnimal import RequestAddAnimal
from net.request.RequestAddPlant import RequestAddPlant
from net.request.RequestResearchDiseases import RequestResearchDiseases
from net.request.RequestResearchWeather import RequestResearchWeather
from net.request.RequestExitGame import RequestExitGame
from net.request.RequestGetPvEWorlds import RequestGetPvEWorlds
from net.request.RequestGetPvPWorlds import RequestGetPvPWorlds
from net.request.RequestSeeOnlinePlayers import RequestSeeOnlinePlayers
from net.request.RequestSeePVEOnlinePlayers import RequestSeePVEOnlinePlayers
from net.request.RequestSeePVPOnlinePlayers import RequestSeePVPOnlinePlayers
from net.request.RequestUpdateEnvironment import RequestUpdateEnvironment
from net.request.RequestStartToReadyWorld import RequestStartToReadyWorld
from net.request.RequestReady import RequestReady



class ServerRequestTable:

    requestTable = {}

    @staticmethod
    def init():
        """Initialize the request table."""
       
        ServerRequestTable.add(Constants.CMSG_AUTH, 'RequestLogin')
        ServerRequestTable.add(Constants.CMSG_REGISTER, 'RequestRegister')
        ServerRequestTable.add(Constants.CMSG_PASSWORD_PRIVATE_WORLD, 'RequestSendPasswordForPrivateWorld')
        ServerRequestTable.add(Constants.CMSG_CURRENT_GAMES, 'RequestCurrentGames')
        ServerRequestTable.add(Constants.CMSG_SEARCH_PRIVATE_WORLD, 'RequestSearchPrivateWorld')
        ServerRequestTable.add(Constants.CMSG_START_GAME, 'RequestStartGame')
        ServerRequestTable.add(Constants.CMSG_JOIN_PVP_WORLD, 'RequestJoinPVPWorld')
        ServerRequestTable.add(Constants.CMSG_JOIN_PVE_WORLD, 'RequestJoinPVEWorld')
        ServerRequestTable.add(Constants.CMSG_CREATE_NEW_WORLD, 'RequestCreateNewWorld')
        ServerRequestTable.add(Constants.CMSG_UNIVERSAL_CHAT, 'RequestUniversalChat')
        ServerRequestTable.add(Constants.CMSG_PVE_MODE_CHAT, 'RequestPVEModeChat')
        ServerRequestTable.add(Constants.CMSG_PVP_MODE_CHAT, 'RequestPVPModeChat')
        ServerRequestTable.add(Constants.CMSG_WORLD_CHAT, 'RequestWorldChat')
        ServerRequestTable.add(Constants.CMSG_WHISPERING_CHAT, 'RequestWhisperingChat')
        ServerRequestTable.add(Constants.CMSG_KICK_PLAYER_OUT, 'RequestKickPlayerOut')
        ServerRequestTable.add(Constants.CMSG_MOVE_ANIMAL, 'RequestMoveAnimal')
        ServerRequestTable.add(Constants.CMSG_ANIMAL_INFO, 'RequestAnimalInfo')
        ServerRequestTable.add(Constants.CMSG_ADD_ANIMAL, 'RequestAddAnimal')
        ServerRequestTable.add(Constants.CMSG_ADD_PLANT, 'RequestAddPlant')
        ServerRequestTable.add(Constants.CMSG_RESEARCH_DISEASES, 'RequestResearchDiseases')
        ServerRequestTable.add(Constants.CMSG_RESEARCH_WEATHER, 'RequestResearchWeather')
        ServerRequestTable.add(Constants.CMSG_SAVE_EXIT_GAME, 'RequestExitGame')
        ServerRequestTable.add(Constants.CMSG_GETPVEWORLDS, 'RequestGetPvEWorlds')
        ServerRequestTable.add(Constants.CMSG_GETPVPWORLDS, 'RequestGetPvPWorlds')
        ServerRequestTable.add(Constants.CMSG_SEEONLINEPLAYERS, 'RequestSeeOnlinePlayers')
        ServerRequestTable.add(Constants.CMSG_SEE_PVE_ONLINE_PLAYERS, 'RequestSeePVEOnlinePlayers')
        ServerRequestTable.add(Constants.CMSG_SEE_PVP_ONLINE_PLAYERS, 'RequestSeePVPOnlinePlayers')
        ServerRequestTable.add(Constants.CMSG_UPDATEENVIRONMENT, 'RequestUpdateEnvironment')
        ServerRequestTable.add(Constants.CMSG_START_TO_READY_GAME, 'RequestStartToReadyWorld')
        ServerRequestTable.add(Constants.CMSG_READY, 'RequestReady')

        

    @staticmethod
    def add(constant, name):
        """Map a numeric request code with the name of an existing request module."""
        if name in globals():
            ServerRequestTable.requestTable[constant] = name
        else:
            print 'Add Request Error: No module named ' + str(name)

    @staticmethod
    def get(requestCode):
        """Retrieve an instance of the corresponding request."""
        serverRequest = None

        if requestCode in ServerRequestTable.requestTable:
            serverRequest = globals()[ServerRequestTable.requestTable[requestCode]]()
        else:
            print 'Bad Request Code: ' + str(requestCode)

        return serverRequest
