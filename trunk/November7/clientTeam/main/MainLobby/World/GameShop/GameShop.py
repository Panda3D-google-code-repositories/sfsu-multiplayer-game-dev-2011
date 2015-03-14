
from common.Constants import Constants
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel
from common.DirectWindow import DirectWindow
from common.MousePicker2D import MousePicker2D
from direct.gui.DirectGui import DGG
from direct.gui.DirectLabel import DirectLabel
from main.MainLobby.World.GameShop.GameShopControl import GameShopControl
from panda3d.core import TransparencyAttrib, TextNode
import threading

class GameShop:
    
    """
    1). Load all item images from models directory
    2). Create Animal, Plant, Research and Vaccine Buttons
    3). Implement left and right scrolling through images
    4). Pop up window when click on an item
    5). (not yet implement)Mouse drag to 3D world when buying an item
    """
    
    def __init__(self, parent):
        
        self.parent = parent
        self.shopButtons=[]
        self.animals=[]
        self.plants =[]
        self.researches=[]
        self.vaccine=[]
        self.items = []
        self.itemDesc=[]
        
        self.key_cost = 'cost'
        self.key_image='image'
        self.key_prey_list='prey_list'
        self.key_predator_list='predator_list'
        self.key_description='description'
        self.key_effect='effect'
        
        self.loadAnimalItems()
        self.loadPlantItems()
        self.loadResearchItems()
        self.loadVaccineItems()
        self.createMainFrame()
        self.createButtons()
        self.createScrollButtons()
        self.createShopItems()
        self.createDescriptionFrame()
        
