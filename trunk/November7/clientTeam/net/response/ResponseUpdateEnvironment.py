# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Oct 29, 2011 6:16:10 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseUpdateEnvironment(ServerResponse):

    def execute(self, data):

        status = data.getUint16()
#
#        try:
#            #if 'Login' in self.main.envMap:
#            numberOfPlayers = data.getUint16()
#
#            print "numberOfWorlds ", numberOfWorlds
#
#            i = 0
#
#            while (i < numberOfPlayers):
#                userName = data.getString()
#
#                print userName
#                print "\n"
#
#                i += 1
#
#            self.log('Received [' + str(Constants.SMSG_SEEONLINEPLAYERS) + '] See Online Players Response')
#
#        except:
#            self.log('Bad [' + str(Constants.SMSG_SEEONLINEPLAYERS) + '] See Online Players Response')
#            print_exc()
#
