#@PydevCodeAnalysisIgnore

from common.DirectControls import DirectControls
from direct.gui.DirectGui import DGG, DirectFrame

#from common.DirectControls import DirectControls

class DirectWindow(DirectFrame):

    def __init__(self,**kw):

        self.controls = DirectControls(self)
        DirectFrame.__init__(self, **kw)
        self.initialiseoptions(DirectWindow)

        self.frameColor = self['frameColor']

        self.textFieldList = []
        self.activeTextField = None

        if self['state'] == DGG.NORMAL:
            self.bind(DGG.B1PRESS, self.onClick)

        self.show()
        main.setWindow(self)

    def show(self):

        DirectFrame.show(self)
        self.setFocus()

    def hide(self):

        DirectFrame.hide(self)
        self.setFocusOut()

    def destroy(self):

        DirectFrame.destroy(self)
        self.removeControls()

        main.removeWindow(self)

    def onClick(self, param = None):

        self.setFocus()
        main.mPicker2D.startFrameDrag(self)

    def setFocus(self):
        main.setCurrentWindow(self)

    def setFocusOut(self):

        main.removeCurrentWindow(self)

    def onFocus(self):

        self.reparentTo(aspect2d)
        self['frameColor'] = self.frameColor
        self.enableControls()

    def onFocusOut(self):

        self['frameColor'] = self.frameColor
        self.disableControls()

        if self.activeTextField != None:
            self.activeTextField['focus'] = 0

    def getControls(self):

        return self.controls

    def setControls(self, controls):

        self.disableControls()
        self.controls = controls

    def removeControls(self):

        self.disableControls()
        self.controls = None

    def enableControls(self):

        if self.controls != None:
            self.controls.enable()

    def disableControls(self):

        if self.controls != None:
            self.controls.disable()

    def getTextFields(self):
        return self.textFieldList

    def getTextField(self, index):
        return self.textFieldList[index]

    def setTextField(self, text_field):

        if text_field not in self.textFieldList:
            self.textFieldList.append(text_field)

    def removeTextField(self, text_field):

        if text_field in self.textFieldList:
            self.textFieldList.remove(text_field)

            if text_field == self.activeTextField:
                self.activeTextField = None

    def getActiveTextField(self):
        return self.activeTextField

    def setActiveTextField(self, text_field):
        self.activeTextField = text_field

    def removeActiveTextField(self):
        self.activeTextField = None
