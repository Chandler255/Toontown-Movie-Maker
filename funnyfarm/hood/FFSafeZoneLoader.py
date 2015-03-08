from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from funnyfarm.toonbase import FFTime
from direct.gui.DirectGui import *

class FFSafeZoneLoader:
	def __init__(self, loaderClass, sfxMgr):
		self.loaderClass = loaderClass
		self.sfxMgr = sfxMgr
		self.playgroundFile = 'phase_14/models/neighborhoods/funny_farm.bam'
		self.winterPlaygroundFile = 'phase_14/models/neighborhoods/funny_farm_winter.bam'
		self.spookyPlaygroundFile = 'phase_14/models/neighborhoods/funny_farm_halloween.bam'
		self.musicFile = 'phase_4/audio/bgm/tt_s_ara_gen_fireworks_auldLangSyne.ogg'
		self.skyFile = 'phase_3.5/models/props/TT_sky.bam'
		self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
	
	def load(self):
		if FFTime.isWinter:
			self.funnyfarm = self.loaderClass.loadModel(self.winterPlaygroundFile)
			self.sky = self.loaderClass.loadModel(self.spookySkyFile)
		elif FFTime.isHalloween:
			self.funnyfarm = self.loaderClass.loadModel(self.spookyPlaygroundFile)
			self.sky = self.loaderClass.loadModel(self.spookySkyFile)
			self.loadSillyMeter()
		else:
			self.funnyfarm = self.loaderClass.loadModel(self.playgroundFile)
			self.sky = self.loaderClass.loadModel(self.skyFile)
			self.loadSillyMeter()
			self.startSkyTrack()
		
		self.funnyfarm.reparentTo(render)
		self.sky.reparentTo(render)
		self.sky.setScale(1.5)
		self.loadPropStage()
		self.sign = self.funnyfarm.find('**/DD_sign2')
		self.font = loader.loadFont('phase_3/models/fonts/Comedy.bam')
		self.text = OnscreenText(parent=self.sign, text='Funny Farm\nCentral', scale=(1.5, 1.4), fg=(0.439216, 0.247059, 0.184314, 1), align=TextNode.ACenter, font=self.font)
		self.text.setDepthOffset(1)
		self.bgm = self.loaderClass.loadSfx(self.musicFile)
		self.bgm.setLoop(True)
		self.bgm.setVolume(0.8)
		
	def loadSfx(self):
		self.bgm.play()
		self.sfxMgr.audio3d.attachSoundToObject(self.sfxMgr.phaseTwo, self.sillyMeter)
		self.sfxMgr.phaseTwo.play()
		if FFTime.isHalloween:
			pass
		else:
			self.sfxMgr.audio3d.attachSoundToObject(self.sfxMgr.propShow, self.stage)
			self.sfxMgr.propShow.play()
		
	def unload(self):
		self.bgm.stop()
		del self.bgm
		self.sfxMgr.audio3d.detachSound(self.sfxMgr.phaseTwo)
		self.sfxMgr.audio3d.detachSound(self.sfxMgr.propShow)
		self.sfxMgr.phaseTwo.stop()
		self.sfxMgr.propShow.stop()
		self.funnyfarm.removeNode()
		del self.funnyfarm
		self.sky.removeNode()
		del self.sky
		self.stage.cleanup()
		self.stage.removeNode()
		del self.stage
		if FFTime.isWinter:
			pass
		elif FFTime.isHalloween:
			self.sillyMeter.cleanup()
			self.sillyMeter.removeNode()
			del self.sillyMeter
		else:
			self.stopSkyTrack()
			self.sillyMeter.cleanup()
			self.sillyMeter.removeNode()
			del self.sillyMeter
	
	def loadSillyMeter(self):
		self.sillyMeter = Actor('phase_4/models/props/tt_a_ara_ttc_sillyMeter_default.bam', 
							  {'phaseOne':'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseOne.bam', 
							  'phaseTwo':'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseTwo.bam', 
							  'phaseThree':'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseThree.bam', 
							  'phaseFour':'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFour.bam', 
							  'phaseFourToFive':'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFourToFive.bam', 
							  'phaseFive':'phase_4/models/props/tt_a_ara_ttc_sillyMeter_phaseFive.bam'})
		self.sillyMeter.reparentTo(render)
		self.sillyMeter.loop('phaseTwo')
	
	def loadPropStage(self):
		if FFTime.isWinter:
			self.stage = Actor('phase_13/models/parties/tt_r_ara_pty_winterProps.bam', 
							{'dance':'phase_13/models/parties/tt_a_ara_pty_hydra_dance.bam'})
			self.stage.actorInterval('dance').loop()
		elif FFTime.isHalloween:
			self.stage = Actor('phase_13/models/parties/tt_a_ara_pty_hydra_default.bam', 
							{'dance':'phase_13/models/parties/tt_a_ara_pty_hydra_dance.bam'})
			self.stage.setColorScale(0.5, 0.5, 0.5, 1)
			self.stage.find('**/pty_hydrantSummer').hide()
			self.stage.find('**/tc_prop_trashcan_dga').hide()
			self.stage.find('**/prop_mailbox_dod').hide()
		else:
			self.stage = Actor('phase_13/models/parties/tt_a_ara_pty_hydra_default.bam', 
							{'dance':'phase_13/models/parties/tt_a_ara_pty_hydra_dance.bam'})
			self.stage.actorInterval('dance').loop()
		
		self.stage.reparentTo(render)
		self.stage.setPos(0, 102, 0)
		self.stage.setScale(2)
		
	def startSkyTrack(self):
		self.Clouds1 = self.sky.find('**/cloud1')
		self.Clouds2 = self.sky.find('**/cloud2')
		self.Clouds1.setScale(0.7, 0.7, 0.7)
		self.Clouds2.setScale(0.9, 0.9, 0.9)

		self.Clouds1Spin = self.Clouds1.hprInterval(360,  Vec3(60,  0,  0))
		self.Clouds1Spin.loop()
		self.Clouds2Spin = self.Clouds2.hprInterval(360,  Vec3(-60,  0,  0))
		self.Clouds2Spin.loop()
		
	def stopSkyTrack(self):
		self.Clouds1Spin.finish()
		self.Clouds2Spin.finish()
		
	def getPetShopDoor(self):
		return self.funnyfarm.find('**/door_double_round_ur_right')
		
	def getGagShopDoor(self):
		return self.funnyfarm.find('**/door_double_square_ur_right')
		
	def getHQDoor(self):
		return self.funnyfarm.find('**/rightDoor_0')
		
	def getCastleDoor(self):
		self.castle = self.funnyfarm.find('**/tt_m_ara_est_house_castle.egg')
		return self.castle.find('**/rightDoor')
			


		
