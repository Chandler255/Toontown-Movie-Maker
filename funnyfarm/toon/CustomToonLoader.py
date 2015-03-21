from funnyfarm.toon.LocalToon import LocalToon
from toontown.toon import ToonDNA

import json


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
