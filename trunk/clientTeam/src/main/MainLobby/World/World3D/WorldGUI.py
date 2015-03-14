'''
Created on Nov 12, 2011

@author: hunvil
'''
from calendar import month_name

from direct.gui.DirectGui import DGG
from direct.gui.DirectFrame import DirectFrame
from direct.gui.OnscreenImage import OnscreenImage
from direct.interval.IntervalGlobal import Func
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import Wait
from direct.interval.LerpInterval import LerpPosInterval

from panda3d.core import TextNode

from common.Chart import Chart
from common.Constants import Constants
from common.CustomTimer import CountUpTimer
from common.DirectBasicButton import DirectBasicButton
from common.DirectBasicLabel import DirectBasicLabel
from common.DirectBasicWindow import DirectBasicWindow
from common.DirectDropDownMenu import DirectDropDownMenu
from common.DirectMeterBar import DirectMeterBar
from common.DirectWindow import DirectWindow
from common.FloatingText import FloatingText

from main.MainLobby.World.Avatars.Avatars import Avatars
from main.MainLobby.World.Chat.Chat import Chat
from main.MainLobby.World.GameShop.GameShop import GameShop
from main.MainLobby.World.Menu.Menu import Menu
from main.MainLobby.World.Weather.Weather import Weather
from main.MainLobby.World.World3D.Camera import Camera
from main.MainLobby.World.World3D.GameState import GameState
from main.MainLobby.World.World3D.Sound import Sound
from main.MainLobby.World.World3D.World3D import World3D

from main.MainLobby.World.World3D.Test import Test
    
class WorldGUI:
    
    def __init__(self):

        if Constants.DEBUG:
            print 'Loading World...'

        # Create an event called 'window-close' whenever the user tries to
        # close the window to perform additional procedures before closing.
        # The event is created in Menu class.

        self.clock = None
#        base.setFrameRateMeter(True) 
        base.userExit = lambda:None
        self.createLoadingImage()
        # render a frame, otehrwise the screen won't chnage
        base.graphicsEngine.renderFrame()
        base.graphicsEngine.renderFrame()
        
        ##Loading info into world, please put all the loading process in between
        base.disableMouse()

        self.createMainFrame()
        self.createDate()

        self.gameState = GameState(self)  
        
        self.weatherFrame = Weather(self.mainFrame)
        self.chat = Chat(self.mainFrame)
        self.gameShop = GameShop(self)
        self.avatar = Avatars(self)
        self.menu = Menu(self)

        self.createChart()

        self.createMessageLabel()
        self.createInfoFrame()
        self.createEnvScoreLabel()
        self.createHighScoreLabel()
        self.createPlayerCountLabel()

        self.floatingText = FloatingText()

        self.leftPendingText = FloatingText(align = TextNode.ALeft)
        self.leftPendingText.setPosition(-1.5, -0.35)

        self.rightPendingText = FloatingText(align = TextNode.ARight)
        self.rightPendingText.setPosition(1.5, -0.35)

        self.soundMgr = Sound()
        self.world = World3D(self)
        self.displayGame()
