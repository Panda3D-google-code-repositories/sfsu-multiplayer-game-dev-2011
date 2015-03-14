from common.Constants import Constants

from net.response.ResponseLogin import ResponseLogin
from net.response.ResponseRegister import ResponseRegister

class ServerResponseTable:

    responseTable = {}

    @staticmethod
    def init():
        """Initialize the response table."""
        ServerResponseTable.add(Constants.SMSG_AUTH, 'ResponseLogin')
        ServerResponseTable.add(Constants.SMSG_REGISTER, 'ResponseRegister')

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
