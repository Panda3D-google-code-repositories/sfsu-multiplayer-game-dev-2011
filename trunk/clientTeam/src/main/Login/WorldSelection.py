from calendar import month_name

from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DGG

from panda3d.core import TextNode
from panda3d.core import TransparencyAttrib

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel
from common.DirectDropDownMenu import DirectDropDownMenu
from common.DirectWindow import DirectWindow

class WorldSelection:

    def __init__(self, parent):

        self.parent = parent

        self.avatarList = []
        self.worldList = []

        self.msgBox = None

        self.aLabelList = []
        self.wLabelList = []
        self.buttonList = []

        self.selectionList = []

        self.createMainFrame()
        self.createAvatar()
        self.createAvatarDescription()
        self.createWorldDescription()
        self.createSelectionMenu()
        self.createButtons()

        main.msgQ.addToCommandList(Constants.SMSG_CREATE_NEW_WORLD, self.responseCreateWorld)
        main.msgQ.addToCommandList(Constants.SMSG_DELETE_WORLD, self.responseDeleteWorld)

    def createMainFrame(self):

        self.mainFrame = DirectWindow( frameSize = (-0.61, 0.61, -0.41, 0.41),
                                       frameColor = Constants.BG_COLOR,
                                       pos = (0, 0, 0) )

        self.mainBox = DirectFrame( frameSize = (-0.6, 0.6, -0.4, 0.4),
                                    frameColor = (0, 0, 0, 0.25),
                                    pos = (0, 0, 0) )
        self.mainBox.reparentTo(self.mainFrame)

        self.mainLabel = DirectBasicLabel ( text = 'World Selection',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.055,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameColor = (0, 0, 0, 0),
                                            pos = (0, 0, 0.325) )
        self.mainLabel.reparentTo(self.mainBox)

        self.closeButtonFrame = DirectFrame( frameSize = (-0.031, 0.031, -0.031, 0.031),
                                             frameColor = Constants.BG_COLOR,
                                             pos = (0.55, 0, 0.35) )
        self.closeButtonFrame.reparentTo(self.mainBox)

        self.closeButton = DirectBasicButton( frameSize = (-0.025, 0.025, -0.025, 0.025),
                                              frameColor = (0, 0, 0, 0.2),
                                              pos = (0, 0, 0),
                                              command = self.closeWindow,
                                              rolloverSound = None,
                                              clickSound = None )
        self.closeButton.reparentTo(self.closeButtonFrame)

    def closeWindow(self):
        return
        main.cManager.sendRequest(Constants.CMSG_SAVE_EXIT_GAME)

        self.hide()
        self.parent.mainFrame.show()

    def createAvatar(self):

        self.avatarFrame = DirectFrame( frameSize = (-0.126, 0.126, -0.126, 0.126),
                                        frameColor = Constants.BG_COLOR,
                                        pos = (-0.28, 0, 0.125) )
        self.avatarFrame.reparentTo(self.mainFrame)

        avatar = 'models/avatar/1a.png'
        self.avatarBox = DirectBasicButton( image = avatar,
                                            image_pos = (0, 0, 0),
                                            image_scale = (0.1, 0.1, 0.1),
                                            frameSize = (-0.12, 0.12, -0.12, 0.12),
                                            frameColor = (0, 0, 0, 0.2),
                                            pos = (0, 0, 0),
                                            command = self.changeAvatar,
                                            rolloverSound = None,
                                            clickSound = None )
        self.avatarBox.setTransparency(TransparencyAttrib.MAlpha)
        self.avatarBox.reparentTo(self.avatarFrame)

    def changeAvatar(self):
        pass

    def createAvatarDescription(self):

        for i in range(4):
            basicLabel = DirectBasicLabel ( text = '',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameColor = (0, 0, 0, 0),
                                            pos = (0, 0, 0) )
            basicLabel.reparentTo(self.mainBox)
            self.aLabelList.append(basicLabel)

        self.aLabelList[0]['text'] = 'N/A'
        self.aLabelList[0]['text_align'] = TextNode.ALeft
        self.aLabelList[0].setPos(-0.08, 0, 0.215)

        self.aLabelList[1]['text'] = 'N/A'
        self.aLabelList[1]['text_align'] = TextNode.ALeft
        self.aLabelList[1].setPos(0.27, 0, 0.215)

        self.aLabelList[2]['text'] = 'N/A'
        self.aLabelList[2]['text_align'] = TextNode.ACenter
        self.aLabelList[2].setPos(0.18, 0, 0.15)

        self.aLabelList[3]['text'] = 'Last Played on N/A'
        self.aLabelList[3]['text_align'] = TextNode.ACenter
        self.aLabelList[3]['text_scale'] = 0.04
        self.aLabelList[3].setPos(0.18, 0, 0.05)

    def setAvatarList(self, avatarList):

        self.avatarList = avatarList

        if len(self.avatarList) > 0:
            self.selectAvatar(0)

    def selectAvatar(self, index):

        avatar = self.avatarList[index]
        # (avatar_id, name, level, currency, last_played)
        self.aLabelList[0]['text'] = avatar[1]
        self.aLabelList[1]['text'] = 'Level ' + str(avatar[2])
        self.aLabelList[2]['text'] = str(avatar[3]) + ' G'

        date = avatar[4].split(' ')[0].split('-')
        self.aLabelList[3]['text'] = 'Last Played on ' + str(date[1] + '-' + date[2] + '-' + date[0])

        args = {'avatar_id' : avatar[0]}
        main.cManager.sendRequest(Constants.CMSG_CHANGE_AVATAR_TYPE, args)

    def createSelectionMenu(self):

        self.selectionMenu = DirectDropDownMenu( frameColor = Constants.BG_COLOR,
                                                 width = 0.7,
                                                 max_items = 10,
                                                 direction = 'down',
                                                 command = self.selectWorld )
        self.selectionMenu.reparentTo(self.mainBox)
        self.selectionMenu.setPos(-0.15, 0, -0.1)

    def setOption(self, option):

        self.selectionMenu.setItem(option)
        self.selectionList.append(option)

        if len(self.selectionList) == 1:
            self.selectionMenu.selectOptionByIndex(0)

    def setOptions(self, optionList):

        for option in optionList:
            self.setOption(option)

    def createWorldDescription(self):

        for i in range(3):
            basicLabel = DirectBasicLabel ( text = '',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameColor = (0, 0, 0, 0),
                                            pos = (0, 0, 0) )
            basicLabel.reparentTo(self.mainBox)
            self.wLabelList.append(basicLabel)

        self.wLabelList[0]['text'] = 'Not Available'
        self.wLabelList[0]['text_align'] = TextNode.ALeft
        self.wLabelList[0].setPos(-0.5, 0, -0.225)

        self.wLabelList[1]['text'] = 'Not Available'
        self.wLabelList[1]['text_align'] = TextNode.ARight
        self.wLabelList[1].setPos(0.19, 0, -0.225)

        self.wLabelList[2]['text'] = 'Not Available'
        self.wLabelList[2]['text_align'] = TextNode.ACenter
        self.wLabelList[2].setPos(-0.15, 0, -0.3)

    def setWorldList(self, worldList):

        self.worldList = worldList

        optionList = []
        for world in worldList:
            optionList.append('World ' + str(world[0]))
        self.setOptions(optionList)

        if len(self.selectionList) > 0:
            self.selectionMenu.selectOptionByIndex(0)
        else:
            for i in range(len(self.buttonList)):
                if i != 1:
                    button = self.buttonList[i]
                    button[1]['text_fg'] = Constants.TEXT_D_COLOR
                    button[1]['text_shadow'] = (0, 0, 0, 0)
                    button[1]['state'] = DGG.DISABLED

    def selectWorld(self, index):

        world = self.worldList[index]

        if len(world) == 2:
            # (world_id, name)
            self.wLabelList[0]['text'] = 'Not Available'
            self.wLabelList[1]['text'] = 'Not Available'
            self.wLabelList[2]['text'] = 'Not Available'
        else:
            # (world_id, name, year, month, play_time, score)
            self.wLabelList[0]['text'] = month_name[world[3]] + ' \'%02d' % world[2]
            self.wLabelList[1]['text'] = 'Played ' + str(round(world[4] / 3600.0, 1)) + ' Hrs'
            self.wLabelList[2]['text'] = 'Score: ' + str(world[5])

    def createButtons(self):

        for i in range(3):
            buttonFrame = DirectFrame( frameSize = (-0.106, 0.106, -0.046, 0.046),
                                       frameColor = Constants.BG_COLOR,
                                       pos = (0, 0, 0) )
            buttonFrame.reparentTo(self.mainBox)

            basicButton = DirectBasicButton( text = '',
                                             text_fg = Constants.TEXT_COLOR,
                                             text_font = Constants.FONT_TYPE_01,
                                             text_pos = (0, -0.015),
                                             text_scale = 0.045,
                                             text_shadow = Constants.TEXT_SHADOW_COLOR,
                                             frameSize = (-0.1, 0.1, -0.04, 0.04),
                                             frameColor = (0, 0, 0, 0.2),
                                             pos = (0, 0, 0),
                                             command = self.submit,
                                             extraArgs = [i],
                                             rolloverSound = None,
                                             clickSound = None )
            basicButton.reparentTo(buttonFrame)

            self.buttonList.append((buttonFrame, basicButton))

        self.buttonList[0][1]['text'] = 'Join'
        self.buttonList[0][0].setPos(0.4, 0, -0.1)

        self.buttonList[1][1]['text'] = 'Create'
        self.buttonList[1][0].setPos(0.4, 0, -0.2)

        self.buttonList[2][1]['text'] = 'Delete'
        self.buttonList[2][0].setPos(0.4, 0, -0.3)

    def submit(self, value):

        if value == 0:
            name = self.worldList[self.selectionMenu.getCurrentIndex()][1]

            args = {'worldName' : name, 
                    'password'  : ''}
            main.cManager.sendRequest(Constants.CMSG_JOIN_PVE_WORLD, args)

            main.createMessageBox(2, 'Joining World...')
        elif value == 1:
            args = {'worldType'       : 1,
                    'worldName'       : '.random',
                    'ecosystem'       : 'Savanna', 
                    'maxPlayerNumber' : 100,
                    'privacyType'     : 1,
                    'password'        : ''}
            main.cManager.sendRequest(Constants.CMSG_CREATE_NEW_WORLD, args)

            self.msgBox = main.createMessageBox(2, 'Creating World...')
        elif value == 2:
            world_id = self.worldList[self.selectionMenu.getCurrentIndex()][0]

            args = {'world_id' : world_id }
            main.cManager.sendRequest(Constants.CMSG_DELETE_WORLD, args)

            self.msgBox = main.createMessageBox(2, 'Deleting World...')

        for button in self.buttonList:
            button[1]['text_fg'] = Constants.TEXT_D_COLOR
            button[1]['text_shadow'] = (0, 0, 0, 0)
            button[1]['state'] = DGG.DISABLED

        self.parent.blackFrame.reparentTo(self.mainFrame, 1)
        self.parent.blackFrame.show()

    def responseCreateWorld(self, args):

        if args['status'] == 0:
            self.worldList.append((args['world_id'], args['name']))
            self.setOption('World ' + str(args['world_id']))
            self.selectionMenu.selectOptionByIndex(len(self.worldList) - 1)

            for button in self.buttonList:
                button[1]['text_fg'] = Constants.TEXT_COLOR
                button[1]['text_shadow'] = Constants.TEXT_SHADOW_COLOR
                button[1]['state'] = DGG.NORMAL

            main.removeMessageBox(self.msgBox)
            main.createMessageBox(0, 'World Created')
        else:
            for i in range(len(self.buttonList)):
                if i == 1 or len(self.selectionList) > 0:
                    button = self.buttonList[i]
                    button[1]['text_fg'] = Constants.TEXT_COLOR
                    button[1]['text_shadow'] = Constants.TEXT_SHADOW_COLOR
                    button[1]['state'] = DGG.NORMAL

            main.createMessageBox(0, 'Failed to Create World')

        self.parent.blackFrame.hide()

    def responseDeleteWorld(self, args):

        if args['status'] == 0:
            for world in self.worldList:
                if world[0] == args['world_id']:
                    index = self.worldList.index(world)

                    for label in self.wLabelList:
                        label['text'] = 'Not Available'

                    del self.worldList[index]
                    self.selectionMenu.removeOption(index)
                    del self.selectionList[index]
                    break

            for i in range(len(self.buttonList)):
                if i == 1 or len(self.selectionList) > 0:
                    button = self.buttonList[i]
                    button[1]['text_fg'] = Constants.TEXT_COLOR
                    button[1]['text_shadow'] = Constants.TEXT_SHADOW_COLOR
                    button[1]['state'] = DGG.NORMAL

            main.removeMessageBox(self.msgBox)
            main.createMessageBox(0, 'World Deleted')
        else:
            main.createMessageBox(0, 'Failed to Delete World')

        self.parent.blackFrame.hide()

    def show(self):
        self.mainFrame.show()

    def hide(self):
        self.mainFrame.hide()

    def setPos(self, x, y, z):
        self.mainFrame.setPos(x, y, z)

    def destroy(self):
        self.mainFrame.destroy()
