from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseLogin(ServerResponse):

    def execute(self, data):

        try:
            #1 = wrong userName or password#2 = account is being used#3 = other error
            args = {'status' : data.getUint16()}

            if args['status'] == 0:
                args['user_id'] = data.getUint32()
                args['name'] = data.getString()

                avatarList = []

                for i in range(data.getUint16()):
                    avatar_id = data.getUint32()
                    name = data.getString()
                    level = data.getUint16()
                    currency = data.getUint32()
                    last_played = data.getString().split('.')[0]

                    avatarList.append((avatar_id, name, level, currency, last_played))

                args['avatarList'] = avatarList

                worldList = []

                for i in range(data.getUint16()):
                    world_id = data.getUint32()
                    name = data.getString()

                    if not data.getBool():
                        year = data.getUint16()
                        month = data.getUint16()
                        play_time = data.getUint32()
                        score = data.getUint32()

                        worldList.append((world_id, name, year, month, play_time, score))
                    else:
                        worldList.append((world_id, name))

                args['worldList'] = worldList

            main.msgQ.putToMsgQ(Constants.CMSG_AUTH, args)

            self.log('Received [' + str(Constants.SMSG_AUTH) + '] Authentication Response')
            taskMgr.doMethodLater(0.01, self.main.updateRoutine, 'updateRoutine-Main')
        except:
            self.log('Bad [' + str(Constants.SMSG_AUTH) + '] Authentication Response')
            print_exc()
