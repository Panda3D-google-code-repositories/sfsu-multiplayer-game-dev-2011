from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeParameters(ServerResponse):

    def execute(self, data):

        try:
            info = {'status' : data.getUint16()}

            params = {}
            for i in range(data.getUint16()):
                parameter = data.getUint16()
                value = data.getFloat32()
                params[parameter] = value

            info['params'] = params

            main.msgQ.putToMsgQ(Constants.CMSG_CHANGE_PARAMETERS, info)

            self.log('Received [' + str(Constants.SMSG_CHANGE_PARAMETERS) + '] Change Parameters Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_CHANGE_PARAMETERS) + '] Change Parameters Response')
            print_exc()