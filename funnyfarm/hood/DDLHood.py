from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from funnyfarm.dna.DNAParser import *
from toontown.toonbase import ToontownGlobals

class DDLHood(DirectObject):

	def __init__(self, dnaStore):
		self.dnaStore = dnaStore
		self.id = ToontownGlobals.DonaldsDreamland
		self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg'
		self.storageFile = 'phase_8/dna/storage_DL.dna'
		self.safeZoneStorageFile = 'phase_8/dna/storage_DL_sz.dna'

		self.holidayStorageDict = {
		 'WINTER_DECORATIONS': ['phase_4/dna/winter_storage_TT.dna', 'phase_4/dna/winter_storage_TT_sz.dna'],
		 'HALLOWEEN_PROPS': ['phase_4/dna/halloween_props_storage_TT.dna', 'phase_4/dna/halloween_props_storage_TT_sz.dna'],
		}

		self.safeZoneFile = 'phase_8/dna/donalds_dreamland_sz.dna'
		self.skyFile = 'phase_8/models/props/DL_sky'
		self.snowySkyFile = 'phase_3.5/models/props/BR_sky'
		self.wantWinter = 0
		self.wantHalloween = 0

	def load(self):
		loadDNAFile(self.dnaStore, self.storageFile)
		loadDNAFile(self.dnaStore, self.safeZoneStorageFile)
		
		if self.wantWinter:
			winterStorage = self.holidayStorageDict['WINTER_DECORATIONS'][0]
			winterSafeZoneStorage = self.holidayStorageDict['WINTER_DECORATIONS'][1]
			loadDNAFile(self.dnaStore, winterStorage)
			loadDNAFile(self.dnaStore, winterSafeZoneStorage)
			self.sky = loader.loadModel(self.snowySkyFile)
		elif self.wantHalloween:
			halloweenStorage = self.holidayStorageDict['HALLOWEEN_PROPS'][0]
			halloweenSafeZoneStorage = self.holidayStorageDict['HALLOWEEN_PROPS'][1]
			loadDNAFile(self.dnaStore, halloweenStorage)
			# We Don't need to load this file because it's the same exact thing as halloween_props_storage_TT.dna
			# loadDNAFile(self.dnaStore, halloweenSafeZoneStorage) 
			self.sky = loader.loadModel(self.snowySkyFile)

		hoodData = loadDNAFile(self.dnaStore, self.safeZoneFile)
		self.geom = NodePath(hoodData)
		self.geom.reparentTo(render)
		self.sky = loader.loadModel(self.skyFile)
		self.sky.reparentTo(render)
		
		self.__fixHood()
		self.loadActors()
		self.startAnimateHood()

	def unload(self):
		self.unloadSfx()
		self.unloadActors()
		self.geom.removeNode()
		del self.geom
		self.sky.removeNode()
		del self.sky

	def loadSfx(self):
		self.sfx = base.loadSfx(self.musicFile)
		self.sfx.setLoop(True)
		self.sfx.setVolume(0.5)
		self.sfx.play()

	def unloadSfx(self):
		self.sfx.stop()
		self.sfx = None

	def __fixHood(self):
		self.gagShop = self.geom.find('**/tb4:toon_landmark_DL_gag_shop_DNARoot')
		self.hq = self.geom.find('**/tb5:toon_landmark_hqDL_DNARoot')
		self.petShop = self.geom.find('**/tb8:toon_landmark_DL_pet_shop_DNARoot')
		self.clothesShop = self.geom.find('**/tb6:toon_landmark_DL_clothes_shop_DNARoot')

		self.__fixDoors(self.gagShop)
		self.__fixDoors(self.petShop)
		self.__fixDoors(self.clothesShop)

		self.hq.find('**/leftDoor_0').setDepthOffset(1)
		self.hq.find('**/rightDoor_0').setDepthOffset(1)
		self.hq.find('**/leftDoor_1').setDepthOffset(1)
		self.hq.find('**/rightDoor_1').setDepthOffset(1)

	def __fixDoors(self, model):
		model.find('**/leftDoor').setDepthOffset(1)
		model.find('**/rightDoor').setDepthOffset(1)

	def loadActors(self):
		fishMod = self.petShop.find('**/animated_prop_PetShopFishAnimatedProp_DNARoot')

		self.fish = Actor('phase_4/models/props/exteriorfish-zero', {'chan': 'phase_4/models/props/exteriorfish-swim'})
		self.fish.reparentTo(self.petShop)
		self.fish.pose('chan', 0)

		fishMod.removeNode()

	def unloadActors(self):
		self.stopAnimateHood()
		self.fish.cleanup()
		self.fish.removeNode()
		del self.fish

	def startAnimateHood(self):
		self.fish.loop('chan')

	def stopAnimateHood(self):
		self.fish.stop()


