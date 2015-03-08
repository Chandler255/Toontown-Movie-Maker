from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.gui import OnscreenText
from MakeAToonGlobals import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase.ToontownGlobals import *

class NameShop:

	def __init__(self):
		self.pickANameGUIElements = []
		self.typeANameGUIElements = []

	def enter(self, toon):
		self.toon = toon
		self.ubershow(self.typeANameGUIElements)

	def exit(self):
		del self.toon
		self.uberhide(self.typeANameGUIElements)
		self.nameEntry.enterText('')

	def load(self):
		nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input.bam')
		guiButton = loader.loadModel('phase_3/models/gui/quit_button.bam')
		gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop.bam')
		self.arrowUp = gui.find('**/tt_t_gui_mat_namePanelArrowUp')
		self.arrowDown = gui.find('**/tt_t_gui_mat_namePanelArrowDown')
		self.arrowHover = gui.find('**/tt_t_gui_mat_namePanelArrowHover')
		self.squareUp = gui.find('**/tt_t_gui_mat_namePanelSquareUp')
		self.squareDown = gui.find('**/tt_t_gui_mat_namePanelSquareDown')
		self.squareHover = gui.find('**/tt_t_gui_mat_namePanelSquareHover')
		typePanel = gui.find('**/tt_t_gui_mat_typeNamePanel')
		self.typeNamePanel = DirectFrame(parent=aspect2d, image=None, relief='flat', scale=(0.75, 0.7, 0.7), state='disabled', pos=(-0.0163333, 0, 0.075), image_pos=(0, 0, 0.025), frameColor=(1, 1, 1, 0))
		self.typePanelFrame = DirectFrame(image=typePanel, relief='flat', frameColor=(1, 1, 1, 0), pos=(-0.008, 0, 0.019))
		self.typePanelFrame.reparentTo(self.typeNamePanel, sort=1)
		self.typeANameGUIElements.append(self.typeNamePanel)
		self.typeANameGUIElements.append(self.typePanelFrame)
		self.nameLabel = OnscreenText.OnscreenText(TTLocalizer.PleaseTypeName, parent=aspect2d, style=OnscreenText.ScreenPrompt, scale=TTLocalizer.NSnameLabel, pos=(-0.0163333, 0.53))
		self.nameLabel.wrtReparentTo(self.typeNamePanel, sort=2)
		self.typeANameGUIElements.append(self.nameLabel)
		self.typeNotification = OnscreenText.OnscreenText(TTLocalizer.AllNewNames, parent=aspect2d, style=OnscreenText.ScreenPrompt, scale=TTLocalizer.NStypeNotification, pos=(-0.0163333, 0.15))
		self.typeNotification.wrtReparentTo(self.typeNamePanel, sort=2)
		self.typeANameGUIElements.append(self.typeNotification)
		self.nameMessages = OnscreenText.OnscreenText(TTLocalizer.NameMessages, parent=aspect2d, style=OnscreenText.ScreenPrompt, scale=0.06, pos=(-0.0163333, -0.05))
		self.nameMessages.wrtReparentTo(self.typeNamePanel, sort=2)
		self.typeANameGUIElements.append(self.nameMessages)
		self.nameEntry = DirectEntry(parent=aspect2d, relief=None, scale=TTLocalizer.NSnameEntry, entryFont=getToonFont(), width=TTLocalizer.NSmaxNameWidth, numLines=2, focus=1, cursorKeys=1, pos=(0.0, 0.0, 0.39), text_align=TextNode.ACenter, autoCapitalize=1)
		self.nameEntry.wrtReparentTo(self.typeNamePanel, sort=2)
		self.typeANameGUIElements.append(self.nameEntry)
		self.submitButton = DirectButton(parent=aspect2d, relief=None, image=(self.squareUp,
		 self.squareDown,
		 self.squareHover,
		 self.squareUp), image_scale=(1.2, 0, 1.1), pos=(-0.01, 0, -0.25), text=TTLocalizer.NameShopSubmitButton, text_scale=0.06, text_pos=(0, -0.02))
		self.submitButton.wrtReparentTo(self.typeNamePanel, sort=2)
		self.typeNamePanel.setPos(-0.42, 0, -0.078)
		self.typeANameGUIElements.append(self.submitButton)
		guiButton.removeNode()
		self.uberhide(self.typeANameGUIElements)

	def ubershow(self, guiObjectsToShow):
		for x in guiObjectsToShow:
			try:
				x.show()
			except:
				print 'NameShop: Tried to show already removed object'

	def hideAll(self):
		self.uberhide(self.pickANameGUIElements)
		self.uberhide(self.typeANameGUIElements)

	def uberhide(self, guiObjectsToHide):
		for x in guiObjectsToHide:
			try:
				x.hide()
			except:
				print 'NameShop: Tried to hide already removed object'

	def uberdestroy(self, guiObjectsToDestroy):
		for x in guiObjectsToDestroy:
			try:
				x.destroy()
				del x
			except:
				print 'NameShop: Tried to destroy already removed object'
