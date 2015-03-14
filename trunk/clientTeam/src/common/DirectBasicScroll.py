'''
Created on Oct 16, 2011

@author: Wenhui
'''
from direct.gui.DirectSlider import DirectSlider

class DirectBasicScroll(DirectSlider):
    
    def __init__(self, maxItemsVisible, scrollCommand, **kw):
        """
        Obj is a list of object to display
        """
        DirectSlider.__init__(self, **kw)
        
        self.maxItemsVisible = maxItemsVisible
        self.lenght = 0
        self.scrollCommand = scrollCommand
        self['command'] = self.scroll()
#        self.bind(self['command'], self.scroll())
        
    def updateObject(self, lenght):
        """
        Len is the lenght of the list
        """
        self.lenght = lenght
        self.updateScrollBar()
        return int(round(self['value']))
    
    def computeMaxItemsVisible(self):
        
        if self.lenght < self.maxItemsVisible:
            maxItems = self.lenght
        else:
            maxItems = self.maxItemsVisible 
            
        return maxItems
    
    def scroll(self):
        """
        This will scroll the list
        """
#        if len(holders) != len(kws) or len(holders) != len(values):
#            print 'the lenght of holder must match key words and values '
#            return;
        
#        maxItems = self.computeMaxItemsVisible()
#        
#        
#                
#        for i in range(maxItems):
#            if self.lenght > self.maxItemsVisible:
#                index = sliderValue + 1
#            else:
#                index = i
#            print 'scroll list'    
        apply(self.scrollCommand, [])
                
#                self.gameList[i]['game']['text'] = self.gameLog[sliderValue + i].gameName
#                self.gameList[i]['player']['text'] = self.gameLog[sliderValue + i].players
#                self.gameList[i]['ecosystem']['text'] = self.gameLog[sliderValue + i].ecosystem
            
#                self.gameList[i]['game']['text'] = self.gameLog[i].gameName
#                self.gameList[i]['player']['text'] = self.gameLog[i].players
#                self.gameList[i]['ecosystem']['text'] = self.gameLog[i].ecosystem
    def updateScrollBar(self):
        
        if self.lenght > self.maxItemsVisible:
            if self.isHidden():
                self.show()
            scrollRange = self.lenght - self.maxItemsVisible
            
            currentSize=self['thumb_frameSize'][3]-self['thumb_frameSize'][2]
            if currentSize > 0.2:
                scrollRatio = float(self.maxItemsVisible)/self.lenght
                if (scrollRatio * currentSize) > 0.2:
                    self['thumb_frameSize'] = (self['thumb_frameSize'][0], self['thumb_frameSize'][1],
                                           self['frameSize'][2]*scrollRatio,
                                           self['frameSize'][3]*scrollRatio)
                else:
                    self['thumb_frameSize'] = (self['thumb_frameSize'][0], self['thumb_frameSize'][1],
                                           -0.1, 0.1)
        else:
            self.hide()
            scrollRange = 1

#        lastRange = self.scrollBar1['range'][0]
        self['range'] = (scrollRange, 0)