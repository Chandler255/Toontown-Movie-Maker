from pandac.PandaModules import *
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from MakeAToonGlobals import *
from direct.directnotify import DirectNotifyGlobal
from funnyfarm.toon import ToonGlobals
from funnyfarm.toon.LocalToon import LocalToon
import random

class GenderShop:
	
	def __init__(self, makeAToon):
		self.gender = 'm'
		self.toon = None
		self.makeAToon = makeAToon
		
	def enter(self):
		self.boyButton.show()
		self.girlButton.show()
		
	def exit(self):
		self.boyButton.hide()
		self.girlButton.hide()
		
	def load(self):
		gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam')
		guiBoyUp = gui.find('**/tt_t_gui_mat_boyUp')
		guiBoyDown = gui.find('**/tt_t_gui_mat_boyDown')
		guiGirlUp = gui.find('**/tt_t_gui_mat_girlUp')
		guiGirlDown = gui.find('**/tt_t_gui_mat_girlDown')
		self.boyButton = DirectButton(relief=None, image=(guiBoyUp,
		 guiBoyDown,
		 guiBoyUp,
		 guiBoyDown), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.4, 0, -0.8), command=self.createRandomBoy, text=('',
		 TTLocalizer.GenderShopBoyButtonText,
		 TTLocalizer.GenderShopBoyButtonText,
		 ''), text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.08, text_pos=(0, 0.19), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
		self.boyButton.hide()
		self.boyButton.setPos(-0.45, 0, 0.19)
		self.boyButton.reparentTo(base.a2dBottomCenter)
		self.girlButton = DirectButton(relief=None, image=(guiGirlUp,
		 guiGirlDown,
		 guiGirlUp,
		 guiGirlDown), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(0.4, 0, -0.8), command=self.createRandomGirl, text=('',
		 TTLocalizer.GenderShopGirlButtonText,
		 TTLocalizer.GenderShopGirlButtonText,
		 ''), text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.08, text_pos=(0, 0.19), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
		self.girlButton.hide()
		self.girlButton.setPos(0.45, 0, 0.19)
		self.girlButton.reparentTo(base.a2dBottomCenter)
		gui.removeNode()
		del gui
		return

	def unload(self):
		self.boyButton.destroy()
		self.girlButton.destroy()
		del self.boyButton
		del self.girlButton
		if self.toon:
			self.toon.destroy()
		self.makeAToon = None
		return
	
	def createRandomBoy(self):
		self._createRandomToon('m')

	def createRandomGirl(self):
		self._createRandomToon('f')

	def _createRandomToon(self, gender):
		if self.toon:
			self.toon.destroy()
		self.toon = LocalToon()
		self.toon.generateRandomToon(gender)
		self.makeAToon.setToon(self.toon)
		self.makeAToon.guiNextButton['state'] = DGG.NORMAL

