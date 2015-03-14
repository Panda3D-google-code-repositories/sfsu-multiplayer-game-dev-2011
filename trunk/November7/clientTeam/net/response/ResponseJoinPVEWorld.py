# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 5, 2011 4:54:52 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
#from direct.showbase.DirectObject import DirectObject
#
#class Listener(DirectObject):
#
#    def __init__(self, parent):
#
#        self.accept(Constants.LISTENER_JOINPVEWORLD, parent.send, [])

class ResponseJoinPVEWorld(ServerResponse):

#    def __init__(self):
#
#        self.listener = Listener(self)
#
#    def send(self):
#        print 'receive message from lobby'
#        messenger.send(Constants.UPDATE_JOINPVEWORLD, [self.players])

    def execute(self, data):

        try:
            self.status = data.getUint16()

            if self.status == 0:                  #success
                self.numberOfPlayers = data.getUint16()

                self.players = []

                for i in range (self.numberOfPlayers):

                    self.userName = data.getString()
                    self.position = data.getUint16()
                    self.avatar   = data.getString()

                    #self.players.append(GameObject(self.userName, self.position, self.avatar))

                    #print self.userName, self.position, self.avatar

                                   
            else:
                main.showAlert(self.status)

            self.log('Received [' + str(Constants.SMSG_JOIN_PVE_WORLD) + '] Authentication Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_JOIN_PVE_WORLD) + '] Authentication Response')
            print_exc()
