from sys import argv
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from colors import Colors
import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from buttons import MovieMaker
from direct.directutil import Mopath
from panda3d.core import TextNode
from funnyfarm.toon.CustomToons import BlackDog
from funnyfarm.toon.CustomToons import Kingleroy
from direct.directbase import DirectStart
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from funnyfarm.toonbase import FunnyFarmGlobals
from pandac.PandaModules import *
from funnyfarm.toonbase import FunnyFarmGlobals
from funnyfarm.toon.LocalToon import LocalToon
from toontown.toon import ToonDNA
from toontown.toon import Toon

base.disableMouse()

base.localAvatar = BlackDog()
base.localAvatar.reparentTo(render)

run()