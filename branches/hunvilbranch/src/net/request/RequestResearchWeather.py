# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestResearchWeather(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_RESEARCH_WEATHER)
            pkg.addUint16(args['stage'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_RESEARCH_WEATHER) + '] Research Weather Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_RESEARCH_WEATHER) + '] Research Weather Request')
            print_exc()
