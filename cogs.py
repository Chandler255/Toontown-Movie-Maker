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

    def hideCogs(self):
        for cog in self.cogs:
            cog.hide()
        self.cogs = []