#           End of loading process
        self.switchToWorld()
        self.camera = Camera(self.gameState)

        self.restartButton = None

    def createChart(self):

        self.chartWindow = DirectBasicWindow( title = 'Charts',
                                              onClose = self.toggleChart,
                                              frameSize = (-1.1, 1.1, -0.6, 0.6),
                                              frameColor = Constants.BG_COLOR,
                                              pos = (0, 0, 0),
                                              state = DGG.NORMAL )
        self.chartWindow.reparentTo(self.mainFrame)
        self.chartWindow.hide()

        self.chart = Chart(self)
        self.chart.reparentTo(self.chartWindow)
        self.chart.hide()

        self.chart.setAxisLabels('Month', 'Biomass')
        game.requestChartBiomass(0)

        self.chartTwo = Chart(self)
        self.chartTwo.reparentTo(self.chartWindow)
        self.chartTwo.hide()

        self.chartTwo.setAxisLabels('Month', '# of Organisms')
        game.requestChartBiomass(1)

        self.chartThree = Chart(self)
        self.chartThree.reparentTo(self.chartWindow)
        self.chartThree.hide()

        self.chartThree.setAxisLabels('Month', 'Environment Score')
        game.requestChartBiomass(2)

        self.chartMenu = DirectDropDownMenu( frameColor = Constants.BG_COLOR,
                                             width = 0.7,
                                             max_items = 10,
                                             direction = 'down',
                                             command = self.switchChart )
        self.chartMenu.reparentTo(self.chartWindow)
        self.chartMenu.setPos(0.69, 0, 0.494)

        self.chartMenu.setItems(['# of Organisms', 'Biomass', 'Environment Score'])
        self.chartMenu.selectOptionByIndex(0)

        self.chartButtonFrame = DirectFrame( frameSize = (-0.086, 0.086, -0.041, 0.041),
                                             frameColor = Constants.BG_COLOR,
                                             pos = (-1.275, 0, -0.72) )
        self.chartButtonFrame.reparentTo(self.mainFrame)

        self.chartButton = DirectBasicButton( text = 'Charts',
                                              text_fg = Constants.TEXT_COLOR,
                                              text_font = Constants.FONT_TYPE_01,
                                              text_pos = (0, -0.015),
                                              text_scale = 0.04,
                                              text_shadow = Constants.TEXT_SHADOW_COLOR,
                                              frameSize = (-0.08, 0.08, -0.035, 0.035),
                                              frameColor = (0, 0, 0, 0.2),
                                              pos = (0, 0, 0),
                                              relief = DGG.FLAT,
                                              command = self.toggleChart )
        self.chartButton.reparentTo(self.chartButtonFrame)

    def switchChart(self, value):

        if value == 0:
            self.chart.hide()
            self.chartTwo.show()
            self.chartThree.hide()
        elif value == 1:
            self.chart.show()
            self.chartTwo.hide()
            self.chartThree.hide()
        elif value == 2:
            self.chart.hide()
            self.chartTwo.hide()
            self.chartThree.show()

    def toggleChart(self):

        if self.chartWindow.isHidden():
            self.chartWindow.show()
        else:
            self.chartWindow.hide()

    def createLoadingImage(self):
        self.loadingImage = OnscreenImage(image = 'models/' + 'Loading.png',
                                          scale = (base.camLens.getAspectRatio(), 1, 1),
                                          sort = 30)
#        self.percentage = OnscreenText(text='0%', pos=(0,1,0), scale=0.1)
    def switchToWorld(self):
        """
        Hide the loading screen and switch to world
        """
        self.loadSequence = Sequence(Wait(0.1), Func(self.loadingImage.hide))
        self.loadSequence.start()
        self.keyMap = {"1":0, "2":0}

    def startWorld(self, args):
        if args['status']:
#            self.gameState.timeRate = args['rate']

