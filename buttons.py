from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.directutil import Mopath
from direct.actor.Actor import Actor
from direct.gui.DirectGui import DirectButton
from toontown.suit import DistributedSuitBase, SuitDNA, BossCog
from toontown.events.DistributedInvasionSuit import DistributedInvasionSuit

class MovieMaker():    
    
    def __init__(self):
        self.movieButtons()
        self.cogValues()
        self.cogs = []
        self.playgrounds = []
        
    def cogValues(self):
        self.aSize = 6.06
        self.bSize = 5.29
        self.cSize = 4.14
        self.corpPolyColor = VBase4(0.95, 0.75, 0.75, 1.0)
        self.legalPolyColor = VBase4(0.75, 0.75, 0.95, 1.0)
        self.moneyPolyColor = VBase4(0.65, 0.95, 0.85, 1.0)
        self.salesPolyColor = VBase4(0.95, 0.75, 0.95, 1.0)
        self.icons = loader.loadModel('phase_3/models/gui/cog_icons.bam')
        #self.chestNull = cog.find('**/joint_attachMeter')
        self.bossbotMed = Vec4(0.863, 0.776, 0.769, 1.0)
        self.sellbotMed = Vec4(0.843, 0.745, 0.745, 1.0)
        self.lawbotMed = Vec4(0.749, 0.776, 0.824, 1.0)
        self.cashbotMed = Vec4(0.749, 0.769, 0.749, 1.0)
        
    def oobeCamera(self):
        base.oobe()
        render.find('**/camera').hide()
    
    def ttcPlayground(self):
        ttcplayground = loader.loadModel('phase_15/hood/toontown_central.bam')
        ttcplayground.reparentTo(render)
        ttcplayground.find('**/hill').setTransparency(TransparencyAttrib.MBinary, 1)
        ttcsky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
        ttcsky.reparentTo(render)
        self.playgrounds.append(ttcplayground)
        self.playgrounds.append(ttcsky)
    
    def cogHollywood(self):
        """cog = Actor('phase_3.5/models/char/suitA-mod.bam', {"Neutral":'phase_4/models/char/suitA-victory.bam'})
        cog.loop('Neutral')
        cog.setPos(base.localAvatar.getPos())
        cog.setScale(7.0 / self.aSize)
        corpMedallion = self.icons.find('**/SalesIcon').copyTo(cog.find('**/joint_attachMeter'))
        corpMedallion.setPosHprScale(0.02, 0.05, 0.04, 180.0, 0.0, 0.0, 0.51, 0.51, 0.51)
        corpMedallion.setColor(self.sellbotMed)
        cog.find('**/hands').setColor(self.salesPolyColor)
        cog.reparentTo(render)
        myTex = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
        cog.findAllMatches('**/torso').setTexture(myTex, 1)
        myTex2 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
        cog.findAllMatches('**/legs').setTexture(myTex2, 1)
        myTex3 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
        cog.findAllMatches('**/arms').setTexture(myTex3, 1)
        head = loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/yesman')
        head.reparentTo(cog.find('**/joint_head'))
        self.cogs.append(cog)"""

        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('hh')
        suit.setDNA(suitDNA)
        suit.reparentTo(render)
        suit.setDisplayName('Head Hunter\nBossbot\nLevel 10')
        self.cogs.append(suit)
        
    def killCogs(self):
        for cog in self.cogs:
            cog.delete()
        self.cogs = []
        
    def killPlayground(self):
        for playground in self.playgrounds:
            playground.removeNode()
        self.playgrounds = []
    
    def ddPlayground(self):
        self.ddplayground = loader.loadModel('phase_15/hood/donalds_dock.bam')
        self.ddplayground.reparentTo(render)
        boat = self.ddplayground.find('**/donalds_boat')
        boat.unstash()
        self.eastWestMopath = Mopath.Mopath()
        self.westEastMopath = Mopath.Mopath()
        self.eastWestMopath.loadFile('phase_6/paths/dd-e-w.bam')
        self.eastWestMopathInterval = MopathInterval(self.eastWestMopath, boat)
        ewBoatTrack = ParallelEndTogether(Parallel(self.eastWestMopathInterval, name='ew-boat'))
        self.westEastMopath.loadFile('phase_6/paths/dd-w-e.bam')
        self.westEastMopathInterval = MopathInterval(self.westEastMopath, boat)
        weBoatTrack = ParallelEndTogether(Parallel(self.westEastMopathInterval, name='we-boat'))
        PIER_TIME = 5.0
        eastPier = self.ddplayground.find('**/east_pier')
        ePierHpr = VBase3(90, -44.2601, 0)
        ePierTargetHpr = VBase3(90, 0.25, 0)
        westPier = self.ddplayground.find('**/west_pier')
        wPierHpr = VBase3(-90, -44.2601, 0)
        wPierTargetHpr = VBase3(-90, 0.25, 0)
        ePierDownTrack = Parallel(LerpHprInterval(eastPier, PIER_TIME, ePierHpr, ePierTargetHpr), name='e-pier-down')
        ePierUpTrack = Parallel(LerpHprInterval(eastPier, PIER_TIME, ePierTargetHpr, ePierHpr), name='e-pier-up')
        wPierDownTrack = Parallel(LerpHprInterval(westPier, PIER_TIME, wPierHpr, wPierTargetHpr), name='w-pier-down')
        wPierUpTrack = Parallel(LerpHprInterval(westPier, PIER_TIME, wPierTargetHpr, wPierHpr), name='w-pier-up')
        self.ewTrack = ParallelEndTogether(Parallel(ewBoatTrack, ePierDownTrack), wPierUpTrack, name='ew-track')
        self.weTrack = ParallelEndTogether(Parallel(weBoatTrack, wPierDownTrack), ePierUpTrack, name='we-track')
        self.ewTrack.start()
        self.ddsky = loader.loadModel('phase_3.5/models/props/BR_sky.bam')
        self.ddsky.reparentTo(render)
            
    def hideButtons(self):
        self.ImgBtn1.hide()
        self.ImgBtn2.hide()
        return 'Buttons Now Hid'
    
    def movieButtons(self):
        #Unlocks
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn1 = DirectButton(frameSize=None, text='Unlocks', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ttcPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.15,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn5 = DirectButton(frameSize=None, text='Global Teleport', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogHollywood, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.15,-0,.03), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        
        """self.ImgBtn5.bind(DirectGuiGlobals.B2PRESS, self.delete_button)
        self.ImgBtn5.bind(DirectGuiGlobals.B3PRESS, self.ImgBtn5.editStart)
        self.ImgBtn5.bind(DirectGuiGlobals.B3RELEASE, self.edit_stop)
        
    def delete_button(self, dispatch):
        self.button.destroy()
        
    def hide(self):
        self.button.hide()
        
    def show(self):
        self.button.show()
        
    def place(self):
        self.button.place()
        
    def set_pos(self, x, y, z):
        self.button.set_pos(x, y, z)
    
    def edit_stop(self, dispatch):
        self.ImgBtn5.editStop(dispatch)"""
        
moviemaker = MovieMaker()            