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
        self.cogs = []
        self.playgrounds = []
        self.toons = []
        
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
        self.playgrounds.append(tf)

    def ddPlayground(self):
        tf = EventBaseDD()
        tf.loadEvent()

    def dgPlayground(self):
        tf = EventBaseDG()
        tf.loadEvent()

    def mmPlayground(self):
        tf = EventBaseMM()
        tf.loadEvent()
        self.playgrounds.append(tf)

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

    """Sellbots"""
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

    def killCogs(self):
        for cog in self.cogs:
            cog.hide()
        self.cogs = []

    """Time for Cog Animations"""

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

    def killToons(self):
        for toon in self.toons:
            toon.delete()
        self.toons = []

    """Time for accessories"""
    """Hat Time"""
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

    """Glasses Time"""
    def glassesRound(self):
        for toon in self.toons:
            toon.setGlasses(1, 0, 0)

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

    def wipeScene(self):
        for toon in self.toons:
            toon.delete()
        self.toons = []

        for cog in self.cogs:
            cog.hide()
        self.cogs = []

        '''for tf in self.playgrounds:
            tf = EventBaseUnload(MMHood)
            tf.loadEvent()
        self.playgrounds = []'''

    """Cheesy Effects Time :D"""

    def effectSmall(self):
        for toon in self.toons:
            toon.applyCheesyEffect(6)

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

        """Sellbot Buttons"""

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
        #Buildings
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn8 = DirectButton(frameSize=None, text='Buildings', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.brPlayground, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,.04), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Animations
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn4 = DirectButton(frameSize=None, text='Animations', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.effectSmall, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,-.05), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Accessories
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn5 = DirectButton(frameSize=None, text='Accessories', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.hatPrincess, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0,-.14), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Effects
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn6 = DirectButton(frameSize=None, text='Effects', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.greenScreen, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0, -.23), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)
        #Wipe Scene
        ButtonImage = loader.loadModel("phase_3/models/gui/quit_button.bam")
        self.ImgBtn7 = DirectButton(frameSize=None, text='Wipe Scene', image=(ButtonImage.find('**/QuitBtn_UP'), \
        ButtonImage.find('**/QuitBtn_DN'), ButtonImage.find('**/QuitBtn_RLVR')), relief=None, command=self.wipeScene, text_pos=(0, -0.015), \
        geom=None, pad=(0.01, 0.01), suppressKeys=0, pos = (-1.70,-0, -.32), text_scale=0.059, borderWidth=(0.015, 0.01), scale=.7)

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