from pandac.PandaModules import *
from direct.directbase import DirectStart
from ElectionEvent import ElectionEvent
from ScienceFairEvent import ScienceFairEvent
from ElectionBalloon import ElectionBalloon
from SafezoneInvasion import SafezoneInvasion
from toontown.toonbase import ToontownGlobals
from funnyfarm.dna import DNAParser
from funnyfarm.hood.TTHood import TTHood
from funnyfarm.hood.DDHood import DDHood
from funnyfarm.hood.DGHood import DGHood
from funnyfarm.hood.MMHood import MMHood
from funnyfarm.hood.BRHood import BRHood
from funnyfarm.hood.DDLHood import DDLHood
from funnyfarm.hood.SBHQHood import SBHQHood
from funnyfarm.events.ToonFest import ToonFest
from funnyfarm.hood.TTHoodWinter import TTHoodWinter
from funnyfarm.hood.TTHoodSpooky import TTHoodSpooky
from funnyfarm.hood.DDHoodWinter import DDHoodWinter
from funnyfarm.hood.DDHoodSpooky import DDHoodSpooky
from funnyfarm.hood.MMHoodWinter import MMHoodWinter
from funnyfarm.hood.MMHoodSpooky import MMHoodSpooky
from funnyfarm.hood.TTHoodStrt import TTHoodStrt

class EventBaseToonfest(ToonFest):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		ToonFest.__init__(self)

	def loadEvent(self):
		ToonFest.load(self)

class EventBaseElections(TTHood, ElectionBalloon, ElectionEvent):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		TTHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		TTHood.load(self)
		#self.geom.find('**/prop_mickey_on_horse_DNARoot').removeNode()
		ElectionBalloon.__init__(self)
		ElectionEvent.__init__(self)
		#SafezoneInvasion.__init__(self)
		self.loadSfx()

class EventBaseScienceFair(TTHood, ScienceFairEvent):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		TTHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		TTHood.load(self)
		#self.geom.find('**/prop_mickey_on_horse_DNARoot').removeNode()
		#ElectionBalloon.__init__(self)
		#ElectionEvent.__init__(self)
		ScienceFairEvent.__init__(self)
		#SafezoneInvasion.__init__(self)
		self.loadSfx()

"""Time For Winters Of Each Playground"""

class EventBaseTTWinter(TTHoodWinter):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		TTHoodWinter.__init__(self, self.dnaStore)

	def loadEvent(self):
		TTHoodWinter.load(self)
		self.loadSfx()

class EventBaseDDWinter(DDHoodWinter):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		DDHoodWinter.__init__(self, self.dnaStore)

	def loadEvent(self):
		DDHoodWinter.load(self)
		self.loadSfx()

class EventBaseMMWinter(MMHoodWinter):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		MMHoodWinter.__init__(self, self.dnaStore)

	def loadEvent(self):
		MMHoodWinter.load(self)

"""Time for Spooky's Of Each Playground"""

class EventBaseTTSpooky(TTHoodSpooky):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		TTHoodSpooky.__init__(self, self.dnaStore)

	def loadEvent(self):
		TTHoodSpooky.load(self)
		self.loadSfx()

class EventBaseDDSpooky(DDHoodSpooky):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		DDHoodSpooky.__init__(self, self.dnaStore)

	def loadEvent(self):
		DDHoodSpooky.load(self)
		self.loadSfx()

class EventBaseMMSpooky(MMHoodSpooky):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		MMHoodSpooky.__init__(self, self.dnaStore)

	def loadEvent(self):
		MMHoodSpooky.load(self)

"""Time for regular Playgrounds"""

class EventBaseTT(TTHood):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		TTHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		TTHood.load(self)
		self.loadSfx()

class EventBaseDD(DDHood):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		DDHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		DDHood.load(self)
		self.loadSfx()

class EventBaseDG(DGHood):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		DGHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		DGHood.load(self)

class EventBaseMM(MMHood):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		MMHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		MMHood.load(self)

class EventBaseBR(BRHood):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		BRHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		BRHood.load(self)

class EventBaseDDL(DDLHood):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		DDLHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		DDLHood.load(self)

class EventBaseTTStrt(TTHoodStrt):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		TTHoodStrt.__init__(self, self.dnaStore)

	def loadEvent(self):
		TTHoodStrt.load(self)
		self.loadSfx()

'''class EventBaseUnload(MMHood):

	def loadEvent(self):
		MMHood.unload(self)'''

'''Cog HQ's'''
class EventBaseSBHQ(SBHQHood):
	def __init__(self):
		self.dnaStore = DNAParser.DNAStorage()
		self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
		self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
		self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
		DNAParser.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
		DNAParser.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
		SBHQHood.__init__(self, self.dnaStore)

	def loadEvent(self):
		SBHQHood.load(self)