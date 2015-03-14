# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Oct 29, 2011 5:46:48 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from main.MainLobby.GameLobby.PvPGameLobby import GameObject

class ResponseGetPvEWorlds(ServerResponse):

    def execute(self, data):

        try:
            #if 'Login' in self.main.envMap:

            numberOfWorlds = data.getUint16()
            #print "numberOfWorlds ", numberOfWorlds

            #create 2-dimensional array
            pveClosedWorlds = []
            pveOpenedWorlds = []
            for i in range(numberOfWorlds):
                isPublic = data.getUint16()
                playedByUser = data.getUint16()
                worldName = data.getString()
                currentPlayerNumber = data.getUint16()
                maxPlayerNumber = data.getUint16()
                ecosystem = data.getString()
                gameObj = GameObject(worldName, currentPlayerNumber, maxPlayerNumber, ecosystem)
                if isPublic == 0:
                    pveClosedWorlds.append(gameObj)
                else:
                    pveOpenedWorlds.append(gameObj)
            print 'send response to pve'
            messenger.send(Constants.LISTENER_PVE_2D, [pveClosedWorlds, pveOpenedWorlds])
            #load pveWorlds to the screen
            #code here

#                if isPublic == 0:
#                    print "Private\n"
#                else:
#                    print "Public\n"
#
#                if playedByUser == 0:
#                    print "Continue Previous Game\n"
#                else:
#                    print "Join\n"
#
#                print "WorldName\tCurrentPlayerName\tMaxPlayerNumber\tEcosystem\n"
#                print worldName, currentPlayerNumber, maxPlayerNumber, ecosystem
#                print "\n"


            self.log('Received [' + str(Constants.SMSG_GETPVEWORLDS) + '] Get PVE Worlds Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_GETPVEWORLDS) + '] Get PVE Worlds Response')
            print_exc()


