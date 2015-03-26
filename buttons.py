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
from toontown.toon import Toon
from toontown.toon import ToonDNA
from toontown.dna import DNAStorage
from toontown.dna import DNAParser
from funnyfarm.toonbase import FunnyFarmGlobals
from funnyfarm.events.EventBase import EventBaseTT
from funnyfarm.events.EventBase import EventBaseDD
from funnyfarm.events.EventBase import EventBaseDG
from funnyfarm.events.EventBase import EventBaseMM
from funnyfarm.events.EventBase import EventBaseBR
from funnyfarm.events.EventBase import EventBaseDDL
from funnyfarm.events.EventBase import EventBaseSBHQ
from funnyfarm.events.EventBase import EventBaseElections
from funnyfarm.events.EventBase import EventBaseScienceFair
from funnyfarm.events.EventBase import EventBaseToonfest
from funnyfarm.events.EventBase import EventBaseTTWinter
from funnyfarm.events.EventBase import EventBaseTTSpooky
from funnyfarm.events.EventBase import EventBaseDDWinter
from funnyfarm.events.EventBase import EventBaseDDSpooky
from funnyfarm.events.EventBase import EventBaseMMWinter
from funnyfarm.events.EventBase import EventBaseMMSpooky
from funnyfarm.events.EventBase import EventBaseTTStrt
from cogs import Cogs
from toons import Toons
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from otp.margins.WhisperPopup import *
from direct.fsm import ClassicFSM, State

