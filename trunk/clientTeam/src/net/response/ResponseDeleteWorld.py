from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseDeleteWorld(ServerResponse):

    def execute(self, data):

        try:
            args = {'status'    : data.getUint16(),
                    'world_id'  : data.getUint32()}

            main.msgQ.putToMsgQ(Constants.SMSG_DELETE_WORLD, args)

            self.log('Received [' + str(Constants.SMSG_DELETE_WORLD) + '] Delete World Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_DELETE_WORLD) + '] Delete World Response')
            print_exc()
