from pandac.PandaModules import *
from direct.gui.DirectGui import *
from funnyfarm.toonbase.Sounds import *
from funnyfarm.makeatoon.MainGui import *
from funnyfarm.load.mfReader import *

def openList():
	bFriendsList.hide()
	openedList.show()
	closeBtn.show()
	
def closeList():
	openedList.hide()
	closeBtn.hide()
	bFriendsList.show()
	
friendsGui = loader.loadModel('phase_3.5/models/gui/friendslist_gui.bam')
friendsButtonNormal = friendsGui.find('**/FriendsBox_Closed')
friendsButtonPressed = friendsGui.find('**/FriendsBox_Rollover')
friendsButtonRollover = friendsGui.find('**/FriendsBox_Rollover')
friendsOpened = friendsGui.find('**/FriendsBox_Open')

openedList = DirectFrame(parent=base.a2dTopRight, relief=None, image=(friendsOpened), pos = (-0.23, 0, -0.4))
openedList.hide()

newScale = oldScale = 0.8
bFriendsList = DirectButton(parent=base.a2dTopRight, image=(friendsButtonNormal, 
 friendsButtonPressed, 
 friendsButtonRollover), relief=None, pos=(-0.14, 0, -0.13), scale=newScale, command=openList)
bFriendsList.hide()

closeGui = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui.bam')
closeButtonNormal = closeGui.find('**/CloseBtn_UP')
closeButtonPressed = closeGui.find('**/CloseBtn_DN')
closeButtonRollover = closeGui.find('**/CloseBtn_Rllvr')
closeBtn = DirectButton(parent=bFriendsList, image=(closeButtonNormal, closeButtonPressed, closeButtonRollover), 
 relief=None, pos = (0, 0, 0), command=closeList)
closeBtn.hide()

