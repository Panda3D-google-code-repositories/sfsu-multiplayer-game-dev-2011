'''
Created on Oct 22, 2011

@author: Wenhui
'''
from common.DirectControls import DirectControls

class WorldControls(DirectControls):
    
    def __init__(self, parent=None):
        
        DirectControls.__init__(self, parent)
        
        self.accept('arrow_up-up', None, [])
        self.accept('arrow_down-up', None, [])
        self.accept('arrow_left-up', None, [])
        self.accept('arrow_right-up', None, [])
        
        self.accept('arrow_up-down', None, [])
        self.accept('arrow_down-down', None, [])
        self.accept('arrow_left-down', None, [])
        self.accept('arrow_right-down', None, [])      