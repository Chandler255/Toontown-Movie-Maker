from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.actor.Actor import Actor
from direct.task import Task
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.directnotify.DirectNotifyGlobal import *

class BattleCogsQ1():
	def __init__(self):
		self.cog = Actor('phase_3.5/models/char/suitA-mod.bam', 
			{'neutral':'phase_4/models/char/suitA-neutral.bam', 
			'walk':'phase_4/models/char/suitA-walk.bam', 
			'pie-hit':'phase_4/models/char/suitA-pie-small.bam'})
		self.cog.reparentTo(render)
		self.cog.actorInterval('walk').loop()
		self.cog.setPos(-81.55,-87.25,0)
		self.pos1 = self.cog.posInterval(5,(-81.55,-43,0),(-81.55,-87.25,0))
		self.hpr1 = self.cog.hprInterval(5,(0,0,0), (0,0,0))
		self.pos2 = self.cog.posInterval(15, (80,-43,0), (-81.55,-43,0))
		self.hpr2 = self.cog.hprInterval(15, (270,0,0), (270,0,0))
		self.pos3 = self.cog.posInterval(4, (80,-29,0), (80,-43,0))
		self.hpr3 = self.cog.hprInterval(4, (0,0,0), (0,0,0))
		self.pos4 = self.cog.posInterval(15, (-90,-29,0), (80,-29,0))
		self.hpr4 = self.cog.hprInterval(15, (90,0,0), (90,0,0))
		self.pos5 = self.cog.posInterval(7, (-90,-87.25,0), (-90,-29,0))
		self.hpr5 = self.cog.hprInterval(7, (180,0,0), (180,0,0))
		self.pos6 = self.cog.posInterval(2, (-81.55,-87.25,0), (-90,-87.25,0))
		self.hpr6 = self.cog.hprInterval(2, (270,0,0), (270,0,0))
		self.posSeq = Sequence(self.pos1,self.pos2,self.pos3,self.pos4,self.pos5,self.pos6)
		self.hprSeq = Sequence(self.hpr1,self.hpr2,self.hpr3,self.hpr4,self.hpr5,self.hpr6)
		self.posSeq.loop()
		self.hprSeq.loop()
		self.cogHead = loader.loadModel('phase_4/models/char/suitA-heads.bam').find('**/bigcheese')
		self.cogHead.reparentTo(self.cog.find('**/joint_head'))
	
	
