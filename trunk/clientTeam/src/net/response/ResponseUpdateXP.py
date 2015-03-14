from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseUpdateXP(ServerResponse):

    def execute(self, data):

        try:
            info = {'amount'    : data.getUint32(),
                    'total'     : data.getUint32()}

            main.msgQ.putToMsgQ(Constants.SMSG_UPDATE_XP, info)

            self.log('Received [' + str(Constants.SMSG_UPDATE_XP) + '] Update XP Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_UPDATE_XP) + '] Update XP Response')
            print_exc()
