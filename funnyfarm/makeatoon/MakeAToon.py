from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from direct.task.Task import Task
from MakeAToonGlobals import *
from funnyfarm.toon.LocalToon import LocalToon
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
import GenderShop
import BodyShop
import ColorShop
import ClothesShop
import NameShop
import random

class MakeAToon:
	
	def __init__(self):
		self.notify = directNotify.newCategory('MakeAToon')
		self.notify.setInfo(True)
		self.toonPosition = Point3(-1.62, -3.49, 0)
		self.toonScale = Point3(1, 1, 1)
		self.toonHpr = Point3(180, 0, 0)
		self.gs = GenderShop.GenderShop(self)
		self.bs = BodyShop.BodyShop()
		self.cos = ColorShop.ColorShop()
		self.cls = ClothesShop.ClothesShop()
		self.ns = NameShop.NameShop()
		self.shop = GENDERSHOP
		self.shopsVisited = []
		self.hprDelta = -1
		self.dropIval = None
		self.roomSquishIval = None
		self.propSquishIval = None	
		
	def enter(self):
		self.notify.info('Starting Make-a-Toon.')
		base.disableMouse()
		base.camLens.setMinFov(ToontownGlobals.MakeAToonCameraFov/(4./3.))
		base.camera.setPosHpr(-5.7, -12.3501, 2.15, -24.8499, 2.73, 0)
		base.playMusic(self.music, looping=1)
		self.guiTopBar.show()
		self.guiBottomBar.show()
		self.guiCancelButton.show()
		self.enterGenderShop()
	
	def exit(self):
		base.camLens.setMinFov(ToontownGlobals.DefaultCameraFov/(4./3.))
		self.guiTopBar.hide()
		self.guiBottomBar.hide()
		self.music.stop()
		self.room.reparentTo(hidden)
	
	def load(self):
		gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui.bam')
		gui.flattenMedium()
		guiAcceptUp = gui.find('**/tt_t_gui_mat_okUp')
		guiAcceptUp.flattenStrong()
		guiAcceptDown = gui.find('**/tt_t_gui_mat_okDown')
		guiAcceptDown.flattenStrong()
		guiCancelUp = gui.find('**/tt_t_gui_mat_closeUp')
		guiCancelUp.flattenStrong()
		guiCancelDown = gui.find('**/tt_t_gui_mat_closeDown')
		guiCancelDown.flattenStrong()
		guiNextUp = gui.find('**/tt_t_gui_mat_nextUp')
		guiNextUp.flattenStrong()
		guiNextDown = gui.find('**/tt_t_gui_mat_nextDown')
		guiNextDown.flattenStrong()
		guiNextDisabled = gui.find('**/tt_t_gui_mat_nextDisabled')
		guiNextDisabled.flattenStrong()
		rotateUp = gui.find('**/tt_t_gui_mat_arrowRotateUp')
		rotateUp.flattenStrong()
		rotateDown = gui.find('**/tt_t_gui_mat_arrowRotateDown')
		rotateDown.flattenStrong()
		self.guiTopBar = DirectFrame(relief=None, text=TTLocalizer.CreateYourToon, text_font=ToontownGlobals.getSignFont(), text_fg=(0.0, 0.65, 0.35, 1), text_scale=0.18, text_pos=(0, -0.03), pos=(0, 0, 0.86))
		self.guiTopBar.hide()
		self.guiBottomBar = DirectFrame(relief=None, image_scale=(1.25, 1, 1), pos=(0.01, 0, -0.86))
		self.guiBottomBar.hide()
		self.guiCancelButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(guiCancelUp,
		 guiCancelDown,
		 guiCancelUp,
		 guiCancelDown), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-1.179, 0, -0.011), text=('', TTLocalizer.MakeAToonCancel, TTLocalizer.MakeAToonCancel), text_font=ToontownGlobals.getInterfaceFont(), text_scale=TTLocalizer.MATguiCancelButton, text_pos=(0, 0.115), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
		self.guiCancelButton.setPos(0.13, 0, 0.13)
		self.guiCancelButton.reparentTo(base.a2dBottomLeft)
		self.guiCancelButton.hide()
		self.guiNextButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(guiNextUp,
		 guiNextDown,
		 guiNextUp,
		 guiNextDisabled), image_scale=(0.3, 0.3, 0.3), image1_scale=(0.35, 0.35, 0.35), image2_scale=(0.35, 0.35, 0.35), pos=(1.165, 0, -0.018), command=self.goToNextShop, text=('',
		 TTLocalizer.MakeAToonNext,
		 TTLocalizer.MakeAToonNext,
		 ''), text_font=ToontownGlobals.getInterfaceFont(), text_scale=TTLocalizer.MATguiNextButton, text_pos=(0, 0.115), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
		self.guiNextButton.setPos(-0.13, 0, 0.13)
		self.guiNextButton.reparentTo(base.a2dBottomRight)
		self.guiNextButton.hide()
		self.guiLastButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(guiNextUp,
		 guiNextDown,
		 guiNextUp,
		 guiNextDown), image3_color=Vec4(0.5, 0.5, 0.5, 0.75), image_scale=(-0.3, 0.3, 0.3), image1_scale=(-0.35, 0.35, 0.35), image2_scale=(-0.35, 0.35, 0.35), pos=(0.825, 0, -0.018), command=self.goToLastShop, text=('',
		 TTLocalizer.MakeAToonLast,
		 TTLocalizer.MakeAToonLast,
		 ''), text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.08, text_pos=(0, 0.115), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
		self.guiLastButton.setPos(-0.37, 0, 0.13)
		self.guiLastButton.reparentTo(base.a2dBottomRight)
		self.guiLastButton.hide()
		self.rotateLeftButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(rotateUp,
		 rotateDown,
		 rotateUp,
		 rotateDown), image_scale=(-0.4, 0.4, 0.4), image1_scale=(-0.5, 0.5, 0.5), image2_scale=(-0.5, 0.5, 0.5), pos=(-0.355, 0, 0.36))
		self.rotateLeftButton.flattenMedium()
		self.rotateLeftButton.reparentTo(base.a2dBottomCenter)
		self.rotateLeftButton.hide()
		self.rotateLeftButton.bind(DGG.B1PRESS, self.rotateToonLeft)
		self.rotateLeftButton.bind(DGG.B1RELEASE, self.stopToonRotateLeftTask)
		self.rotateRightButton = DirectButton(parent=self.guiBottomBar, relief=None, image=(rotateUp,
		 rotateDown,
		 rotateUp,
		 rotateDown), image_scale=(0.4, 0.4, 0.4), image1_scale=(0.5, 0.5, 0.5), image2_scale=(0.5, 0.5, 0.5), pos=(0.355, 0, 0.36))
		self.rotateRightButton.flattenStrong()
		self.rotateRightButton.reparentTo(base.a2dBottomCenter)
		self.rotateRightButton.hide()
		self.rotateRightButton.bind(DGG.B1PRESS, self.rotateToonRight)
		self.rotateRightButton.bind(DGG.B1RELEASE, self.stopToonRotateRightTask)
		gui.removeNode()
		self.roomDropActor = Actor()
		self.roomDropActor.loadModel('phase_3/models/makeatoon/roomAnim_model.bam')
		self.roomDropActor.loadAnims({'drop': 'phase_3/models/makeatoon/roomAnim_roomDrop.bam'})
		self.roomDropActor.reparentTo(render)
		self.dropJoint = self.roomDropActor.find('**/droppingJoint')
		self.roomSquishActor = Actor()
		self.roomSquishActor.loadModel('phase_3/models/makeatoon/roomAnim_model.bam')
		self.roomSquishActor.loadAnims({'squish': 'phase_3/models/makeatoon/roomAnim_roomSquish.bam'})
		self.roomSquishActor.reparentTo(render)
		self.squishJoint = self.roomSquishActor.find('**/scalingJoint')
		self.propSquishActor = Actor()
		self.propSquishActor.loadModel('phase_3/models/makeatoon/roomAnim_model.bam')
		self.propSquishActor.loadAnims({'propSquish': 'phase_3/models/makeatoon/roomAnim_propSquish.bam'})
		self.propSquishActor.reparentTo(render)
		self.propSquishActor.pose('propSquish', 0)
		self.propJoint = self.propSquishActor.find('**/propJoint')
		self.spotlightActor = Actor()
		self.spotlightActor.loadModel('phase_3/models/makeatoon/roomAnim_model.bam')
		self.spotlightActor.loadAnims({'spotlightShake': 'phase_3/models/makeatoon/roomAnim_spotlightShake.bam'})
		self.spotlightActor.reparentTo(render)
		self.spotlightJoint = self.spotlightActor.find('**/spotlightJoint')
		self.room = loader.loadModel('phase_3/models/makeatoon/tt_m_ara_mat_room.bam')
		self.room.flattenMedium()
		self.genderWalls = self.room.find('**/genderWalls')
		self.genderWalls.flattenStrong()
		self.genderProps = self.room.find('**/genderProps')
		self.genderProps.flattenStrong()
		self.bodyWalls = self.room.find('**/bodyWalls')
		self.bodyWalls.flattenStrong()
		self.bodyProps = self.room.find('**/bodyProps')
		self.bodyProps.flattenStrong()
		self.colorWalls = self.room.find('**/colorWalls')
		self.colorWalls.flattenStrong()
		self.colorProps = self.room.find('**/colorProps')
		self.colorProps.flattenStrong()
		self.clothesWalls = self.room.find('**/clothWalls')
		self.clothesWalls.flattenMedium()
		self.clothesProps = self.room.find('**/clothProps')
		self.clothesProps.flattenMedium()
		self.nameWalls = self.room.find('**/nameWalls')
		self.nameWalls.flattenStrong()
		self.nameProps = self.room.find('**/nameProps')
		self.nameProps.flattenStrong()
		self.background = self.room.find('**/background')
		self.background.flattenStrong()
		self.background.reparentTo(render)
		self.floor = self.room.find('**/floor')
		self.floor.flattenStrong()
		self.floor.reparentTo(render)
		self.spotlight = self.room.find('**/spotlight')
		self.spotlight.reparentTo(self.spotlightJoint)
		self.spotlight.setColor(1, 1, 1, 0.3)
		self.spotlight.setPos(1.18, -1.27, 0.41)
		self.spotlight.setScale(2.6)
		self.spotlight.setHpr(0, 0, 0)
		smokeSeqNode = SequenceNode('smoke')
		smokeModel = loader.loadModel('phase_3/models/makeatoon/tt_m_ara_mat_smoke.bam')
		smokeFrameList = list(smokeModel.findAllMatches('**/smoke_*'))
		smokeFrameList.reverse()
		for smokeFrame in smokeFrameList:
			smokeSeqNode.addChild(smokeFrame.node())

		smokeSeqNode.setFrameRate(12)
		self.smoke = render.attachNewNode(smokeSeqNode)
		self.smoke.setScale(1, 1, 0.75)
		self.smoke.hide()
		self.gs.load()
		self.bs.load()
		self.cos.load()
		self.cls.load()
		self.ns.load()
		self.music = base.loadMusic('phase_3/audio/bgm/create_a_toon.ogg')
		self.crashSounds = map(base.loadSfx, ['phase_3/audio/sfx/tt_s_ara_mat_crash_boing.ogg',
											  'phase_3/audio/sfx/tt_s_ara_mat_crash_glassBoing.ogg',
											  'phase_3/audio/sfx/tt_s_ara_mat_crash_wood.ogg',
											  'phase_3/audio/sfx/tt_s_ara_mat_crash_woodBoing.ogg',
											  'phase_3/audio/sfx/tt_s_ara_mat_crash_woodGlass.ogg'])
	
	def unload(self):
		self.exit()
		self.gs.unload()
		self.bs.unload()
		self.cos.unload()
		self.cls.unload()
		self.ns.unload()
		del self.gs
		del self.bs
		del self.cos
		del self.cls
		del self.ns
		self.guiTopBar.destroy()
		self.guiBottomBar.destroy()
		self.guiCancelButton.destroy()
		self.guiNextButton.destroy()
		self.guiLastButton.destroy()
		self.rotateLeftButton.destroy()
		self.rotateRightButton.destroy()
		del self.guiTopBar
		del self.guiBottomBar
		del self.guiCancelButton
		del self.guiNextButton
		del self.guiLastButton
		del self.rotateLeftButton
		del self.rotateRightButton
		del self.music
		if self.toon:
			self.toon.destroy()
		del self.toon
		self.cleanupDropIval()
		self.cleanupRoomSquishIval()
		self.cleanupPropSquishIval()
		self.room.removeNode()
		del self.room
		self.genderWalls.removeNode()
		self.genderProps.removeNode()
		del self.genderWalls
		del self.genderProps
		self.bodyWalls.removeNode()
		self.bodyProps.removeNode()
		del self.bodyWalls
		del self.bodyProps
		self.colorWalls.removeNode()
		self.colorProps.removeNode()
		del self.colorWalls
		del self.colorProps
		self.clothesWalls.removeNode()
		self.clothesProps.removeNode()
		del self.clothesWalls
		del self.clothesProps
		self.nameWalls.removeNode()
		self.nameProps.removeNode()
		del self.nameWalls
		del self.nameProps
		self.background.removeNode()
		del self.background
		self.floor.removeNode()
		del self.floor
		self.spotlight.removeNode()
		del self.spotlight
		self.smoke.removeNode()
		del self.smoke
		while len(self.crashSounds):
			del self.crashSounds[0]
			
	def setToon(self, toon):
		self.toon = toon
		
	def goToNextShop(self):
		if self.shop == GENDERSHOP:
			self.exitGenderShop()
			self.enterBodyShop()
		elif self.shop == BODYSHOP:
			self.exitBodyShop()
			self.enterColorShop()
		elif self.shop == COLORSHOP:
			self.exitColorShop()
			self.enterClothesShop()
		elif self.shop == CLOTHESSHOP:
			self.exitClothesShop()
			self.enterNameShop()
		
	def goToLastShop(self):
		if self.shop == BODYSHOP:
			self.exitBodyShop()
			self.enterGenderShop()
		elif self.shop == COLORSHOP:
			self.exitColorShop()
			self.enterBodyShop()
		elif self.shop == CLOTHESSHOP:
			self.exitClothesShop()
			self.enterColorShop()
		elif self.shop == NAMESHOP:
			self.exitNameShop()
			self.enterClothesShop()
			
	def enterGenderShop(self):
		self.shop = GENDERSHOP
		if GENDERSHOP not in self.shopsVisited:
			self.shopsVisited.append(GENDERSHOP)
			self.genderWalls.reparentTo(self.squishJoint)
			self.genderProps.reparentTo(self.propJoint)
			self.roomSquishActor.pose('squish', 0)
			self.guiNextButton['state'] = DGG.DISABLED
		else:
			self.dropRoom(self.genderWalls, self.genderProps)
		self.guiTopBar['text'] = TTLocalizer.CreateYourToonTitle
		self.guiTopBar['text_fg'] = (1, 0.92, 0.2, 1)
		self.guiTopBar['text_scale'] = TTLocalizer.MATenterGenderShop
		self.gs.enter()
		self.guiLastButton.hide()
		self.guiNextButton.show()
		self.rotateLeftButton.hide()
		self.rotateRightButton.hide()
		
	def exitGenderShop(self):
		self.squishRoom(self.genderWalls)
		self.squishProp(self.genderProps)
		self.gs.exit()
		
	def enterBodyShop(self):
		self.toon.show()
		self.shop = BODYSHOP
		self.guiTopBar['text'] = TTLocalizer.ShapeYourToonTitle
		self.guiTopBar['text_fg'] = (0.0, 0.98, 0.5, 1)
		self.guiTopBar['text_scale'] = TTLocalizer.MATenterBodyShop
		self.dropRoom(self.bodyWalls, self.bodyProps)
		self.bs.enter(self.toon)
		if BODYSHOP not in self.shopsVisited:
			self.shopsVisited.append(BODYSHOP)
		self.guiNextButton.show()
		self.guiLastButton.show()
		self.rotateLeftButton.show()
		self.rotateRightButton.show()

	def exitBodyShop(self):
		self.squishRoom(self.bodyWalls)
		self.squishProp(self.bodyProps)
		self.bs.exit()
		
	def enterColorShop(self):
		self.shop = COLORSHOP
		self.guiTopBar['text'] = TTLocalizer.PaintYourToonTitle
		self.guiTopBar['text_fg'] = (0, 1, 1, 1)
		self.guiTopBar['text_scale'] = TTLocalizer.MATenterColorShop
		self.dropRoom(self.colorWalls, self.colorProps)
		self.cos.enter(self.toon)
		if COLORSHOP not in self.shopsVisited:
			self.shopsVisited.append(COLORSHOP)

	def exitColorShop(self):
		self.squishRoom(self.colorWalls)
		self.squishProp(self.colorProps)
		self.cos.exit()
		
	def enterClothesShop(self):
		self.shop = CLOTHESSHOP
		self.guiTopBar['text'] = TTLocalizer.PickClothesTitle
		self.guiTopBar['text_fg'] = (1, 0.92, 0.2, 1)
		self.guiTopBar['text_scale'] = TTLocalizer.MATenterClothesShop
		self.dropRoom(self.clothesWalls, self.clothesProps)
		self.toon.setPos(-1.62, -3.49, 0)
		self.toon.setHpr(180, 0, 0)
		self.rotateLeftButton.show()
		self.rotateRightButton.show()
		self.guiNextButton.show()
		self.cls.enter(self.toon)
		if CLOTHESSHOP not in self.shopsVisited:
			self.shopsVisited.append(CLOTHESSHOP)

	def exitClothesShop(self):
		self.squishRoom(self.clothesWalls)
		self.squishProp(self.clothesProps)
		self.cls.exit()

	def enterNameShop(self):
		self.shop = NAMESHOP
		self.guiTopBar['text'] = TTLocalizer.NameToonTitle
		self.guiTopBar['text_fg'] = (0.0, 0.98, 0.5, 1)
		self.guiTopBar['text_scale'] = TTLocalizer.MATenterNameShop
		self.dropRoom(self.nameWalls, self.nameProps)
		self.spotlight.setPos(2, -1.95, 0.41)
		self.toon.setPos(1.5, -4, 0)
		self.toon.setH(120)
		self.rotateLeftButton.hide()
		self.rotateRightButton.hide()
		self.guiNextButton.hide()
		self.ns.enter(self.toon)
		if NAMESHOP not in self.shopsVisited:
			self.shopsVisited.append(NAMESHOP)

	def exitNameShop(self):
		self.squishRoom(self.nameWalls)
		self.squishProp(self.nameProps)
		self.spotlight.setPos(1.18, -1.27, 0.41)
		self.ns.exit()
		
	def squishRoom(self, room):
		if self.roomSquishIval and self.roomSquishIval.isPlaying():
			self.roomSquishIval.finish()
		squishDuration = self.roomSquishActor.getDuration('squish')
		self.roomSquishIval = Sequence(Func(self.roomSquishActor.play, 'squish'), Wait(squishDuration), Func(room.hide))
		self.roomSquishIval.start()

	def squishProp(self, prop):
		if not prop.isEmpty():
			if self.propSquishIval and self.propSquishIval.isPlaying():
				self.propSquishIval.finish()
			squishDuration = self.propSquishActor.getDuration('propSquish')
			self.propSquishIval = Sequence(Func(self.propSquishActor.play, 'propSquish'), Wait(squishDuration), Func(prop.hide))
			self.propSquishIval.start()

	def dropRoom(self, walls, props):

		def propReparentTo(props):
			if not props.isEmpty():
				props.reparentTo(self.propJoint)

		if self.dropIval and self.dropIval.isPlaying():
			self.dropIval.finish()
		walls.reparentTo(self.dropJoint)
		walls.show()
		if not props.isEmpty():
			props.reparentTo(self.dropJoint)
			props.show()
		dropDuration = self.roomDropActor.getDuration('drop')
		self.dropIval = Parallel(Sequence(Func(self.roomDropActor.play, 'drop'), Wait(dropDuration), Func(walls.reparentTo, self.squishJoint), Func(propReparentTo, props), Func(self.propSquishActor.pose, 'propSquish', 0), Func(self.roomSquishActor.pose, 'squish', 0)), Sequence(Wait(0.25), Func(self.smoke.show), Func(self.smoke.node().play), LerpColorScaleInterval(self.smoke, 0.5, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1)), Func(self.smoke.hide)), Func(self.spotlightActor.play, 'spotlightShake'), Func(self.playRandomCrashSound))
		self.dropIval.start()
	
	def cleanupDropIval(self):
		if self.dropIval:
			self.dropIval.finish()
			del self.dropIval

	def cleanupRoomSquishIval(self):
		if self.roomSquishIval:
			self.roomSquishIval.finish()
			del self.roomSquishIval

	def cleanupPropSquishIval(self):
		if self.propSquishIval:
			self.propSquishIval.finish()
			del self.propSquishIval
	
	def playRandomCrashSound(self):
		index = random.randint(0, len(self.crashSounds) - 1)
		base.playSfx(self.crashSounds[index])
		
	def rotateToonLeft(self, event):
		taskMgr.add(self.rotateToonLeftTask, 'rotateToonLeftTask')

	def rotateToonLeftTask(self, task):
		self.toon.setH(self.toon.getH() + self.hprDelta)
		return task.cont

	def stopToonRotateLeftTask(self, event):
		taskMgr.remove('rotateToonLeftTask')

	def rotateToonRight(self, event):
		taskMgr.add(self.rotateToonRightTask, 'rotateToonRightTask')

	def rotateToonRightTask(self, task):
		self.toon.setH(self.toon.getH() - self.hprDelta)
		return task.cont

	def stopToonRotateRightTask(self, event):
		taskMgr.remove('rotateToonRightTask')
		


