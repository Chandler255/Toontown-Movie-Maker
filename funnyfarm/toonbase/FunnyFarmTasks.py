from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.task.Task import Task
from funnyfarm.toonbase.FunnyFarmLoader import FunnyFarmLoader
from funnyfarm.hood.FFSafeZoneLoader import FFSafeZoneLoader
from funnyfarm.hood.FFShopLoader import FFShopLoader
from funnyfarm.hood.CZSafeZoneLoader import CZSafeZoneLoader
from funnyfarm.town.RicketyRoadLoader import RicketyRoadLoader

class TaskManager:
	def __init__(self, loaderClass, sfxMgr, ivalMgr, localAvatar):
		self.loaderClass = loaderClass
		self.sfxMgr = sfxMgr
		self.ivalMgr = ivalMgr
		self.localAvatar = localAvatar
		self.loadedArea = 'funnyfarm'

	def initFFShopLoader(self, szLoader):
		self.szLoader = szLoader
		self.shopLoader = FFShopLoader(self.sfxMgr, self.localAvatar)

	def addFFTask(self):
		base.taskMgr.add(self.UpdateFFShops, 'FFShops')
		
	def removeFFTask(self):
		base.taskMgr.remove('FFShops')
		
	def loadFF(self):
		self.szLoader.load()
		self.szLoader.loadSfx()

	def UpdateFFShops(self, task):
		self.x = self.localAvatar.getPos().get_x()
		self.y = self.localAvatar.getPos().get_y()
		
		if self.x >= -57.5416 and self.x <= -53.8681  and self.y >= 72.7419 and self.y <= 76.4045 and self.loadedArea == 'funnyfarm':
			self.ivalMgr.loadDoorInterval(self.localAvatar, self.szLoader.getPetShopDoor(), (-52.6333, 73.1321, 0), (-56.0671, 76.2939, 0), 45, 0, 0, self.shopLoader.loadPetShop, self.szLoader.unload)
			self.loadedArea = 'petinterior'
			
		if self.x <= 3.53673 and self.x >= -2.90245 and self.y <= -18 and self.y >= -18.5 and self.loadedArea == 'petinterior':
			self.ivalMgr.loadDoorInterval(self.localAvatar, self.shopLoader.getPetShopDoor(), (-1.17738, -15, 0), (-1.17738, -20.5, 0), 180, 0, 0, self.loadFF, self.shopLoader.unloadPetShop)
			self.loadedArea = 'funnyfarm'
		
		if self.x >= 57.5367 and self.x <= 61.1981 and self.y <= 78.3454 and self.y >= 74.693 and self.loadedArea == 'funnyfarm':
			self.ivalMgr.loadDoorInterval(self.localAvatar, self.szLoader.getGagShopDoor(), (57.9, 73.95, 0), (61.5264, 77.445, 0), 315, 0, 0, self.shopLoader.loadGagShop, self.szLoader.unload)
			self.loadedArea = 'gaginterior'
			
		if self.x >= -3.46 and self.x <= 3.46 and self.y >= -2.46 and self.y <= -1.25 and self.loadedArea == 'gaginterior':
			self.ivalMgr.loadDoorInterval(self.localAvatar, self.shopLoader.getGagShopDoor(), (-0.690567, -0.400715, 0), (-0.690567, -4.5176, 0), 180, 0, 0, self.loadFF, self.shopLoader.unloadGagShop)
			self.loadedArea = 'funnyfarm'

		return Task.cont

