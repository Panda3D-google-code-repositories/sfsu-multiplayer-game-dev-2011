# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 22, 2011 11:52:07 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseWaterSources(ServerResponse):

    def execute(self, data):

        try:
            self.status = data.getUint16()              #0 = success, 1 = fail

            self.numberOfPlayers = data.getUint16()

            self.players = []

            for i in range (self.numberOfPlayers):
                self.info = { 'zoneID'  : data.getUint16(),
                              'x'   : data.getUint32(),
                              'y'   : data.getUint32(),
                              'z'   : data.getUint32() }

                self.players.append(self.info)

            for i in range (self.numberOfPlayers):
                print self.info['zoneID'], " ", self.info['x'], " ", self.info['y'], " ", self.info['z']

            main.msgQ.putToMsgQ(Constants.CMSG_REQUESTWATERSOURCES, self.players)

            self.log('Received [' + str(Constants.SMSG_REQUESTWATERSOURCES) + '] Water sources Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_REQUESTWATERSOURCES) + '] Water sources Response')
            print_exc()