#        self.control = GameShopControl(self)
#        self.control.disable()
        
    def createMainFrame(self):
        
        self.mainFrame = DirectWindow(frameSize=(-0.8,0.8,-0.19,0.19),
                                      frameColor=(0,0,0,0.2),
                                      pos=(-0.8, 0, -0.81))
        
        self.mainFrame.reparentTo(self.parent)
    
    def loadAnimalItems(self):
        imageDirectory = "models/weathers"
        _costs=['$10', '$20', '$30', '$40', '$50', '$60', '$70', '$80']
        _images=[imageDirectory+'/Ice.png',
                 imageDirectory+'/Moon_Phase_Full.png',
                 imageDirectory+'/Night_Rain.png',
                 imageDirectory+'/Pollen_Flower.png',
                 imageDirectory+'/Rainbow.png',
                 imageDirectory+'/Sleet.png',
                 imageDirectory+'/Snow_Occasional.png',
                 imageDirectory+'/Sunny.png']
        _desc = ['some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here']
        _effect=['18', '28', '38', '48', '58', '68', '78', '88']
        _prey_list=['', '', '', '','','','','']
        _predator_list=['', '', '', '','','','','']
        for i in range(8):
            self.animals.append({self.key_cost: _costs[i], 
                            self.key_image: _images[i], 
                            self.key_prey_list: _prey_list[i],
                            self.key_predator_list:_predator_list[i],
                            self.key_description:_desc[i],
                            self.key_effect:'Weight Value: '+_effect[i]})

    def loadPlantItems(self):
        imageDirectory = "models/weathers"
        _costs=['$10', '$30', '$20', '$50', '$40', '$60', '&70', '$80']
        _images=[imageDirectory+'/Ice.png',
                 imageDirectory+'/Moon_Phase_Full.png',
                 imageDirectory+'/Night_Rain.png',
                 imageDirectory+'/Rainbow.png',
                 imageDirectory+'/Sunny.png',
                 imageDirectory+'/Pollen_Flower.png',
                 imageDirectory+'/Snow_Occasional.png',
                 imageDirectory+'/Sleet.png']
        _desc = ['some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here']
        _effect=['1', '2', 'Weight Value: 3', 
                 '48', '5', '68', 
                 '78', '8']
        _prey_list=['', '', '', '','','','','']
        _predator_list=['', '', '', '','','','','']
        
        for i in range(8):
            self.plants.append({self.key_cost: _costs[i], 
                            self.key_image: _images[i], 
                            self.key_prey_list: _prey_list[i],
                            self.key_predator_list:_predator_list[i],
                            self.key_description:_desc[i],
                            self.key_effect:'Weight Value: '+_effect[i]})  
        
    def loadResearchItems(self):
        imageDirectory = "models/weathers"
        _costs=['$100', '$300', '$20', '$50', '$40', '$60', '&70', '$80']
        _images=[imageDirectory+'/Ice.png',
                 imageDirectory+'/Night_Rain.png',
                 imageDirectory+'/Moon_Phase_Full.png',
                 imageDirectory+'/Sunny.png',
                 imageDirectory+'/Pollen_Flower.png',
                 imageDirectory+'/Rainbow.png',
                 imageDirectory+'/Snow_Occasional.png',
                 imageDirectory+'/Sleet.png']
        _desc = ['some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here']
        _effect=['18', '28', '38', '48', '58', '68', '78', '88']
        _prey_list=['', '', '', '','','','','']
        _predator_list=['', '', '', '','','','','']
        for i in range(8):
            self.researches.append({self.key_cost: _costs[i], 
                            self.key_image: _images[i], 
                            self.key_prey_list: _prey_list[i],
                            self.key_predator_list:_predator_list[i],
                            self.key_description:_desc[i],
                            self.key_effect: 'Effect: '+_effect[i]})  
        
    def loadVaccineItems(self):
        imageDirectory = "models/weathers"
        _costs=['$100', '$300', '$20', '$50', '$40', '$60', '&70']
        _images=[imageDirectory+'/Ice.png',
                 imageDirectory+'/Night_Rain.png',
                 imageDirectory+'/Moon_Phase_Full.png',
                 imageDirectory+'/Sunny.png',
                 imageDirectory+'/Pollen_Flower.png',
                 imageDirectory+'/Rainbow.png',
                 imageDirectory+'/Sleet.png']
        _desc = ['some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here',
                 'some description of the purchasable item should go here']
        _effect=['18', '28', '38', '48', '68', '78', '88']
        _prey_list=['', '', '', '','','','']
        _predator_list=['', '', '','','','','']
        for i in range(7):
            self.vaccine.append({self.key_cost: _costs[i], 
                            self.key_image: _images[i], 
                            self.key_prey_list: _prey_list[i],
                            self.key_predator_list:_predator_list[i],
                            self.key_description:_desc[i],
                            self.key_effect:'Effect: '+_effect[i]})   
                
    def createButtons(self):
        for i in range(4):
            self.shopButtons.append(DirectBasicButton(text = '',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.045,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.15, 0.15, -0.045, 0.045),
                                            frameColor = Constants.BG_COLOR,
                                            pos = (-0.64, 0, 0.143-i*0.095),
                                            relief = DGG.FLAT,
                                            extraArgs=[i],
                                            command=self.switchCategpry))
            self.shopButtons[i].reparentTo(self.mainFrame)
            
        self.shopButtons[0]['text']='Animal'
        self.shopButtons[1]['text']='Plant'
        self.shopButtons[2]['text']='Research'
        self.shopButtons[3]['text']='Vaccine'
        
    def createScrollButtons(self):
        
        self.leftScrollButton = DirectBasicButton(text='<',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.06,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.03, 0.03, -0.06, 0.06),
                                            frameColor = (0,0,0,0.2),
                                            pos = (-0.45, 0, 0),
                                            relief = DGG.FLAT,
                                            command=self.leftScroll)
        self.leftScrollButton.setTransparency(TransparencyAttrib.MAlpha)
        self.leftScrollButton.reparentTo(self.mainFrame)    
        
        self.rightScrollButton = DirectBasicButton(text='>',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_01,
                                            text_pos = (0, -0.015),
                                            text_scale = 0.06,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameSize = (-0.03, 0.03, -0.06, 0.06),
                                            frameColor = (0,0,0,0.2),
                                            pos = (0.76, 0, 0),
                                            relief = DGG.FLAT,
                                            command=self.rightScroll)
        self.rightScrollButton.setTransparency(TransparencyAttrib.MAlpha)
        self.rightScrollButton.reparentTo(self.mainFrame)                          
        
    def createShopItems(self):
        for i in range(4):
            self.items.append(DirectBasicButton(text='',
                                          text_scale=0.05,
                                          text_pos=(0.05, -0.08),
                                          image_pos=(0,0,0),
                                          text_fg = (0,0,0,1),
                                          text_font = Constants.FONT_TYPE_01,
                                          text_shadow = Constants.TEXT_SHADOW_COLOR,
                                          image_scale=(0.09,0.09,0.09),
                                          frameSize=(-0.135, 0.135, -0.135, 0.135),
                                          frameColor=(0,0,0,0),
                                          pos = (-0.27625+i*0.2875,0,0),
                                          textMayChange=1,
#                                          onMouseOverExtraArgs=[i],
                                          onMouseOver=self.showDescriptionFrame,
                                          onMouseOut=self.hideDescriptionFrame))
