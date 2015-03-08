from direct.directbase import DirectStart
from pandac.PandaModules import *
from direct.showbase import DirectObject
from direct.showbase import Audio3DManager
from direct.showbase.ShowBase import ShowBase

class SfxManager:
	def __init__(self, loaderClass):
		self.loaderClass = loaderClass
		self.audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)
		
		self.FF_theme = self.loaderClass.loadSfx('phase_4/audio/bgm/firework_music.ogg')
		self.FF_theme.setLoop(True)
		
		self.FF_theme_winter = self.loaderClass.loadSfx('phase_4/audio/bgm/new_years_fireworks_music.ogg')
		self.FF_theme_winter.setLoop(True)

		self.click = self.loaderClass.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg')
		self.rollover = self.loaderClass.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg')
		self.rollover.setVolume(2)

		self.book_open = self.loaderClass.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_open.ogg')
		self.book_close = self.loaderClass.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_delete.ogg')
		self.PageTurn = self.loaderClass.loadSfx('phase_3.5/audio/sfx/GUI_stickerbook_turn.ogg')
		self.doorOpen = self.loaderClass.loadSfx('phase_3.5/audio/sfx/Door_Open_1.ogg')

		self.activity = self.loaderClass.loadSfx('phase_4/audio/bgm/m_match_bg2.ogg')
		self.activity.setLoop(True)

		self.centralMusic = self.loaderClass.loadSfx('phase_13/audio/bgm/party_swing_dance.ogg')
		self.centralMusic.setLoop(True)

		self.roadMusic = self.loaderClass.loadSfx('phase_13/audio/bgm/party_generic_theme.ogg')
		self.roadMusic.setLoop(True)

		self.trainLoop = self.audio3d.loadSfx('phase_14/audio/train_loop.ogg')
		self.trainLoop.setLoop(True)
		self.trainLoop.setVolume(20)

		self.create_music = self.loaderClass.loadSfx('phase_3/audio/bgm/create_a_toon.ogg')
		self.create_music.setLoop(True)

		self.nameSound = self.loaderClass.loadSfx('phase_4/audio/sfx/MG_pairing_all_matched.ogg')
		self.acceptedSound = self.loaderClass.loadSfx('phase_4/audio/sfx/MG_sfx_travel_game_bonus.ogg')

		self.boing = self.loaderClass.loadSfx('phase_3/audio/sfx/tt_s_ara_mat_crash_boing.ogg')
		self.glassBoing = self.loaderClass.loadSfx('phase_3/audio/sfx/tt_s_ara_mat_crash_glassBoing.ogg')
		self.wood = self.loaderClass.loadSfx('phase_3/audio/sfx/tt_s_ara_mat_crash_wood.ogg')
		self.woodBoing = self.loaderClass.loadSfx('phase_3/audio/sfx/tt_s_ara_mat_crash_woodBoing.ogg')
		self.woodGlass = self.loaderClass.loadSfx('phase_3/audio/sfx/tt_s_ara_mat_crash_woodGlass.ogg')

		self.phaseOne = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseOne.ogg')
		self.phaseOne.setLoop(True)
		self.phaseOne.setVolume(5)

		self.phaseTwo = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseTwo.ogg')
		self.phaseTwo.setLoop(True)
		self.phaseTwo.setVolume(5)

		self.phaseThree = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseThree.ogg')
		self.phaseThree.setLoop(True)
		self.phaseThree.setVolume(5)

		self.phaseFour = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseFour.ogg')
		self.phaseFour.setLoop(True)
		self.phaseFour.setVolume(5)

		self.phaseFourToFive = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseFourToFive.ogg')
		self.phaseFourToFive.setLoop(True)
		self.phaseFourToFive.setVolume(5)

		self.phaseFive = self.audio3d.loadSfx('phase_4/audio/sfx/tt_s_prp_sillyMeterPhaseFive.ogg')
		self.phaseFive.setLoop(True)
		self.phaseFive.setVolume(5)

		self.propShow = self.audio3d.loadSfx('phase_13/audio/sfx/tt_s_ara_pty_propsShow_dance.ogg')
		self.propShow.setLoop(True)
		self.propShow.setVolume(5)
