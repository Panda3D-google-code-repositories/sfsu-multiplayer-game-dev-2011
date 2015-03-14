# To change this template, choose Tools | Templates
# and open the template in the editor.
from common.Constants import Constants
from direct.showbase.DirectObject import DirectObject
from net.response.ServerResponse import ServerResponse
from traceback import print_exc
from main.MainLobby.GameLobby.PvPGameLobby import GameObject

__author__ = "kelvin"
__date__ = "$Oct 29, 2011 5:59:35 PM$"


class ResponseGetPvPWorlds(ServerResponse):
        
    def execute(self, data):

        try:
            numberOfWorlds = data.getUint16()
            self.pvpWorlds = []

            for i in range (numberOfWorlds):
                
                worldName = data.getString()
                currentPlayerNumber = data.getUint16()
                maxPlayerNumber = data.getUint16()
                ecosystem = data.getString()
                gameObj = GameObject(worldName, currentPlayerNumber, maxPlayerNumber, ecosystem)
                self.pvpWorlds.append(gameObj)
            
            messenger.send(Constants.LISTENER_PVP_ONLINE_PLAYERS, [self.pvpWorlds])

            self.log('Received [' + str(Constants.SMSG_GETPVPWORLDS) + '] Get PVP Worlds Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_GETPVPWORLDS) + '] Get PVP Worlds Response')
            print_exc()
