# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 5, 2011 1:13:44 PM$"

from common.Constants import Constants
#from direct.showbase.DirectObject import DirectObject
from net.response.ServerResponse import ServerResponse
from traceback import print_exc
#from main.MainLobby.GameLobby.PvPGameLobby import GameObject

class ResponseCreateNewWorld(ServerResponse):


    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 0:         #success

                self.worldType = data.getUint16()   #1 = PvE, 2 = PvP
                self.worldName = data.getString()
                self.ecosystem = data.getString()
                self.maxPlayerNumber = data.getUint16()
                
                print 'worldType: ', self.worldType
                print 'worldName: ', self.worldName
                print 'maxPlayerNumber: ', self.maxPlayerNumber
                print 'ecosystem: ', self.ecosystem

            else:
                main.showAlert(self.status)

            #print 'send message to client'
            #messenger.send(Constants.LISTENER_PVP_ONLINE_PLAYERS, [self.pvpWorlds])
#            messenger.send("UPDATE_PVP_ONLINE_PLAYERS", [self.pvpWorlds])

            self.log('Received [' + str(Constants.SMSG_CREATE_NEW_WORLD) + '] Get PVP Worlds Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CREATE_NEW_WORLD) + '] Get PVP Worlds Response')
            print_exc()
