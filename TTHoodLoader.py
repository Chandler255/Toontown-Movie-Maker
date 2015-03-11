from pandac.PandaModules import *

from direct.actor.Actor import Actor
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.gui.DirectGui import *

class TTHoodLoader:
	def __init__(self, model, sfx):
		self.model = model
		self.sfx = sfx
	
	def load(self):
		self.tthood = loader.loadModel(self.model)
		self.tthood.reparentTo(render)
		self.tthoodsfx = loader.loadSfx(self.sfx)
		self.tthoodsfx.setLoop(1)
		self.tthoodsfx.play()
	
	def unload(self):
		self.tthood.removeNode()
		del self.tthood
		self.tthoodsfx.stop()
		
		
