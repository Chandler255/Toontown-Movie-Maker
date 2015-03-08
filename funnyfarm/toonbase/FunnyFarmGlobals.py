from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
from otp.margins.MarginManager import MarginManager
from otp.nametag import NametagGlobals
from otp.nametag.ChatBalloon import ChatBalloon
from direct.particles import ParticleManagerGlobal
from direct.showbase import PhysicsManagerGlobal

nametagFonts = []
for font in TTLocalizer.NametagFonts:
	nametagFonts.append(loader.loadFont(font))

Simple = nametagFonts[0]
Shivering = nametagFonts[1]
Wonky = nametagFonts[2]
Fancy = nametagFonts[3]
Silly = nametagFonts[4]
Zany = nametagFonts[5]
Practical = nametagFonts[6]
Nautical = nametagFonts[7]
Whimsical = nametagFonts[8]
Spooky = nametagFonts[9]
Action = nametagFonts[10]
Poetic = nametagFonts[11]
Boardwalk = nametagFonts[12]
Western = nametagFonts[13]

FunnyFarm = 1000
FFCentral = 2000
SillySprings = 3000
ChillyVillage = 4000
MoonlitMeadow = 5000

RicketyRoad = 3100
WintryWay = 4100
BreezyBend = 5100

def setNametagGlobals():
	base.wantNametags = True
	base.marginManager = MarginManager()
	arrow = loader.loadModel('phase_3/models/gui/chat_button_gui').find('**/Horiz_Arrow_UP')
	panel = loader.loadModel('phase_3/models/props/panel')
	balloonMod = loader.loadModel('phase_3/models/props/chatbox')
	balloon = ChatBalloon(balloonMod)

	NametagGlobals.setMouseWatcher(base.mouseWatcherNode)
	NametagGlobals.setArrowModel(arrow)
	NametagGlobals.setCamera(base.cam)
	NametagGlobals.setNametagCard(panel, 0)
	NametagGlobals.setSpeechBalloon2d(balloon)
	NametagGlobals.setSpeechBalloon3d(balloon)

def setParticleManagers():
	base.particleMgr = ParticleManagerGlobal.particleMgr
	base.physicsMgr = PhysicsManagerGlobal.physicsMgr
