from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseUpdateLevel(ServerResponse):

    def execute(self, data):
        
        try:
            info = {'amount'    : data.getUint16(),
                    'level'     : data.getUint16(),
                    'range'     : map(int, data.getString().split(','))}

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_LEVEL, info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_LEVEL) + '] Update Level Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_LEVEL) + '] Update Level Response')
            print_exc()
