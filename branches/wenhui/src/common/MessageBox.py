from direct.gui.DirectGui import DGG
from direct.gui.DirectGui import DirectLabel

from panda3d.core import TextNode

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectWindow import DirectWindow

class MessageBox:

    def __init__(self, type, text, command = None, extraArgs = []):

        self.type = type

        self.text = text
        self.command = command
        self.extraArgs = extraArgs

        self.maxWidth = 18

        self.textNode = TextNode('textNode')
        self.textNode.setText(self.text)
        self.textNode.setWordwrap(self.maxWidth)

        self.frameWidth = 0.05 * self.textNode.getWidth() / 2
        self.frameHeight = 0.06 * len(self.textNode.getWordwrappedText().split('\n')) / 2

        self.createMainFrame()
        self.createButtons()

    def createMainFrame(self):

        self.mainFrame = DirectWindow( frameSize = (-self.frameWidth - 0.095, self.frameWidth + 0.095,
                                                    -self.frameHeight - 0.16, self.frameHeight + 0.16),
                                       frameColor = Constants.BG_COLOR,
                                       pos = (0, 0, 0),
                                       state = DGG.NORMAL )
        self.mainFrame.reparentTo(aspect2d, 10)

        self.textBox = DirectLabel( text = self.text,
                                    text_align = TextNode.ALeft,
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_pos = (-self.frameWidth, self.mainFrame['frameSize'][3] - 0.13),
                                    text_scale = 0.05,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_wordwrap = self.maxWidth,
                                    frameSize = (self.mainFrame['frameSize'][0] + 0.01, self.mainFrame['frameSize'][1] - 0.01,
                                                 self.mainFrame['frameSize'][2] + 0.01, self.mainFrame['frameSize'][3] - 0.01),
                                    frameColor = (0, 0, 0, 0.3) )
        self.textBox.reparentTo(self.mainFrame)

    def createButtons(self):

        if self.type == 0:
            buttonList = ['Continue']
        else:
            buttonList = ['Yes', 'No']

        text = ''
        for button in buttonList:
            text += button + '\n'

        self.textNode.setText(text)

        buttonWidth = 0.05 * self.textNode.getWidth()
        buttonHeight = 0.05

        self.button01 = DirectBasicButton( text = buttonList[0],
                                           text_fg = Constants.TEXT_COLOR,
                                           text_font = Constants.FONT_TYPE_01,
                                           text_pos = (0, -0.015),
                                           text_scale = 0.05,
                                           text_shadow = Constants.TEXT_SHADOW_COLOR,
                                           frameSize = (-buttonWidth / 2 - 0.025, buttonWidth / 2 + 0.025,
                                                        -buttonHeight / 2 - 0.025, buttonHeight / 2 + 0.025),
                                           frameColor = (0, 0, 0, 0.2),
                                           relief = DGG.FLAT,
                                           command = self.submit )
        self.button01.reparentTo(self.mainFrame)

        if self.type == 0:
            self.button01.setPos(0, 0, self.mainFrame['frameSize'][2] + 0.11)
            self.button01['extraArgs'] = [self.extraArgs]
        else:
            self.button01.setPos(-0.04 - buttonWidth / 2, 0, self.mainFrame['frameSize'][2] + 0.11)
            self.button01['extraArgs'] = [[True] + self.extraArgs]

            self.button02 = DirectBasicButton( text = buttonList[1],
                                               text_fg = Constants.TEXT_COLOR,
                                               text_font = Constants.FONT_TYPE_01,
                                               text_pos = (0, -0.015),
                                               text_scale = 0.05,
                                               text_shadow = Constants.TEXT_SHADOW_COLOR,
                                               frameSize = (-buttonWidth / 2 - 0.025, buttonWidth / 2 + 0.025,
                                                            -buttonHeight / 2 - 0.025, buttonHeight / 2 + 0.025),
                                               frameColor = (0, 0, 0, 0.2),
                                               relief = DGG.FLAT,
                                               pos = (0.04 + buttonWidth / 2, 0, self.mainFrame['frameSize'][2] + 0.11),
                                               command = self.submit,
                                               extraArgs = [[False] + self.extraArgs] )
            self.button02.reparentTo(self.mainFrame)

    def submit(self, extraArgs = []):

        main.removeMessageBox(self)

        if self.command:
            apply(self.command, extraArgs)

    def cancel(self):

        if self.type == 1:
            self.button02.commandFunc(None)

        self.mainFrame.destroy()

    def destroy(self):
        self.mainFrame.destroy()
