from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.task import Task
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.directnotify.DirectNotifyGlobal import *
from otp.otpbase import OTPGlobals
from direct.controls.GhostWalker import GhostWalker
from direct.controls.GravityWalker import GravityWalker
from direct.controls.ObserverWalker import ObserverWalker
from direct.controls.PhysicsWalker import PhysicsWalker
from direct.controls.SwimWalker import SwimWalker
from direct.controls.TwoDWalker import TwoDWalker
from direct.controls import ControlManager
from toontown.toon import Toon
from toontown.toon.LaffMeter import LaffMeter
from ToonGlobals import *
import random

class LocalToon(Toon.Toon):
	notify = directNotify.newCategory('LocalToon')
	movingNeutral, movingForward = (False, False)
	movingRotation, movingBackward = (False, False)
	movingJumping = False

	def __init__(self):
		Toon.Toon.__init__(self)
		self.hasGM = False
		self.accessLevel = 0
		self.accessList = [100, 200, 300]
		self.hp = 15
		self.maxHp = 15
		self.soundWalk = base.loadSfx('phase_3.5/audio/sfx/AV_footstep_walkloop.ogg')
		self.soundRun = base.loadSfx('phase_3.5/audio/sfx/AV_footstep_runloop.ogg')
		self.soundWalk.setLoop(True)
		self.soundRun.setLoop(True)
		self.soundWalk.setVolume(50)
		self.soundRun.setVolume(50)
		self.cTrav = CollisionTraverser('base.cTrav')
		base.pushCTrav(self.cTrav)
		self.cTrav.setRespectPrevTransform(1)
		self.avatarControlsEnabled = 0
		self.controlManager = ControlManager.ControlManager(True, False)
		self.offset = 3.2375
		
	def destroy(self):
		Toon.Toon.delete(self)
		
	def startLaffMeter(self):
		self.laffMeter = LaffMeter(self.style, self.hp, self.maxHp)
		self.laffMeter.setAvatar(self)
		self.laffMeter.setScale(0.075)
		if self.style.head[0] == 'p' or self.style.head[0] == 's':
			self.laffMeter.setPos(-1.18, 0.0, -0.87)
		else:
			self.laffMeter.setPos(-1.2, 0.0, -0.87)
		self.laffMeter.start()
		
	def setHealth(self, hp, maxHp):
		self.hp = hp
		self.maxHp = maxHp
		self.laffMeter.adjustFace(hp, maxHp)

	def setName(self, name):
		self.nametag.setName(name)

	def setNametagFont(self, font):
		self.nametag.setFont(font)

	def setAccessLevel(self, level):
		self.accessLevel = level
	
	def setGMIcon(self):
		if self.hasGM:
			self.removeGMIcon()
		if self.accessLevel not in self.accessList:
			self.notify.warning('Invalid access level! Must match one of: ' + str(self.accessList))
			return
		self.hasGM = True
		self.gmIcon = loader.loadModel('phase_14/models/gui/gmIcon-' + str(self.accessLevel))
		self.gmIcon.reparentTo(NodePath(self.nametag.getNameIcon()))
		self.gmIcon.setScale(3.25)
		self.gmIcon.setZ(-1.5)
		self.gmIcon.setY(0.0)
		self.gmIcon.setTransparency(1)
		self.gmIconInterval = LerpHprInterval(self.gmIcon, 3.0, Point3(0, 0, 0), Point3(-360, 0, 0))
		self.gmIconInterval.loop()
			
	def setGMPartyIcon(self, gmType):
		if self.hasGM:
			self.removeGMIcon()
		iconInfo = ('phase_3.5/models/gui/tt_m_gui_gm_toonResistance_fist', 'phase_3.5/models/gui/tt_m_gui_gm_toontroop_whistle', 'phase_3.5/models/gui/tt_m_gui_gm_toonResistance_fist', 'phase_3.5/models/gui/tt_m_gui_gm_toontroop_getConnected')
		if gmType > len(iconInfo) - 1:
			return
		self.gmIcon = loader.loadModel(iconInfo[gmType])
		self.gmIcon.reparentTo(NodePath(self.nametag.getNameIcon()))
		self.gmIcon.find('**/gmPartyHat').removeNode()
		self.gmIcon.setScale(3.25)
		self.gmIcon.setZ(-1.5)
		self.gmIcon.setY(0.0)
		self.gmIcon.setTransparency(1)
		self.gmIconInterval = LerpHprInterval(self.gmIcon, 3.0, Point3(0, 0, 0), Point3(-360, 0, 0))
		self.gmIconInterval.loop()
		
	def removeGMIcon(self):
		if not self.hasGM:
			self.notify.warning('LocalToon has no GMIcon to remove!')
			return
		self.hasGM = False
		self.gmIconInterval.finish()
		del self.gmIconInterval
		self.gmIcon.removeNode()
		del self.gmIcon

	def uniqueName(self, idString):
		return idString
		
	def setAnimState(self, anim, startFrame=None, endFrame=None, playRate=1.0):
		self.actorInterval(anim, startFrame=startFrame, endFrame=endFrame, playRate=playRate).loop()
		
	def useSwimControls(self):
		self.controlManager.use('swim', self)

	def useGhostControls(self):
		self.controlManager.use('ghost', self)

	def useWalkControls(self):
		self.controlManager.use('walk', self)

	def useTwoDControls(self):
		self.controlManager.use('twoD', self)

	def wantLegacyLifter(self):
		return False

	def setupControls(self, avatarRadius = 1.4, floorOffset = OTPGlobals.FloorOffset, reach = 4.0, wallBitmask = OTPGlobals.WallBitmask, floorBitmask = OTPGlobals.FloorBitmask, ghostBitmask = OTPGlobals.GhostBitmask):
		walkControls = GravityWalker(legacyLifter=self.wantLegacyLifter())
		walkControls.setWallBitMask(wallBitmask)
		walkControls.setFloorBitMask(floorBitmask)
		walkControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
		walkControls.setAirborneHeightFunc(self.getAirborneHeight)
		self.controlManager.add(walkControls, 'walk')
		self.physControls = walkControls
		twoDControls = TwoDWalker()
		twoDControls.setWallBitMask(wallBitmask)
		twoDControls.setFloorBitMask(floorBitmask)
		twoDControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
		twoDControls.setAirborneHeightFunc(self.getAirborneHeight)
		self.controlManager.add(twoDControls, 'twoD')
		swimControls = SwimWalker()
		swimControls.setWallBitMask(wallBitmask)
		swimControls.setFloorBitMask(floorBitmask)
		swimControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
		swimControls.setAirborneHeightFunc(self.getAirborneHeight)
		self.controlManager.add(swimControls, 'swim')
		ghostControls = GhostWalker()
		ghostControls.setWallBitMask(ghostBitmask)
		ghostControls.setFloorBitMask(floorBitmask)
		ghostControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
		ghostControls.setAirborneHeightFunc(self.getAirborneHeight)
		self.controlManager.add(ghostControls, 'ghost')
		observerControls = ObserverWalker()
		observerControls.setWallBitMask(ghostBitmask)
		observerControls.setFloorBitMask(floorBitmask)
		observerControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
		observerControls.setAirborneHeightFunc(self.getAirborneHeight)
		self.controlManager.add(observerControls, 'observer')
		self.controlManager.use('walk', self)
		self.setWalkSpeedNormal()
		self.setupCamera()
		base.taskMgr.add(self.handleAnimation, 'AnimationHandler')
		
	def enableAvatarControls(self):
		if self.avatarControlsEnabled:
			return
		self.avatarControlsEnabled = 1
		self.controlManager.enable()
		base.taskMgr.add(self.handleAnimation, 'AnimationHandler')

	def disableAvatarControls(self):
		if not self.avatarControlsEnabled:
			return
		self.avatarControlsEnabled = 0
		self.controlManager.disable()
		base.taskMgr.remove('AnimationHandler')

	def setWalkSpeedNormal(self):
		self.controlManager.setSpeeds(OTPGlobals.ToonForwardSpeed, OTPGlobals.ToonJumpForce, OTPGlobals.ToonReverseSpeed, OTPGlobals.ToonRotateSpeed)

	def setWalkSpeedSlow(self):
		self.controlManager.setSpeeds(OTPGlobals.ToonForwardSlowSpeed, OTPGlobals.ToonJumpSlowForce, OTPGlobals.ToonReverseSlowSpeed, OTPGlobals.ToonRotateSlowSpeed)

	def setupCamera(self):
		base.disableMouse()
		base.camera.reparentTo(self)
		base.camera.setPos(0, -6.5 - max(self.height, 3.0), (self.height * (1.0/3.0)) + 2.2)
		base.camLens.setMinFov(OTPGlobals.DefaultCameraFov/(4./3.))
		
	def collisionsOff(self):
		self.controlManager.collisionsOff()

	def collisionsOn(self):
		self.controlManager.collisionsOn()

	def runSound(self):
		self.soundWalk.stop()
		base.playSfx(self.soundRun, looping=1)

	def walkSound(self):
		self.soundRun.stop()
		base.playSfx(self.soundWalk, looping=1)

	def stopSound(self):
		self.soundRun.stop()
		self.soundWalk.stop()

	def setMovementAnimation(self, loopName, playRate=1.0):
		if 'jump' in loopName:
			self.movingJumping = True
			self.movingForward = False
			self.movingNeutral = False
			self.movingRotation = False
			self.movingBackward = False
			self.stopSound()
		elif loopName == 'run':
			self.movingJumping = False
			self.movingForward = True
			self.movingNeutral = False
			self.movingRotation = False
			self.movingBackward = False
			self.runSound()
		elif loopName == 'walk':
			self.movingJumping = False
			self.movingForward = False
			self.movingNeutral = False
			if playRate == -1.0:
				self.movingBackward = True
				self.movingRotation = False
			else:
				self.movingBackward = False
				self.movingRotation = True
			self.walkSound()
		elif loopName == 'neutral':
			self.movingJumping = False
			self.movingForward = False
			self.movingNeutral = True
			self.movingRotation = False
			self.movingBackward = False
			self.stopSound()
		else:
			self.movingJumping = False
			self.movingForward = False
			self.movingNeutral = False
			self.movingRotation = False
			self.movingBackward = False
			self.stopSound()
		ActorInterval(self, loopName, playRate=playRate).loop()
			
	def handleAnimation(self, task):
		forward = KeyboardButton.up()
		backward = KeyboardButton.down()
		left = KeyboardButton.left()
		right = KeyboardButton.right()	
		control = KeyboardButton.control()
		keyPressed = base.mouseWatcherNode.is_button_down
		if keyPressed(control):
			if keyPressed(forward) or keyPressed(backward) or keyPressed(left) or keyPressed(right):
				if self.movingJumping == False:
					if self.physControls.isAirborne:
						self.setMovementAnimation('running-jump-idle')
					else:
						if keyPressed(forward):
							if self.movingForward == False:
								self.setMovementAnimation('run')
						elif keyPressed(backward):
							if self.movingBackward == False:
								self.setMovementAnimation('walk', playRate=-1.0)
						elif keyPressed(left) or keyPressed(right):
							if self.movingRotation == False:
								self.setMovementAnimation('walk')
				else:
					if not self.physControls.isAirborne:
						if keyPressed(forward):
							if self.movingForward == False:
								self.setMovementAnimation('run')
						elif keyPressed(backward):
							if self.movingBackward == False:
								self.setMovementAnimation('walk', playRate=-1.0)
						elif keyPressed(left) or keyPressed(right):
							if self.movingRotation == False:
								self.setMovementAnimation('walk')
			else:
				if self.movingJumping == False:
					if self.physControls.isAirborne:
						self.setMovementAnimation('jump-idle')
					else:
						if self.movingNeutral == False:
							self.setMovementAnimation('neutral')
				else:
					if not self.physControls.isAirborne:
						if self.movingNeutral == False:
							self.setMovementAnimation('neutral')
		elif keyPressed(forward) == 1:
			if self.movingForward == False:
				if not self.physControls.isAirborne:
					self.setMovementAnimation('run')
		elif keyPressed(backward) == 1:
			if self.movingBackward == False:
				if not self.physControls.isAirborne:
					self.setMovementAnimation('walk', playRate=-1.0)
		elif keyPressed(left) or keyPressed(right):
			if self.movingRotation == False:
				if not self.physControls.isAirborne:
					self.setMovementAnimation('walk')
		else:
			if not self.physControls.isAirborne:
				if self.movingNeutral == False:
					self.setMovementAnimation('neutral')
		return Task.cont

	def nextCameraPos(self, forward):
		if not self.avatarControlsEnabled:
			return
		self.wakeUp()
		self.__cameraHasBeenMoved = 1
		if forward:
			self.cameraIndex += 1
			if self.cameraIndex > len(self.cameraPositions) - 1:
				self.cameraIndex = 0
		else:
			self.cameraIndex -= 1
			if self.cameraIndex < 0:
				self.cameraIndex = len(self.cameraPositions) - 1
		self.setCameraPositionByIndex(self.cameraIndex)

	def initCameraPositions(self):
		camHeight = self.getClampedAvatarHeight()
		heightScaleFactor = camHeight * 0.3333333333
		defLookAt = Point3(0.0, 1.5, camHeight)
		scXoffset = 3.0
		scPosition = (Point3(scXoffset - 1, -10.0, camHeight + 5.0), Point3(scXoffset, 2.0, camHeight))
		self.cameraPositions = [(Point3(0.0, -9.0 * heightScaleFactor, camHeight),
		  defLookAt,
		  Point3(0.0, camHeight, camHeight * 4.0),
		  Point3(0.0, camHeight, camHeight * -1.0),
		  0),
		 (Point3(0.0, 0.7, camHeight),
		  defLookAt,
		  Point3(0.0, camHeight, camHeight * 1.33),
		  Point3(0.0, camHeight, camHeight * 0.66),
		  1),
		 (Point3(5.7 * heightScaleFactor, 7.65 * heightScaleFactor, camHeight + 2.0),
		  Point3(0.0, 1.0, camHeight),
		  Point3(0.0, 1.0, camHeight * 4.0),
		  Point3(0.0, 1.0, camHeight * -1.0),
		  0),
		 (Point3(0.0, 8.65 * heightScaleFactor, camHeight),
		  Point3(0.0, 1.0, camHeight),
		  Point3(0.0, 1.0, camHeight * 4.0),
		  Point3(0.0, 1.0, camHeight * -1.0),
		  0),
		 (Point3(-camHeight * 3, 0.0, camHeight),
		  Point3(0.0, 0.0, camHeight),
		  Point3(0.0, camHeight, camHeight * 1.1),
		  Point3(0.0, camHeight, camHeight * 0.9),
		  1),
		 (Point3(camHeight * 3, 0.0, camHeight),
		  Point3(0.0, 0.0, camHeight),
		  Point3(0.0, camHeight, camHeight * 1.1),
		  Point3(0.0, camHeight, camHeight * 0.9),
		  1),
		 (Point3(0.0, -24.0 * heightScaleFactor, camHeight + 4.0),
		  defLookAt,
		  Point3(0.0, 1.5, camHeight * 4.0),
		  Point3(0.0, 1.5, camHeight * -1.0),
		  0),
		 (Point3(0.0, -12.0 * heightScaleFactor, camHeight + 4.0),
		  defLookAt,
		  Point3(0.0, 1.5, camHeight * 4.0),
		  Point3(0.0, 1.5, camHeight * -1.0),
		  0)] + self.auxCameraPositions
		if self.wantDevCameraPositions:
			self.cameraPositions += [(Point3(0.0, 0.0, camHeight * 3),
			  Point3(0.0, 0.0, 0.0),
			  Point3(0.0, camHeight * 2, 0.0),
			  Point3(0.0, -camHeight * 2, 0.0),
			  1),
			 (Point3(camHeight * 3, 0.0, camHeight),
			  Point3(0.0, 0.0, camHeight),
			  Point3(0.0, camHeight, camHeight * 1.1),
			  Point3(0.0, camHeight, camHeight * 0.9),
			  1),
			 (Point3(camHeight * 3, 0.0, 0.0),
			  Point3(0.0, 0.0, camHeight),
			  Point3(0.0, camHeight, camHeight * 1.1),
			  Point3(0.0, camHeight, camHeight * 0.9),
			  1),
			 (Point3(-camHeight * 3, 0.0, camHeight),
			  Point3(0.0, 0.0, camHeight),
			  Point3(0.0, camHeight, camHeight * 1.1),
			  Point3(0.0, camHeight, camHeight * 0.9),
			  1),
			 (Point3(0.0, -60, 60),
			  defLookAt + Point3(0, 15, 0),
			  defLookAt + Point3(0, 15, 0),
			  defLookAt + Point3(0, 15, 0),
			  1),
			 (Point3(0.0, -20, 20),
			  defLookAt + Point3(0, 5, 0),
			  defLookAt + Point3(0, 5, 0),
			  defLookAt + Point3(0, 5, 0),
			  1)]


