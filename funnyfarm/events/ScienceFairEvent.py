from pandac.PandaModules import *
from direct.directbase import DirectStart
from direct.actor.Actor import Actor

class ScienceFairEvent:

	def __init__(self):
		self.scienceFair = NodePath('ScienceFair')
		self.scienceFair.reparentTo(base.render)

		self.tent = loader.loadModel('phase_4/models/events/event_tent')
		self.tent.reparentTo(self.scienceFair)
		self.tent.setPosHpr(0, 0, 0, 270, 0, 0)

		self.redFlag = Actor('phase_4/models/events/event-flag-mod')
		self.redFlag.loadAnims({'waving': 'phase_4/models/events/event-flag-anim'})
		self.redFlag.reparentTo(self.tent.find('**/flag1_jnt'))
		self.redFlag.loop('waving')

		self.blueFlag = Actor('phase_4/models/events/event-flag-mod')
		self.blueFlag.loadAnims({'waving': 'phase_4/models/events/event-flag-anim'})
		self.blueFlag.reparentTo(self.tent.find('**/flag2_jnt'))
		self.blueFlag.loop('waving')

		self.tent2 = loader.loadModel('phase_4/models/events/event_tent')
		self.tent2.reparentTo(self.scienceFair)
		self.tent2.setPosHpr(85.91, 149.76, 2.61, 327.99, 0, 0)

		self.balloonArchway = loader.loadModel('phase_4/models/events/balloon_archway_spiraled')
		self.balloonArchway.reparentTo(self.scienceFair)
		self.balloonArchway.setPosHpr(-24.25, 17.24, 0, 0, 0, 0)
		self.balloonArchway.flattenStrong()

		self.balloonArchway2 = loader.loadModel('phase_4/models/events/balloon_archway_spiraled')
		self.balloonArchway2.reparentTo(self.scienceFair)
		self.balloonArchway2.setPosHpr(-24.25, -31.03, 0, 0, 0, 0)
		self.balloonArchway2.flattenStrong()

		self.balloonArchway3 = loader.loadModel('phase_4/models/events/balloon_archway_spiraled')
		self.balloonArchway3.reparentTo(self.scienceFair)
		self.balloonArchway3.setPosHpr(99.6, 0.65, 4, 272.39, 0, 0)
		self.balloonArchway3.setScale(1.21)
		self.balloonArchway3.flattenStrong()

		self.balloontowerCake = loader.loadModel('phase_4/models/events/balloon_set_cake')
		self.balloontowerCake.reparentTo(self.scienceFair)
		self.balloontowerCake.setPosHpr(95.65, 6.75, 4, 270, 0, 0)
		self.balloontowerCake.flattenStrong()

		self.balloontowerStar = loader.loadModel('phase_4/models/events/balloon_set_star')
		self.balloontowerStar.reparentTo(self.scienceFair)
		self.balloontowerStar.setPosHpr(95.70, -5.56, 4, 270, 0, 0)
		self.balloontowerStar.flattenStrong()