# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 19, 2011 12:57:06 AM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseWeatherPrediction(ServerResponse):

    def execute(self, data):

        try:
            self.info = { 'day'          : data.getUint16(),
                          'lightOutput'  : data.getUint16(),
                          'rainOutput'   : data.getUint16() }

            main.msgQ.putToMsgQ(SMSG_WEATHER_PREDICTION, self.info)

            self.log('Received [' + str(Constants.SMSG_WEATHER_PREDICTION) + '] Weather Prediction Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_WEATHER_PREDICTION) + '] Weather Prediction Response')
            print_exc()
