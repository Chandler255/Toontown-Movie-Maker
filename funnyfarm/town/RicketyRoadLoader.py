from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from funnyfarm.toonbase import FFTime

class RicketyRoadLoader:
	def __init__(self, loaderClass):
		self.loaderClass = loaderClass
		self.playgroundFile = 'phase_14/models/streets/rickety_road.bam'
		self.musicFile = 'phase_13/audio/bgm/party_generic_theme.ogg'
		self.skyFile = 'phase_3.5/models/props/TT_sky.bam'
		self.spookySkyFile = 'phase_3.5/models/props/BR_sky.bam'
	
	def load(self):
		self.ricketyroad = self.loaderClass.loadModel(self.playgroundFile)
		self.ricketyroad.reparentTo(render)
		self.sky = self.loaderClass.loadModel(self.skyFile)
		self.sky.reparentTo(render)
		self.sky.setScale(2.2)
		self.bgm = self.loaderClass.loadSfx(self.musicFile)
		self.bgm.setLoop(True)
		self.bgm.setVolume(0.8)
		self.bgm.play()
		self.startSkyTrack()
		
	def unload(self):
		self.stopSkyTrack()
		self.bgm.stop()
		del self.bgm
		self.centralZone.removeNode()
		del self.centralZone
		self.sky.removeNode()
		del self.sky
	
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

