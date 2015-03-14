'''
Created on Apr 7, 2012

@author: hunvil
'''
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectControls import DirectControls
from common.DirectWindow import DirectWindow
from common.DirectTextField import DirectTextField
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectSlider import DirectSlider
from panda3d.core import TransparencyAttrib, TextNode
from main.MainLobby.World.Avatars.ParamWindow import ParamWindow
from direct.gui.DirectOptionMenu import DirectOptionMenu
from direct.gui.DirectScrolledList import DirectScrolledList
from direct.gui.DirectButton import DirectButton

class ParamsControls(DirectControls):

    def __init__(self, parent):

        DirectControls.__init__(self, parent)

        self.accept('escape', parent.hide)
        self.accept('control-p', parent.toggleVisibility)

class Params:
    
    def __init__(self, world):
        
        self.world = world
        self.parent=self.world.mainFrame
        self.eFocus = -1
        self.growthRateScale = 5 #This value has to be retrieved from server upon startup
        self.metabolicRateScale = 5
        self.metabolicRateAScale = 5
        self.assimilationEfficiencyScale = 5
        self.functionalResponseControlScale = 5
        self.relativeHalfSaturationDensityScale = 5
        self.predatorInterferenceScale = 5
        self.numItemsVisible = 4
        self.itemHeight = 0.11
        self.createMainFrame()
        self.createPlantLabel()
        self.createAnimalLabel()
        self.createCarryingCapacityPlantsParamK()
        self.createGrowthRatePlantsParamR()
#        self.createMetabolicRatePlantsParamX()
#        self.createMetabolicRateAnimalsParamX()
#        self.createAssimilationEfficiencyAnimalsParamE()
#        self.createFunctionalResponseControlAnimalsParamQ()
#        self.createRelativeHalfSaturationDensityAnimalsParamA()
#        self.createPredatorInterferenceAnimalsParamD()

        self.createButtons()
#        self.createFunctionalParameterButtons()
        self.control = ParamsControls(self)
        self.paramWindow = ParamWindow(self,self.world)
        main.cManager.sendRequest(Constants.CMSG_PARAMS)
        main.msgQ.addToCommandList(Constants.CMSG_CHANGE_PARAMETERS, self.setParameters)
        
        #New methods added
        self.predatorTypes = []
        self.predatorCategory = ['Select','Herbivore', 'Carnivore', 'Omnivore']
        #self.parameterCategory = ['Select Parameter Type','Metabolic Rate Plants(x)','Metabolic Rate Animals(x)','Relative Half Saturation Density(a)','Assimilation Efficiency(e)','Functional Response Control(q)','Predator Interference(d)']        
        self.parameterCategory = ['Select Parameter Type','Metabolic Rate Animals(x)','Relative Half Saturation Density(a)','Assimilation Efficiency(e)','Functional Response Control(q)','Predator Interference(d)']        
        #self.createPredatorCategory(self.predatorCategory)
        self.createParameterCategory(self.parameterCategory)
        self.selectedPredatoryCategory = None
        buttons=[]
        self.createPredatorTypes(buttons)
        self.createPredatorCategory(self.predatorCategory)

    def setParameters(self, args):

        status = args['status']

        if status == 0:
            params = args['params']

            for parameter in params.keys():
                value = params[parameter]

                if parameter == Constants.PARAMETER_K:
                    self.carryingCapacityEntry.enterText(str(int(value)))
                elif parameter == Constants.PARAMETER_R:
                    self.growthRateScaleBar['value'] = value * 10
                    self.setGrowthRateScale()
