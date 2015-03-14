'''
Created on Oct 16, 2011

@author: Wenhui
'''
from common.DirectControls import DirectControls

class GameShopControl(DirectControls):
    
    def __init__(self, parent):

        DirectControls.__init__(self, parent)

        self.accept('mouse1', parent.startItemDrag, [])
        self.accept('mouse1-up', parent.stopItemDrag, [])
    
    