#                                          extraArgs=[i],
#                                          command=self.startItemDrag))
            self.items[i].setTransparency(TransparencyAttrib.MAlpha)
            self.items[i].reparentTo(self.mainFrame)
        self.initializeItems()
        
    def initializeItems(self, mode=0):
        
        self.currentLefeMost=0
        self.currentRightMost=3
        self.leftScrollButton.hide()
        self.rightScrollButton.show() 
        self.setFocus(mode)
        
        if mode == 0:
            self.images=self.animals
        elif mode==1:
            self.images = self.plants
        elif mode==2:
            self.images=self.researches
        else:
            self.images=self.vaccine
        
        self.loadImages()
        
    def loadImages(self):
        
        for i in range(4):
            self.items[i]['text']=self.images[self.currentLefeMost+i][self.key_cost]
            self.items[i]['image']=self.images[self.currentLefeMost+i][self.key_image]
            # extraArgs is used to store all the needed info for later, but it is not for command
            self.items[i].setOnMouseOverExtraArgs([self.images[self.currentLefeMost+i][self.key_cost], 
                                        self.images[self.currentLefeMost+i][self.key_image],
                                        self.images[self.currentLefeMost+i][self.key_description],
                                        self.images[self.currentLefeMost+i][self.key_effect],
                                        self.images[self.currentLefeMost+i][self.key_prey_list],
                                        self.images[self.currentLefeMost+i][self.key_predator_list]])
            self.items[i]['image_scale']=(0.1,0.1,0.1)
        
    def leftScroll(self):
        """ """
        if self.currentLefeMost > 0:
            self.currentLefeMost = self.currentLefeMost - 1
            self.currentRightMost = self.currentRightMost - 1
            self.rightScrollButton.show()
            self.loadImages()
            if self.currentLefeMost == 0:
                self.leftScrollButton.hide()
        
    def rightScroll(self):
        """  """
        if self.currentRightMost < len(self.images)-1:
            self.currentLefeMost = self.currentLefeMost + 1
            self.currentRightMost = self.currentRightMost + 1
            self.leftScrollButton.show()
            self.loadImages()
            if self.currentRightMost == len(self.images)-1: 
                self.rightScrollButton.hide()
    def setFocus(self, mode):
        """ Change color when click on one of the buttons """
        _frameColor = (0.5,0.5,0.5,0.7)
        for i in range(4):
            if i == mode:
                self.shopButtons[i]['frameColor']=_frameColor
            else:
                self.shopButtons[i]['frameColor']=Constants.BG_COLOR
                
    def switchCategpry(self,mode):
        self.initializeItems(mode)
            
    def createDescriptionFrame(self):
        
        self.descriptionFrame = DirectWindow(frameSize=(-0.6, 0.6, -0.4, 0.4),
                                      frameColor=Constants.BG_COLOR,
                                      pos=(0, 0, 0.15),
                                      state=DGG.NORMAL)
        self.descriptionFrame.reparentTo(self.parent)
        self.descriptionFrame.hide()
#        self.hideButton = DirectBasicButton(text=" - ",
#                                       text_fg=(1, 1, 1, 1),
#                                       text_pos=(-0.007, -0.015),
#                                       text_scale=0.05,
#                                       frameColor=(0, 0, 0, 0.2),
#                                       frameSize=(-0.04, 0.04, -0.025, 0.025),
#                                       pos=(0.54, 0, 0.36),
#                                       relief=DGG.FLAT,
#                                       command=self.hideDescriptionFrame)
#        self.hideButton.setTransparency(TransparencyAttrib.MAlpha)
#        self.hideButton.reparentTo(self.descriptionFrame)
        
