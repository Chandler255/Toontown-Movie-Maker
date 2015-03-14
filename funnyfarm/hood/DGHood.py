from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from funnyfarm.dna.DNAParser import *
from toontown.toonbase import ToontownGlobals

class DGHood(DirectObject):

	def __init__(self, dnaStore):
		self.dnaStore = dnaStore
		self.id = ToontownGlobals.DaisyGardens
		self.musicFile = 'phase_8/audio/bgm/DG_nbrhood.mid'
		self.storageFile = 'phase_8/dna/storage_DG.dna'
		self.safeZoneStorageFile = 'phase_8/dna/storage_DG_sz.dna'

		self.holidayStorageDict = {
		 'WINTER_DECORATIONS': 'phase_6/dna/winter_storage_DD.dna',
		 'HALLOWEEN_PROPS': 'phase_6/dna/halloween_props_storage_DD.dna',
		}

		self.safeZoneFile = 'phase_8/dna/daisys_garden_sz.dna'
		self.skyFile = 'phase_3.5/models/props/TT_sky'
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
		else:
			self.sky = loader.loadModel(self.skyFile)
			self.startSkyTrack()

		hoodData = loadDNAFile(self.dnaStore, self.safeZoneFile)
		self.geom = NodePath(hoodData)
		self.geom.reparentTo(render)
		self.sky.reparentTo(render)
		self.sky.setScale(1.2)

		self.__fixHood()
		self.loadActors()
		self.startAnimateHood()

	def unload(self):
		self.unloadSfx()
		self.stopSkyTrack()
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

	def startSkyTrack(self):
		self.clouds1 = self.sky.find('**/cloud1')
		self.clouds2 = self.sky.find('**/cloud2')
		self.clouds1.setScale(0.7, 0.7, 0.7)
		self.clouds2.setScale(0.9, 0.9, 0.9)

		self.clouds1Spin = self.clouds1.hprInterval(360,  Vec3(60,  0,  0))
		self.clouds2Spin = self.clouds2.hprInterval(360,  Vec3(-60,  0,  0))

		self.clouds1Spin.loop()
		self.clouds2Spin.loop()

	def stopSkyTrack(self):
		self.clouds1Spin.finish()
		self.clouds2Spin.finish()

	def __fixHood(self):
		self.gagShop = self.geom.find('**/tb1:toon_landmark_DG_gag_shop_DNARoot')
		self.petShop = self.geom.find('**/tb5:toon_landmark_DG_pet_shop_DNARoot')
		self.clothesShop = self.geom.find('**/tb3:toon_landmark_DG_clothes_shop_DNARoot')
		self.hq = self.geom.find('**/tb2:toon_landmark_hqDG_DNARoot')

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