#                elif parameter == Constants.PARAMETER_X:
#                    self.metabolicRateScaleBar['value'] = value * 10
#                    self.setMetabolicRateScale()
#                elif parameter == Constants.PARAMETER_X_A:
#                    self.metabolicRateAScaleBar['value'] = value * 10
#                    self.setMetabolicRateAScale()
#                elif parameter == Constants.PARAMETER_E:
#                    self.assimilationefficiencyScaleBar['value'] = value * 10
#                    self.setAssimilationEfficiencyScale()
#                elif parameter == Constants.PARAMETER_D:
#                    self.functionalResponseControlScaleBar['value'] = value * 10
#                    self.setFunctionalResponseControlScale()
#                elif parameter == Constants.PARAMETER_Q:
#                    self.relativeHalfSaturationDensityScaleBar['value'] = value * 10
#                    self.setRelativeHalfSaturationDensityScale()
#                elif parameter == Constants.PARAMETER_A:
#                    self.predatorInterferenceScaleBar['value'] = value * 10
#                    self.setPredatorInterferenceScale()

    def createMainFrame(self):
 
        self.headerFrame = DirectWindow(frameSize=(-0.9, 1.1, -0.05, 0.05),
                                      frameColor=(0.3, 0.3, 0.3, 0.3),
                                      pos=(0, 0, 0.5),
                                      state=DGG.NORMAL)
        self.headerFrame.reparentTo(self.parent)
        self.headerFrame.hide()
        
        self.paramFrame = DirectFrame(frameSize=(-0.9, 1.1, -0.40, 0.65),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(0, 0, -0.59),
                                      state=DGG.NORMAL)
        self.paramFrame.reparentTo(self.headerFrame)
        
#        self.systemParamLabel = DirectLabel(text='System Parameters for Plants and Animals',
#                                    text_scale=0.06,
#                                    text_pos=(0,-0.015),
#                                    text_fg = Constants.TEXT_COLOR,
#                                    text_font = Constants.FONT_TYPE_02,
#                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
#                                    text_align=TextNode.ALeft,
#                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
#                                    frameColor = (0,0,0,0),
#                                    pos = (-0.69, 0, 0.1))
#        self.systemParamLabel.setTransparency(TransparencyAttrib.MAlpha)
#        self.systemParamLabel.reparentTo(self.headerFrame)
        
        
        self.hideButton = DirectBasicButton(text=" - ",
                                       text_fg=(1, 1, 1, 1),
                                       text_pos=(-0.007, -0.015),
                                       text_scale=0.05,
                                       frameColor=(0, 0, 0, 0.2),
                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
                                       pos=(1.04, 0, 0.1),
                                       relief=DGG.FLAT,
                                       command=self.hide)
        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
        self.hideButton.reparentTo(self.headerFrame)
        
    def show(self):
        self.headerFrame.show()
        
    def hide(self):
        self.headerFrame.hide()
    
    def toggleVisibility(self):
        
        if self.headerFrame.isHidden():
            self.headerFrame.show()
        else:
            self.headerFrame.hide()
            
    def createPlantLabel(self):
        self.createPlantLabel = DirectLabel(text='System Parameters for Plants:',
                                    text_scale=0.055,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_02,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.85, 0, 0.57))
        self.createPlantLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.createPlantLabel.reparentTo(self.paramFrame)
        
    def createAnimalLabel(self):
        self.createAnimalLabel = DirectLabel(text='System Parameters for Animals:',
                                    text_scale=0.055,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_02,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.85, 0, 0.27))
        self.createAnimalLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.createAnimalLabel.reparentTo(self.paramFrame)        
    
#################################  Params for Plants  #############################
#carryingCapacityDefault(k)>0
    def createCarryingCapacityPlantsParamK(self):
        self.createCarryingCapacityLabel = DirectLabel(text='Carrying Capacity(k):',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.85, 0, 0.47))
        self.createCarryingCapacityLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.createCarryingCapacityLabel.reparentTo(self.paramFrame)
        
        
        self.carryingCapacityEntry = DirectTextField(self.headerFrame,
                                              text_font=Constants.FONT_TYPE_01,
                                              scale=0.04,
                                              pos=(-0.8, 0, -0.2),
                                              frameColor=(0.8, 0.8, 0.8, 0.7),
                                              width=7,
                                              numLines = 1,
                                              focusInCommand=self.onWorldEntryFocus,
                                              focusOutCommand=self.onWorldEntryFocusOut)                                              
        self.carryingCapacityEntry.reparentTo(self.headerFrame)

    def onWorldEntryFocus(self):
        self.carryingCapacityEntry['frameColor'] = (0.8, 0.8, 0.8, 0.9)
        self.headerFrame.getControls().enable()

    def onWorldEntryFocusOut(self):
        self.carryingCapacityEntry['frameColor'] = (0.8, 0.8, 0.8, 0.4)
        self.headerFrame.getControls().disable()
        
    def submit(self, text=None):

        if len(self.carryingCapacityEntry.get()) == 0:
            carryingCapacity = 0
        else:
            try:
                carryingCapacity = float(self.carryingCapacityEntry.get())
            except:
                carryingCapacity = 1.0

        args = {'carry_capacity': carryingCapacity,
                'growth_rate'   : self.growthRateScale,
                'meta_rate'     : self.metabolicRateScale,
                'meta_rate_a'   : self.metabolicRateAScale,
                'assim_scale'   : self.assimilationEfficiencyScale,
                'funcr_scale'   : self.functionalResponseControlScale,
                'sat_scale'     : self.relativeHalfSaturationDensityScale,
                'pred_scale'    : self.predatorInterferenceScale}
        main.cManager.sendRequest(Constants.CMSG_CHANGE_PARAMETERS, args)

