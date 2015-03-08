from pandac.PandaModules import *
from direct.directbase import DirectStart
from ElectionEvent import ElectionEvent
from ScienceFairEvent import ScienceFairEvent
from ElectionBalloon import ElectionBalloon
from SafezoneInvasion import SafezoneInvasion
from toontown.toonbase import ToontownGlobals
from funnyfarm.dna import DNAParser
from funnyfarm.hood.TTHood import TTHood

class EventBase(TTHood, ElectionBalloon, ScienceFairEvent, ElectionEvent, SafezoneInvasion):
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
		self.geom.find('**/prop_mickey_on_horse_DNARoot').removeNode()
		ElectionBalloon.__init__(self)
		ElectionEvent.__init__(self)
		ScienceFairEvent.__init__(self)
		SafezoneInvasion.__init__(self)
		self.loadSfx()
