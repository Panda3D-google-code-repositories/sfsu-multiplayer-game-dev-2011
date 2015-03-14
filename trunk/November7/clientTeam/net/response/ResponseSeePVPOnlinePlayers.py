# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 6, 2011 11:47:49 PM$"

from common.Constants import Constants
#from direct.showbase.DirectObject import DirectObject
from net.response.ServerResponse import ServerResponse
from traceback import print_exc


#class PvPOnlinePlayerListener(DirectObject):
#
#    def __init__(self, parent):
#
#        self.accept(Constants.LISTENER_PVP_REQUEST_ONLINE_PLAYER, parent.execute, [] )

class ResponseSeePVPOnlinePlayers(ServerResponse):


#    def __init__(self):
#
#        self.listener = PvPOnlinePlayerListener(self)

    def execute(self, data):

        try:
            numberOfPlayers = data.getUint16()

            print "numberOfPlayers ", numberOfPlayers

            onlinePlayers = []

            for i in range (numberOfPlayers):
                i = data.getString()
                onlinePlayers.append(i)

#            messenger.send("UPDATE_MAIN_ONLINE_PLAYERS", [onlinePlayers])
                print i
                print "\n"

#            messenger.send(Constants.UPDATE_PVP_ONLINE_PLAYERS, [onlinePlayers])

            self.log('Received [' + str(Constants.SMSG_SEE_PVP_ONLINE_PLAYERS) + '] See PVP Online Players Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_SEE_PVP_ONLINE_PLAYERS) + '] See PVP Online Players Response')
            print_exc()


