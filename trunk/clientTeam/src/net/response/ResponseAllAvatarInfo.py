# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="kelvin"
__date__ ="$Nov 26, 2011 9:56:56 PM$"

from traceback import print_exc

from common.Constants import Constants
from net.response.ServerResponse import ServerResponse
from direct.showbase.DirectObject import DirectObject

class ResponseAllAvatarInfo(ServerResponse):

    def execute(self, data):

        self.numberOfAvatar = data.getUint16()

        try:
            self.avatars = []

            for i in range (self.numberOfAvatar):
                self.info = { 'avatarID'    : data.getUint16(),
                              'avatarType'  : data.getString(),
                              'envScore'    : data.getUint16(),
                              'charName'    : data.getString() }

                self.avatars.append(self.info)

            main.msgQ.putToMsgQ(Constants.CMSG_ALL_AVATAR_INFO, self.avatars)

            self.log('Received [' + str(Constants.SMSG_ALL_AVATAR_INFO) + '] All Avatar Info Response')

        except:
            self.log('Bad [' + str(Constants.SMSG_ALL_AVATAR_INFO) + '] All Avatar Info Response')
            print_exc()
