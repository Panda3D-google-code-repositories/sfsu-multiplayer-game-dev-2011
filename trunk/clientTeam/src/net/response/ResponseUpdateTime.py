from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseUpdateTime(ServerResponse):

    def execute(self, data):

        try:
            args = {'month'     : data.getUint16(),
                    'year'      : data.getUint16(),
                    'duration'  : data.getUint32(),
                    'current'   : data.getUint32(),
                    'rate'      : data.getFloat32()}

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_TIME, args)

            self.log('Received [' + str(Constants.SMSG_UPDATE_TIME) + '] Update Time Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_TIME) + '] Update Time Response')
            print_exc()
