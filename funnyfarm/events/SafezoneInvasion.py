from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownGlobals
from otp.avatar import Emote
import SafezoneInvasionGlobals

class SafezoneInvasion(DirectObject):

	def __init__(self):
		self.invasionOn = False
		self.showFloor = base.render.find('**/ShowFloor')
		self.scienceFair = base.render.find('**/ScienceFair')

		# Let's load some models
		self.cogSky = loader.loadModel(SafezoneInvasionGlobals.CogSkyFile)
		self.cogSky.setBin('background', 100)
		self.cogSky.setColor(0.3, 0.3, 0.28, 1)
		self.cogSky.setTransparency(TransparencyAttrib.MDual, 1)
		self.cogSky.setDepthWrite(0)
		self.cogSky.setFogOff()
		self.cogSky.setZ(-20.0)
		ce = CompassEffect.make(NodePath(), CompassEffect.PRot | CompassEffect.PZ)
		self.cogSky.node().setEffect(ce)

		self.fadeIn = self.cogSky.colorScaleInterval(5.0, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0), blendType='easeInOut')
		self.cogSkyBegin = LerpColorScaleInterval(self.geom, 6.0, Vec4(0.4, 0.4, 0.4, 1), blendType='easeInOut')
		self.cogSkyBeginStage = LerpColorScaleInterval(self.showFloor, 6.0, Vec4(0.4, 0.4, 0.4, 1), blendType='easeInOut')
		self.cogSkyBeginScience = LerpColorScaleInterval(self.scienceFair, 6.0, Vec4(0.4, 0.4, 0.4, 1), blendType='easeInOut')
		self.beginSkySequence = Sequence(Func(self.fadeIn.start), Func(self.cogSkyBegin.start), Func(self.cogSkyBeginStage.start), Func(self.cogSkyBeginScience.start))

		self.fadeOut = self.cogSky.colorScaleInterval(6.0, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeInOut')
		self.cogSkyEnd = LerpColorScaleInterval(self.geom, 7.0, Vec4(1, 1, 1, 1), blendType='easeInOut') 
		self.cogSkyEndStage = LerpColorScaleInterval(self.showFloor, 7.0, Vec4(1, 1, 1, 1), blendType='easeInOut')
		self.cogSkyEndScience = LerpColorScaleInterval(self.scienceFair, 7.0, Vec4(1, 1, 1, 1), blendType='easeInOut')
		self.endSkySequence = Sequence(Func(self.fadeOut.start), Func(self.cogSkyEnd.start), Func(self.cogSkyEndStage.start), Func(self.cogSkyEndScience.start), Wait(7), Func(self.cogSky.removeNode))

		self.musicEnter = base.loadMusic(SafezoneInvasionGlobals.InvasionMusicEnter)
		self.victoryMusic = base.loadMusic('phase_9/audio/bgm/CogHQ_finale.ogg')

	def delete(self):
		if self.invasionOn:
			# These are only called if the sky is loaded
			del self.fadeIn
			del self.fadeOut
			del self.cogSkyBegin
			del self.cogSkyEnd
			del self.cogSkyBeginStage
			del self.cogSkyEndStage
			del self.musicEnter
			del self.beginSkySequence
			del self.endSkySequence
		self.ignoreAll()

	'''
	 INVASION-RELATED
	   We don't really have much to do here except for cueing the music and setting the stage.
	   Most of the invasion itself is handled in the DSafezoneInvasionAI.
	'''
	def setInvasionStarted(self, started):
		if started and not self.invasionOn:
			# self.startCogSky()
			self.sky.hide()
			self.cogSky.reparentTo(render)
			self.beginSkySequence.start()
			base.playMusic(self.musicEnter, looping=1, volume=1.0)
		elif not started and self.invasionOn:
			self.endInvasion()
		else:
			return # We don't care about this change...
		self.invasionOn = started

	def endInvasion(self):
		self.endSkySequence.start() # Done with the cog sky, we're all done with that
		base.playMusic(self.victoryMusic, looping=0, volume=0.9) # Cue the music
		# Dance the night away
		# victoryDanceDuration = (2 * 5.15)
		'''
		self.victoryIval = Sequence(
			Func(Emote.globalEmote.disableAll, base.localAvatar, 'dbattle, enterReward'),
			Func(base.localAvatar.disableAvatarControls),
			Func(base.localAvatar.b_setEmoteState, 6, 1.0),
			Wait(5.15),
			Func(Emote.globalEmote.releaseAll, base.localAvatar, 'dbattle, enterReward'),
			Func(base.localAvatar.enableAvatarControls),
			# Func(self.showThanks)
			# Func(self.delete) # Might as well clean up
		)
		self.victoryIval.start()
		'''

	def startCogSky(self):
		self.fadeIn.start()
		self.cogSkyBegin.start()
		self.cogSkyBeginStage.start()

	def stopCogSky(self):
		if self.invasionOn:
			cogSkySequence = Sequence(
				Func(self.cogSkyEnd.start),
				Func(self.cogSkyEndStage.start),
				Func(self.fadeOut.start),
				Wait(7),
				Func(self.cogSky.removeNode) # Remove the sky node after the fade out
				)

	def stopMusic(self):
		self.musicEnter.stop()
