from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.toon import NPCToons
from toontown.toonbase import ToontownGlobals
from direct.task import Task
from direct.showbase.DirectObject import DirectObject
from random import choice
import ElectionGlobals

class ElectionBalloon(DirectObject):

	def __init__(self):
		self.avId = 0
		self.flightPathIndex = 0
		
		# Create the balloon
		self.balloon = loader.loadModel('phase_4/models/events/election_slappyBalloon-static')
		self.balloon.reparentTo(render)
		self.balloon.setPos(*ElectionGlobals.BalloonBasePosition)
		self.balloon.setScale(ElectionGlobals.BalloonScale)
		
		# Balloon collision NodePath (outside)
		self.collisionNP = self.balloon.find('**/Collision_Outer')

		self.slappy = NPCToons.createLocalNPC(2021)
		self.slappy.loop('neutral')

		# Create balloon flight paths and Slappy speeches. It's important we do this AFTER we load everything
		# else as this requires both the balloon and Slappy.
		#self.flightPaths = ElectionGlobals.generateFlightPaths(self)
		#self.toonFlightPaths = ElectionGlobals.generateToonFlightPaths(self)
		#self.speechSequence = ElectionGlobals.generateSpeechSequence(self)

	def delete(self):
		# Clean up after our mess...
		self.balloon.removeNode()
		del self.balloon
		if self.slappy:
			self.slappy.delete()

	def enterWaiting(self):
		# Render Slappy, since we're going to be giving rides
		self.slappy.reparentTo(self.balloon)
		self.slappy.setPos(0.7, 0.7, 0.4)
		self.slappy.setH(150)
		self.slappy.setScale(0.4)

		# Mini animation for the balloon hovering near the floor
		self.balloonIdle = Sequence(
			Wait(0.3),
			self.balloon.posInterval(3, (-15, 33, 1.5), blendType='easeInOut'),
			Wait(0.3),
			self.balloon.posInterval(3, (-15, 33, 1.1), blendType='easeInOut'),
		)
		self.balloonIdle.loop()
	
	def enterElectionIdle(self):
		# Slappy is off for the election, but he left his balloon parked in TTC.
		self.balloon.setPos(*ElectionGlobals.BalloonElectionPosition)
		self.balloon.setH(283)
		self.balloonElectionIdle = Sequence(
			self.balloon.posInterval(3, (166.5, 64.0, 52.0), blendType='easeInOut'),
			self.balloon.posInterval(3, (166.5, 64.0, 53.0), blendType='easeInOut'),
		)
		self.balloonElectionIdle.loop()

	def enterElectionCrashing(self):
		# Slappy has gone sad, and in turn his balloon has ran out of silliness.
		# It's tumbling down behind Toon Hall.
		self.balloonElectionFall = Sequence(
			self.balloon.posHprInterval(17, (200.0, 20.0, 0.0), (105, -5, -5), blendType='easeInOut'),
			Func(self.balloon.hide)
		)
		self.balloonElectionFall.start()

	def exitWaiting(self):
		self.balloonIdle.finish()

	def exitElectionIdle(self):
		self.balloonElectionIdle.finish()