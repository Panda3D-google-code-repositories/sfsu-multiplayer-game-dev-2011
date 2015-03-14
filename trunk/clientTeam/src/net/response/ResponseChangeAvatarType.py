from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChangeAvatarType(ServerResponse):

    def execute(self, data):

        try:
            status = data.getUint16()

            if status == 0:
                info = {'avatar_id'     : data.getUint32(),
                        'level'         : data.getUint16(),
                        'min_exp'       : data.getUint32(),
                        'max_exp'       : data.getUint32(),
                        'xp'            : data.getUint32(),
                        'gold'          : data.getUint32()}

                main.msgQ.addToPendingObj(Constants.SMSG_CHANGE_AVATAR_TYPE, info)

                self.log('Received [' + str(Constants.SMSG_CHANGE_AVATAR_TYPE) + '] Change Avatar Type Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_CHANGE_AVATAR_TYPE) + '] Change Avatar Type Response')
            print_exc()
