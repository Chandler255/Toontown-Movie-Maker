from direct.directbase import DirectStart
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from funnyfarm.toonbase import FFTime
import random

class ToontownLoadingScreen:

    def __init__(self):
        self.__expectedCount = 0
        self.__count = 0
        self.mickey = loader.loadFont('phase_3/models/fonts/MickeyFont.bam')
        self.minnie = loader.loadFont('phase_3/models/fonts/MinnieFont.bam')
        self.gui = loader.loadModel('phase_3/models/gui/progress-background.bam')
        self.title = DirectLabel(guiId='ToontownLoadingScreenTitle', parent=self.gui, relief=None, pos=(base.a2dRight/5, 0, 0.235), text='', textMayChange=1, text_scale=0.08, text_fg=(0.03, 0.83, 0, 1), text_align=TextNode.ALeft, text_font=self.mickey)
        self.logo = DirectLabel(guiId='ToontownLoadingScreenLogo', parent=self.gui, relief=None, text="Toontown's\nFunny Farm", text_fg=(0.788235, 0.090196, 0.176471, 1.0), text_scale=0.2, text_shadow=(0, 0, 0, 1), text_font=self.minnie)
        self.waitBar = DirectWaitBar(guiId='ToontownLoadingScreenWaitBar', parent=self.gui, frameSize=(base.a2dLeft+(base.a2dRight/4.95), base.a2dRight-(base.a2dRight/4.95), -0.03, 0.03), pos=(0, 0, 0.15), text='')

    def destroy(self):
        self.title.destroy()
        self.gui.removeNode()
    '''
    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + '\n' + random.choice(TTLocalizer.TipDict.get(tipCategory))
    '''
    def begin(self, range, label, zoneId):
        self.waitBar['range'] = range
        self.title['text'] = label
        self.__count = 0
        self.__expectedCount = range
        self.gui.reparentTo(aspect2d, NO_FADE_SORT_INDEX)
        self.title.reparentTo(base.a2dpBottomLeft, NO_FADE_SORT_INDEX)
        self.title.setPos(0.24, 0, 0.23)
        self.logo.reparentTo(base.a2dpTopCenter)
        self.logo.setPos(0, 0, -0.23)
        self.waitBar.reparentTo(base.a2dpBottomCenter, NO_FADE_SORT_INDEX)
        self.waitBar.update(self.__count)

    def end(self):
        self.waitBar.finish(N=30)
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.logo.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        return (self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)

    def tick(self):
        self.__count = self.__count + 1
        self.waitBar.update(self.__count)