#            self.startClock(args['day'], args['hour'], args['rate'])
            self.world.startTime(0, 1.0)

    def createMainFrame(self):
        
        self.mainFrame = DirectWindow(frameSize = (0,0,0,0),
                                      frameColor = Constants.BG_COLOR,
                                      pos = (0,0,0))
        self.mainFrame.reparentTo(aspect2d)

    def createMessageLabel(self):

        self.msgLabel = DirectBasicLabel( text = '',
                                          text_fg = Constants.TEXT_COLOR,
                                          text_font = Constants.FONT_TYPE_01,
                                          text_scale = 0.045,
                                          text_shadow = Constants.TEXT_SHADOW_COLOR,
                                          frameColor = (0, 0, 0, 0),
                                          pos = (0, 0, -0.45) )
        self.msgLabel.reparentTo(self.mainFrame)

    def createInfoFrame(self):

        self.infoFrame = DirectFrame( frameSize = (-0.95, 0.95, -0.05, 0.05),
                                      frameColor = Constants.BG_COLOR,
                                      pos = (-0.64, 0, -0.935),
                                      state = DGG.NORMAL )
        self.infoFrame.reparentTo(self.mainFrame)

        self.levelFrame = DirectFrame( frameSize = (-0.165, 0.165, -0.04, 0.04),
                                       frameColor = (0, 0, 0, 0.2),
                                       pos = (-0.775, 0, 0) )
        self.levelFrame.reparentTo(self.infoFrame)

        self.levelBar = DirectFrame( frameSize = (-0.159, 0.159, -0.034, 0.034),
                                     frameColor = (0, 0, 0, 0.2),
                                     pos = (0, 0, 0) )
        self.levelBar.reparentTo(self.levelFrame)

        self.levelText = DirectBasicLabel( text = 'Level',
                                           text_align = TextNode.ALeft,
                                           text_fg = Constants.TEXT_COLOR,
                                           text_font = Constants.FONT_TYPE_02,
                                           text_pos = (0, -0.0125),
                                           text_scale = 0.05,
                                           text_shadow = Constants.TEXT_SHADOW_COLOR,
                                           frameColor = (0, 0, 0, 0),
                                           pos = (-0.13, 0, 0) )
        self.levelText.reparentTo(self.levelFrame)

        self.levelLabel = DirectBasicLabel( text = '1',
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_02,
                                            text_pos = (0, -0.0125),
                                            text_scale = 0.05,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameColor = (0, 0, 0, 0),
                                            pos = (0.08, 0, 0) )
        self.levelLabel.reparentTo(self.levelFrame)

        self.expFrame = DirectFrame( frameSize = (-0.6, 0.6, -0.04, 0.04),
                                     frameColor = (0, 0, 0, 0.2),
                                     pos = (0, 0, 0) )
        self.expFrame.reparentTo(self.infoFrame)

        self.expBar = DirectMeterBar( text = '0 / 0',
                                      text_fg = Constants.TEXT_COLOR,
                                      text_font = Constants.FONT_TYPE_02,
                                      text_pos = (0, -0.0125),
                                      text_scale = 0.05,
                                      text_shadow = Constants.TEXT_SHADOW_COLOR,
                                      frameSize = (-0.594, 0.594, -0.034, 0.034),
                                      frameColor = (0, 0, 0, 0.2),
                                      pos = (0, 0, 0),
                                      barColor = (0.8, 0.8, 0, 1),
                                      command = self.levelUp )
        self.expBar.reparentTo(self.expFrame)

        self.expText = DirectBasicLabel( text = 'XP',
                                         text_align = TextNode.ALeft,
                                         text_fg = Constants.TEXT_COLOR,
                                         text_font = Constants.FONT_TYPE_02,
                                         text_pos = (0, -0.0125),
                                         text_scale = 0.05,
                                         text_shadow = Constants.TEXT_SHADOW_COLOR,
                                         frameColor = (0, 0, 0, 0),
                                         pos = (-0.575, 0, 0) )
        self.expText.reparentTo(self.expFrame)

        self.goldFrame = DirectFrame( frameSize = (-0.165, 0.165, -0.04, 0.04),
                                      frameColor = (0, 0, 0, 0.2),
                                      pos = (0.775, 0, 0) )
        self.goldFrame.reparentTo(self.infoFrame)

        self.goldBar = DirectFrame( frameSize = (-0.159, 0.159, -0.034, 0.034),
                                    frameColor = (0, 0, 0, 0.2),
                                    pos = (0, 0, 0) )
        self.goldBar.reparentTo(self.goldFrame)

        self.goldLabel = DirectBasicLabel( text = '0',
                                           text_align = TextNode.ARight,
                                           text_fg = Constants.TEXT_COLOR,
                                           text_font = Constants.FONT_TYPE_02,
                                           text_pos = (0, -0.0125),
                                           text_scale = 0.05,
                                           text_shadow = Constants.TEXT_SHADOW_COLOR,
                                           frameColor = (0, 0, 0, 0),
                                           pos = (0.095, 0, 0) )
        self.goldLabel.reparentTo(self.goldFrame)

        self.goldText = DirectBasicLabel( text = 'G',
                                          text_align = TextNode.ALeft,
                                          text_fg = Constants.TEXT_COLOR,
                                          text_font = Constants.FONT_TYPE_02,
                                          text_pos = (0, -0.0125),
                                          text_scale = 0.05,
                                          text_shadow = Constants.TEXT_SHADOW_COLOR,
                                          frameColor = (0, 0, 0, 0),
                                          pos = (0.105, 0, 0) )
        self.goldText.reparentTo(self.goldFrame)

    def levelUp(self):

        self.levelLabel['text'] = str(int(self.levelLabel['text']) + 1)
        self.leftPendingText.createPendingText(Constants.TEXT_TYPE_LEVEL_UP, 'Level Up!')

    def createEnvScoreLabel(self):

        self.envScoreText = DirectBasicLabel( text = 'Environment Score',
                                              text_fg = (1, 0.93, 0.73, 1),
                                              text_font = Constants.FONT_TYPE_02,
                                              text_scale = 0.065,
                                              text_shadow = Constants.TEXT_SHADOW_COLOR,
                                              frameColor = (0, 0, 0, 0),
                                              pos = (0, 0, 0.76) )
        self.envScoreText.reparentTo(self.mainFrame)

        self.envScoreStatus = DirectBasicLabel( text = '',
                                                text_fg = (0, 1, 0, 1),
                                                text_pos = (-0.002, -0.002),
                                                text_font = Constants.FONT_TYPE_02,
                                                text_scale = 0.08,
                                                text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                frameColor = (0, 0, 0, 0),
                                                pos = (0.375, 0, 0.76) )
        self.envScoreStatus.reparentTo(self.mainFrame)

        self.envScoreLabel = DirectBasicLabel( text = '0',
                                               text_fg = Constants.TEXT_COLOR,
                                               text_font = Constants.FONT_TYPE_02,
                                               text_scale = 0.1,
                                               text_shadow = Constants.TEXT_SHADOW_COLOR,
                                               frameColor = (0, 0, 0, 0),
                                               pos = (0, 0, 0.66) )
        self.envScoreLabel.reparentTo(self.mainFrame)

    def setEnvScoreStatus(self, status):

        if status:
            self.envScoreStatus['text'] = '+'
            self.envScoreStatus['text_fg'] = (0, 1, 0, 1)
            self.envScoreStatus['text_pos'] = (-0.002, -0.002)
            self.envScoreStatus['text_scale'] = 0.08
        else:
            self.envScoreStatus['text'] = '_'
            self.envScoreStatus['text_fg'] = (1, 0, 0, 1)
            self.envScoreStatus['text_pos'] = (0, 0.025)
            self.envScoreStatus['text_scale'] = 0.065

    def createDate(self):

        self.yearLabel = DirectBasicLabel( text = 'Year 1',
                                           text_fg = Constants.TEXT_COLOR,
                                           text_font = Constants.FONT_TYPE_02,
                                           text_scale = 0.06,
                                           text_shadow = Constants.TEXT_SHADOW_COLOR,
                                           frameColor = (0, 0, 0, 0),
                                           pos = (0, 0, 0.94) )
        self.yearLabel.reparentTo(self.mainFrame)

        self.monthLabel = DirectBasicLabel( text = month_name[1],
                                            text_fg = Constants.TEXT_COLOR,
                                            text_font = Constants.FONT_TYPE_02,
                                            text_scale = 0.06,
                                            text_shadow = Constants.TEXT_SHADOW_COLOR,
                                            frameColor = (0, 0, 0, 0),
                                            pos = (0, 0, 0.88) )
        self.monthLabel.reparentTo(self.mainFrame)

        self.startDotLabel = DirectBasicLabel( text = '.',
                                               text_fg = (0.65, 0.65, 0.65, 1),
                                               text_font = Constants.FONT_TYPE_02,
                                               text_scale = 0.09,
                                               text_shadow = Constants.TEXT_SHADOW_COLOR,
                                               frameColor = (0, 0, 0, 0),
                                               pos = (-0.198, 0, 0.8325) )
        self.startDotLabel.reparentTo(self.mainFrame)

        self.endDotLabel = DirectBasicLabel( text = '.',
                                             text_fg = (0.35, 0.35, 0.35, 1),
                                             text_font = Constants.FONT_TYPE_02,
                                             text_scale = 0.09,
                                             text_shadow = Constants.TEXT_SHADOW_COLOR,
                                             frameColor = (0, 0, 0, 0),
                                             pos = (0.198, 0, 0.8325) )
        self.endDotLabel.reparentTo(self.mainFrame)

        self.timeDotLabel = DirectBasicLabel( text = '.',
                                              text_fg = (1, 1, 1, 1),
                                              text_font = Constants.FONT_TYPE_02,
                                              text_scale = 0.13,
                                              text_shadow = Constants.TEXT_SHADOW_COLOR,
                                              frameColor = (0, 0, 0, 0),
                                              pos = (-0.17, 0, 0.83) )
        self.timeDotLabel.reparentTo(self.mainFrame)

        self.timeSequence = Sequence()

    def setTime(self, current, duration, rate):

        self.timeSequence.finish()

        percent = current / duration
        startPos = (-0.198 + 0.396 * percent, 0, 0.8325)
        endPos = (0.198, 0, 0.8325)

        self.timeSequence = LerpPosInterval(self.timeDotLabel, duration / rate, endPos, startPos)
        self.timeSequence.start()
        self.timeSequence.setT(current / rate)

    def setYear(self, year):
        self.yearLabel['text'] = 'Year ' + str(year)

    def setMonth(self, month):
        self.monthLabel['text'] = month_name[month]

    def createHighScoreLabel(self):

        self.scoreList = {}
        self.scoreList['scoreList'] = ['User - 0', 'User - 0', 'User - 0']
        self.scoreList['totalScoreList'] = ['User - 0', 'User - 0', 'User - 0']
        self.scoreList['currentScoreList'] = ['User - 0', 'User - 0', 'User - 0']

        self.topScoreLabel = DirectBasicLabel( text = 'Top Scores',
                                               text_align = TextNode.ARight,
                                               text_fg = Constants.TEXT_COLOR,
                                               text_font = Constants.FONT_TYPE_02,
                                               text_scale = 0.065,
                                               text_shadow = Constants.TEXT_SHADOW_COLOR,
                                               frameColor = (0, 0, 0, 0),
                                               pos = (1.55, 0, 0.94) )
        self.topScoreLabel.reparentTo(self.mainFrame)

        self.bestEnvScoreLabel = DirectBasicLabel( text = 'High Score',
                                                   text_align = TextNode.ARight,
                                                   text_fg = (1, 0.93, 0.73, 1),
                                                   text_font = Constants.FONT_TYPE_02,
                                                   text_scale = 0.05,
                                                   text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                   frameColor = (0, 0, 0, 0),
                                                   pos = (1.55, 0, 0.86) )
        self.bestEnvScoreLabel.reparentTo(self.mainFrame)

        self.bestEnvScoreTextList = []

        for i in range(3):
            bestEnvScoreText = DirectBasicLabel( text = 'User - 0',
                                                 text_align = TextNode.ARight,
                                                 text_fg = Constants.TEXT_COLOR,
                                                 text_font = Constants.FONT_TYPE_02,
                                                 text_scale = 0.055,
                                                 text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                 frameColor = (0, 0, 0, 0),
                                                 pos = (1.55, 0, 0.8 - i * 0.06) )
            bestEnvScoreText.reparentTo(self.mainFrame)
            self.bestEnvScoreTextList.append(bestEnvScoreText)

        self.bestTotalEnvScoreLabel = DirectBasicLabel( text = 'Total Score',
                                                        text_align = TextNode.ARight,
                                                        text_fg = (1, 0.93, 0.73, 1),
                                                        text_font = Constants.FONT_TYPE_02,
                                                        text_scale = 0.05,
                                                        text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                        frameColor = (0, 0, 0, 0),
                                                        pos = (1.55, 0, 0.6) )
        self.bestTotalEnvScoreLabel.reparentTo(self.mainFrame)

        self.bestTotalEnvScoreTextList = []

        for i in range(3):
            bestTotalEnvScoreText = DirectBasicLabel( text = 'User - 0',
                                                      text_align = TextNode.ARight,
                                                      text_fg = Constants.TEXT_COLOR,
                                                      text_font = Constants.FONT_TYPE_02,
                                                      text_scale = 0.055,
                                                      text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                      frameColor = (0, 0, 0, 0),
                                                      pos = (1.55, 0, 0.54 - i * 0.06) )
            bestTotalEnvScoreText.reparentTo(self.mainFrame)
            self.bestTotalEnvScoreTextList.append(bestTotalEnvScoreText)

        self.bestCurrentScoreLabel = DirectBasicLabel( text = 'Current Score',
                                                       text_align = TextNode.ARight,
                                                       text_fg = (1, 0.93, 0.73, 1),
                                                       text_font = Constants.FONT_TYPE_02,
                                                       text_scale = 0.05,
                                                       text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                       frameColor = (0, 0, 0, 0),
                                                       pos = (1.55, 0, 0.34) )
        self.bestCurrentScoreLabel.reparentTo(self.mainFrame)

        self.bestCurrentScoreTextList = []

        for i in range(3):
            bestCurrentScoreText = DirectBasicLabel( text = 'User - 0',
                                                     text_align = TextNode.ARight,
                                                     text_fg = Constants.TEXT_COLOR,
                                                     text_font = Constants.FONT_TYPE_02,
                                                     text_scale = 0.055,
                                                     text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                     frameColor = (0, 0, 0, 0),
                                                     pos = (1.55, 0, 0.28 - i * 0.06) )
            bestCurrentScoreText.reparentTo(self.mainFrame)
            self.bestCurrentScoreTextList.append(bestCurrentScoreText)

        self.scoreSequence = Sequence()

        game.requestHighScore(0)

    def setBestEnvScore(self, scoreList):
        self.scoreList['scoreList'] = scoreList

    def setBestTotalEnvScore(self, totalScoreList):
        self.scoreList['totalScoreList'] = totalScoreList

    def setBestCurrentEnvScore(self, currentScoreList):
        self.scoreList['currentScoreList'] = currentScoreList

    def startScoreSequence(self):

        if not self.scoreSequence.isPlaying():
            self.scoreSequence = Sequence(Func(self.setBestScoreInfo, 0), Wait(10), Func(self.setBestScoreInfo, 1), Wait(10))
            self.scoreSequence.loop()

    def setBestScoreInfo(self, type):

        scoreList = self.scoreList['scoreList']
        totalScoreList = self.scoreList['totalScoreList']
        currentScoreList = self.scoreList['currentScoreList']

        if type == 0:
            self.topScoreLabel['text'] = 'Your Scores'

            bestEnvScoreText = self.bestEnvScoreTextList[0]
            bestEnvScoreText['text'] = str(scoreList[0][1])

            bestTotalEnvScoreText = self.bestTotalEnvScoreTextList[0]
            bestTotalEnvScoreText.setZ(0.66)

            bestTotalEnvScoreText['text'] = str(totalScoreList[0][1])

            bestCurrentScoreText = self.bestCurrentScoreTextList[0]
            bestCurrentScoreText.setZ(0.52)

            bestCurrentScoreText['text'] = str(currentScoreList[0][1])

            self.bestTotalEnvScoreLabel.setZ(0.72)
            self.bestCurrentScoreLabel.setZ(0.58)

            for i in range(1, 3):
                self.bestEnvScoreTextList[i].hide()
                self.bestTotalEnvScoreTextList[i].hide()
                self.bestCurrentScoreTextList[i].hide()

            game.requestHighScore(1)
        else:
            self.topScoreLabel['text'] = 'Top Scores'

            self.bestTotalEnvScoreLabel.setZ(0.6)
            self.bestCurrentScoreLabel.setZ(0.34)

            for i in range(3):
                bestEnvScoreText = self.bestEnvScoreTextList[i]
                bestEnvScoreText.setZ(0.8 - i * 0.06)
                bestEnvScoreText.show()

                if i < len(scoreList):
                    bestEnvScoreText['text'] = scoreList[i][0] + ' - ' + str(scoreList[i][1])
                else:
                    bestEnvScoreText['text'] = '-'

                bestTotalEnvScoreText = self.bestTotalEnvScoreTextList[i]
                bestTotalEnvScoreText.setZ(0.54 - i * 0.06)
                bestTotalEnvScoreText.show()

                if i < len(totalScoreList):
                    bestTotalEnvScoreText['text'] = totalScoreList[i][0] + ' - ' + str(totalScoreList[i][1])
                else:
                    bestTotalEnvScoreText['text'] = '-'

                bestCurrentScoreText = self.bestCurrentScoreTextList[i]
                bestCurrentScoreText.setZ(0.28 - i * 0.06)
                bestCurrentScoreText.show()

                if i < len(currentScoreList):
                    bestCurrentScoreText['text'] = currentScoreList[i][0] + ' - ' + str(currentScoreList[i][1])
                else:
                    bestCurrentScoreText['text'] = '-'

            game.requestHighScore(0)

    def createPlayerCountLabel(self):

        self.playerCountLabel = DirectBasicLabel( text = '0 Players Online',
                                                  text_align = TextNode.ALeft,
                                                  text_fg = Constants.TEXT_COLOR,
                                                  text_font = Constants.FONT_TYPE_02,
                                                  text_scale = 0.05,
                                                  text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                  frameColor = (0, 0, 0, 0),
                                                  pos = (-1.35, 0, 0.93) )
        self.playerCountLabel.reparentTo(self.mainFrame)

        game.requestPlayers()

    def setOnlinePlayers(self, args):

        self.playerCountLabel['text'] = str(len(args)) + ' Players Online'

    def createClock(self):

        self.timeFrame = DirectLabel(text='Day: -  HR: -',
                                     text_fg = Constants.TEXT_COLOR,
                                    text_font = Constants.FONT_TYPE_01,
                                    text_align=TextNode.ACenter,
                                    text_pos = (0, -0.015),
                                    text_scale = 0.06,
                                    text_shadow = Constants.TEXT_SHADOW_COLOR,
                                    frameSize = (-0.25, 0.25, -0.05, 0.05),
                                    frameColor = Constants.BG_COLOR,
                                    pos = (0, 0, 0.95),
                                    relief = DGG.FLAT)
        self.timeFrame.reparentTo(self.mainFrame)

        self.clock = CountUpTimer(self.timeFrame)

    def startClock(self, day, hour, rate):
        """
        Calculate the seconds map to hours
        """

        if self.clock != None:
            self.clock.stop()

        self.clock.setTime(hour, rate)
        self.clock.start()

    def resetClock(self, _range):
        """
        restart the clock
        """
        self.startClock(_range)

    def createRestartBox(self):

        if self.restartButton == None:
            main.createMessageBox(1, 'Ecosystem Collapsed. Restart?', self.gameState.requestRestart)
            self.createRestartButton()

    def createRestartButton(self):

        self.restartButton = DirectFrame( frameSize = (-0.22, 0.22, -0.055, 0.055),
                                          frameColor = Constants.BG_COLOR,
                                          pos = (0, 0, 0.8),
                                          state = DGG.NORMAL )

        self.restartButton_2 = DirectBasicButton( text = 'Restart Ecosystem',
                                                  text_fg = Constants.TEXT_COLOR,
                                                  text_font = Constants.FONT_TYPE_01,
                                                  text_pos = (0, -0.015),
                                                  text_scale = 0.045,
                                                  text_shadow = Constants.TEXT_SHADOW_COLOR,
                                                  frameSize = (-0.21, 0.21, -0.045, 0.045),
                                                  frameColor = (0, 0, 0, 0.3),
                                                  pos = (0, 0, 0),
                                                  relief = DGG.FLAT,
                                                  command = self.gameState.requestRestart,
                                                  extraArgs = [True] )
        self.restartButton_2.reparentTo(self.restartButton)

    def hideBottom(self):

        self.chat.hide()
        self.weatherFrame.hide()
        self.gameShop.hide()
        self.avatar.reposition()
        
    def showBottom(self):
        self.avatar.restorePos()
        self.chat.show()
        self.weatherFrame.show()
        self.gameShop.show()

    def getControls(self):
        return self.controls
    
    def displayGame(self):

        self.effectStatus = 'day'
        self.scaleFactor = 0.5  
        #Test(self.gameState,self.gameShop,self.avatar)
        taskMgr.add(self.updateTask, "update")

    def updateTask(self, task):
        return task.cont

    def loadParticleConfig(self, file):
        print('not yet implemented')

    def unload(self):
        if Constants.DEBUG:
            print 'Unloading World...'
        if self.clock:
            self.clock.stop()
        main.audioManager.removeMusic()
        main.removeGameControls()        
        self.avatar.unload()
        self.gameShop.unload()
        self.weatherFrame.unload()
        self.chat.unload()
        self.menu.unload()
        self.soundMgr.unload()
        self.mainFrame.destroy()
