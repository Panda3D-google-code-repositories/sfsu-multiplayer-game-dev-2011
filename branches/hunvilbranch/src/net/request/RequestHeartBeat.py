#@PydevCodeAnalysisIgnore
# To change this template, choose Tools | Templates
# and open the template in the editor.

from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestHeartBeat(ServerRequest):

    def send(self, args):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_HEARTBEAT)

            self.cWriter.send(pkg, self.connection)

#            self.log('Sent [' + str(Constants.CMSG_HEARTBEAT) + '] Heartbeat Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_HEARTBEAT) + '] Heartbeat Request')
            print_exc()