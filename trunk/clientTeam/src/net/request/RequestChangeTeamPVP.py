# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 12, 2011 10:39:16 PM$"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestChangeTeamPVP(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_CHANGE_TEAM_PVP)
            pkg.addString(args['worldName'])
            pkg.addUint16(args['teamNumber'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_CHANGE_TEAM_PVP) + '] Change Team PVP Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_CHANGE_TEAM_PVP) + '] Change Team PVP Request')
            print_exc()


