#@PydevCodeAnalysisIgnore

from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectWindow import DirectWindow
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from panda3d.core import TransparencyAttrib

class Weather:
    
    """ Request weather prediction from game logic; 
        weather type:
        0 -> sunny
        1 -> cloudiness
        2 -> rain
        
        weather prediction:
        0 -> 3 days
        1 -> 7 days
        2 -> 14 days
        3 -> 21 days
        4 -> 28 days
        
        Change weather prediction from 3 days to 7 days by changing the variable CURRENT_PREDICTION from 0 to 1
    """
    
    def __init__(self, parent):
        
        self.parent = parent
        self.days = []
        self.weathers = []
        self.CURRENT_PREDICTION = 4;
        
        self.loadPrediction()
        self.loadWeatherImages()
        self.createMainFrame()
        self.createWeatherImage()
        self.createWeatherLabel()
        self.createViewMoreButton()
        self.createWeatherPrediction()
        
    def createMainFrame(self):
        self.mainFrame = DirectWindow(frameSize=(-0.2, 0.2, -0.19, 0.19),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(0.2, 0, -0.81))
        
        self.mainFrame.reparentTo(self.parent)
    
    def loadWeatherImages(self):
        
        _weatherDirectory = 'models/weathers/'
        self.weathers.append(_weatherDirectory + 'Sunny.png')
        self.weathers.append(_weatherDirectory + 'Cloud.png')
        self.weathers.append(_weatherDirectory + 'rain.png')
    
    def loadPrediction(self):
        """ Load prediction from Server """
        self.prediction = [0,1,2,1,0,2,0,1,2,0,0,2,1,0,0,2,0,1,2,0,2,1,0,0,2,1,0,0,2,0,1,0]
        
    def createWeatherImage(self):
        """ create weather image for mainFrame """
        
        _imageDirectory = "models/weathers/Cloud.png"
        self.weather = DirectLabel(image=_imageDirectory,
                                   image_pos=(0, 0, 0),
                                   image_scale=(0.08, 0.08, 0.08),
                                   frameSize=(-0.38, 0.38, -0.1, 0.1),
                                   frameColor=(0, 0, 0, 0),
                                   pos=(0, 0, 0.01))
        self.weather.setTransparency(TransparencyAttrib.MAlpha)
        self.weather.reparentTo(self.mainFrame)
        
    def createWeatherLabel(self):
        
        self.weatherLabel = DirectLabel(text='Weather',
                                        text_scale=0.06,
                                        text_pos=(0, -0.025),
                                        text_fg = Constants.TEXT_COLOR,
                                        text_font = Constants.FONT_TYPE_01,
                                        text_shadow = Constants.TEXT_SHADOW_COLOR,
                                        frameSize=(-0.2, 0.2, -0.04, 0.04),
                                        pos=(0, 0, 0.15),
                                        frameColor=(0, 0, 0, 0))
        self.weatherLabel.reparentTo(self.mainFrame)

    def createViewMoreButton(self):
        
        self.viewMoreButton = DirectBasicButton(text='View More',
                                                text_scale=0.04,
                                                text_pos=(0, -0.01),
                                                text_fg = Constants.TEXT_COLOR,
                                                text_font = Constants.FONT_TYPE_01,
                                                text_shadow = Constants.TEXT_SHADOW_COLOR,                                                
                                                frameSize=(-0.13, 0.13, -0.04, 0.04),
                                                frameColor=(0, 0, 0, 0.2),
                                                pos=(0, 0, -0.13),
                                                relief=DGG.FLAT,
                                                state=DGG.NORMAL,
                                                command=self.showPrediction)
        self.viewMoreButton.setTransparency(TransparencyAttrib.MAlpha)
        self.viewMoreButton.reparentTo(self.mainFrame)
    
        
    def createThreeDaysPrediction(self):
        """
        create title, hide button, and 3 days weather prediction
        """
        self.threeDaysFrame = DirectWindow(frameSize=(-0.5, 0.5, -0.2, 0.2),
                                           frameColor=Constants.BG_COLOR,
                                           pos=(0, 0, 0.2),
                                           state=DGG.NORMAL)
        self.threeDaysFrame.reparentTo(self.parent)
        self.threeDaysFrame.hide()
        self.threeDaysLabel = DirectLabel(text='Weather prediction of next 3 days',
                                        text_scale=0.05,
                                        text_pos=(0, -0.02),
                                        text_fg = Constants.TEXT_COLOR,
#                                        text_font = Constants.FONT_TYPE_01,
                                        text_shadow = Constants.TEXT_SHADOW_COLOR,                                       
                                        frameSize=(-0.2, 0.2, -0.04, 0.04),
                                        pos=(0, 0, 0.14),
                                        frameColor=(0, 0, 0, 0))
        self.threeDaysLabel.reparentTo(self.threeDaysFrame)
        
        self.hideButton3 = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(0.44, 0, 0.16),
                                       relief=DGG.FLAT,
                                       command=self.hideThreeDaysFrame)
        self.hideButton3.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton3.reparentTo(self.threeDaysFrame)
        
        for i in range(3):
            self.days.append(DirectLabel(image=self.weathers[self.prediction[i]],
                                         text=str(i+1),
                                         text_scale=0.05,
                                         text_pos=(0.065, -0.08),
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,      
                                         image_pos=(0, 0, 0),
                                         image_scale=(0.09, 0.09, 0.09),
                                         frameSize=(-0.28, 0.28, -0.1, 0.1),
                                         frameColor=(1, 1, 1, 0),
                                         pos=(-0.3 + i * 0.3, 0, -0.05)))
            self.days[i].setTransparency(TransparencyAttrib.MAlpha)
            self.days[i].reparentTo(self.threeDaysFrame)
    
    def createWeatherPrediction(self):
        
        if self.CURRENT_PREDICTION == 0:
            self.createThreeDaysPrediction()
        elif self.CURRENT_PREDICTION == 1:
            self.createSevenDaysPrediction()
        elif self.CURRENT_PREDICTION == 2:
            self.create14DaysPrediction()
        elif self.CURRENT_PREDICTION == 3:
            self.create21DaysPrediction()
        elif self.CURRENT_PREDICTION == 4:
            self.create28DaysPrediction()
              
    def showPrediction(self):
        """ 0 -> 3 days; 1 -> 7 days, 2 -> 14 days, 3 -> 21 days, 4 -> 28 days """
        # This block is to test the upgrade function
        if self.CURRENT_PREDICTION == 0:
            self.upgradeWeatherPrediction(1)
        elif self.CURRENT_PREDICTION == 1:
            self.upgradeWeatherPrediction(2)
        elif self.CURRENT_PREDICTION == 2:
            self.upgradeWeatherPrediction(3)
        elif self.CURRENT_PREDICTION == 3:
            self.upgradeWeatherPrediction(4)
        elif self.CURRENT_PREDICTION == 4:
            self.upgradeWeatherPrediction(0)
    
        if self.CURRENT_PREDICTION == 0:
            self.showThreeDaysFrame()
        elif self.CURRENT_PREDICTION == 1:
            self.showSevenDaysFrame()
        elif self.CURRENT_PREDICTION == 2:
            self.show14DaysFrame()
        elif self.CURRENT_PREDICTION == 3:
            self.show21DaysFrame()
        elif self.CURRENT_PREDICTION == 4:
            self.show28DaysFrame()
            
    def hideThreeDaysFrame(self):
        self.threeDaysFrame.hide()
    
    def showThreeDaysFrame(self):
        self.threeDaysFrame.show()     
        
    def createSevenDaysPrediction(self):
        """
        create title, hide button, and seven days weather prediction
        """
        self.sevenDaysFrame = DirectWindow(frameSize=(-1, 1, -0.2, 0.2),
                                           frameColor=Constants.BG_COLOR,
                                           pos=(0, 0, 0.2),
                                           state=DGG.NORMAL)
        self.sevenDaysFrame.reparentTo(self.parent)
        self.sevenDaysFrame.hide()
        
        self.sevenDaysLabel = DirectLabel(text='Weather prediction of next 7 days',
                                        text_scale=0.06,
                                        text_pos=(0, -0.02),
                                        text_fg = Constants.TEXT_COLOR,
#                                        text_font = Constants.FONT_TYPE_01,
                                        text_shadow = Constants.TEXT_SHADOW_COLOR,
                                        frameSize=(-0.2, 0.2, -0.04, 0.04),
                                        pos=(0, 0, 0.135),
                                        frameColor=(0, 0, 0, 0))
        
        self.sevenDaysLabel.reparentTo(self.sevenDaysFrame)
        
        self.hideButton7 = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(0.94, 0, 0.16),
                                       relief=DGG.FLAT,
                                       command=self.hideSevenDaysFrame)
        self.hideButton7.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton7.reparentTo(self.sevenDaysFrame)
        
        for i in range(7):
            self.days.append(DirectLabel(image=self.weathers[self.prediction[i]],
                                         text=str(i+1),
                                         text_scale=0.05,
                                         text_pos=(0.06, -0.08),
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         image_pos=(0, 0, 0),
                                         image_scale=(0.09, 0.09, 0.09),
                                         frameSize=(-0.28, 0.28, -0.1, 0.1),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.81 + i * 0.27, 0, -0.05)))
            self.days[i].setTransparency(TransparencyAttrib.MAlpha)
            self.days[i].reparentTo(self.sevenDaysFrame)
        
    def hideSevenDaysFrame(self):
        self.sevenDaysFrame.hide()
    
    def showSevenDaysFrame(self):
        self.sevenDaysFrame.show()
     
    def destroyFrame(self):
        
        if self.CURRENT_PREDICTION == 0:
            self.threeDaysFrame.destroy()
        elif self.CURRENT_PREDICTION == 1:
            self.sevenDaysFrame.destroy()
        elif self.CURRENT_PREDICTION == 2:
            self.daysFrame14.destroy()
        elif self.CURRENT_PREDICTION == 3:
            self.daysFrame21.destroy()
        elif self.CURRENT_PREDICTION == 4:
            self.daysFrame28.destroy()
        else:
            return False
        return True
    
    def upgradeWeatherPrediction(self, index):
        """ 
        upgrade weather prediction, first destroy the current weather prediction frame, then
        create the new weather frame 
        """
        if self.destroyFrame():
            del self.days[0:len(self.days)]    
            self.CURRENT_PREDICTION = index
            self.createWeatherPrediction()
        
    def create14DaysPrediction(self):
        
        self.daysFrame14 = DirectWindow(frameSize=(-1, 1, -0.35, 0.35),
                                           frameColor=Constants.BG_COLOR,
                                           pos=(0, 0, 0.2),
                                           state=DGG.NORMAL)
        self.daysFrame14.reparentTo(self.parent)
        self.daysFrame14.hide()
        
        self.daysLabel14 = DirectLabel(text='weather prediction of next 14 days',
                                        text_scale=0.065,
                                        text_pos=(0, -0.02),
                                        text_fg = Constants.TEXT_COLOR,
#                                        text_font = Constants.FONT_TYPE_01,
                                        text_shadow = Constants.TEXT_SHADOW_COLOR,
                                        frameSize=(-0.2, 0.2, -0.04, 0.04),
                                        pos=(0, 0, 0.28),
                                        frameColor=(0, 0, 0, 0))
        self.daysLabel14.reparentTo(self.daysFrame14)
        
        self.hideButton14 = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(0.94, 0, 0.31),
                                       relief=DGG.FLAT,
                                       command=self.hide14DaysFrame)
        self.hideButton14.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton14.reparentTo(self.daysFrame14)
        
        for j in range(2):
            for i in range(7):
                self.days.append(DirectLabel(image=self.weathers[self.prediction[i+j*7]],
                                         text=str(j*7+i+1),
                                         text_scale=0.05,
                                         text_pos=(0.06, -0.08),
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         image_pos=(0, 0, 0),
                                         image_scale=(0.09, 0.09, 0.09),
                                         frameSize=(-0.28, 0.28, -0.1, 0.1),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.81 + i * 0.27, 0, 0.09 - j * 0.25)))
                self.days[j*7+i].setTransparency(TransparencyAttrib.MAlpha)
                self.days[j*7+i].reparentTo(self.daysFrame14)  
                
    def hide14DaysFrame(self):
        self.daysFrame14.hide()
    
    def show14DaysFrame(self):
        self.daysFrame14.show()     
    
    def create21DaysPrediction(self):
        self.daysFrame21 = DirectWindow(frameSize=(-1, 1, -0.5, 0.5),
                                           frameColor=Constants.BG_COLOR,
                                           pos=(0, 0, 0.2),
                                           state=DGG.NORMAL)
        self.daysFrame21.reparentTo(self.parent)
        self.daysFrame21.hide()
        
        self.daysLabel21 = DirectLabel(text='Weather prediction of next 21 days',
                                        text_scale=0.07,
                                        text_pos=(0, -0.02),
                                        text_fg = Constants.TEXT_COLOR,
#                                        text_font = Constants.FONT_TYPE_01,
                                        text_shadow = Constants.TEXT_SHADOW_COLOR,
                                        frameSize=(-0.2, 0.2, -0.04, 0.04),
                                        pos=(0, 0, 0.41),
                                        frameColor=(0, 0, 0, 0))
        self.daysLabel21.reparentTo(self.daysFrame21)
        
        self.hideButton21 = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(0.94, 0, 0.46),
                                       relief=DGG.FLAT,
                                       command=self.hide21DaysFrame)
        self.hideButton21.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton21.reparentTo(self.daysFrame21)
        
        for j in range(3):
            for i in range(7):
                self.days.append(DirectLabel(image=self.weathers[self.prediction[i+j*7]],
                                         text=str(j*7+i+1),
                                         text_scale=0.05,
                                         text_pos=(0.06, -0.08),
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         image_pos=(0, 0, 0),
                                         image_scale=(0.09, 0.09, 0.09),
                                         frameSize=(-0.28, 0.28, -0.1, 0.1),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.81 + i * 0.27, 0, 0.2 - j * 0.25)))
                self.days[j*7+i].setTransparency(TransparencyAttrib.MAlpha)
                self.days[j*7+i].reparentTo(self.daysFrame21) 
                         
    def hide21DaysFrame(self):
        self.daysFrame21.hide()
    
    def show21DaysFrame(self):
        self.daysFrame21.show()  
        
        
    def create28DaysPrediction(self):
        self.daysFrame28 = DirectWindow(frameSize=(-1, 1, -0.65, 0.65),
                                           frameColor=Constants.BG_COLOR,
                                           pos=(0, 0, 0.2),
                                           state=DGG.NORMAL)
        self.daysFrame28.reparentTo(self.parent)
        self.daysFrame28.hide()
        
        self.daysLabel28 = DirectLabel(text='Weather prediction of next 28 days',
                                        text_scale=0.07,
                                        text_pos=(0, -0.02),
                                        text_fg = Constants.TEXT_COLOR,
#                                        text_font = Constants.FONT_TYPE_01,
                                        text_shadow = Constants.TEXT_SHADOW_COLOR,
                                        frameSize=(-0.2, 0.2, -0.04, 0.04),
                                        pos=(0, 0, 0.54),
                                        frameColor=(0, 0, 0, 0))
        self.daysLabel28.reparentTo(self.daysFrame28)
        
        self.hideButton28 = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(0.94, 0, 0.61),
                                       relief=DGG.FLAT,
                                       command=self.hide28DaysFrame)
        self.hideButton28.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton28.reparentTo(self.daysFrame28)
        
        for j in range(4):
            for i in range(7):
                self.days.append(DirectLabel(image=self.weathers[self.prediction[i+j*7]],
                                         text=str(j*7+i+1),
                                         text_scale=0.05,
                                         text_pos=(0.06, -0.08),
                                         text_fg=Constants.TEXT_COLOR,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_shadow=Constants.TEXT_SHADOW_COLOR,
                                         image_pos=(0, 0, 0),
                                         image_scale=(0.09, 0.09, 0.09),
                                         frameSize=(-0.28, 0.28, -0.1, 0.1),
                                         frameColor=(0, 0, 0, 0),
                                         pos=(-0.81 + i * 0.27, 0, 0.32 - j * 0.25)))
                self.days[j*7+i].setTransparency(TransparencyAttrib.MAlpha)
                self.days[j*7+i].reparentTo(self.daysFrame28) 
                         
    def hide28DaysFrame(self):
        self.daysFrame28.hide()
    
    def show28DaysFrame(self):
        self.daysFrame28.show()   
        
    def recreatePrediction(self):
        """
        When weather prediction is re-loaded from server, display should be updated
        """
        if self.destroyFrame():
            self.createWeatherPrediction()
    def hide(self):
        self.mainFrame.hide()
    def show(self):
        self.mainFrame.show()  
    
    def unload(self):
        self.mainFrame.destroy()