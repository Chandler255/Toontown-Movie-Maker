from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from funnyfarm.dna.DNAParser import *
from toontown.toonbase import ToontownGlobals
import random

class TTHoodStrt(DirectObject):

	def __init__(self, dnaStore):
		self.dnaStore = dnaStore
		self.id = ToontownGlobals.SillyStreet
		self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg'
		self.storageFile = 'phase_4/dna/storage_TT.dna'
		self.safeZoneStorageFile = 'phase_4/dna/storage_TT_sz.dna'

		self.holidayStorageDict = {
		 'WINTER_DECORATIONS': ['phase_4/dna/winter_storage_TT.dna', 'phase_4/dna/winter_storage_TT_sz.dna'],
		 'HALLOWEEN_PROPS': ['phase_4/dna/halloween_props_storage_TT.dna', 'phase_4/dna/halloween_props_storage_TT_sz.dna'],
		}

		self.safeZoneFile = 'phase_5/dna/toontown_central_2100.dna'
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
		spawnPoints = ((-90, 70, 0, 250, 0, 0), (0, 70, 0, 120, 0, 0), (0, -70, 0, 30, 0, 0))
		spawnPoint = random.choice(spawnPoints)
		base.localAvatar.setPosHpr(*spawnPoint)
		self.__fixHood()
		#self.loadActors()
		#self.startAnimateHood()

	def unload(self):
		self.unloadSfx()
		self.stopSkyTrack()
		#self.unloadActors()
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
		#self.gagShop = self.geom.find('**/sz19:toon_landmark_TT_gag_shop_DNARoot')
		self.hq = self.geom.find('**/tb71:toon_landmark_hqTT_DNARoot')
		#self.petShop = self.geom.find('**/sz22:toon_landmark_TT_pet_shop_DNARoot')
		#self.library = self.geom.find('**/sz18:toon_landmark_TT_library_DNARoot')
		#self.bank = self.geom.find('**/sz14:toon_landmark_TT_bank_DNARoot')
		#self.school = self.geom.find('**/sz16:toon_landmark_TT_school_house_DNARoot')
		#self.clothesShop = self.geom.find('**/sz21:toon_landmark_TT_clothes_shop_DNARoot')
		#self.toonhall = self.geom.find('**/sz13:toon_landmark_TT_toonhall_DNARoot')

		#self.__fixDoors(self.gagShop)
		#self.__fixDoors(self.petShop)
		#self.__fixDoors(self.library)
		#self.__fixDoors(self.bank)
		#self.__fixDoors(self.school)
		#self.__fixDoors(self.clothesShop)
		#self.__fixDoors(self.toonhall)

		self.hq.find('**/leftDoor_0').setDepthOffset(1)
		self.hq.find('**/rightDoor_0').setDepthOffset(1)
		self.hq.find('**/leftDoor_1').setDepthOffset(1)
		self.hq.find('**/rightDoor_1').setDepthOffset(1)

		#self.geom.find('**/hill').setTransparency(TransparencyAttrib.MBinary, 1)

	#def __fixDoors(self, model):
#		model.find('**/leftDoor').setDepthOffset(1)
#		model.find('**/rightDoor').setDepthOffset(1)

	def loadActors(self):
		#periscopeMod = self.hq.find('**/animated_prop_HQPeriscopeAnimatedProp_DNARoot')
		#telescopeMod = self.hq.find('**/animated_prop_HQTelescopeAnimatedProp_DNARoot')
		#fishMod = self.petShop.find('**/animated_prop_PetShopFishAnimatedProp_DNARoot')
		
		'''self.telescope = Actor('phase_3.5/models/props/HQ_telescope-mod', {'chan':'phase_3.5/models/props/HQ_telescope-chan'})
		self.telescope.reparentTo(self.geom)
		self.telescope.setPosHprScale(telescopeMod.getPos(), telescopeMod.getHpr(), telescopeMod.getScale())
		self.telescope.pose('chan', 0)

		self.fish = Actor('phase_4/models/props/exteriorfish-zero', {'chan': 'phase_4/models/props/exteriorfish-swim'})
		self.fish.reparentTo(self.petShop)
		self.fish.pose('chan', 0)

		#periscopeMod.removeNode()
		telescopeMod.removeNode()
		fishMod.removeNode()'''

		'''self.animSeq = Sequence(
			Wait(5.0), 
			self.telescope.actorInterval('chan', startFrame=0, endFrame=32), 
			Wait(0.5), 
			self.telescope.actorInterval('chan', startFrame=32, endFrame=78), 
			Wait(0.5), 
			self.telescope.actorInterval('chan', startFrame=79, endFrame=112), 
			Wait(0.5), 
			self.telescope.actorInterval('chan', startFrame=112, endFrame=79), 
			Wait(0.5), 
			self.telescope.actorInterval('chan', startFrame=78, endFrame=32), 
			Wait(0.5), 
			self.telescope.actorInterval('chan', startFrame=32, endFrame=78), 
			Wait(0.5), 
			self.telescope.actorInterval('chan', startFrame=79, endFrame=112), 
			Wait(0.5), 
			self.telescope.actorInterval('chan', startFrame=112, endFrame=148), 
			Wait(4.0)'''
		#)

	'''def unloadActors(self):
		#self.stopAnimateHood()
		self.telescope.cleanup()
		self.telescope.removeNode()
		del self.telescope
		self.fish.cleanup()
		self.fish.removeNode()
		del self.fish'''

	#def startAnimateHood(self):
	#	self.animSeq.loop()
	#	self.fish.loop('chan')

	#def stopAnimateHood(self):
	#	self.animSeq.finish()
#		self.fish.stop()


