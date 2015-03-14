from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseGetFunctionalParameters(ServerResponse):

    def execute(self, data):

        try:
            args = {}
            args['status'] = data.getUint16()
            
            #params = {}
            if args['status'] == 0:
                args['parameterType'] = data.getUint16()
                preyListSize = data.getUint16()
                args['preyListSize'] = preyListSize 
                for i in range(preyListSize):
                    args['animalType' +str(i)] = data.getString()
                    args['percentValue' +str(i)] = data.getFloat32()
                #params[parameter] = value

            #info['params'] = params
            
            main.msgQ.putToMsgQ(Constants.CMSG_GET_FUNCTIONAL_PARAMETERS, args)

            self.log('Received [' + str(Constants.SMSG_GET_FUNCTIONAL_PARAMETERS) + '] Get Functional Parameters Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_GET_FUNCTIONAL_PARAMETERS) + '] Get Functional Parameters Response')
            print_exc()