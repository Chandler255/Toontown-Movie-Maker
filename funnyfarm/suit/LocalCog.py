from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.task.Task import Task
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.gui.DirectGui import *
import sys
from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.task.Task import Task
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.gui.DirectGui import *
import sys
	
class LocalCog:
	def __init__(self,setType,setSuit,b_setAnimState,x,y,z,h,p,r,scale):
		self.setType = setType
		self.setSuit = setSuit
		self.b_setAnimState = b_setAnimState
		self.x = x
		self.y = y
		self.z = z
		self.h = h
		self.p = p
		self.r = r
		self.scale = scale
	def buildCog(self):
		self.sellBody = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
		self.sellArm = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
		self.sellLeg = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
		self.cashBody = loader.loadTexture('phase_3.5/maps/m_blazer.jpg')
		self.cashArm = loader.loadTexture('phase_3.5/maps/m_sleeve.jpg')
		self.cashLeg = loader.loadTexture('phase_3.5/maps/m_leg.jpg')
		self.lawBody = loader.loadTexture('phase_3.5/maps/l_blazer.jpg')
		self.lawArm = loader.loadTexture('phase_3.5/maps/l_sleeve.jpg')
		self.lawLeg = loader.loadTexture('phase_3.5/maps/l_leg.jpg')
		self.bossBody = loader.loadTexture('phase_3.5/maps/c_blazer.jpg')
		self.bossArm = loader.loadTexture('phase_3.5/maps/c_sleeve.jpg')
		self.bossLeg = loader.loadTexture('phase_3.5/maps/c_leg.jpg')
		self.salesIcon = loader.loadModel('phase_4/models/minigames/salesIcon.bam')
		self.moneyIcon = loader.loadModel('phase_4/models/minigames/moneyIcon.bam')
		self.legalIcon = loader.loadModel('phase_4/models/minigames/legalIcon.bam')
		self.corpIcon = loader.loadModel('phase_4/models/minigames/corpIcon.bam')
		self.suitA = Actor('phase_3.5/models/char/suitA-mod.bam',{
			'neutral':'phase_4/models/char/suitA-neutral.bam'})
		self.suitB = Actor('phase_3.5/models/char/suitB-mod.bam',{
			'neutral':'phase_4/models/char/suitB-neutral.bam'})
		self.suitC = Actor('phase_3.5/models/char/suitC-mod.bam',{
			'neutral':'phase_3.5/models/char/suitC-neutral.bam'})
		self.shadowtex = loader.loadTexture('phase_3/maps/drop-shadow.jpg', 'phase_3/maps/drop-shadow_a.rgb')
		self.shadowcm = CardMaker('shadow')
		self.shadowcm.setFrame(2, -2, 2, -2)
		self.shadow1 = render.attachNewNode(self.shadowcm.generate())
		self.jointshadow1 = self.suitA.find('**/joint_shadow')
		self.shadow1.reparentTo(self.jointshadow1)
		self.shadow1.setTexture(self.shadowtex)
		self.shadow1.setP(270)
		self.shadow1.setTransparency(True)
		self.shadow1.setBin('fixed', 40)
		self.shadow1.setColor(1, 1, 1, 0.45)
		self.jointshadow1.setBin('fixed', 50)
		self.shadow2 = render.attachNewNode(self.shadowcm.generate())
		self.jointshadow2 = self.suitB.find('**/joint_shadow')
		self.shadow2.reparentTo(self.jointshadow2)
		self.shadow2.setTexture(self.shadowtex)
		self.shadow2.setP(270)
		self.shadow2.setTransparency(True)
		self.shadow2.setBin('fixed', 40)
		self.shadow2.setColor(1, 1, 1, 0.45)
		self.jointshadow2.setBin('fixed', 50)
		self.shadow3 = render.attachNewNode(self.shadowcm.generate())
		self.jointshadow3 = self.suitC.find('**/joint_shadow')
		self.shadow3.reparentTo(self.jointshadow3)
		self.shadow3.setTexture(self.shadowtex)
		self.shadow3.setP(270)
		self.shadow3.setTransparency(True)
		self.shadow3.setBin('fixed', 40)
		self.shadow3.setColor(1, 1, 1, 0.45)
		self.jointshadow3.setBin('fixed', 50)
		if self.setType == 'a':
			self.suitA.reparentTo(render)
			self.suitA.setX(self.x)
			self.suitA.setY(self.y)
			self.suitA.setZ(self.z)
			self.suitA.setH(self.h)
			self.suitA.setP(self.p)
			self.suitA.setR(self.r)
			self.suitA.setScale(self.scale)
		if self.setType == 'b':
			self.suitB.reparentTo(render)
			self.suitB.setX(self.x)
			self.suitB.setY(self.y)
			self.suitB.setZ(self.z)
			self.suitB.setH(self.h)
			self.suitB.setP(self.p)
			self.suitB.setR(self.r)
			self.suitB.setScale(self.scale)
		if self.setType == 'c':
			self.suitC.reparentTo(render)
			self.suitC.setX(self.x)
			self.suitC.setY(self.y)
			self.suitC.setZ(self.z)
			self.suitC.setH(self.h)
			self.suitC.setP(self.p)
			self.suitC.setR(self.r)
			self.suitC.setScale(self.scale)
		if self.setSuit == 'sb':
			self.suitA.findAllMatches('**/torso').setTexture(self.sellBody, 1)
			self.suitA.findAllMatches('**/legs').setTexture(self.sellLeg, 1)
			self.suitA.findAllMatches('**/arms').setTexture(self.sellArm, 1)
			self.suitB.findAllMatches('**/torso').setTexture(self.sellBody, 1)
			self.suitB.findAllMatches('**/legs').setTexture(self.sellLeg, 1)
			self.suitB.findAllMatches('**/arms').setTexture(self.sellArm, 1)
			self.suitC.findAllMatches('**/torso').setTexture(self.sellBody, 1)
			self.suitC.findAllMatches('**/legs').setTexture(self.sellLeg, 1)
			self.suitC.findAllMatches('**/arms').setTexture(self.sellArm, 1)
			self.salesIcon.reparentTo(self.suitA.find('**/joint_attachMeter'))
			self.salesIcon.setScale(.6)
			self.salesIcon.setPosHpr(0,.03,.17,180,0,0)
			self.salesIcon2 = self.salesIcon.copyTo(self.suitB.find('**/joint_attachMeter'))
			self.salesIcon2.setScale(.5)
			self.salesIcon2.setPosHpr(0,.03,.17,180,0,0)
			self.salesIcon3 = self.salesIcon.copyTo(self.suitC.find('**/joint_attachMeter'))
			self.salesIcon3.setScale(.6)
			self.salesIcon3.setPosHpr(0,.03,.17,180,0,0)
		if self.setSuit == 'cb':
			self.suitA.findAllMatches('**/torso').setTexture(self.cashBody, 1)
			self.suitA.findAllMatches('**/legs').setTexture(self.cashLeg, 1)
			self.suitA.findAllMatches('**/arms').setTexture(self.cashArm, 1)
			self.suitB.findAllMatches('**/torso').setTexture(self.cashBody, 1)
			self.suitB.findAllMatches('**/legs').setTexture(self.cashLeg, 1)
			self.suitB.findAllMatches('**/arms').setTexture(self.cashArm, 1)
			self.suitC.findAllMatches('**/torso').setTexture(self.cashBody, 1)
			self.suitC.findAllMatches('**/legs').setTexture(self.cashLeg, 1)
			self.suitC.findAllMatches('**/arms').setTexture(self.cashArm, 1)
			self.moneyIcon.reparentTo(self.suitA.find('**/joint_attachMeter'))
			self.moneyIcon.setScale(.6)
			self.moneyIcon.setPosHpr(0,.03,.17,180,0,0)
			self.moneyIcon2 = self.moneyIcon.copyTo(self.suitB.find('**/joint_attachMeter'))
			self.moneyIcon2.setScale(.5)
			self.moneyIcon2.setPosHpr(0,.03,.17,180,0,0)
			self.moneyIcon3 = self.moneyIcon.copyTo(self.suitC.find('**/joint_attachMeter'))
			self.moneyIcon3.setScale(.6)
			self.moneyIcon3.setPosHpr(0,.03,.17,180,0,0)
		if self.setSuit == 'lb':
			self.suitA.findAllMatches('**/torso').setTexture(self.lawBody, 1)
			self.suitA.findAllMatches('**/legs').setTexture(self.lawLeg, 1)
			self.suitA.findAllMatches('**/arms').setTexture(self.lawArm, 1)
			self.suitB.findAllMatches('**/torso').setTexture(self.lawBody, 1)
			self.suitB.findAllMatches('**/legs').setTexture(self.lawLeg, 1)
			self.suitB.findAllMatches('**/arms').setTexture(self.lawArm, 1)
			self.suitC.findAllMatches('**/torso').setTexture(self.lawBody, 1)
			self.suitC.findAllMatches('**/legs').setTexture(self.lawLeg, 1)
			self.suitC.findAllMatches('**/arms').setTexture(self.lawArm, 1)
			self.legalIcon.reparentTo(self.suitA.find('**/joint_attachMeter'))
			self.legalIcon.setScale(.6)
			self.legalIcon.setPosHpr(0,.03,.17,180,0,0)
			self.legalIcon2 = self.legalIcon.copyTo(self.suitB.find('**/joint_attachMeter'))
			self.legalIcon2.setScale(.5)
			self.legalIcon2.setPosHpr(0,.03,.17,180,0,0)
			self.legalIcon3 = self.legalIcon.copyTo(self.suitC.find('**/joint_attachMeter'))
			self.legalIcon3.setScale(.6)
			self.legalIcon3.setPosHpr(0,.03,.17,180,0,0)
		if self.setSuit == 'bb':
			self.suitA.findAllMatches('**/torso').setTexture(self.bossBody, 1)
			self.suitA.findAllMatches('**/legs').setTexture(self.bossLeg, 1)
			self.suitA.findAllMatches('**/arms').setTexture(self.bossArm, 1)
			self.suitB.findAllMatches('**/torso').setTexture(self.bossBody, 1)
			self.suitB.findAllMatches('**/legs').setTexture(self.bossLeg, 1)
			self.suitB.findAllMatches('**/arms').setTexture(self.bossArm, 1)
			self.suitC.findAllMatches('**/torso').setTexture(self.bossBody, 1)
			self.suitC.findAllMatches('**/legs').setTexture(self.bossLeg, 1)
			self.suitC.findAllMatches('**/arms').setTexture(self.bossArm, 1)
			self.corpIcon.reparentTo(self.suitA.find('**/joint_attachMeter'))
			self.corpIcon.setScale(.6)
			self.corpIcon.setPosHpr(0,.03,.17,180,0,0)
			self.corpIcon2 = self.corpIcon.copyTo(self.suitB.find('**/joint_attachMeter'))
			self.corpIcon2.setScale(.5)
			self.corpIcon2.setPosHpr(0,.03,.17,180,0,0)
			self.corpIcon3 = self.corpIcon.copyTo(self.suitC.find('**/joint_attachMeter'))
			self.corpIcon3.setScale(.6)
			self.corpIcon3.setPosHpr(0,.03,.17,180,0,0)
		if self.b_setAnimState == 'neutral':
			self.suitA.actorInterval('neutral').loop()
			self.suitB.actorInterval('neutral').loop()
			self.suitC.actorInterval('neutral').loop()
	def removeSuit(self):
		self.suitA.cleanup()
		self.suitA.removeNode()
		del self.suitA
		self.suitB.cleanup()
		self.suitB.removeNode()
		del self.suitB
		self.suitC.cleanup()
		self.suitC.removeNode()
		del self.suitC
