# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseSearchPrivateWorld(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 0:                                                    #private game exists
                self.worldType = data.getUint16()
                self.numberOfWorlds = data.getUint16()

                self.private = []

                if self.worldType == 1:                                             #(1 = 'PvE', 2 = 'PvP')

                    messenger.send(Constants.LISTENER_SEARCH_RESPONSE, [0,1])
                    for i in range (self.numberOfWorlds):
                        self.info = {#'isPublic'      : data.getUint16(),            #(0 = closed world, 1 = open world)
                                     #'isPlayedByUser': data.getUint16(),            #(0 = true, 1 = false)
                                     'worldName'     : data.getString(),
                                     'numberOfPlayers': data.getUint16(),
                                     'maxPlayers'    : data.getUint16(),
                                     'ecosystem'     : data.getString() }

                        worldObj = WorldObj(worldName, ecosystem, maxPlayer)

                        main.msgQ.addToPendingObj(Constants.PENDING_SEARCH_PRIVATE_WORLD, worldObj)

                elif self.worldType == 2:

                    messenger.send(Constants.LISTENER_SEARCH_RESPONSE, [0,2])
                    for i in range (self.numberOfWorlds):
                        self.info = { 'worldName'     : data.getString(),
                                      'numberOfPlayers': data.getUint16(),
                                      'maxPlayers'    : data.getUint16(),
                                      'ecosystem'     : data.getString() }

                        worldObj = WorldObj(worldName, ecosystem, maxPlayer)

                        main.msgQ.addToPendingObj(Constants.PENDING_SEARCH_PRIVATE_WORLD, worldObj)

            main.msgQ.putToMsgQ(Constants.CMSG_SEARCH_PRIVATE_WORLD, self.status)


            self.log('Received [' + str(Constants.SMSG_SEARCH_PRIVATE_WORLD) + '] Search Private World Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SEARCH_PRIVATE_WORLD) + '] Search Private World Response')
            print_exc()
