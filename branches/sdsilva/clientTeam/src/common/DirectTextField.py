#@PydevCodeAnalysisIgnore
from direct.gui.DirectGui import DirectEntry

class DirectTextField(DirectEntry):

    def __init__(self, window, parent = None, **kw):

        self.window = window

        DirectEntry.__init__(self, parent, **kw)
        self.initialiseoptions(DirectTextField)

        self.isFocus = False

    def destroy(self):

        DirectEntry.destroy(self)
        self.window.removeTextField(self)

    def focusInCommandFunc(self):

        DirectEntry.focusInCommandFunc(self)
        self.isFocus = True

        self.window.setActiveTextField(self)
        self.window.setFocus()

        main.getGlobalControls().disable()
        main.disableGameControls()

    def focusOutCommandFunc(self):

        DirectEntry.focusOutCommandFunc(self)
        self.isFocus = False

        self.window.removeActiveTextField()

        main.getGlobalControls().enable()
        main.enableGameControls()

    def getFocus(self):
        return self.isFocus
