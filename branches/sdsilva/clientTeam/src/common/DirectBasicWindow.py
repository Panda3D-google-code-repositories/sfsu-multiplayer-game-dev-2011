#@PydevCodeAnalysisIgnore

from GameClient.common import Constants, DirectWindow, DirectBasicButton
from direct.gui.DirectGui import DGG, DirectFrame, DirectLabel
from panda3d.core import TextNode

class DirectBasicWindow(DirectWindow):

    def __init__(self, title = '', onClose = None, **kw):

        if onClose == None:
            onClose = self.hide

        self.titleBar = None
        self.rightShadow = None
        self.bottomShadow = None

        DirectWindow.__init__(self, **kw)
        self.initialiseoptions(DirectBasicWindow)

        self.titleBar = DirectFrame( frameSize = (self['frameSize'][0], self['frameSize'][1], -0.05, 0.05),
                                     frameColor = Constants.BAR_COLOR,
                                     pos = (0, 0, self['frameSize'][3] + 0.05),
                                     state = DGG.NORMAL )
        self.titleBar.reparentTo(self)

        self.titleBar.bind(DGG.B1PRESS, self.onClick)

        self.titleName = DirectLabel( text = title,
                                      text_align = TextNode.ALeft,
                                      text_fg = Constants.TEXT_COLOR,
                                      text_font = Constants.FONT_TYPE_01,
                                      text_scale = 0.045,
                                      text_shadow = Constants.TEXT_SHADOW_COLOR,
                                      frameColor = (0, 0, 0, 0),
                                      pos = (self['frameSize'][0] + 0.05, 0, -0.02) )
        self.titleName.reparentTo(self.titleBar)

        self.closeButton = DirectBasicButton( frameSize = (-0.05, 0.05, -0.025, 0.025),
                                              frameColor = (0, 0, 0, 0.2),
                                              pos = (self['frameSize'][1] - 0.1, 0, 0),
                                              relief = DGG.FLAT,
                                              command = onClose )
        self.closeButton.reparentTo(self.titleBar)

        self.rightShadow = DirectFrame( frameSize = (-0.015, 0.015, self['frameSize'][2] + 0.025, self['frameSize'][3] - 0.025),
                                        frameColor = Constants.BAR_COLOR,
                                        pos = (self['frameSize'][1] + 0.015, 0, -0.055) )
        self.rightShadow.reparentTo(self)

        self.bottomShadow = DirectFrame( frameSize = (self['frameSize'][0] + 0.05, self['frameSize'][1] - 0.05, -0.015, 0.015),
                                         frameColor = Constants.BAR_COLOR,
                                         pos = (0.05, 0, self['frameSize'][2] - 0.015) )
        self.bottomShadow.reparentTo(self)

    def setFrameSize(self, fClearFrame = 0):

        DirectWindow.setFrameSize(self, fClearFrame)

        if self.titleBar != None:
            self.titleBar['frameSize'] = (self['frameSize'][0], self['frameSize'][1], -0.05, 0.05)
            self.titleBar.setPos(0, 0, self['frameSize'][3] + 0.05)

        if self.rightShadow != None and self.bottomShadow != None:
            self.rightShadow['frameSize'] = (-0.015, 0.015, self['frameSize'][2] + 0.025, self['frameSize'][3] - 0.025)
            self.rightShadow.setPos(self['frameSize'][1] + 0.015, 0, -0.055)

            self.bottomShadow['frameSize'] = (self['frameSize'][0] + 0.05, self['frameSize'][1] - 0.05, -0.015, 0.015)
            self.bottomShadow.setPos(0.05, 0, self['frameSize'][2] - 0.015)
