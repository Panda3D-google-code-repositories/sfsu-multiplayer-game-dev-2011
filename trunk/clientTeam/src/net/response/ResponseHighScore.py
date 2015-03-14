from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse

class ResponseHighScore(ServerResponse):

    def execute(self, data):

        try:
            args = {'type' : data.getUint16()}

            scoreList = []
            for i in range(data.getUint16()):
                scoreList.append((data.getString(), data.getUint32()))
            args['scoreList'] = scoreList

            totalScoreList = []
            for i in range(data.getUint16()):
                totalScoreList.append((data.getString(), data.getUint32()))
            args['totalScoreList'] = totalScoreList

            currentScoreList = []
            for i in range(data.getUint16()):
                currentScoreList.append((data.getString(), data.getUint32()))
            args['currentScoreList'] = currentScoreList

            main.msgQ.putToMsgQ(Constants.SMSG_HIGH_SCORE, args)

            self.log('Received [' + str(Constants.SMSG_HIGH_SCORE) + '] High Score Response')
        except:
            self.log('Bad [' + str(Constants.SMSG_HIGH_SCORE) + '] High Score Response')
            print_exc()
