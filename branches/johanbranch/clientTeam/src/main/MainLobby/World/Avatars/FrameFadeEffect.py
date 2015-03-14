'''
Created on Oct 10, 2011

@author: Wenhui
'''
from threading import Timer

class FrameFadeEffect:
    
    """
    This is used for notification fade out, frameColor, and textColor must be passed to __init__ method,
    if there is no text, just make up a color which will not affect the effect.
    """
    def __init__(self, frame, frameColor, textColor):
        
        self.frame = frame
        self.frameColor=frameColor
        self.textColor= textColor
        
    def startFadeIn(self):
        self.frame['frameColor']=self.createFadeInOutColor(self.frameColor, 0.1)
        self.frame.show()
        self.fadeInOneFifth()
        
    def startFadeOut(self, seconds):
        """ secondes: how many seconds the frame will stay before it starts to fade out """
        _t = Timer(seconds, self.fadeOutOneFifth)
        _t.start()
        
    def createFadeInOutColor(self, color, alpha):
    
        _color = (color[0], color[1], color[2], alpha)
        return _color
    
    def fadeOutOneFifth(self):
        self.frame['frameColor'] = self.createFadeInOutColor(self.frameColor, self.frameColor[3]*4./5.)
        self.frame['text_fg'] = self.createFadeInOutColor(self.textColor, self.textColor[3]*4./5.)
        _t = Timer(0.4, self.fadeOutTwoFifth)
        _t.start()   
    
    def fadeOutTwoFifth(self):
         
        self.frame['frameColor'] = self.createFadeInOutColor(self.frameColor,self.frameColor[3]*3./5.)
        self.frame['text_fg'] = self.createFadeInOutColor(self.textColor, self.textColor[3]*3./5.)
        _t = Timer(0.3, self.fadeOutThreeFifth)
        _t.start()      

    def fadeOutThreeFifth(self):
         
        self.frame['frameColor'] = self.createFadeInOutColor(self.frameColor,self.frameColor[3]*2./5.)
        self.frame['text_fg'] = self.createFadeInOutColor(self.textColor, self.textColor[3]*2./5.)
        _t = Timer(0.2, self.fadeOutFourFifth)
        _t.start()  
          
    def fadeOutFourFifth(self):
        self.frame['frameColor'] = self.createFadeInOutColor(self.frameColor,self.frameColor[3]/5.)
        self.frame['text_fg'] = self.createFadeInOutColor(self.textColor, self.textColor[3]/5.)
        _t = Timer(0.1, self.hideFrame)
        _t.start() 
         
    def hideFrame(self):
        self.frame.hide() 
        
    """ *************** Frame fade in effect ************************** """
    def fadeInOneFifth(self):
        self.frame['frameColor'] = self.createFadeInOutColor(self.frameColor, self.frameColor[3]*1./5.)
        self.frame['text_fg'] = self.createFadeInOutColor(self.textColor, self.textColor[3]*1./5.)
        _t = Timer(0.2, self.fadeInTwoFifth)
        _t.start()   
    
    def fadeInTwoFifth(self):
         
        self.frame['frameColor'] = self.createFadeInOutColor(self.frameColor,self.frameColor[3]*2./5.)
        self.frame['text_fg'] = self.createFadeInOutColor(self.textColor, self.textColor[3]*2./5.)
        _t = Timer(0.2, self.fadeInThreeFifth)
        _t.start()      

    def fadeInThreeFifth(self):
         
        self.frame['frameColor'] = self.createFadeInOutColor(self.frameColor,self.frameColor[3]*3./5.)
        self.frame['text_fg'] = self.createFadeInOutColor(self.textColor, self.textColor[3]*3./5.)
        _t = Timer(0.2, self.fadeInFourFifth)
        _t.start()  
          
    def fadeInFourFifth(self):
        self.frame['frameColor'] = self.createFadeInOutColor(self.frameColor,self.frameColor[3]*4./5.)
        self.frame['text_fg'] = self.createFadeInOutColor(self.textColor, self.textColor[3]*4./5.)
        _t = Timer(0.2, self.fadeInComplete)
        _t.start() 
        
    def fadeInComplete(self):
        self.frame['frameColor'] = self.frameColor
        self.frame['text_fg'] = self.textColor 
         
