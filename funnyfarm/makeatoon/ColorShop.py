from pandac.PandaModules import *
from direct.gui.DirectGui import *
from MakeAToonGlobals import *
from toontown.toonbase import TTLocalizer
from funnyfarm.toon.LocalToon import LocalToon
from funnyfarm.toon.ToonGlobals import *

class ColorShop:
	
	def __init__(self):
		self.toon = None
		self.headColor = 0
		self.armColor = 0
		self.legColor = 0
		
	def enter(self, toon):
		self.toon = toon
		self.headColor = self.toon.getHeadColor()
		self.armColor = self.toon.getTorsoColor()
		self.legColor = self.toon.getLegColor()
		self.updateScrollButtons(self.headColor, self.allLButton, self.allRButton)
		self.updateScrollButtons(self.headColor, self.headLButton, self.headRButton)
		self.updateScrollButtons(self.armColor, self.armLButton, self.armRButton)
		self.updateScrollButtons(self.legColor, self.legLButton, self.legRButton)
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
		self.toonFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.073), hpr=(0, 0, 0), scale=1.3, frameColor=(1, 1, 1, 1), text=TTLocalizer.ColorShopToon, text_scale=TTLocalizer.CStoonFrame, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.allLButton = DirectButton(parent=self.toonFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapAllColor, extraArgs=[-1])
		self.allRButton = DirectButton(parent=self.toonFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapAllColor, extraArgs=[1])
		self.headFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.3), hpr=(0, 0, 2), scale=0.9, frameColor=(1, 1, 1, 1), text=TTLocalizer.ColorShopHead, text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.headLButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapHeadColor, extraArgs=[-1])
		self.headRButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapHeadColor, extraArgs=[1])
		self.bodyFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonScale, relief=None, pos=(0, 0, -0.5), hpr=(0, 0, -2), scale=0.9, frameColor=(1, 1, 1, 1), text=TTLocalizer.ColorShopBody, text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.armLButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapArmColor, extraArgs=[-1])
		self.armRButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapArmColor, extraArgs=[1])
		self.legsFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.7), hpr=(0, 0, 3), scale=0.9, frameColor=(1, 1, 1, 1), text=TTLocalizer.ColorShopLegs, text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.legLButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapLegColor, extraArgs=[-1])
		self.legRButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapLegColor, extraArgs=[1])
		self.parentFrame.hide()
		return

	def unload(self):
		self.gui.removeNode()
		del self.gui
		self.parentFrame.destroy()
		self.toonFrame.destroy()
		self.headFrame.destroy()
		self.bodyFrame.destroy()
		self.legsFrame.destroy()
		self.headLButton.destroy()
		self.headRButton.destroy()
		self.armLButton.destroy()
		self.armRButton.destroy()
		self.legLButton.destroy()
		self.legRButton.destroy()
		self.allLButton.destroy()
		self.allRButton.destroy()
		del self.parentFrame
		del self.toonFrame
		del self.headFrame
		del self.bodyFrame
		del self.legsFrame
		del self.headLButton
		del self.headRButton
		del self.armLButton
		del self.armRButton
		del self.legLButton
		del self.legRButton
		del self.allLButton
		del self.allRButton
		
	def updateScrollButtons(self, value, button1, button2):
		if value == 0:
			button1['state'] = DGG.DISABLED
			button2['state'] = DGG.NORMAL
		elif value == 25:
			button1['state'] = DGG.NORMAL
			button2['state'] = DGG.DISABLED
		else:
			button1['state'] = DGG.NORMAL
			button2['state'] = DGG.NORMAL
			
	def __swapAllColor(self, offset):
		length = len(MATColorsList)
		self.headColor = (self.headColor + offset) % length
		self.armColor = self.headColor
		self.legColor = self.headColor
		self.toon.setColorAll(self.headColor, mat=True)
		self.updateScrollButtons(self.headColor, self.allLButton, self.allRButton)
		self.updateScrollButtons(self.headColor, self.headLButton, self.headRButton)
		self.updateScrollButtons(self.armColor, self.armLButton, self.armRButton)
		self.updateScrollButtons(self.legColor, self.legLButton, self.legRButton)
			
	def __swapHeadColor(self, offset):
		length = len(MATColorsList)
		self.headColor = (self.headColor + offset) % length
		self.toon.setHeadColor(self.headColor, mat=True)
		self.updateScrollButtons(self.headColor, self.headLButton, self.headRButton)
		self.updateScrollButtons(self.headColor, self.allLButton, self.allRButton)
		
	def __swapArmColor(self, offset):
		length = len(MATColorsList)
		self.armColor = (self.armColor + offset) % length
		self.toon.setTorsoColor(self.armColor, mat=True)
		self.updateScrollButtons(self.armColor, self.armLButton, self.armRButton)
		
	def __swapLegColor(self, offset):
		length = len(MATColorsList)
		self.legColor = (self.legColor + offset) % length
		self.toon.setLegColor(self.legColor, mat=True)
		self.updateScrollButtons(self.legColor, self.legLButton, self.legRButton)


