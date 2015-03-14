from pandac.PandaModules import *
import __builtin__

if __debug__:
	loadPrcFile('config/config_dev.prc')

from direct.directbase import DirectStart
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from funnyfarm.toonbase import FunnyFarmGlobals

FunnyFarmGlobals.setNametagGlobals()
FunnyFarmGlobals.setParticleManagers()

class game:
	name = 'toontown'
	process = 'client'

base.game = game()
__builtin__.game = base.game

from funnyfarm.events.EventBase import EventBase
from funnyfarm.toon.CustomToons import Bear, Chuckie, Kingleroy
from funnyfarm.toonbase import Injector
from toontown.election.DistributedInvasionSuit import DistributedInvasionSuit
from toontown.suit import DistributedSuitBase, SuitDNA, BossCog
from funnyfarm.events.SafezoneInvasionGlobals import *
from funnyfarm.events.ToonFest import ToonFest
from funnyfarm.dna import DNAParser
from funnyfarm.hood.TTHood import TTHood
base.localAvatar = Kingleroy()
base.localAvatar.reparentTo(render)

tf = EventBase()
tf.loadEvent()
#tf.loadSfx()

def spawnCogs():
	suit = DistributedInvasionSuit(None)
	suitDNA = SuitDNA.SuitDNA()
	suitDNA.newSuitRandom()
	suit.setDNA(suitDNA)
	suit.reparentTo(render)
	mtrack = suit.beginSupaFlyMove(Point3(0,0,0), 1, 'fromSky', walkAfterLanding=False).start()
	suit.loop('neutral')
base.accept('2',spawnCogs)
try:
	run()
except:
	base.notify.setInfo(True)
	base.notify.info('User closed main window.')
	base.notify.info('Exiting ShowBase.')
