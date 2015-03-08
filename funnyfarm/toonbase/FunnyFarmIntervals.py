from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *

#In progress. Do not edit.

class IntervalManager:
	def __init__(self, sfxMgr):
		self.sfxMgr = sfxMgr

	def loadDoorInterval(self, localAvatar, door, pos1, pos2, h, p, r, loadFunc, unloadFunc):
		self.localAvatar = localAvatar
		self.door = door
		self.pos1 = pos1
		self.pos2 = pos2
		self.h = h
		self.p = p
		self.r = r
		self.loadFunc = loadFunc
		self.unloadFunc = unloadFunc
		Sequence(Func(self.startDoorMovement), Wait(0.7), Func(self.pause), Wait(0.7), Func(self.finishDoorMovement), Wait(0.2), Func(base.transitions.irisOut), Wait(0.5), Func(self.loadFunc), Func(unloadFunc)).start()
	
	def startDoorMovement(self):
		self.localAvatar.disableControls()
		self.localAvatar.collisionsOff()
		self.localAvatar.posInterval(0.7, self.pos1, blendType='easeIn')
		self.localAvatar.setHpr(self.h, self.p, self.r)
		self.localAvatar.setAnimState('walk', startFrame=5, playRate=-1.0)
		self.door.hprInterval(0.7, (90, 0, 0)).start()
		self.sfxMgr.doorOpen.play()
		
	def pause(self):
		self.localAvatar.setAnimState('neutral')

	def finishDoorMovement(self):
		self.localAvatar.posInterval(0.7, self.pos2)
		self.localAvatar.setAnimState('walk')
		
		


