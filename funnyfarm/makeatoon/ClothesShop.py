from pandac.PandaModules import *
from direct.gui.DirectGui import *
from MakeAToonGlobals import *
from toontown.toonbase import TTLocalizer
from funnyfarm.toon.ToonGlobals import *

class ClothesShop:
	
	def __init__(self):
		self.toon = None
		self.shirt = 0
		self.sleeve = 0
		self.shorts = 0
		self.shirtColor = 0
		self.sleeveColor = 0
		self.shortsColor = 0
		
	def enter(self, toon):
		self.toon = toon
		self.gender = self.toon.getGender()
		self.shirt = self.toon.getShirt()
		self.sleeve = self.toon.getShirt()
		self.shorts = self.toon.getShorts()
		self.shirtColor = self.toon.getShirtColor()
		self.sleeveColor = self.toon.getShirtColor()
		self.shortsColor = self.toon.getShortsColor()
		if self.gender == 'shorts':
			self.bottomFrame['text'] = TTLocalizer.ClothesShopShorts
		else:
			self.bottomFrame['text'] = TTLocalizer.ClothesShopBottoms
		self.parentFrame.show()
		
	def exit(self):
		del self.toon
		self.parentFrame.hide()
	
	def load(self):
		self.gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam')
		guiRArrowUp = self.gui.find('**/tt_t_gui_mat_arrowUp')
		guiRArrowRollover = self.gui.find('**/tt_t_gui_mat_arrowUp')
		guiRArrowDown = self.gui.find('**/tt_t_gui_mat_arrowDown')
		guiRArrowDisabled = self.gui.find('**/tt_t_gui_mat_arrowDisabled')
		shuffleFrame = self.gui.find('**/tt_t_gui_mat_shuffleFrame')
		shuffleArrowUp = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
		shuffleArrowDown = self.gui.find('**/tt_t_gui_mat_shuffleArrowDown')
		shuffleArrowRollover = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
		shuffleArrowDisabled = self.gui.find('**/tt_t_gui_mat_shuffleArrowDisabled')
		self.parentFrame = DirectFrame(relief=DGG.RAISED, pos=(0.98, 0, 0.416), frameColor=(1, 0, 0, 0))
		self.parentFrame.setPos(-0.36, 0, -0.5)
		self.parentFrame.reparentTo(base.a2dTopRight)
		self.shirtFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.4), hpr=(0, 0, 3), scale=1.2, frameColor=(1, 1, 1, 1), text=TTLocalizer.ClothesShopShirt, text_scale=0.0575, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.topLButton = DirectButton(parent=self.shirtFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), extraArgs=[-1])
		self.topRButton = DirectButton(parent=self.shirtFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), extraArgs=[1])
		self.bottomFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.65), hpr=(0, 0, -2), scale=1.2, frameColor=(1, 1, 1, 1), text='', text_scale=0.0575, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.bottomLButton = DirectButton(parent=self.bottomFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), extraArgs=[-1])
		self.bottomRButton = DirectButton(parent=self.bottomFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), extraArgs=[1])
		self.parentFrame.hide()
		return

	def unload(self):
		self.gui.removeNode()
		del self.gui
		self.parentFrame.destroy()
		self.shirtFrame.destroy()
		self.bottomFrame.destroy()
		self.topLButton.destroy()
		self.topRButton.destroy()
		self.bottomLButton.destroy()
		self.bottomRButton.destroy()
		del self.parentFrame
		del self.shirtFrame
		del self.bottomFrame
		del self.topLButton
		del self.topRButton
		del self.bottomLButton
		del self.bottomRButton




