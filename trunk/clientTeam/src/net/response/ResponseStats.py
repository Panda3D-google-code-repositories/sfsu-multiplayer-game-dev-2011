'''
Created on Apr 14, 2012

@author: hunvil
'''
# To change this template, choose Tools | Templates
# and open the template in the editor.

from traceback import print_exc

from common.Constants import Constants
#@PydevCodeAnalysisIgnore
from net.response.ServerResponse import ServerResponse

class ResponseStats(ServerResponse):

    def execute(self, data):
        print 'ResponseStats Execute'
        try:
            status = data.getUint16()

            if status == 0: 
                self.numberOfStats = data.getUint16()
                self.statList = []
                for i in range (self.numberOfStats):
                    activityDay  = data.getUint16()
                    animalName   = data.getString()
                    activityType = data.getString()
                    count        = data.getUint16()
                    #envScore     = data.getUint32()                                 
                    #activityMsg  = data.getString()
    
                    self.info = (activityDay,animalName,activityType,count)
                    self.statList.append(self.info)

                print self.statList    
                main.msgQ.putToMsgQ(Constants.SMSG_STATISTICS, self.statList)

                self.log('Received [' + str(Constants.SMSG_STATISTICS) + '] Statistics')
            else:
                self.log('Failed [' + str(Constants.SMSG_STATISTICS) + '] Statistics')

        except:
            self.log('Bad [' + str(Constants.SMSG_STATISTICS) + '] Statistics')
            print_exc()

