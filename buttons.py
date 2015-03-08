from pandac.PandaModules import *
loadPrcFile('config/config_dev.prc')

from direct.actor.Actor import Actor
from direct.gui import DirectGuiGlobals
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
from toontown.election.DistributedInvasionSuit import DistributedInvasionSuit
from toontown.suit import DistributedSuitBase, SuitDNA, BossCog
from direct.directbase import DirectStart
from direct.directbase import DirectStart
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from funnyfarm.toonbase import FunnyFarmGlobals
from toontown.toon import NPCToons
import __builtin__
FunnyFarmGlobals.setNametagGlobals()
FunnyFarmGlobals.setParticleManagers()

class game:
	name = 'toontown'
	process = 'client'

base.game = game()
__builtin__.game = base.game

class MovieMaker():    
    
    def __init__(self):
        self.movieButtons()
        self.cogs = []
        self.playgrounds = []
        
    def oobeCamera(self):
        base.oobe()
        render.find('**/camera').hide()
    """Lets Start Off With Playgrounds"""
    def ttcPlayground(self):
        ttcplayground = loader.loadModel('phase_15/hood/toontown_central.bam')
        ttcplayground.reparentTo(render)
        ttcplayground.find('**/hill').setTransparency(TransparencyAttrib.MBinary, 1)
        ttcsky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
        ttcsky.reparentTo(render)
        self.playgrounds.append(ttcplayground)
        self.playgrounds.append(ttcsky)

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
        self.playgrounds.append(self.ddplayground)
        self.playgrounds.append(self.ddsky)

    def dgPlayground(self):
        dgplayground = loader.loadModel('phase_15/hood/daisys_garden.bam')
        dgplayground.reparentTo(render)
        dgsky = loader.loadModel('phase_3.5/models/props/TT_sky.bam')
        dgsky.reparentTo(render)
        self.playgrounds.append(dgplayground)
        self.playgrounds.append(dgsky)

    def killPlayground(self):
        for playground in self.playgrounds:
            playground.removeNode()
        self.playgrounds = []

    def randomCog(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuitRandom()
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.loop('neutral')
        suit.reparentTo(render)
        self.cogs.append(suit)
    
    def cogHollywood(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('bf')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Mr. Hollywood\nSellbot')
        self.cogs.append(suit)

    def cogMingler(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('f')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        #suit.loop('phone')
        suit.reparentTo(render)
        suit.setDisplayName('Mingler\nSellbot')
        self.cogs.append(suit)

    def killCogs(self):
        for cog in self.cogs:
            cog.delete()
        self.cogs = []

    def toonDim(self):
        self.dimm = NPCToons.createLocalNPC(2018)
        self.dimm.useLOD(1000)
        self.dimm.find('**/250').removeNode()
        self.dimm.find('**/500').removeNode()
        self.dimm.setPos(base.localAvatar.getPos())
        self.dimm.initializeBodyCollisions('toon')
        self.dimm.addActive()
        self.dimm.startBlink()
        self.dimm.loop('neutral')
        self.dimm.reparentTo(render)

    def hideButtons(self):
        self.ImgBtn1.hide()
        self.ImgBtn2.hide()
        return 'Buttons Now Hid'
    
    def movieButtons(self):
        #Unlocks
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn1 = DirectButton(frameSize=None, text='Unlocks', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.dgPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.15,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn5 = DirectButton(frameSize=None, text='Global Teleport', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonDim, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.15,-0,.03), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        
        self.ImgBtn5.bind(DirectGuiGlobals.B2PRESS, self.delete_button)
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
        self.ImgBtn5.editStop(dispatch)
        
moviemaker = MovieMaker()            