#growthRateDefault(r)(0-1)
    def createGrowthRatePlantsParamR(self):
        self.growthRateLabel = DirectLabel(text='Growth Rate(r):',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.34, 0, 0.47))
        self.growthRateLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.growthRateLabel.reparentTo(self.paramFrame) 
                            #1st horizontal -ve left    last vertical +ve up
        self.growthRateScaleBar = DirectSlider( pos = (-0.05, 0, 0.4),
                                       scale = 0.13,
                                       value = self.growthRateScale,
                                       range = (0, 10),
#                                       scrollSize = 1,
                                       frameSize = (-2.,2.,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setGrowthRateScale )
        self.growthRateScaleBar.reparentTo(self.paramFrame)

    def setGrowthRateScale(self):
        
        self.growthRateScale=self.growthRateScaleBar['value']/10
        self.growthRateLabel['text']='Growth Rate(r): '+ str('%.5f' % self.growthRateScale)
        
#metabolicRateDefault(x) (0-1)
    def createMetabolicRatePlantsParamX(self):
        self.metabolicRateLabel = DirectLabel(text='Metabolic Rate(x):',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (0.31, 0, 0.47))
        self.metabolicRateLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.metabolicRateLabel.reparentTo(self.paramFrame) 
                            #1st horizontal -ve left    last vertical +ve up
        self.metabolicRateScaleBar = DirectSlider( pos = (0.6, 0, 0.4),
                                       scale = 0.13,
                                       value = self.metabolicRateScale,
                                       range = (0, 10),
#                                       scrollSize = 1,
                                       frameSize = (-2.,2.,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setMetabolicRateScale )
        self.metabolicRateScaleBar.reparentTo(self.paramFrame)

    def setMetabolicRateScale(self):
        
        self.metabolicRateScale=self.metabolicRateScaleBar['value']/10
        self.metabolicRateLabel['text']='Metabolic Rate(x): '+ str('%.5f' % self.metabolicRateScale)     
    
#################################   Params for Animals   #############################  

#metabolicRateDefault(x) (0-1)
    def createMetabolicRateAnimalsParamX(self):
        self.metabolicRateALabel = DirectLabel(text='Metabolic Rate(x):',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.85, 0, 0.17))
        self.metabolicRateALabel.setTransparency(TransparencyAttrib.MAlpha)
        self.metabolicRateALabel.reparentTo(self.paramFrame) 
                            #1st horizontal -ve left    last vertical +ve up
        self.metabolicRateAScaleBar = DirectSlider( pos = (-0.56, 0, 0.1),
                                       scale = 0.13,
                                       value = self.metabolicRateAScale,
                                       range = (0, 10),
#                                       scrollSize = 1,
                                       frameSize = (-2.,2.,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setMetabolicRateAScale )
        self.metabolicRateAScaleBar.reparentTo(self.paramFrame)

    def setMetabolicRateAScale(self):
        
        self.metabolicRateAScale=self.metabolicRateAScaleBar['value']/10
        self.metabolicRateALabel['text']='Metabolic Rate(x): '+ str('%.5f' % self.metabolicRateAScale)
    
#assimilationEfficiencyDefault(e) (0-1)
    def createAssimilationEfficiencyAnimalsParamE(self):
        self.assimilationefficiencyLabel = DirectLabel(text='Assimilation Efficiency(e):',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (0.2, 0, 0.17))
        self.assimilationefficiencyLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.assimilationefficiencyLabel.reparentTo(self.paramFrame) 
                            #1st horizontal -ve left    last vertical +ve up
        self.assimilationefficiencyScaleBar = DirectSlider( pos = (0.5, 0, 0.1),
                                       scale = 0.13,
                                       value = self.assimilationEfficiencyScale,
                                       range = (0, 10),
#                                       scrollSize = 1,
                                       frameSize = (-2.,2.,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setAssimilationEfficiencyScale )
        self.assimilationefficiencyScaleBar.reparentTo(self.paramFrame)

        self.assimilationefficiencyLabel.hide()
        self.assimilationefficiencyScaleBar.hide()

    def setAssimilationEfficiencyScale(self):
        
        self.assimilationEfficiencyScale=self.assimilationefficiencyScaleBar['value']/10
        self.assimilationefficiencyLabel['text']='Assimilation Efficiency(e): '+ str('%.5f' % self.assimilationEfficiencyScale)
    
#relativeHalfSaturationDensityDefault(a) (0-1)
    def createRelativeHalfSaturationDensityAnimalsParamA(self):
        self.relativeHalfSaturationDensityLabel = DirectLabel(text='Assimilation Efficiency(e):',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.85, 0, 0))
        self.relativeHalfSaturationDensityLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.relativeHalfSaturationDensityLabel.reparentTo(self.paramFrame) 
                            #1st horizontal -ve left    last vertical +ve up
        self.relativeHalfSaturationDensityScaleBar = DirectSlider( pos = (-0.56, 0, -0.07),
                                       scale = 0.13,
                                       value = self.relativeHalfSaturationDensityScale,
                                       range = (0, 10),
#                                       scrollSize = 1,
                                       frameSize = (-2.,2.,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setRelativeHalfSaturationDensityScale )
        self.relativeHalfSaturationDensityScaleBar.reparentTo(self.paramFrame)

        self.relativeHalfSaturationDensityLabel.hide()
        self.relativeHalfSaturationDensityScaleBar.hide()

    def setRelativeHalfSaturationDensityScale(self):
        
        self.relativeHalfSaturationDensityScale=self.relativeHalfSaturationDensityScaleBar['value']/10
        self.relativeHalfSaturationDensityLabel['text']='Relative Half Saturation Density(a): '+ str('%.5f' % self.relativeHalfSaturationDensityScale)   
    
#functionalResponseControlParameterDefault(q) (0-1)
    def createFunctionalResponseControlAnimalsParamQ(self):         
        self.functionalResponseControlLabel = DirectLabel(text='Functional Response Control(q):',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (0.2, 0, 0))
        self.functionalResponseControlLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.functionalResponseControlLabel.reparentTo(self.paramFrame) 
                            #1st horizontal -ve left    last vertical +ve up
        self.functionalResponseControlScaleBar = DirectSlider( pos = (0.5, 0, -0.07),
                                       scale = 0.13,
                                       value = self.functionalResponseControlScale,
                                       range = (0, 10),
#                                       scrollSize = 1,
                                       frameSize = (-2.,2.,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setFunctionalResponseControlScale )
        self.functionalResponseControlScaleBar.reparentTo(self.paramFrame)

        self.functionalResponseControlLabel.hide()
        self.functionalResponseControlScaleBar.hide()

    def setFunctionalResponseControlScale(self):
        
        self.functionalResponseControlScale=self.functionalResponseControlScaleBar['value']/10
        self.functionalResponseControlLabel['text']='Functional Response Control(q): '+ str('%.5f' % self.functionalResponseControlScale)   

    
#predatorInterferenceDefault(d) (0-1)
    def createPredatorInterferenceAnimalsParamD(self):
        self.predatorInterferenceLabel = DirectLabel(text='Predator Interference(d):',
                                    text_scale=0.045,
                                    text_pos=(0,-0.015),
                                    text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    text_align=TextNode.ALeft,
                                    frameSize = (-0.1, 0.1, -0.04, 0.04),
                                    frameColor = (0,0,0,0),
                                    pos = (-0.85, 0, -0.2))
        self.predatorInterferenceLabel.setTransparency(TransparencyAttrib.MAlpha)
        self.predatorInterferenceLabel.reparentTo(self.paramFrame) 
                            #1st horizontal -ve left    last vertical +ve up
        self.predatorInterferenceScaleBar = DirectSlider( pos = (-0.56, 0, -0.27),
                                       scale = 0.13,
                                       value = self.predatorInterferenceScale,
                                       range = (0, 10),
#                                       scrollSize = 1,
                                       frameSize = (-2.,2.,-0.06,0.06),
                                       pageSize = 1,
                                       orientation = DGG.HORIZONTAL,
                                       thumb_frameSize = (-0.25, 0.25, -0.2, 0.2),
                                       thumb_relief = DGG.FLAT,
                                       command = self.setPredatorInterferenceScale )
        self.predatorInterferenceScaleBar.reparentTo(self.paramFrame)

        self.predatorInterferenceLabel.hide()
        self.predatorInterferenceScaleBar.hide()

    def setPredatorInterferenceScale(self):
        
        self.predatorInterferenceScale=self.predatorInterferenceScaleBar['value']/10
        self.predatorInterferenceLabel['text']='Predator Interference(d): '+ str('%.5f' % self.predatorInterferenceScale)   

    
    def createButtons(self):
        """Create some buttons."""
        self.submitButton = DirectBasicButton(text='Submit',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(-0.3, 0, -0.85),
                                         relief=DGG.FLAT,
                                         command=self.submit)
        self.submitButton.reparentTo(self.headerFrame)

        self.cancel = DirectBasicButton(text='Cancel',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(-0.65, 0, -0.85),
                                         relief=DGG.FLAT,
                                         command=self.hide)
        self.cancel.reparentTo(self.headerFrame)
        
    def createFunctionalParameterButtons(self):
        """Create some buttons."""
        self.functionalParametersButton = DirectBasicButton(text='Functional Parameters',
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(-0.3, 0, -0.85),
                                         relief=DGG.FLAT,
                                         command=self.showFunctionalParametersMenu)
        self.functionalParametersButton.reparentTo(self.headerFrame)
        self.functionalParametersButton.hide()
    def showFunctionalParametersMenu(self):
        self.paramWindow.show()
        return
 
    def createParameterCategory(self,paramType):
        self.parameterType = DirectLabel(text = "Parameter Type",
                                           text_fg = (1,1,1,1),
                                           text_font = Constants.FONT_TYPE_01,
                                           text_pos = ( 0, -0.015),
                                           text_scale = 0.05,
                                           frameSize = ( -0.25, 0.25, -0.06, 0.06),
                                           frameColor = (0,0,0,0),
                                           pos = (-0.58, 0,-0.4),
                                           relief = DGG.FLAT)
        self.parameterType.reparentTo(self.headerFrame)
                
        self.parameterChoice = DirectOptionMenu(text = "Parameter Type",
                                             text_pos = (-1.6, -0.22),
                                             text_scale = 0.55,
                                             scale = 0.1,
                                             items=paramType,
                                             initialitem = 0,
                                             frameSize = (-2.0, 6.5, -0.45, 0.45), 
                                             highlightColor = (0.9, 0.2, 0.1, 0.8),
                                             pos = (-0.6, 0 , -0.5),
                                             popupMarker_scale=0.3,
                                             command=self.requestChangeParameterType)
        self.parameterChoice.reparentTo(self.headerFrame)   
        
    def requestChangeParameterType(self,parameterType):
        self.parameterType = parameterType
        if parameterType != self.parameterCategory[0]:
            obj = {"same clicked parameterType": parameterType}
            print obj
#            if parameterType == self.parameterCategory[1]:  # metabolic rate plants
#                self.predatorCategoryLabel.hide()
#                self.predatorCategoryChoice.hide()
#                self.predatorTypeLabel.hide()
#                self.myScrolledList.hide()
#                self.loadPlantSpeciesInfo()
            if parameterType == self.parameterCategory[1]:  # metabolic rate animals
                self.predatorCategoryLabel.show()
                self.predatorCategoryChoice.show()
                self.predatorTypeLabel.hide()
                self.myScrolledList.hide()
                 
            else:   
                self.predatorCategoryLabel.show()
                self.predatorCategoryChoice.show()
                self.predatorTypeLabel.hide()
                self.myScrolledList.hide()

        return     
        
    def createPredatorCategory(self,predatorCategory):
        self.predatorCategoryLabel = DirectLabel(text = "Predator Category",
                                           text_fg = (1,1,1,1),
                                           text_font = Constants.FONT_TYPE_01,
                                           text_pos = ( 0, -0.015),
                                           text_scale = 0.05,
                                           frameSize = ( -0.25, 0.25, -0.06, 0.06),
                                           frameColor = (0,0,0,0),
                                           pos = (-0.58, 0,-0.6),
                                           relief = DGG.FLAT)
        self.predatorCategoryLabel.reparentTo(self.headerFrame)
                
        self.predatorCategoryChoice = DirectOptionMenu(text = "Predator Category",
                                             text_pos = (-1.6, -0.22),
                                             text_scale = 0.55,
                                             scale = 0.1,
                                             items=predatorCategory,
                                             initialitem = 0,
                                             frameSize = (-2.0, 2.0, -0.45, 0.45), 
                                             highlightColor = (0.9, 0.2, 0.1, 0.8),
                                             pos = (-0.6, 0 , -0.7),
                                             popupMarker_scale=0.3,
                                             command=self.requestChangePredatorCategory)
        self.predatorCategoryChoice.reparentTo(self.headerFrame)    
        self.predatorCategoryLabel.hide()
        self.predatorCategoryChoice.hide()    
    
    def requestChangePredatorCategory(self,predatorCategory):
        if predatorCategory != self.predatorCategory[0]:
            obj = {"same clicked predatorCategory": predatorCategory}
            print obj
            self.selectedPredatoryCategory = predatorCategory
            self.predatorTypeLabel.hide()
            self.myScrolledList.hide()
#            if self.parameterType == self.parameterCategory[1]: # show plant species
#                print 'show plant species'
#                self.loadPlantSpeciesInfo()
            if self.parameterType == self.parameterCategory[1]: # show animal species
                print 'show animal species'
                self.loadAnimalSpeciesInfo(predatorCategory)
            else:
                self.loadAnimalItemInfo(predatorCategory)
        return
 
    def loadAnimalSpeciesInfo(self,predatorCategory):
        self.predatorTypes = self.world.gameState.getListOfAnimalTypesByCategory(predatorCategory)
        self.paramWindow.showAnimalSpecies(self.predatorTypes,predatorCategory)
        return
    
    def loadPlantSpeciesInfo(self):
        self.plantTypes = self.world.gameState.getListOfPlants()
        if self.plantTypes.__len__()!=0:
            self.paramWindow.showPlantSpecies(self.plantTypes)
        return
    
    def createPredatorTypes(self,buttons):
        self.predatorTypeLabel = DirectLabel(text = "Select Predator Type",
                                           text_fg = (1,1,1,1),
                                           text_font = Constants.FONT_TYPE_01,
                                           text_pos = ( 0, -0.015),
                                           text_scale = 0.05,
                                           frameSize = ( -0.25, 0.25, -0.06, 0.06),
                                           frameColor = (0,0,0,0),
                                           pos = (0.6, 0,-0.3),
                                           relief = DGG.FLAT)
        self.predatorTypeLabel.reparentTo(self.headerFrame)
                
#        self.predatorChoice = DirectOptionMenu(text = "Predator Type",
#                                             text_pos = (-1.6, -0.22),
#                                             text_scale = 0.55,
#                                             scale = 0.1,
#                                             items=predatorTypes,
#                                             initialitem = 0,
#                                             frameSize = (-2.0, 2.0, -0.45, 0.45), 
#                                             highlightColor = (0.9, 0.2, 0.1, 0.8),
#                                             pos = (-0.6, 0 , -0.9),
#                                             popupMarker_scale=0.3,
#                                             command=self.requestChangePredator)
#        self.predatorChoice.reparentTo(self.headerFrame)  
    
#        b1 = DirectButton(text = ("Button1", "click!", "roll", "disabled"),
#                      text_scale=0.1, borderWidth = (0.01, 0.01),
#                      relief=2)
# 
#        b2 = DirectButton(text = ("Button2", "click!", "roll", "disabled"),
#                          text_scale=0.1, borderWidth = (0.01, 0.01),
#                          relief=2)
        self. myScrolledList = DirectScrolledList(
                                                decButton_pos= (0.35, 0, 0.53),
                                                decButton_text = "Dec",
                                                decButton_text_scale = 0.04,
                                                decButton_borderWidth = (0.005, 0.005),
                                             
                                                incButton_pos= (0.35, 0, -0.02),
                                                incButton_text = "Inc",
                                                incButton_text_scale = 0.04,
                                                incButton_borderWidth = (0.005, 0.005),
                                             
                                                frameSize = (0.0, 0.7, -0.05, 0.59),
                                                frameColor = (0,0,0,0.3),
                                                pos = (0.3, 0, -0.95),
#                                                items = [b1, b2],
                                                items = buttons,
                                                numItemsVisible = self.numItemsVisible,
                                                forceHeight = self.itemHeight,
                                                itemFrame_frameSize = (-0.3, 0.3, -0.37, 0.11),
                                                itemFrame_pos = (0.35, 0, 0.4),
                                                )
        self.myScrolledList.reparentTo(self.headerFrame) 
        
        self.predatorTypeLabel.hide()
        self.myScrolledList.hide()
#    def requestChangePredator(self,predatorChoice):
#        print 'predatorChoice ',predatorChoice
#        if (self.selectedPredatoryCategory == 'Herbivore' and predatorChoice == 'Select Herbivore'):
#            pass
#            print 'Herbivore 0' 
#        elif(self.selectedPredatoryCategory == 'Carnivore' and predatorChoice == 'Select Carnivore'):
#            pass
#            print 'Carnivore 0'             
#        elif(self.selectedPredatoryCategory == 'Omnivore' and predatorChoice == 'Select Omnivore'):
#            pass
#            print 'Omnivore 0'
#        else:
#            preys = self.world.gameState.getListOfPreys(predatorChoice)
#            preyList = preys.rsplit(',')
#            print preyList
#            if self.selectedPredatoryCategory!='Select' and self.parameterType != 'Select Parameter Type':
#                self.paramWindow.show(self.parameterType,predatorChoice,preyList)
#        return    
    
    def loadAnimalItemInfo(self,predatorCategory):
        self.predatorTypes = self.world.gameState.getListOfAnimalTypesByCategory(predatorCategory)

        #for item in self.predatorTypes:
            #l = DirectLabel(text = item, text_scale=0.05)
        self.buttons = []
        for item in self.predatorTypes:
            self.buttons.append(DirectBasicButton(text=item,
                                         text_font=Constants.FONT_TYPE_01,
                                         text_pos=(0, -0.015),
                                         text_scale=0.05,
                                         frameSize=(-0.13, 0.13, -0.05, 0.05),
                                         frameColor=(0.8, 0.8, 0.8, 0.7),
                                         pos=(0.3, 0, -0.85),
                                         relief=DGG.FLAT,
                                         command = self.predatoryTypeSelected,
                                         extraArgs = [item]
                                         ))
            #self.myScrolledList.addItem(self.buttons)             
        self.createPredatorTypes(self.buttons)
        self.predatorTypeLabel.show()
        self.myScrolledList.show()
        
    def predatoryTypeSelected(self,item):
        print 'predator type clicked '+item
        preys = self.world.gameState.getListOfPreys(item)
        preyList = preys.rsplit(',')
        print preyList
        if self.selectedPredatoryCategory!='Select' and self.parameterType != 'Select Parameter Type':
            self.paramWindow.show(self.parameterType,item,preyList)