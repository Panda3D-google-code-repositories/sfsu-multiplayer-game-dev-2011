from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseChat(ServerResponse):

    def execute(self, data):

        try:
            status = data.getUint16()

            if status == 0:
                args = {'type' : data.getUint16()}

                if args['type'] == 0:
                    args['name'] = data.getString()
                    args['message'] = data.getString()
                else:
                    args['message'] = data.getString()

                main.msgQ.putToMsgQ(Constants.SMSG_CHAT, args)

            self.log('Received [' + str(Constants.SMSG_CHAT) + '] Chat Response')   
        except:
            self.log('Bad [' + str(Constants.SMSG_CHAT) + '] Chat Response')
            print_exc()
