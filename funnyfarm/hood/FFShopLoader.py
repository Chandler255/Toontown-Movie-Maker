from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *

class FFShopLoader:
	def __init__(self, sfxMgr, localAvatar):
		self.sfxMgr = sfxMgr
		self.localAvatar = localAvatar
		self.petShopFile = 'phase_4/models/modules/PetShopInterior.bam'
		self.gagShopFile = 'phase_4/models/modules/gagShop_interior.bam'
		self.hqFile = 'phase_3.5/models/modules/HQ_interior.bam'
		self.castleFile = 'phase_3.5/models/modules/tt_m_ara_int_toonhall.bam'
		self.doors = 'phase_3.5/models/modules/doors_practical.bam' 
		self.musicFile = 'phase_4/audio/bgm/m_match_bg2.ogg'
		self.bgm = loader.loadSfx(self.musicFile)
		self.bgm.setLoop(True)
	
	def renderBlackScreen(self):
		self.image = OnscreenImage(image='phase_14/maps/loading_black.jpg', parent = render2d)
		base.graphicsEngine.renderFrame()
		base.graphicsEngine.renderFrame()
		Sequence(Wait(1), Func(self.image.hide), Func(base.transitions.irisIn), Func(self.sfxMgr.doorOpen.play)).start()
		
	def loadPetShop(self):
		def setAvatar():
			self.localAvatar.collisionsOn()
			self.localAvatar.enableControls()
			self.localAvatar.setPos(0, -11, 0)
			self.localAvatar.setHpr(0, 0, 0)

		self.renderBlackScreen()
		self.petShop = loader.loadModel(self.petShopFile)
		self.petShop.reparentTo(render)
		self.petDoors = loader.loadModel(self.doors).find('**/door_double_round_ur')
		self.petDoors.setColor(0.996094, 0.957031, 0.597656, 1.0)
		self.petDoors.reparentTo(self.petShop.find('**/door_origin'))
		self.__fixDoor(self.petDoors)
		Sequence(Wait(1), Func(self.bgm.play), Func(setAvatar)).start()
		
	def unloadPetShop(self):
		self.renderBlackScreen()
		self.bgm.stop()
		self.petShop.removeNode()
		self.localAvatar.collisionsOn()
		self.localAvatar.enableControls()
		self.localAvatar.setPos(-51.7991, 68.0257, 0)
		self.localAvatar.setHpr(225, 0, 0)
		
	def loadGagShop(self):
		def setAvatar():
			self.localAvatar.collisionsOn()
			self.localAvatar.enableControls()
			self.localAvatar.setPos(1, 4, 0)
			self.localAvatar.setHpr(0, 0, 0)
		
		self.renderBlackScreen()
		self.gagShop = loader.loadModel(self.gagShopFile)
		self.gagShop.reparentTo(render)
		self.counter1 = loader.loadModel('phase_3.5/models/modules/counterShort.bam')
		self.counter1.reparentTo(self.gagShop.find('**/random_mo1_TI_counterShort'))
		self.counter2 = self.counter1.copyTo(self.gagShop.find('**/random_mo2_TI_counterShort'))
		self.wall = loader.loadTexture('phase_5.5/maps/big_stripes2.jpg')
		self.gagShop.find('**/random_tc1_TI_wallpaper').setTexture(self.wall, 1)
		self.gagShop.find('**/random_tc1_TI_wallpaper').setColor(0.45, 0.7, 0.45)
		self.gagShop.find('**/random_tc1_TI_wallpaper_border').setTexture(self.wall, 1)
		self.gagShop.find('**/random_tc1_TI_wallpaper_border').setColor(0.45, 0.7, 0.45)
		self.wainscot = loader.loadTexture('phase_3.5/maps/wall_paper_b4.jpg')
		self.gagShop.find('**/random_tc1_TI_wainscotting').setTexture(self.wainscot, 1)
		self.gagShop.find('**/random_tc1_TI_wainscotting').setColor(0.832031, 0.5, 0.296875, 1.0)
		self.gagDoors = loader.loadModel(self.doors).find('**/door_double_round_ur')
		self.gagDoors.setColor(0.832031, 0.5, 0.296875, 1.0)
		self.gagDoors.reparentTo(self.gagShop.find('**/door_origin'))
		self.__fixDoor(self.gagDoors)
		Sequence(Wait(1), Func(self.bgm.play), Func(setAvatar)).start()
		
	def unloadGagShop(self):
		self.renderBlackScreen()
		self.bgm.stop()
		self.gagShop.removeNode()
		self.localAvatar.collisionsOn()
		self.localAvatar.enableControls()
		self.localAvatar.setPos(53.0105, 72.8147, 0)
		self.localAvatar.setHpr(135, 0, 0)
		
	def __fixDoor(self, door):
		door.find('**/door_double_round_ur_hole_left').setColor(0, 0, 0, 1)
		door.find('**/door_double_round_ur_hole_right').setColor(0, 0, 0, 1)
		door.find('**/door_double_round_ur_right').setDepthOffset(True)
		door.find('**/door_double_round_ur_left').setDepthOffset(True)
		door.setDepthOffset(True)
		
	def getPetShopDoor(self):
		return self.petDoors.find('**/door_double_round_ur_right')
		
	def getGagShopDoor(self):
		return self.gagDoors.find('**/door_double_round_ur_right')

