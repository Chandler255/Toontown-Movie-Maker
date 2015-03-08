from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from direct.directutil import Mopath
from toontown.toonbase import ToontownGlobals

class DistributedBoat(DirectObject):

	def __init__(self, hood):
		self.hood = hood
		self.eastWestMopath = Mopath.Mopath()
		self.westEastMopath = Mopath.Mopath()
		self.eastWestMopathInterval = None
		self.westEastMopathInterval = None

	def generate(self):
		self.boat = self.hood.boat
		self.setupTracks()
		self.accept('enterdonalds_boat_floor', self.__handleOnFloor)
		self.accept('exitdonalds_boat_floor', self.__handleOffFloor)

	def setupTracks(self):
		boat = self.boat
		boat.unstash()
		dockSound = self.hood.dockSound
		foghornSound = self.hood.foghornSound
		bellSound = self.hood.bellSound
		self.eastWestMopath.loadFile('phase_6/paths/dd-e-w')
		self.eastWestMopathInterval = MopathInterval(self.eastWestMopath, boat)
		ewBoatTrack = ParallelEndTogether(Parallel(self.eastWestMopathInterval, SoundInterval(bellSound, node=boat)), SoundInterval(foghornSound, node=boat), name='ew-boat')
		self.westEastMopath.loadFile('phase_6/paths/dd-w-e')
		self.westEastMopathInterval = MopathInterval(self.westEastMopath, boat)
		weBoatTrack = ParallelEndTogether(Parallel(self.westEastMopathInterval, SoundInterval(bellSound, node=boat)), SoundInterval(foghornSound, node=boat), name='we-boat')
		PIER_TIME = 5.0
		eastPier = self.hood.geom.find('**/east_pier')
		ePierHpr = VBase3(90, -44.2601, 0)
		ePierTargetHpr = VBase3(90, 0.25, 0)
		westPier = self.hood.geom.find('**/west_pier')
		wPierHpr = VBase3(-90, -44.2601, 0)
		wPierTargetHpr = VBase3(-90, 0.25, 0)
		ePierDownTrack = Parallel(LerpHprInterval(eastPier, PIER_TIME, ePierHpr, ePierTargetHpr), SoundInterval(dockSound, node=eastPier), name='e-pier-down')
		ePierUpTrack = Parallel(LerpHprInterval(eastPier, PIER_TIME, ePierTargetHpr, ePierHpr), SoundInterval(dockSound, node=eastPier), name='e-pier-up')
		wPierDownTrack = Parallel(LerpHprInterval(westPier, PIER_TIME, wPierHpr, wPierTargetHpr), SoundInterval(dockSound, node=westPier), name='w-pier-down')
		wPierUpTrack = Parallel(LerpHprInterval(westPier, PIER_TIME, wPierTargetHpr, wPierHpr), SoundInterval(dockSound, node=westPier), name='w-pier-up')
		self.ewTrack = ParallelEndTogether(Parallel(ewBoatTrack, ePierDownTrack), wPierUpTrack, name='ew-track')
		self.weTrack = ParallelEndTogether(Parallel(weBoatTrack, wPierDownTrack), ePierUpTrack, name='we-track')

	def disable(self):
		self.ignore('enterdonalds_boat_floor')
		self.ignore('exitdonalds_boat_floor')
		self.ewTrack.finish()
		self.weTrack.finish()

	def delete(self):
		self.eastWestMopath.reset()
		self.westEastMopath.reset()
		if self.eastWestMopathInterval.mopath:
			self.eastWestMopathInterval.destroy()
		if self.westEastMopathInterval.mopath:
			self.westEastMopathInterval.destroy()
		del self.eastWestMopath
		del self.westEastMopath
		del self.ewTrack
		del self.weTrack

	def __handleOnFloor(self, event):
		base.localAvatar.wrtReparentTo(self.boat)
		base.playSfx(self.hood.waterSound, looping=1)

	def __handleOffFloor(self, event):
		base.localAvatar.wrtReparentTo(render)
		self.hood.waterSound.stop()

	def enterDockedEast(self, ts):
		self.weTrack.finish()

	def exitDockedEast(self):
		return None

	def enterSailingWest(self):
		self.ewTrack.start()

	def exitSailingWest(self):
		self.ewTrack.finish()

	def enterDockedWest(self):
		self.ewTrack.finish()

	def exitDockedWest(self):
		return None

	def enterSailingEast(self):
		self.weTrack.start()

	def exitSailingEast(self):
		self.weTrack.finish()
