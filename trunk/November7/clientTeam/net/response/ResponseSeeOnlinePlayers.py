# To change this template, choose Tools | Templates
# and open the template in the editor.
from common.Constants import Constants
from direct.showbase.DirectObject import DirectObject
from net.response.ServerResponse import ServerResponse
from traceback import print_exc

__author__="kelvin"
__date__ ="$Oct 29, 2011 6:11:52 PM$"



class PvPOnlinePlayerListener(DirectObject):
    
    def __init__(self, parent):
        
        self.accept(Constants.LISTENER_PVP_REQUEST_ONLINE_PLAYER, parent.execute, [] )

class ResponseSeeOnlinePlayers(ServerResponse):

    
    def __init__(self):
        
        self.listener = PvPOnlinePlayerListener(self)
        
    def execute(self, data):

        try:
            #if 'Login' in self.main.envMap:

            numberOfPlayers = data.getUint16()

            print "numberOfPlayers ", numberOfPlayers

            onlinePlayers = []

            for i in range (numberOfPlayers):
                i = data.getString()
                onlinePlayers.append(i)

#            messenger.send("UPDATE_MAIN_ONLINE_PLAYERS", [onlinePlayers])
#                print i
#                print "\n"

            #code to load the list of onlinePlayers will be here
            #
            messenger.send(Constants.UPDATE_PVP_ONLINE_PLAYERS, [onlinePlayers])
            self.log('Received [' + str(Constants.SMSG_SEEONLINEPLAYERS) + '] See Online Players Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_SEEONLINEPLAYERS) + '] See Online Players Response')
            print_exc()

