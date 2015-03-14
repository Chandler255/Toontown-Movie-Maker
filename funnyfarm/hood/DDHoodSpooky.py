from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from funnyfarm.dna.DNAParser import *
from toontown.toonbase import ToontownGlobals
from DistributedBoat import DistributedBoat

class DDHoodSpooky(DirectObject):

	def __init__(self, dnaStore):
		self.dnaStore = dnaStore
		self.id = ToontownGlobals.DonaldsDock
		self.musicFile = 'phase_6/audio/bgm/DD_nbrhood.ogg'
		self.storageFile = 'phase_6/dna/storage_DD.dna'
		self.safeZoneStorageFile = 'phase_6/dna/storage_DD_sz.dna'

		self.holidayStorageDict = {
		 'WINTER_DECORATIONS': 'phase_6/dna/winter_storage_DD.dna',
		 'HALLOWEEN_PROPS': 'phase_6/dna/halloween_props_storage_DD.dna',
		}

		self.safeZoneFile = 'phase_6/dna/donalds_dock_sz.dna'
		self.skyFile = 'phase_3.5/models/props/BR_sky'
		self.whiteFogColor = Vec4(0.8, 0.8, 0.8, 1)
		self.underwaterFogColor = Vec4(0.0, 0.0, 0.6, 1.0)
		self.sfx = None
		self.wantWinter = 0
		self.wantHalloween = 1

	def load(self):
		self.dockSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.ogg')
		self.foghornSound = base.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.ogg')
		self.bellSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.ogg')
		self.waterSound = base.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.ogg')

		loadDNAFile(self.dnaStore, self.storageFile)
		loadDNAFile(self.dnaStore, self.safeZoneStorageFile)
		
		if self.wantWinter:
			winterStorage = self.holidayStorageDict['WINTER_DECORATIONS']
			loadDNAFile(self.dnaStore, winterStorage)
		elif self.wantHalloween:
			halloweenStorage = self.holidayStorageDict['HALLOWEEN_PROPS']
			loadDNAFile(self.dnaStore, halloweenStorage)

		hoodData = loadDNAFile(self.dnaStore, self.safeZoneFile)
		self.geom = NodePath(hoodData)
		self.geom.reparentTo(render)
		self.sky = loader.loadModel(self.skyFile)
		self.sky.reparentTo(render)
		self.fog = Fog('DDFog')
		self.setWhiteFog()
		
		water = self.geom.find('**/water')
		water.setTransparency(1)
		water.setColor(1, 1, 1, 0.8)
		self.boat = self.geom.find('**/donalds_boat')
		wheel = self.boat.find('**/wheel')
		wheel.hide()
		self.boat.stash()
		self.dBoat = DistributedBoat(self)

		self.__fixHood()
		self.loadActors()
		self.startAnimateHood()
		self.startBoatTrack()

	def unload(self):
		if self.sfx:
			self.unloadSfx()
		self.unloadActors()
		self.stopBoatTrack()
		self.setNoFog()
		self.dBoat.delete()
		self.geom.removeNode()
		self.sky.removeNode()
		del self.dBoat
		del self.geom
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
		self.gagShop = self.geom.find('**/tb6:toon_landmark_DD_gag_shop_DNARoot')
		self.petShop = self.geom.find('**/tb10:toon_landmark_DD_pet_shop_DNARoot')
		self.clothesShop = self.geom.find('**/tb8:toon_landmark_DD_clothes_shop_DNARoot')
		self.hq = self.geom.find('**/tb7:toon_landmark_hqDD_SZ_DNARoot')

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
		periscopeMod = self.hq.find('**/animated_prop_HQPeriscopeAnimatedProp_DNARoot')
		fishMod = self.petShop.find('**/animated_prop_PetShopFishAnimatedProp_DNARoot')

		self.periscope = Actor('phase_3.5/models/props/HQ_periscope-mod', {'chan':'phase_3.5/models/props/HQ_periscope-chan'})		
		self.periscope.reparentTo(self.geom)
		self.periscope.setPosHprScale(periscopeMod.getPos(), periscopeMod.getHpr(), periscopeMod.getScale())
		self.periscope.pose('chan', 0)

		self.fish = Actor('phase_4/models/props/exteriorfish-zero', {'chan': 'phase_4/models/props/exteriorfish-swim'})
		self.fish.reparentTo(self.petShop)
		self.fish.pose('chan', 0)

		periscopeMod.removeNode()
		fishMod.removeNode()

		self.animSeq = Sequence(
			Wait(2.0), 
			self.periscope.actorInterval('chan', startFrame=0, endFrame=40), 
			Wait(0.7), 
			self.periscope.actorInterval('chan', startFrame=40, endFrame=90), 
			Wait(0.7), 
			self.periscope.actorInterval('chan', startFrame=91, endFrame=121), 
			Wait(0.7), 
			self.periscope.actorInterval('chan', startFrame=121, endFrame=91), 
			Wait(0.7), 
			self.periscope.actorInterval('chan', startFrame=90, endFrame=40), 
			Wait(0.7), 
			self.periscope.actorInterval('chan', startFrame=40, endFrame=90), 
			Wait(0.7), 
			self.periscope.actorInterval('chan', startFrame=91, endFrame=121), 
			Wait(0.5), 
			self.periscope.actorInterval('chan', startFrame=121, endFrame=148), 
			Wait(3.0)
		)

	def unloadActors(self):
		self.stopAnimateHood()
		self.periscope.cleanup()
		self.periscope.removeNode()
		self.fish.cleanup()
		self.fish.removeNode()
		del self.periscope
		del self.fish

	def startAnimateHood(self):
		self.animSeq.loop()
		self.fish.loop('chan')

	def stopAnimateHood(self):
		self.animSeq.finish()
		self.fish.stop()

	def startBoatTrack(self):
		self.dBoat.generate()
		self.boatSeq = Sequence(
			Func(self.dBoat.enterSailingEast), 
			Wait(20), 
			Func(self.dBoat.exitSailingEast), 
			Wait(10), 
			Func(self.dBoat.enterSailingWest), 
			Wait(20), 
			Func(self.dBoat.exitSailingWest), 
			Wait(10)
		)
		self.boatSeq.loop()

	def stopBoatTrack(self):
		self.dBoat.disable()
		self.boatSeq.finish()
		del self.boatSeq

	def setUnderwaterFog(self):
		self.fog.setColor(self.underwaterFogColor)
		self.fog.setLinearRange(0.1, 100.0)
		render.setFog(self.fog)
		self.sky.setFog(self.fog)

	def setWhiteFog(self):
		self.fog.setColor(self.whiteFogColor)
		self.fog.setLinearRange(0.0, 400.0)
		render.clearFog()
		render.setFog(self.fog)
		self.sky.clearFog()
		self.sky.setFog(self.fog)

	def setNoFog(self):
		render.clearFog()
		self.sky.clearFog()