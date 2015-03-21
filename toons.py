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
from direct.directbase import DirectStart
from direct.directbase import DirectStart
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from funnyfarm.toonbase import FunnyFarmGlobals
from toontown.toon import NPCToons
from toontown.toon import Toon
from toontown.toon import ToonDNA
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from otp.margins.WhisperPopup import *
from direct.fsm import ClassicFSM, State

class Toons():

    def __init__(self):
        self.toons = []

    def randomToon(self):
        toon = NPCToons.createRandomToon()
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonFlippy(self):
        toon = NPCToons.createLocalNPC(20001)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonDim(self):
        toon = NPCToons.createLocalNPC(2018)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonSurlee(self):
        toon = NPCToons.createLocalNPC(2019)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonSlappy(self):
        toon = NPCToons.createLocalNPC(2021)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonAlec(self):
        toon = NPCToons.createLocalNPC(2022)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonPrep(self):
        toon = NPCToons.createLocalNPC(2020)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonDaffy(self):
        toon = NPCToons.createLocalNPC(2132)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonChuckle(self):
        toon = NPCToons.createLocalNPC(2121)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonClara(self):
        toon = NPCToons.createLocalNPC(2011)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonPenny(self):
        toon = NPCToons.createLocalNPC(3007)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonWill(self):
        toon = NPCToons.createLocalNPC(1001)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)

    def toonOldman(self):
        toon = NPCToons.createLocalNPC(3112)
        toon.useLOD(1000)
        toon.find('**/250').removeNode()
        toon.find('**/500').removeNode()
        toon.setPos(base.localAvatar.getPos())
        toon.setHpr(base.localAvatar.getHpr())
        toon.initializeBodyCollisions('toon')
        toon.addActive()
        toon.startBlink()
        toon.loop('neutral')
        toon.reparentTo(render)
        self.toons.append(toon)
        """End off at oldman"""

    def hatBaseballCap(self):
        for toon in self.toons:
            toon.setHat(1, 0, 0)

    def hatSafari(self):
        for toon in self.toons:
            toon.setHat(2, 0, 0)

    def hatRibbon(self):
        for toon in self.toons:
            toon.setHat(3, 0, 0)

    def hatHeart(self):
        for toon in self.toons:
            toon.setHat(4, 0, 0)

    def hatTophat(self):
        for toon in self.toons:
            toon.setHat(5, 0, 0)

    def hatAnvil(self):
        for toon in self.toons:
            toon.setHat(6, 0, 0)

    def hatFlowerpot(self):
        for toon in self.toons:
            toon.setHat(7, 0, 0)

    def hatSandbag(self):
        for toon in self.toons:
            toon.setHat(8, 0, 0)

    def hatWeight(self):
        for toon in self.toons:
            toon.setHat(9, 0, 0)

    def hatFez(self):
        for toon in self.toons:
            toon.setHat(10, 0, 0)

    def hatGolf(self):
        for toon in self.toons:
            toon.setHat(11, 0, 0)

    def hatParty(self):
        for toon in self.toons:
            toon.setHat(12, 0, 0)

    def hatPill(self):
        for toon in self.toons:
            toon.setHat(13, 0, 0)

    def hatCrown(self):
        for toon in self.toons:
            toon.setHat(14, 0, 0)

    def hatCowboy(self):
        for toon in self.toons:
            toon.setHat(15, 0, 0)

    def hatPirate(self):
        for toon in self.toons:
            toon.setHat(16, 0, 0)

    def hatPropeller(self):
        for toon in self.toons:
            toon.setHat(17, 0, 0)

    def hatFishing(self):
        for toon in self.toons:
            toon.setHat(18, 0, 0)

    def hatSombreor(self):
        for toon in self.toons:
            toon.setHat(19, 0, 0)

    def hatStraw(self):
        for toon in self.toons:
            toon.setHat(20, 0, 0)

    def hatSun(self):
        for toon in self.toons:
            toon.setHat(21, 0, 0)

    def hatAntenna(self):
        for toon in self.toons:
            toon.setHat(22, 0, 0)

    def hatBeehive(self):
        for toon in self.toons:
            toon.setHat(23, 0, 0)

    def hatBowler(self):
        for toon in self.toons:
            toon.setHat(24, 0, 0)

    def hatChef(self):
        for toon in self.toons:
            toon.setHat(25, 0, 0)

    def hatDetective(self):
        for toon in self.toons:
            toon.setHat(26, 0, 0)

    def hatFeather(self):
        for toon in self.toons:
            toon.setHat(27, 0, 0)

    def hatFedora(self):
        for toon in self.toons:
            toon.setHat(28, 0, 0)

    def hatBand(self):
        for toon in self.toons:
            toon.setHat(29, 0, 0)

    def hatNative(self):
        for toon in self.toons:
            toon.setHat(30, 0, 0)

    def hatHairdo(self):
        for toon in self.toons:
            toon.setHat(31, 0, 0)

    def hatPrincess(self):
        for toon in self.toons:
            toon.setHat(32, 0, 0)

    def hatRobin(self):
        for toon in self.toons:
            toon.setHat(33, 0, 0)

    def hatRoman(self):
        for toon in self.toons:
            toon.setHat(34, 0, 0)

    def hatSpider(self):
        for toon in self.toons:
            toon.setHat(35, 0, 0)

    def hatTiara(self):
        for toon in self.toons:
            toon.setHat(36, 0, 0)

    def hatViking(self):
        for toon in self.toons:
            toon.setHat(37, 0, 0)

    def hatWitch(self):
        for toon in self.toons:
            toon.setHat(38, 0, 0)

    def hatWizard(self):
        for toon in self.toons:
            toon.setHat(39, 0, 0)

    def hatConHelmet(self):
        for toon in self.toons:
            toon.setHat(40, 0, 0)

    def hatFirefighter(self):
        for toon in self.toons:
            toon.setHat(41, 0, 0)

    def hatPyrimad(self):
        for toon in self.toons:
            toon.setHat(42, 0, 0)

    def hatMiner(self):
        for toon in self.toons:
            toon.setHat(43, 0, 0)

    def hatNapoleon(self):
        for toon in self.toons:
            toon.setHat(44, 0, 0)

    def hatPilot(self):
        for toon in self.toons:
            toon.setHat(45, 0, 0)

    def hatPolice(self):
        for toon in self.toons:
            toon.setHat(46, 0, 0)

    def hatAfro(self):
        for toon in self.toons:
            toon.setHat(47, 0, 0)

    def hatSailor(self):
        for toon in self.toons:
            toon.setHat(48, 0, 0)

    def hatFruit(self):
        for toon in self.toons:
            toon.setHat(49, 0, 0)

    def hatBobby(self):
        for toon in self.toons:
            toon.setHat(50, 0, 0)

    def hatJughead(self):
        for toon in self.toons:
            toon.setHat(51, 0, 0)

    def hatWinter(self):
        for toon in self.toons:
            toon.setHat(52, 0, 0)

    def hatBandana(self):
        for toon in self.toons:
            toon.setHat(53, 0, 0)

    def hatDinosaur(self):
        for toon in self.toons:
            toon.setHat(54, 0, 0)

    def hatBand(self):
        for toon in self.toons:
            toon.setHat(55, 0, 0)

    def hatBird(self):
        for toon in self.toons:
            toon.setHat(56, 0, 0)


    """Glasses Time"""
    def glassesRound(self):
        for toon in self.toons:
            toon.setGlasses(1, 0, 0)

    def glassesMiniblinds(self):
        for toon in self.toons:
            toon.setGlasses(2, 0, 0)

    def glassesNarrow(self):
        for toon in self.toons:
            toon.setGlasses(3, 0, 0)

    def glassesStar(self):
        for toon in self.toons:
            toon.setGlasses(4, 0, 0)

    def glasses3D(self):
        for toon in self.toons:
            toon.setGlasses(5, 0, 0)

    def glassesAviator(self):
        for toon in self.toons:
            toon.setGlasses(6, 0, 0)

    def glassesCat(self):
        for toon in self.toons:
            toon.setGlasses(7, 0, 0)

    def glassesDork(self):
        for toon in self.toons:
            toon.setGlasses(8, 0, 0)

    def glassesJackie(self):
        for toon in self.toons:
            toon.setGlasses(9, 0, 0)

    def glassesScuba(self):
        for toon in self.toons:
            toon.setGlasses(10, 0, 0)

    def glassesGoggles(self):
        for toon in self.toons:
            toon.setGlasses(11, 0, 0)

    """Backpack Time"""
    def backpackJetpack(self):
        for toon in self.toons:
            toon.setBackpack(11, 0 , 0)

    """Shoe Time"""

    """Time for animations for toons"""

    def animationThrow(self):
        for toon in self.toons:
            toon.loop('throw')

    def animationWalk(self):
        for toon in self.toons:
            toon.loop('walk')

    def animationRun(self):
        for toon in self.toons:
            toon.loop('run')

    def animationTeleport(self):
        for toon in self.toons:
            toon.loop('teleport')

    def animationBook(self):
        for toon in self.toons:
            toon.loop('book')

    def animationJump(self):
        for toon in self.toons:
            toon.loop('jump')

    def animationRunningJump(self):
        for toon in self.toons:
            toon.loop('running-jump')

    def animationJumpSquat(self):
        for toon in self.toons:
            toon.loop('jump-squat')

    def animationPushButton(self):
        for toon in self.toons:
            toon.loop('pushbutton')

    def animationBored(self):
        for toon in self.toons:
            toon.loop('victory')

    def killToons(self):
        for toon in self.toons:
            toon.delete()
        self.toons = []


    def chatTest(self):
        for toon in self.toons:
            toon.setChatAbsolute('', CFSpeech)
            toon.setChatAbsolute(TTLocalizer.NPCChatTest, CFSpeech|CFTimeout)
