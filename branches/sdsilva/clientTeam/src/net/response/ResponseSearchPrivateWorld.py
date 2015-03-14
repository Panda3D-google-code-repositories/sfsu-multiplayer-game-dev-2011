# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

#class Receiver(DirectObject):
#
#    def __init__(self, parent):
#
#        self.accept(Constants.LISTENER_PRIVATE_WORLD_2D, parent.send, [])

class ResponseSearchPrivateWorld(ServerResponse):

#    def __init__(self):
#
#        self.rec = Receiver(self)
#
#    def send(self):
#        print 'receive message from lobby'
#        messenger.send(Constants.UPDATE_PRIVATE_ONLINE_PLAYERS, [self.private])

    def execute(self, data):

        try:
            self.status = data.getUint16()

            print self.status

            if self.status == 0:                  #private game exists
                self.worldType = data.getUint16()
                self.numberOfWorlds = data.getUint16()

                print "numberOfWorlds ", self.numberOfWorlds
                self.private = []

                if self.worldType == 1:           #(1 = 'PvE', 2 = 'PvP')

                    for i in range (self.numberOfWorlds):
                        self.isPublic = data.getUint16()            #(0 = closed world, 1 = open world)
                        self.isPlayedByUser = data.getUint16()      #(0 = true, 1 = false)
                        self.worldName = data.getString()
                        self.numberOfPlayers = data.getUint16()
                        self.maxPlayers = data.getUint16()
                        self.ecosystem = data.getString()

                        #self.private.append(GameObject(self.isPublic, self.isPlayedByUser, self.worldName, self.numberOfPlayers, self.maxPlayers, self.ecosystem))
                    

                        print self.isPublic, self.isPlayedByUser, self.worldName, self.numberOfPlayers, self.maxPlayers, self.ecosystem

                elif self.worldType == 2:

                    for i in range (self.numberOfWorlds):
                        self.worldName = data.getString()
                        self.numberOfPlayers = data.getUint16()
                        self.maxPlayers = data.getUint16()
                        self.ecosystem = data.getString()

                        #self.private.append(GameObject(self.worldName, self.numberOfPlayers, self.maxPlayers, self.ecosystem))
                    

                        print self.worldName, self.numberOfPlayers, self.maxPlayers, self.ecosystem

            else:
                main.showAlert(self.status)   #private game doesn't exist
                print self.status

            self.log('Received [' + str(Constants.SMSG_SEARCH_PRIVATE_WORLD) + '] Search Private World Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_SEARCH_PRIVATE_WORLD) + '] Search Private World Response')
            print_exc()
