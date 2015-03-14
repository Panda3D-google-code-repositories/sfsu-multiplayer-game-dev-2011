from traceback import print_exc

from direct.distributed.PyDatagram import PyDatagram
from common.Constants import Constants
from net.request.ServerRequest import ServerRequest

class RequestGetPlayerWorlds(ServerRequest):

    def send(self, args = None):

        try:
            pkg = PyDatagram()
            pkg.addUint16(Constants.CMSG_GET_PLAYER_WORLDS)
            pkg.addUint32(args['player_id'])

            self.cWriter.send(pkg, self.connection)

            self.log('Sent [' + str(Constants.CMSG_GET_PLAYER_WORLDS) + '] Get Player Worlds Request')
        except:
            self.log('Bad [' + str(Constants.CMSG_GET_PLAYER_WORLDS) + '] Get Player Worlds Request')
            print_exc()