import __builtin__
import sys, os

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
        self.playgrounds = []
        self.cogMaker = Cogs()
        self.toonMaker = Toons()
        
    def oobeCamera(self):
        base.oobe()
        render.find('**/camera').hide()

    def greenScreen(self):
        base.setBackgroundColor(Vec4(0, 1, 0, 0))

    def driveCamera(self):
        base.useDrive()

    """Lets Start Off With Playgrounds"""

    def ttcPlayground(self):
        tf = EventBaseTT()
        tf.loadEvent()

    def ddPlayground(self):
        tf = EventBaseDD()
        tf.loadEvent()

    def dgPlayground(self):
        tf = EventBaseDG()
        tf.loadEvent()

    def mmPlayground(self):
        tf = EventBaseMM()
        tf.loadEvent()

    def brPlayground(self):
        tf = EventBaseBR()
        tf.loadEvent()

    def ddlPlayground(self):
        tf = EventBaseDDL()
        tf.loadEvent()

    def sbPlayground(self):

        for playground in self.playgrounds:
            playground.removeNode()
        self.playgrounds = []

        sbplayground = loader.loadModel('phase_15/hood/sellbot_hq.bam')
        sbplayground.reparentTo(render)
        self.playgrounds.append(sbplayground)

    def sbfacPlayground(self):

        for playground in self.playgrounds:
            playground.removeNode()
        self.playgrounds = []

        sbfacplayground = loader.loadModel('phase_15/hood/sellbot_hq_factory.bam')
        sbfacplayground.reparentTo(render)
        self.playgrounds.append(sbfacplayground)

    def cbPlayground(self):

        for playground in self.playgrounds:
            playground.removeNode()
        self.playgrounds = []

        cbplayground = loader.loadModel('phase_15/hood/cashbot_hq.bam')
        cbplayground.reparentTo(render)
        self.playgrounds.append(cbplayground)

    def lbPlayground(self):

        for playground in self.playgrounds:
            playground.removeNode()
        self.playgrounds = []

        lbplayground = loader.loadModel('phase_15/hood/lawbot_hq.bam')
        lbplayground.reparentTo(render)
        self.playgrounds.append(lbplayground)

    def bbPlayground(self):

        for playground in self.playgrounds:
            playground.removeNode()
        self.playgrounds = []

        bbplayground = loader.loadModel('phase_15/hood/bossbot_hq.bam')
        bbplayground.reparentTo(render)
        self.playgrounds.append(bbplayground)

    def killPlayground(self):
        for playground in self.playgrounds:
            playground.removeNode()
        self.playgrounds = []

    '''Now Time for special Toontown Events'''
    def ttrElections(self):
        tf = EventBaseElections()
        tf.loadEvent()

    def ttrToonfest(self):
        tf = EventBaseToonfest()
        tf.loadEvent()

    def ttiScienceFair(self):
        tf = EventBaseScienceFair()
        tf.loadEvent()

    """Time For Cogs"""

    def hideCogs(self):
        self.cogMaker.hideCogs()

    def randomCog(self):
        self.cogMaker.randomCog()

    """Sellbots"""
    def cogHollywood(self):
        self.cogMaker.cogHollywood()

    def cogMingler(self):
        self.cogMaker.cogMingler()

    def cogFace(self):
        self.cogMaker.cogFace()

    def cogShaker(self):
        self.cogMaker.cogShaker()

    def cogGlad(self):
        self.cogMaker.cogGlad()

    def cogDropper(self):
        self.cogMaker.cogDropper()

    def cogTelemarketer(self):
        self.cogMaker.cogTelemarketer()

    def cogCold(self):
        self.cogMaker.cogCold()

    """Time For Cashbots"""

    def cogRobber(self):
        self.cogMaker.cogRobber()

    def cogShark(self):
        self.cogMaker.cogShark()

    def cogMoney(self):
        self.cogMaker.cogMoney()

    def cogNumber(self):
        self.cogMaker.cogNumber()

    def cogBean(self):
        self.cogMaker.cogBean()

    def cogTight(self):
        self.cogMaker.cogTight()

    def cogPenny(self):
        self.cogMaker.cogPenny()

    def cogShort(self):
        self.cogMaker.cogShort()

    """Time for Lawbots"""

    def cogWig(self):
        self.cogMaker.cogWig()

    def cogEagle(self):
        self.cogMaker.cogEagle()

    def cogDoctor(self):
        self.cogMaker.cogDoctor()

    def cogChaser(self):
        self.cogMaker.cogChaser()

    def cogStabber(self):
        self.cogMaker.cogStabber()

    def cogTalker(self):
        self.cogMaker.cogTalker()

    def cogBlood(self):
        self.cogMaker.cogBlood()

    def cogFeeder(self):
        self.cogMaker.cogFeeder()

    def cogCheese(self):
        self.cogMaker.cogCheese()

    def cogRaider(self):
        self.cogMaker.cogRaider()

    def cogHunter(self):
        self.cogMaker.cogHunter()

    def cogDownsizer(self):
        self.cogMaker.cogDownsizer()

    def cogMicro(self):
        self.cogMaker.cogMicro()

    def cogYesman(self):
        self.cogMaker.cogYesman()

    def cogPencil(self):
        self.cogMaker.cogPencil()

    def cogFlunky(self):
        self.cogMaker.cogFlunky()

    """Time for the toons"""

    def randomToon(self):
        self.toonMaker.randomToon()

    def toonFlippy(self):
        self.toonMaker.toonFlippy()

    def toonDim(self):
        self.toonMaker.toonDim()

    def toonSurlee(self):
        self.toonMaker.toonSurlee()

    def toonSlappy(self):
        self.toonMaker.toonSlappy()

    def toonAlec(self):
        self.toonMaker.toonAlec()

    def toonPrep(self):
        self.toonMaker.toonPrep()

    def toonDaffy(self):
        self.toonMaker.toonDaffy()

    def toonChuckle(self):
        self.toonMaker.toonChuckle()

    def toonClara(self):
        self.toonMaker.toonClara()

    def toonPenny(self):
        self.toonMaker.toonPenny()

    def toonWill(self):
        self.toonMaker.toonWill()

    def toonOldman(self):
        self.toonMaker.toonOldman()
        """End off at oldman"""

    def killToons(self):
        for toon in self.toons:
            toon.delete()
        self.toons = []


    def chatTest(self):
        for toon in self.toons:
            toon.setChatAbsolute('', CFSpeech)
            toon.setChatAbsolute(TTLocalizer.NPCChatTest, CFSpeech|CFTimeout)

    '''def chatTestCogs(self):
        for suit in self.cogs:
            suit.setChatAbsolute('', CFSpeech)
            suit.setChatAbsolute('Hello, welcome to death!', CFSpeech|CFTimeout)'''

    """Time for accessories"""
    """Hat Time"""
    def hatBaseballCap(self):
        self.toonMaker.hatBaseballCap()

    def hatSafari(self):
        self.toonMaker.hatSafari()

    def hatRibbon(self):
        self.toonMaker.hatRibbon()

    def hatHeart(self):
        self.toonMaker.hatHeart()

    def hatTophat(self):
        self.toonMaker.hatTophat()

    def hatAnvil(self):
        self.toonMaker.hatAnvil()

    def hatFlowerpot(self):
        self.toonMaker.hatFlowerpot()

    def hatSandbag(self):
        self.toonMaker.hatSandbag()

    def hatWeight(self):
        self.toonMaker.hatWeight()

    def hatFez(self):
        self.toonMaker.hatFez()

    def hatGolf(self):
        self.toonMaker.hatGolf()

    def hatParty(self):
        self.toonMaker.hatParty()

    def hatPill(self):
        self.toonMaker.hatPill()

    def hatCrown(self):
        self.toonMaker.hatCrown()

    def hatCowboy(self):
        self.toonMaker.hatCowboy()

    def hatPirate(self):
        self.toonMaker.hatPirate()

    def hatPropeller(self):
        self.toonMaker.hatPropeller()

    def hatFishing(self):
        self.toonMaker.hatFishing()

    def hatSombreor(self):
        self.toonMaker.hatSombreor()

    def hatStraw(self):
        self.toonMaker.hatStraw()

    def hatSun(self):
        self.toonMaker.hatSun()

    def hatAntenna(self):
        self.toonMaker.hatAntenna()

    def hatBeehive(self):
        self.toonMaker.hatBeehive()

    def hatBowler(self):
        self.toonMaker.hatBowler()

    def hatChef(self):
        self.toonMaker.hatChef()

    def hatDetective(self):
        self.toonMaker.hatDetective()

    def hatFeather(self):
        self.toonMaker.hatFeather()

    def hatFedora(self):
        self.toonMaker.hatFedora()

    def hatBand(self):
        self.toonMaker.hatBand()

    def hatNative(self):
        self.toonMaker.hatNative()

    def hatHairdo(self):
        self.toonMaker.hatHairdo()

    def hatPrincess(self):
        self.toonMaker.hatPrincess()

    def hatRobin(self):
        self.toonMaker.hatRobin()

    def hatRoman(self):
        self.toonMaker.hatRoman()

    def hatSpider(self):
        self.toonMaker.hatSpider()

    def hatTiara(self):
        self.toonMaker.hatTiara()

    def hatViking(self):
        self.toonMaker.hatViking()

    def hatWitch(self):
        self.toonMaker.hatWitch()

    def hatWizard(self):
        self.toonMaker.hatWizard()

    def hatConHelmet(self):
        self.toonMaker.hatConHelmet()

    def hatFirefighter(self):
        self.toonMaker.hatFirefighter()

    def hatPyrimad(self):
        self.toonMaker.hatPyrimad()

    def hatMiner(self):
        self.toonMaker.hatMiner()

    def hatNapoleon(self):
        self.toonMaker.hatNapoleon()

    def hatPilot(self):
        self.toonMaker.hatPilot()

    def hatPolice(self):
        self.toonMaker.hatPolice()

    def hatAfro(self):
        self.toonMaker.hatAfro()

    def hatSailor(self):
        self.toonMaker.hatSailor()

    def hatFruit(self):
        self.toonMaker.hatFruit()

    def hatBobby(self):
        self.toonMaker.hatBobby()

    def hatJughead(self):
        self.toonMaker.hatJughead()

    def hatWinter(self):
        self.toonMaker.hatWinter()

    def hatBandana(self):
        self.toonMaker.hatBandana()

    def hatDinosaur(self):
        self.toonMaker.hatDinosaur()

    def hatBand(self):
        self.toonMaker.hatBand()

    def hatBird(self):
        self.toonMaker.hatBird()


    """Glasses Time"""
    def glassesRound(self):
        self.toonMaker.glassesRound()

    def glassesMiniblinds(self):
        self.toonMaker.glassesMiniblinds()

    def glassesNarrow(self):
        self.toonMaker.glassesNarrow()

    def glassesStar(self):
        self.toonMaker.glassesStar()

    def glasses3D(self):
        self.toonMaker.glasses3D()

    def glassesAviator(self):
        self.toonMaker.glassesAviator()

    def glassesCat(self):
        self.toonMaker.glassesCat()

    def glassesDork(self):
        self.toonMaker.glassesDork()

    def glassesJackie(self):
        self.toonMaker.glassesJackie()

    def glassesScuba(self):
        self.toonMaker.glassesScuba()

    def glassesGoggles(self):
        self.toonMaker.glassesGoggles()

    """Backpack Time"""
    def backpackJetpack(self):
        self.toonMaker.backpackJetpack()

    """Shoe Time"""

    def shoeBlank(self):
        self.toonMaker.shoeBlank()

    """Time for animations for toons"""

    def animationThrow(self):
        self.toonMaker.animationThrow()

    def animationWalk(self):
        self.toonMaker.animationWalk()

    def animationRun(self):
        self.toonMaker.animationRun()

    def animationTeleport(self):
        self.toonMaker.animationTeleport()

    def animationBook(self):
        self.toonMaker.animationBook()

    def animationJump(self):
        self.toonMaker.animationJump()

    def animationRunningJump(self):
        self.toonMaker.animationRunningJump()

    def animationJumpSquat(self):
        self.toonMaker.animationJumpSquat()

    def animationPushButton(self):
        self.toonMaker.animationPushButton()

    def animationBored(self):
        self.toonMaker.animationBored()

    def animationWave(self):
        self.toonMaker.animationWave()

    def animationShrug(self):
        self.toonMaker.animationShrug()

    def animationAngry(self):
        self.toonMaker.animationAngry()

    def animationSwim(self):
        self.toonMaker.animationSwim()

    def animationBow(self):
        self.toonMaker.animationBow()

    def wipeScene(self):
        self.cogMaker.hideCogs()
        self.toonMaker.killToons()

    def makeCogsChat(self):
        self.cogMaker.chatTestCogs()

    """Cheesy Effects Time :D"""

    def effectSmall(self):
        self.toonMaker.effectSmall()

    def hidecogButtons(self):
        self.RandomCog.hide()
        self.CloseMenu.hide()
        self.Hollywood.hide()
        self.Mingler.hide()
        self.TwoFace.hide()
        self.MoverShaker.hide()
        self.GladHander.hide()
        self.NameDropper.hide()
        self.Telemarketer.hide()
        self.ColdCaller.hide()
        self.RobberBaron.hide()
        self.LoanShark.hide()
        self.Moneybags.hide()
        self.NumberCruncher.hide()
        self.BeanCounter.hide()
        self.Tightwad.hide()
        self.PennyPincher.hide()
        self.ShortChange.hide()
        self.BigWig.hide()
        self.LegalEagle.hide()
        self.SpinDoctor.hide()
        self.Backstabber.hide()
        self.AmbulanceChaser.hide()
        self.DoubleTalker.hide()
        self.Bloodsucker.hide()
        self.BottomFeeder.hide()
        self.BigCheese.hide()
        self.CorporateRaider.hide()
        self.HeadHunter.hide()
        self.Downsizer.hide()
        self.Micromanager.hide()
        self.Yesman.hide()
        self.PencilPusher.hide()
        self.Flunky.hide()

    def hideplaygroundButtons(self):
        self.ClosePlaygroundButtons.hide()
        self.TTC.hide()
        self.DD.hide()
        self.DG.hide()
        self.MM.hide()
        self.BR.hide()
        self.DDL.hide()
        self.SBHQ.hide()
        self.CBHQ.hide()
        self.LWHQ.hide()
        self.BBHQ.hide()
        self.SBHQFAC.hide()

    def hidetoonButtons(self):
        self.CloseToonButtons.hide()
        self.RandomToon.hide()
        self.Flippy.hide()
        self.Slappy.hide()
        self.Alec.hide()
        self.Prepostera.hide()
        self.Surlee.hide()
        self.Dimm.hide()
        self.Daffy.hide()
        self.Chuckle.hide()
        self.Clara.hide()
        self.Penny.hide()
        self.Will.hide()
        self.Oldman.hide()

    def hideAnimationButtons(self):
        self.Throw.hide()
        self.Walk.hide()
        self.Run.hide()
        self.Teleport.hide()
        self.Book.hide()
        self.Jump.hide()
        self.JumpSquat.hide()
        self.PushButton.hide()
        self.Bored.hide()
        self.Wave.hide()
        self.Shrug.hide()
        self.Angry.hide()
        self.Swim.hide()
        self.Bow.hide()
        self.hideAnimationButtons.hide()

    def hideEventButtons(self):
        self.ttrElectionButton.hide()
        self.ttrToonfestButton.hide()
        self.ttiScienceFairButton.hide()
        self.closeButtons.hide()

    def hideAccessoriesButtons(self):
        self.hatsButton.hide()
        self.glassesButton.hide()
        self.backpacksButton.hide()
        self.shoesButton.hide()
        self.buttonsClose.hide()

    '''def toggleButtons(self):
        self.ImgBtn1.hide()
        self.ImgBtn2.hide()
        self.ImgBtn3.hide()
        self.ImgBtn4.hide()
        self.ImgBtn5.hide()
        self.ImgBtn6.hide()
        self.ImgBtn7.hide()
        self.ImgBtn8.hide()'''

    def cogButtons(self):
        """Extra Buttons"""
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.CloseMenu = DirectButton(frameSize=None, text='Close Menu', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.hidecogButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,-.41), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.RandomCog = DirectButton(frameSize=None, text='Random Cog', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.randomCog, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,-.41), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        """Time For Sellbots"""

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Hollywood = DirectButton(frameSize=None, text='Mr.Hollywood', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogHollywood, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Mingler = DirectButton(frameSize=None, text='Mingler', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogMingler, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.TwoFace = DirectButton(frameSize=None, text='Two Face', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogFace, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.MoverShaker = DirectButton(frameSize=None, text='Mover & Shaker', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogShaker, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.GladHander = DirectButton(frameSize=None, text='Glad Hander', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogGlad, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.NameDropper = DirectButton(frameSize=None, text='Name Dropper', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogDropper, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Telemarketer = DirectButton(frameSize=None, text='Telemarketer', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogTelemarketer, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ColdCaller = DirectButton(frameSize=None, text='Cold Caller', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogCold, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.32), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        """Time For Cashbots"""

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ShortChange = DirectButton(frameSize=None, text='Short Change', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogShort, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,-.32), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.PennyPincher = DirectButton(frameSize=None, text='Penny Pincher', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogPenny, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,-.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Tightwad = DirectButton(frameSize=None, text='Tightwad', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogTight, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.BeanCounter = DirectButton(frameSize=None, text='Bean Counter', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogBean, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.NumberCruncher = DirectButton(frameSize=None, text='Number Cruncher', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogNumber, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Moneybags = DirectButton(frameSize=None, text='Moneybags', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogMoney, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.LoanShark = DirectButton(frameSize=None, text='Loan Shark', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogShark, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.RobberBaron = DirectButton(frameSize=None, text='Robber Baron', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogRobber, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        """Time For Lawbots"""

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.BottomFeeder = DirectButton(frameSize=None, text='Bottom Feeder', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogFeeder, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,-.32), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Bloodsucker = DirectButton(frameSize=None, text='Bloodsucker', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogBlood, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,-.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.DoubleTalker = DirectButton(frameSize=None, text='Double Talker', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogTalker, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Backstabber = DirectButton(frameSize=None, text='Backstabber', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogStabber, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.AmbulanceChaser = DirectButton(frameSize=None, text='Chaser', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogChaser, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.SpinDoctor = DirectButton(frameSize=None, text='Spin Doctor', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogDoctor, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.LegalEagle = DirectButton(frameSize=None, text='Legal Eagle', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogEagle, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.BigWig = DirectButton(frameSize=None, text='Big Wig', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogWig, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        """Time for Bossbots"""

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Flunky = DirectButton(frameSize=None, text='Flunky', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogFlunky, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.4,-0,-.32), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.PencilPusher = DirectButton(frameSize=None, text='Pencil Pusher', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogPencil, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.4,-0,-.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Yesman = DirectButton(frameSize=None, text='Yesman', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogYesman, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.4,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Micromanager = DirectButton(frameSize=None, text='Micromanager', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogMicro, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.4,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Downsizer = DirectButton(frameSize=None, text='Downsizer', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogDownsizer, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.4,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.HeadHunter = DirectButton(frameSize=None, text='Head Hunter', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogHunter, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.4,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.CorporateRaider = DirectButton(frameSize=None, text='Corporate Raider', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogRaider, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.4,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.BigCheese = DirectButton(frameSize=None, text='Big Cheese', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogCheese, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.4,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
    
    def toonButtons(self):
        #Extra Buttons
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.CloseToonButtons = DirectButton(frameSize=None, text='Close Menu', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.hidetoonButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Random Toon
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.RandomToon = DirectButton(frameSize=None, text='Random Toon', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.randomToon, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,-.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Flippy
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Flippy = DirectButton(frameSize=None, text='Flippy', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonFlippy, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Slappy
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Slappy = DirectButton(frameSize=None, text='Slappy', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonSlappy, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Alec Tinn
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Alec = DirectButton(frameSize=None, text='Alec Tinn', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonAlec, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Prep
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Prepostera = DirectButton(frameSize=None, text='Prepostera', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonPrep, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Surlee
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Surlee = DirectButton(frameSize=None, text='Surlee', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonSurlee, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Dimm
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Dimm = DirectButton(frameSize=None, text='Dimm', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonDim, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Daffy
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Daffy = DirectButton(frameSize=None, text='Daffy Don', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonDaffy, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Chuckle
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Chuckle = DirectButton(frameSize=None, text='Madam Chuckle', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonChuckle, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Clara
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Clara = DirectButton(frameSize=None, text='Clerk Clara', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonClara, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Penny
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Penny = DirectButton(frameSize=None, text='Clerk Penny', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonPenny, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Will
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Will = DirectButton(frameSize=None, text='Clerk Will', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonWill, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Oldman
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Oldman = DirectButton(frameSize=None, text='Lil Oldman', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonOldman, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

    def playgroundButtons(self):
        #Toontown Central
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.TTC = DirectButton(frameSize=None, text='TTC', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ttcPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Donalds Dock
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.DD = DirectButton(frameSize=None, text='DD', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ddPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Daisys Garden
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.DG = DirectButton(frameSize=None, text='DG', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.dgPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Minnies Melodyland
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.MM = DirectButton(frameSize=None, text='MM', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.mmPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #The Brrrgh
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.BR = DirectButton(frameSize=None, text='BR', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.brPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Donalds Dreamland
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.DDL = DirectButton(frameSize=None, text='DDL', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ddlPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Sellbot HQ
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.SBHQ = DirectButton(frameSize=None, text='SBHQ', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.sbPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0, .31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Cashbot HQ
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.CBHQ = DirectButton(frameSize=None, text='CBHQ', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cbPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #LBHQ
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.LWHQ = DirectButton(frameSize=None, text='LWHQ', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.lbPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #BBHQ
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.BBHQ = DirectButton(frameSize=None, text='BBHQ', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.bbPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Sellbot Factory
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.SBHQFAC = DirectButton(frameSize=None, text='SBHQ Factory', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.sbfacPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Close Menu
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ClosePlaygroundButtons = DirectButton(frameSize=None, text='Close Menu', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.hideplaygroundButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

    def animationButtons(self):
        #Throw
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Throw = DirectButton(frameSize=None, text='Throw', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationThrow, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Walk
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Walk = DirectButton(frameSize=None, text='Walk', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationWalk, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Run
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Run = DirectButton(frameSize=None, text='Run', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationRun, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Teleport
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Teleport = DirectButton(frameSize=None, text='Teleport', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationTeleport, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Book
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Book = DirectButton(frameSize=None, text='Book', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationBook, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Jump
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Jump = DirectButton(frameSize=None, text='Jump', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationJump, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #JumpSquat
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.JumpSquat = DirectButton(frameSize=None, text='Jump Squat', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationJumpSquat, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #PushButton
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.PushButton = DirectButton(frameSize=None, text='Push Button', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationPushButton, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Bored
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Bored = DirectButton(frameSize=None, text='Bored', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationBored, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Wave
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Wave = DirectButton(frameSize=None, text='Wave', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationWave, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Shrug
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Shrug = DirectButton(frameSize=None, text='Shrug', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationShrug, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Angry
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Angry = DirectButton(frameSize=None, text='Angry', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationAngry, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Swim
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Swim = DirectButton(frameSize=None, text='Swim', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationSwim, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Bow
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.Bow = DirectButton(frameSize=None, text='Bow', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationBow, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #HideAnimationButtons
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.hideAnimationButtons = DirectButton(frameSize=None, text='Hide Animations', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.hideAnimationButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-.7,-0,-.41), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

    def accessoriesButtons(self):
        #Hats
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.hatsButton = DirectButton(frameSize=None, text='Hats', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ttrElections, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Glasses
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.glassesButton = DirectButton(frameSize=None, text='Glasses', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ttrToonfest, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Backpack
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.backpacksButton = DirectButton(frameSize=None, text='Backpacks', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ttiScienceFair, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Shoes
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.shoesButton = DirectButton(frameSize=None, text='Shoes', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.hideEventButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Close Menu
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.buttonsClose = DirectButton(frameSize=None, text='Close Menu', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.hideAccessoriesButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

    def eventButtons(self):
        #Elections
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ttrElectionButton = DirectButton(frameSize=None, text='Elections', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ttrElections, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Toonfest
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ttrToonfestButton = DirectButton(frameSize=None, text='Toonfest', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ttrToonfest, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Science Fair
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ttiScienceFairButton = DirectButton(frameSize=None, text='Science Fair', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.ttiScienceFair, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Close Menu
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.closeButtons = DirectButton(frameSize=None, text='Close Menu', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.hideEventButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.30,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)


    def movieButtons(self):
        #Cogs
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn1 = DirectButton(frameSize=None, text='Cogs', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.cogButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,.31), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Toons
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn2 = DirectButton(frameSize=None, text='Toons', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.toonButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,.22), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Playgrounds
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn3 = DirectButton(frameSize=None, text='Playgrounds', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.playgroundButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,.13), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Events
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn8 = DirectButton(frameSize=None, text='Events', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.eventButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Animations
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn4 = DirectButton(frameSize=None, text='Animations', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.animationButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Accessories
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn5 = DirectButton(frameSize=None, text='Accessories', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.accessoriesButtons, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Effects
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn6 = DirectButton(frameSize=None, text='Effects', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.makeCogsChat, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0, -.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Wipe Scene
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn7 = DirectButton(frameSize=None, text='Wipe Scene', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.wipeScene, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0, -.32), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        
moviemaker = MovieMaker()            