#        self.title = DirectLabel(text = 'Title',
#                                 text_scale=0.08,
#                                 text_pos=(0, -0.025),
#                                 text_fg = Constants.TEXT_COLOR,
#                                 text_font = Constants.FONT_TYPE_01,
#                                 text_shadow = Constants.TEXT_SHADOW_COLOR,
#                                 frameSize=(-0.1, 0.1, -0.04, 0.04),
#                                 pos=(0, 0, 0.51),
#                                 frameColor=(0, 0, 0, 0))
#        self.title.reparentTo(self.descriptionFrame)
        
        self.objImage = DirectLabel(image_pos=(0,0,0),
                                    image_scale=(0.1,0.1,0.1),
                                 frameSize=(-0.2, 0.2, -0.04, 0.04),
                                 pos=(-0.4, 0, 0.2),
                                 frameColor=(0, 0, 0, 0))
        self.objImage.setTransparency(TransparencyAttrib.MAlpha)
        self.objImage.reparentTo(self.descriptionFrame)
        
        for i in range(4):
            self.itemDesc.append( DirectLabel(text = '',
                                 text_scale=0.05,
                                 text_pos=(0, -0.025),
                                 text_fg = Constants.TEXT_COLOR,
                                 text_font = Constants.FONT_TYPE_01,
                                 text_align=TextNode.ALeft,
                                 text_shadow = Constants.TEXT_SHADOW_COLOR,
                                 frameSize=(-0.1, 0.1, -0.04, 0.04),
                                 pos=(-0.55, 0, 0-i*0.09),
                                 frameColor=(0, 0, 0, 0)))
            self.itemDesc[i].reparentTo(self.descriptionFrame)
        
        
#        self.itemDesc[0]['text']='Cost: '
#        self.itemDesc[1]['text']='Effect: '
        self.itemDesc[2]['text']='Prey List: '
        self.itemDesc[3]['text']='Predator List:'
        
        self.desc = DirectLabel(text = '',
                                 text_scale=0.05,
                                 text_pos=(0, -0.025),
                                 text_fg = Constants.TEXT_COLOR,
                                 text_font = Constants.FONT_TYPE_01,
                                 text_align=TextNode.ALeft,
                                 text_wordwrap = 15,
                                 text_shadow = Constants.TEXT_SHADOW_COLOR,
                                 frameSize=(-0.1, 0.1, -0.04, 0.04),
                                 pos=(-0.23, 0, 0.3),
                                 frameColor=(0, 0, 0, 0))
        self.desc.reparentTo(self.descriptionFrame)
        
#    def showDescriptionFrame(self, cost, image, description, effect, prey_list, predator_list):
    def showDescriptionFrame(self, cost, image, description, effect, preyList, predatorList):   
        if self.descriptionFrame.isHidden():
            self.descriptionFrame.show()
        _thread = UpdateThread(self.objImage, image, 1)
        _thread.setDaemon(True)
        _thread.start()
        self.itemDesc[0]['text'] = 'Cost: '+cost
        self.itemDesc[1]['text'] = effect
        self.desc['text'] = description
        
#        self.control.enable()
#        self.objImage['image']=image
#        self.objImage['image_scale']=(0.1,0.1,0.1)
        
    def hideDescriptionFrame(self):
        self.descriptionFrame.hide()
#        self.control.disable()
        
    def hide(self):
        self.mainFrame.hide()
    def show(self):
        self.mainFrame.show()
        
    def unload(self):
        self.mainFrame.destroy()
    
    def dragItem(self, index):
        print 'drag item'
        
    def startItemDrag(self, index):
        print 'start item drag '
        
    def stopItemDrag(self):
        print 'stop item drag'
      
class UpdateThread (threading.Thread):
    
    """
    This thread is used to update image and description of each item when use switch from item to item.
    It may very useful when the resolution of an image is high, update image lieanerly may be a bit slow.
    """
    def __init__(self, label, obj, index):
        """
        obj is either image or text, index to identify image or text, 0 is text, 1 is image
        """
        threading.Thread.__init__(self)
        self.label = label
        self.obj = obj
        self.index = index
        
    def run(self):
#        print 'update image or text'
        if self.index == 0:
            self.label['text'] = self.obj
        else:
            self.label['image']=self.obj
            self.label['image_scale']=(0.1,0.1,0.1)

        