from pandac.PandaModules import *
from direct.gui.DirectGui import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from MakeAToonGlobals import *
from funnyfarm.toon.ToonGlobals import *

class BodyShop:
	
	def __init__(self):
		self.toon = None
		self.torsoChoice = 0
		self.legChoice = 0
		self.speciesChoice = 0
		return
	
	def enter(self, toon):
		self.toon = toon
		self.gender = self.toon.getGender()
		self.speciesChoice = self.toon.getSpecies()
		self.torsoChoice = self.toon.getTorsoType()
		self.legChoice = self.toon.getLegType()
		self.updateSpeciesButtons()
		self.updateTorsoButtons()
		self.updateLegButtons()
		self.parentFrame.show()
		
	def exit(self):
		del self.toon
		self.parentFrame.hide()
	
	def load(self):
		self.gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam')
		guiRArrowUp = self.gui.find('**/tt_t_gui_mat_arrowUp')
		guiRArrowDown = self.gui.find('**/tt_t_gui_mat_arrowDown')
		guiRArrowRollover = self.gui.find('**/tt_t_gui_mat_arrowUp')
		guiRArrowDisabled = self.gui.find('**/tt_t_gui_mat_arrowDisabled')
		shuffleFrame = self.gui.find('**/tt_t_gui_mat_shuffleFrame')
		shuffleArrowUp = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
		shuffleArrowDown = self.gui.find('**/tt_t_gui_mat_shuffleArrowDown')
		shuffleArrowRollover = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
		shuffleArrowDisabled = self.gui.find('**/tt_t_gui_mat_shuffleArrowDisabled')
		self.parentFrame = DirectFrame(relief=DGG.RAISED, pos=(0.98, 0, 0.416), frameColor=(1, 0, 0, 0))
		self.parentFrame.setPos(-0.36, 0, -0.5)
		self.parentFrame.reparentTo(base.a2dTopRight)
		self.speciesFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.073), hpr=(0, 0, 0), scale=1.3, frameColor=(1, 1, 1, 1), text='Species', text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.speciesLButton = DirectButton(parent=self.speciesFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapSpecies, extraArgs=[-1])
		self.speciesRButton = DirectButton(parent=self.speciesFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapSpecies, extraArgs=[1])
		self.bodyFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonScale, relief=None, pos=(0, 0, -0.5), hpr=(0, 0, -2), scale=0.9, frameColor=(1, 1, 1, 1), text=TTLocalizer.BodyShopBody, text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.torsoLButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapTorso, extraArgs=[-1])
		self.torsoRButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapTorso, extraArgs=[1])
		self.legsFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.7), hpr=(0, 0, 3), scale=0.9, frameColor=(1, 1, 1, 1), text=TTLocalizer.BodyShopLegs, text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
		self.legLButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapLegs, extraArgs=[-1])
		self.legRButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
		 shuffleArrowDown,
		 shuffleArrowRollover,
		 shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapLegs, extraArgs=[1])
		self.parentFrame.hide()
		return

	def unload(self):
		self.gui.removeNode()
		del self.gui
		self.parentFrame.destroy()
		self.speciesFrame.destroy()
		self.bodyFrame.destroy()
		self.legsFrame.destroy()
		self.speciesLButton.destroy()
		self.speciesRButton.destroy()
		self.torsoLButton.destroy()
		self.torsoRButton.destroy()
		self.legLButton.destroy()
		self.legRButton.destroy()
		del self.parentFrame
		del self.speciesFrame
		del self.bodyFrame
		del self.legsFrame
		del self.speciesLButton
		del self.speciesRButton
		del self.torsoLButton
		del self.torsoRButton
		del self.legLButton
		del self.legRButton
		
	def updateSpeciesButtons(self):
		if self.speciesChoice == 0:
			self.speciesLButton['state'] = DGG.DISABLED
			self.speciesRButton['state'] = DGG.NORMAL
		elif self.speciesChoice == 8:
			self.speciesLButton['state'] = DGG.NORMAL
			self.speciesRButton['state'] = DGG.DISABLED
		else:
			self.speciesLButton['state'] = DGG.NORMAL
			self.speciesRButton['state'] = DGG.NORMAL
			
	def updateTorsoButtons(self):
		if self.torsoChoice == 0:
			self.torsoLButton['state'] = DGG.DISABLED
			self.torsoRButton['state'] = DGG.NORMAL
		elif self.torsoChoice == 2:
			self.torsoLButton['state'] = DGG.NORMAL
			self.torsoRButton['state'] = DGG.DISABLED
		else:
			self.torsoLButton['state'] = DGG.NORMAL
			self.torsoRButton['state'] = DGG.NORMAL
			
	def updateLegButtons(self):
		if self.legChoice == 0:
			self.legLButton['state'] = DGG.DISABLED
			self.legRButton['state'] = DGG.NORMAL
		elif self.legChoice == 2:
			self.legLButton['state'] = DGG.NORMAL
			self.legRButton['state'] = DGG.DISABLED
		else:
			self.legLButton['state'] = DGG.NORMAL
			self.legRButton['state'] = DGG.NORMAL
		
	def __swapSpecies(self, offset):
		length = len(toonSpeciesTypes)
		self.speciesChoice = (self.speciesChoice + offset) % length
		self.toon.swapSpecies(toonSpeciesTypes[self.speciesChoice])
		self.updateSpeciesButtons()
		
	def __swapTorso(self, offset):
		length = len(toonBodyTypes)
		self.torsoChoice = (self.torsoChoice + offset) % length
		self.toon.swapTorso(toonBodyTypes[self.torsoChoice])
		self.updateTorsoButtons()
			
	def __swapLegs(self, offset):
		length = len(toonBodyTypes)
		self.legChoice = (self.legChoice + offset) % length
		self.toon.swapLegs(toonBodyTypes[self.legChoice])
		self.updateLegButtons()



