# Embedded file name: ChatInput.py
from direct.directbase import DirectStart
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import *
from otp.nametag.NametagConstants import *
from ChatBalloon import ChatBalloon

class ChatInput(DirectObject):

    def __init__(self):
        self.keyList = ['a',
         'b',
         'c',
         'd',
         'e',
         'f',
         'g',
         'h',
         'i',
         'j',
         'k',
         'l',
         'm',
         'n',
         'o',
         'p',
         'q',
         'r',
         's',
         't',
         'u',
         'v',
         'w',
         'x',
         'y',
         'z',
         ',',
         '.',
         '/',
         ';',
         ':',
         '"',
         "'",
         '{',
         '}',
         '[',
         ']',
         '-',
         '_',
         '+',
         '=',
         '<',
         '>',
         '?',
         '!',
         '`',
         '~',
         '@',
         '#',
         '$',
         '%',
         '^',
         '&',
         '*',
         '(',
         ')',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9',
         '0',
         '|']
        self.chat_btn_model = None
        self.chatBx = None
        self.chat_btn = None
        self.chatInput = None
        self.chatBx_send = None
        self.chatBx_close = None
        self.state = None
        return

    def createGui(self):
        self.state = 'closed'
        self.chat_btn_model = loader.loadModel('phase_3.5/models/gui/chat_input_gui.bam')
        self.chatBx = self.chat_btn_model.find('**/Chat_Bx_FNL')
        self.chatBx.reparentTo(aspect2d)
        self.chatBx.hide()
        self.chat_btn = DirectButton(text=('', 'Chat', 'Chat', ''), text_shadow=(0, 0, 0, 1), image=(self.chat_btn_model.find('**/ChtBx_ChtBtn_UP'), 
         self.chat_btn_model.find('**/ChtBx_ChtBtn_DN'), 
         self.chat_btn_model.find('**/ChtBx_ChtBtn_RLVR')), relief=None, text_scale=0.0525, text_pos=(0, -0.08), text_fg=(1, 1, 1, 1), command=self.openChatInput, pos=(0.085, 0, -0.075), scale=1.25, parent=base.a2dTopLeft, extraArgs=[None])
        return

    def deleteGui(self):
        self.chat_btn_model.removeNode()
        self.chat_btn_model = None
        self.chatBx.removeNode()
        self.chatBx = None
        self.chat_btn.destroy()
        self.chat_btn = None
        return

    def enableKeyboardShortcuts(self):
        for key in self.keyList:
            self.acceptOnce(key, self.openChatInput, [key])
            self.acceptOnce('shift-' + key, self.openChatInput, [key.upper()])

    def disableKeyboardShortcuts(self):
        for key in self.keyList:
            self.ignore(key)
            self.ignore('shift-' + key)

    def openChatInput(self, key):
        self.disableKeyboardShortcuts()
        self.chat_btn.hide()
        self.chatBx.show()
        self.chatBx.setPos(-1.027, 0, 0.74)
        self.chatBx.setScale(1.2)
        self.chatBx_close = DirectButton(text=('', 'Cancel', 'Cancel', ''), text_shadow=(0, 0, 0, 1), geom=(self.chat_btn_model.find('**/CloseBtn_UP'), self.chat_btn_model.find('**/CloseBtn_DN'), self.chat_btn_model.find('**/CloseBtn_Rllvr')), relief=None, text_scale=0.0525, text_pos=(0, -0.08), text_fg=(1, 1, 1, 1), pos=(-1.208, 0, 0.637), scale=1.25, command=self.close_ChtBx)
        self.chatInput = DirectEntry(focus=1, cursorKeys=0, relief=None, geom=None, numLines=3, pos=(-1.27, 0, 0.875), scale=0.0675, command=self.sendChat, width=8, initialText=key)
        self.chatBx_send = DirectButton(text=('', 'Say It', 'Say It', ''), text_shadow=(0, 0, 0, 1), geom=(self.chat_btn_model.find('**/ChtBx_ChtBtn_UP'), self.chat_btn_model.find('**/ChtBx_ChtBtn_DN'), self.chat_btn_model.find('**/ChtBx_ChtBtn_RLVR')), relief=None, text_scale=0.0525, text_pos=(0, -0.08), text_fg=(1, 1, 1, 1), pos=(-0.81, 0, 0.637), scale=1.25, command=self.sendChat, extraArgs=[self.chatInput.get()])
        self.state = 'open'
        return

    def sendChat(self, chat):
        base.localAvatar.setChatAbsolute(chat, CFSpeech|CFTimeout)
        self.close_ChtBx()

    def close_ChtBx(self):
        self.chatBx.hide()
        self.chatBx_close.destroy()
        self.chatBx_close = None
        self.chatBx_send.destroy()
        self.chatBx_send = None
        self.chatInput.destroy()
        self.chatInput = None
        self.chat_btn.show()
        self.enableKeyboardShortcuts()
        self.state = 'closed'
        return

    def delete(self):
        if self.state == 'open':
            self.close_ChtBx()
        self.deleteGui()
        self.disableKeyboardShortcuts()
        self.state = None
        return

