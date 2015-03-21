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
from funnyfarm.toonbase import FunnyFarmGlobals
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from otp.margins.WhisperPopup import *
from direct.fsm import ClassicFSM, State

class Cogs():

    def __init__(self):
        self.cogs = []

    def randomCog(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuitRandom()
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        self.cogs.append(suit)

    def cogHollywood(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('mh')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Mr. Hollywood\nSellbot')
        self.cogs.append(suit)

    def cogMingler(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('m')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Mingler\nSellbot')
        self.cogs.append(suit)

    def cogFace(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('tf')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Two Face\nSellbot')
        self.cogs.append(suit)

    def cogShaker(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('ms')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Mover & Shaker\nSellbot')
        self.cogs.append(suit)

    def cogGlad(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('gh')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Glad Hander\nSellbot')
        self.cogs.append(suit)

    def cogDropper(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('nd')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Name Dropper\nSellbot')
        self.cogs.append(suit)

    def cogTelemarketer(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('tm')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Telemarketer\nSellbot')
        self.cogs.append(suit)

    def cogCold(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('cc')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Cold Caller\nSellbot')
        self.cogs.append(suit)

    """Time For Cashbots"""

    def cogRobber(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('rb')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Robber Baron\nCashbot')
        self.cogs.append(suit)

    def cogShark(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('ls')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Loan Shark\nCashbot')
        self.cogs.append(suit)

    def cogMoney(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('mb')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Moneybags\nCashbot')
        self.cogs.append(suit)

    def cogNumber(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('nc')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Number Cruncher\nCashbot')
        self.cogs.append(suit)

    def cogBean(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('bc')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Bean Counter\nCashbot')
        self.cogs.append(suit)

    def cogTight(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('tw')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Tightwad\nCashbot')
        self.cogs.append(suit)

    def cogPenny(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('pp')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Penny Pincher\nCashbot')
        self.cogs.append(suit)

    def cogShort(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('sc')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Short Change\nCashbot')
        self.cogs.append(suit)

    """Time for Lawbots"""

    def cogWig(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('bw')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Big Wig\nLawbot')
        self.cogs.append(suit)

    def cogEagle(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('le')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Legal Eagle\nLawbot')
        self.cogs.append(suit)

    def cogDoctor(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('sd')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Spin Doctor\nLawbot')
        self.cogs.append(suit)

    def cogChaser(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('ac')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Ambulance Chaser\nLawbot')
        self.cogs.append(suit)

    def cogStabber(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('bs')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Backstabber\nLawbot')
        self.cogs.append(suit)

    def cogTalker(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('dt')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Double Talker\nLawbot')
        self.cogs.append(suit)

    def cogBlood(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('b')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Bloodsucker\nLawbot')
        self.cogs.append(suit)

    def cogFeeder(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('bf')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Bottom Feeder\nLawbot')
        self.cogs.append(suit)

    def cogCheese(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('tbc')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('The Big Cheese\nBossbot')
        self.cogs.append(suit)

    def cogRaider(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('cr')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Corporate Raider\nBossbot')
        self.cogs.append(suit)

    def cogHunter(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('hh')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Head Hunter\nBossbot')
        self.cogs.append(suit)

    def cogDownsizer(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('ds')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Downsizer\nBossbot')
        self.cogs.append(suit)

    def cogMicro(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('mm')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Micromanager\nBossbot')
        self.cogs.append(suit)

    def cogYesman(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('ym')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Yesman\nBossbot')
        self.cogs.append(suit)

    def cogPencil(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('p')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Pencil Pusher\nBossbot')
        self.cogs.append(suit)

    def cogFlunky(self):
        suit = DistributedInvasionSuit(None)
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit('f')
        suit.setDNA(suitDNA)
        suit.setPos(base.localAvatar.getPos())
        suit.setHpr(base.localAvatar.getHpr())
        suit.loop('neutral')
        suit.reparentTo(render)
        suit.setDisplayName('Flunky\nBossbot')
        self.cogs.append(suit)

    def hideCogs(self):
        for suit in self.cogs:
            suit.hide()
        self.cogs = []

    def chatTestCogs(self):
        for suit in self.cogs:
            suit.setChatAbsolute('', CFSpeech)
            suit.setChatAbsolute('Hello, welcome to death!', CFSpeech|CFTimeout)

