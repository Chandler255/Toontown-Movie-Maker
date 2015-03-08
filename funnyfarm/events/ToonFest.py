from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
import ElectionGlobals

# Since TTR uses xml files for their DNA Parsing, we have to load everything in manually.
# It's a hassle, but there's not too many models, and we load them efficiently.

class ToonFest(DirectObject):

	def __init__(self):
		self.musicFile = 'phase_6/audio/bgm/TF_SZ_1.ogg'
		self.skyFile = 'phase_3.5/models/props/TT_sky'
		self.sfx = None
		self.models = [
			'phase_6/models/events/tf_grounds_1', 
			'phase_6/models/events/tf_tower', 
			'phase_6/models/events/tf_balloon', 
			'phase_6/models/golf/outdoor_zone_entrance',
			'phase_6/models/golf/game_table', '', '', '', '', '',
			'phase_6/models/golf/picnic_table', '', '', 
			'phase_4/models/props/piers_tt', '', '', '', '', ''
		]
		self.posList = [
			Point3(0, 0, 0), 
			Point3(221, -61, 4.5), 
			Point3(273.75, -260.89, 24.76),
			Point3(-83.9, -303.4, 18.3),
			Point3(58, -143, 14.4),
			Point3(94, 14, 7.6),
			Point3(362, 37, 9.65),
			Point3(354, -118, 9.63),
			Point3(326, -514, 0.93),
			Point3(195, -278, 12.2),
			Point3(150, -320, 11.6),
			Point3(319, -535, 1),
			Point3(66, -180, 12),
			Point3(239, -551, 0.9),
			Point3(262, -543, 0.9),
			Point3(275, -524, 0.9),
			Point3(273, -503, 0.9),
			Point3(260, -494, 0.9),
			Point3(245, -493, 0.9),
		]
		self.hprList = [
			Vec3(0, 0, 0),
			Vec3(-30, 0, 0),
			Vec3(278.75, 0, 0),
			Vec3(82.5, 0, 0),
			Vec3(260, -4, 2),
			Vec3(-121, -7, 0),
			Vec3(-212, 0, 0),
			Vec3(105, 0, 0),
			Vec3(-260, 0, 0),
			Vec3(90, -3, 1),
			Vec3(10, 0, 0),
			Vec3(20, 0, 0),
			Vec3(-75, -1, -1),
			Vec3(0, 0, 0),
			Vec3(40, 0, 0),
			Vec3(75, 0, 0),
			Vec3(120, 0, 0),
			Vec3(170, 0, 0),
			Vec3(170, 0, 0),
		]

	def load(self):
		self.geom = NodePath('toonfest')
		for model in self.models:
			if model == '':
				pass
			else:
				index = self.models.index(model)
				ret = loader.loadModel(model)
				ret.reparentTo(self.geom)
				ret.setPosHpr(self.posList[index], self.hprList[index])
				if index == 4:
					ret.copyTo(self.geom).setPosHpr(self.posList[5], self.hprList[5])
					ret.copyTo(self.geom).setPosHpr(self.posList[6], self.hprList[6])
					ret.copyTo(self.geom).setPosHpr(self.posList[7], self.hprList[7])
					ret.copyTo(self.geom).setPosHpr(self.posList[8], self.hprList[8])
					ret.copyTo(self.geom).setPosHpr(self.posList[9], self.hprList[9])
				elif index == 10:
					ret.copyTo(self.geom).setPosHpr(self.posList[11], self.hprList[11])
					ret.copyTo(self.geom).setPosHpr(self.posList[12], self.hprList[12])
				elif index == 13:
					ret.copyTo(self.geom).setPosHpr(self.posList[14], self.hprList[14])
					ret.copyTo(self.geom).setPosHpr(self.posList[15], self.hprList[15])
					ret.copyTo(self.geom).setPosHpr(self.posList[16], self.hprList[16])
					ret.copyTo(self.geom).setPosHpr(self.posList[17], self.hprList[17])
					ret.copyTo(self.geom).setPosHpr(self.posList[18], self.hprList[18])
		self.geom.reparentTo(render)
		self.sky = loader.loadModel(self.skyFile)
		self.sky.reparentTo(render)
		self.sky.setScale(5.0)
		self.startSkyTrack()
		self.loadActors()
		self.startTowerSpin()
		return

	def unload(self):
		if self.sfx:
			self.unloadSfx()
		self.stopTowerSpin()
		self.stopSkyTrack()
		self.unloadActors()
		self.geom.removeNode()
		self.sky.removeNode()
		del self.geom
		del self.sky

	def loadSfx(self):
		self.sfx = base.loadSfx(self.musicFile)
		self.sfx.setVolume(0.5)
		self.sfx.setLoop(True)
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

	def loadActors(self):
		self.flippyStand = Actor('phase_4/models/events/election_flippyStand-mod', {'idle': 'phase_4/models/events/election_flippyStand-idle'})
		self.flippyStand.reparentTo(self.geom)
		self.flippyStand.setPosHprScale(170.55, -257.59, 9.23, 305.84, 3.37, -8.75, 0.55, 0.55, 0.55)
		self.flippyStand.exposeJoint(None,"modelRoot", "LInnerShoulder")
		flippyTable = self.flippyStand.find('**/LInnerShoulder')
		self.flippyStand.exposeJoint(None,"modelRoot", "Box_Joint")
		wheelbarrowJoint = self.flippyStand.find('**/Box_Joint').attachNewNode('Pie_Joint')
		wheelbarrow = self.flippyStand.find('**/Box')
		wheelbarrow.setPosHprScale(-2.39, 0.00, 1.77, 0.00, 0.00, 6.00, 1.14, 1.54, 0.93)

		pie = loader.loadModel('phase_3.5/models/props/tart')
		pieS = pie.copyTo(flippyTable)
		pieS.setPosHprScale(-2.61, -0.37, -1.99, 355.60, 90.00, 4.09, 1.6, 1.6, 1.6)

		for pieSettings in ElectionGlobals.FlippyWheelbarrowPies:
			pieModel = pie.copyTo(wheelbarrowJoint)
			pieModel.setPosHprScale(*pieSettings)
		wheelbarrowJoint.setPosHprScale(3.94, 0.00, 1.06, 270.00, 344.74, 0.00, 1.43, 1.12, 1.0)
		self.restockSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_SOS_pies_restock.ogg')
		self.splashSfx = loader.loadSfx('phase_9/audio/sfx/CHQ_FACT_paint_splash.ogg')

		cs = CollisionBox(Point3(7, 0, 0), 12, 5, 18)
		self.pieCollision = self.flippyStand.attachNewNode(CollisionNode('wheelbarrow_collision'))
		self.pieCollision.node().addSolid(cs)

		self.flippyStand.loop('idle')

	def unloadActors(self):
		self.flippyStand.cleanup()
		self.flippyStand.removeNode()
		del self.flippyStand

	def startTowerSpin(self):
		tower = self.geom.find('**/tf_tower')	
		base1 = tower.find('**/base1')
		base2 = tower.find('**/base2')
		base3 = tower.find('**/base3')

		base1Spin = base1.hprInterval(20, (360, 0, 0))
		base2Spin = base2.hprInterval(15, (-360, 0, 0))
		base3Spin = base3.hprInterval(10, (360, 0, 0))

		self.accept('enterbase1_collision', self.__handleCollisionOn, extraArgs=[base1])
		self.accept('enterbase2_collision', self.__handleCollisionOn, extraArgs=[base2])
		self.accept('enterbase3_collision', self.__handleCollisionOn, extraArgs=[base3])
		self.accept('enterbase4_collision', self.__handleCollisionOff)

		self.accept('exitbase1_collision', self.__handleCollisionOff)
		self.accept('exitbase2_collision', self.__handleCollisionOn, extraArgs=[base1])
		self.accept('exitbase3_collision', self.__handleCollisionOn, extraArgs=[base2])
		self.accept('exitbase4_collision', self.__handleCollisionOn, extraArgs=[base3])
		
		base1Spin.loop()
		base2Spin.loop()
		base3Spin.loop()

	def stopTowerSpin(self):
		self.spinSeq.finish()
		self.ignoreAll()

	def __handleCollisionOn(self, model, event):
		base.localAvatar.wrtReparentTo(model)

	def __handleCollisionOff(self, event):
		base.localAvatar.wrtReparentTo(render)




