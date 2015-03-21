from pandac.PandaModules import *
from funnyfarm.toonbase import FunnyFarmGlobals
from funnyfarm.toon.LocalToon import LocalToon
from toontown.toon import ToonDNA
from toontown.toon import Toon
import json

Toon.loadDialog()

class CustomToon(LocalToon):
    def __init__(self, name, dna):
        LocalToon.__init__(self)

        self.dna = ToonDNA.ToonDNA()
        self.dna.newToonFromProperties(*dna)
        self.setDNA(self.dna)
        self.setName(name)
        self.setupControls()
        self.startLaffMeter()
        self.startLookAround()
        self.startBlink()
        self.startChat()

class CustomToonLoader:
    def __init__(self):
        with open('custom-toons.json') as f:
            self.customToons = json.loads(f.read())

    def loadCustomToon(self, toonName):
        if toonName not in self.customToons:
            print 'Error: No custom toon named %s' % toonName
            return

        return CustomToon(toonName, self.customToons[toonName])

class Bear(LocalToon):

	def __init__(self):
		LocalToon.__init__(self)
		self.dna = ToonDNA.ToonDNA()
		self.dna.newToonFromProperties('bss', 'ss', 's', 'm', 20, 0, 20, 20, 4, 2, 4, 2, 12, 27)
		self.setDNA(self.dna)
		self.setName('Bear E. Funny')
		self.setNametagFont(FunnyFarmGlobals.Zany)
		self.setHat(11, 0, 0)
		self.setAccessLevel(300)
		self.setGMIcon()
		self.setupControls()
		self.startLookAround()
		self.startBlink()
		self.startLaffMeter()
		self.startChat()

class Chuckie(LocalToon):

	def __init__(self):
		LocalToon.__init__(self)
		self.dna = ToonDNA.ToonDNA()
		self.dna.newToonFromProperties('css', 'ms', 's', 'm', 20, 0, 20, 20, 4, 10, 4, 10, 7, 31)
		self.setDNA(self.dna)
		self.setName('Chuckie')
		self.setNametagFont(FunnyFarmGlobals.Wonky)
		self.setHat(28, 0, 0)
		self.setGlasses(2, 0, 0)
		self.setShoes(1, 8, 0)
		self.setGMPartyIcon(1)
		self.setupControls()
		self.startLaffMeter()
		self.startChat()

class Kingleroy(LocalToon):

	def __init__(self):
		LocalToon.__init__(self)
		self.dna = ToonDNA.ToonDNA()
		self.dna.newToonFromProperties('css', 'ms', 's', 'm', 26, 0, 26, 26, 0,27, 0,27, 1,14)
		self.setDNA(self.dna)
		self.setName('King Leroy')
		self.setNametagFont(FunnyFarmGlobals.Wonky)
		self.setAccessLevel(300)
		self.setGMPartyIcon(1)
		self.reparentTo(render)
		self.startLaffMeter()
		self.applyCheesyEffect(6)
		self.setGMPartyIcon(1)
		self.setupControls()
		self.startLaffMeter()
		#self.startChat()

class BlackDog(LocalToon):

	def __init__(self):
		LocalToon.__init__(self)
		self.dna = ToonDNA.ToonDNA()
		self.dna.newToonFromProperties('dss', 'ms', 's', 'm', 26, 0, 26, 26, 0,27, 0, 27, 0, 27)
		self.setDNA(self.dna)
		self.setupControls()
		self.startLaffMeter()
		self.startLookAround()
		self.startBlink()
		self.startChat()
