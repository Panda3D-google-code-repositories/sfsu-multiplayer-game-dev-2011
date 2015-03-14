# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 21, 2011 1:17:50 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseCancelToJoinGame(ServerResponse):

    def execute(self, data):

        try:
            if self.status == 0:

                self.numberOfPlayers = data.getUint16()
                self.players = []

                for i in range (self.numberOfPlayers):
                    self.info = { 'userName'     : data.getString(),
                                  'teamNumber'   : data.getUint16(),
                                  'position'     : data.getUint16(),
                                  'avatar'       : data.getString(),
                                  'isReady'      : data.getUint16(),
                                  'isTimerRunning'  : data.getUint16() }        #0 = Timer is running, #1 = Timer is not running

                self.players.append(self.info)

            main.msgQ.putToMsgQ(Constants.CMSG_CANCEL_TO_JOIN_GAME, self.info)

            self.log('Received [' + str(Constants.SMSG_CANCEL_TO_JOIN_GAME) + '] Cancel To Join Game Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_CANCEL_TO_JOIN_GAME) + '] Cancel To Join Game Response')
            print_exc()