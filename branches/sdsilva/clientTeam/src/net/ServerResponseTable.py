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
