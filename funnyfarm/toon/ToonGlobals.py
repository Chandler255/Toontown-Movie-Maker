from pandac.PandaModules import *

toonSpeciesTypes = [
 'dog',
 'cat',
 'mouse',
 'duck',
 'rabbit',
 'bear',
 'monkey',
 'horse',
 'pig'
]

toonBodyTypes = ['dgs', 'dgm', 'dgl']

HeadDict = {
    'dls':'/models/char/tt_a_chr_dgm_shorts_head_1000',
    'dss':'/models/char/tt_a_chr_dgm_skirt_head_1000',
    'dsl':'/models/char/tt_a_chr_dgs_shorts_head_1000',
    'dll':'/models/char/tt_a_chr_dgl_shorts_head_1000',
    'c':'/models/char/cat-heads-1000',
    'h':'/models/char/horse-heads-1000',
    'm':'/models/char/mouse-heads-1000',
    'r':'/models/char/rabbit-heads-1000',
    'f':'/models/char/duck-heads-1000',
    'p':'/models/char/monkey-heads-1000',
    'b':'/models/char/bear-heads-1000',
    's':'/models/char/pig-heads-1000'
}
EyelashDict = {
    'd':'/models/char/dog-lashes',
    'c':'/models/char/cat-lashes',
    'h':'/models/char/horse-lashes',
    'm':'/models/char/mouse-lashes',
    'r':'/models/char/rabbit-lashes',
    'f':'/models/char/duck-lashes',
    'p':'/models/char/monkey-lashes',
    'b':'/models/char/bear-lashes',
    's':'/models/char/pig-lashes'
}
DogMuzzleDict = {
    'dls':'/models/char/dogMM_Shorts-headMuzzles-1000',
    'dss':'/models/char/dogMM_Skirt-headMuzzles-1000',
    'dsl':'/models/char/dogSS_Shorts-headMuzzles-1000',
    'dll':'/models/char/dogLL_Shorts-headMuzzles-1000'
}
toonHeadScales = {
    'mouse':Point3(1.0),
    'cat':Point3(1.0),
    'duck':Point3(1.0),
    'rabbit':Point3(1.0),
    'horse':Point3(1.0),
    'dog':Point3(1.0),
    'monkey':Point3(1.0),
    'bear':Point3(1.0),
    'pig':Point3(1.0)
}
headHeightDict = {
    'dls':0.75,
    'dss':0.5,
    'dsl':0.5,
    'dll':0.75,
    'cls':0.75,
    'css':0.5,
    'csl':0.5,
    'cll':0.75,
    'hls':0.75,
    'hss':0.5,
    'hsl':0.5,
    'hll':0.75,
    'mls':0.75,
    'mss':0.5,
    'rls':0.75,
    'rss':0.5,
    'rsl':0.5,
    'rll':0.75,
    'fls':0.75,
    'fss':0.5,
    'fsl':0.5,
    'fll':0.75,
    'pls':0.75,
    'pss':0.5,
    'psl':0.5,
    'pll':0.75,
    'bls':0.75,
    'bss':0.5,
    'bsl':0.5,
    'bll':0.75,
    'sls':0.75,
    'sss':0.5,
    'ssl':0.5,
    'sll':0.75
}

# Body
LegDict = {
    's':'/models/char/tt_a_chr_dgs_shorts_legs_1000',
    'm':'/models/char/tt_a_chr_dgm_shorts_legs_1000',
    'l':'/models/char/tt_a_chr_dgl_shorts_legs_1000'
}
TorsoDict = {
    's':'/models/char/dogSS_Naked-torso-1000',
    'm':'/models/char/dogMM_Naked-torso-1000',
    'l':'/models/char/dogLL_Naked-torso-1000',
    'ss':'/models/char/tt_a_chr_dgs_shorts_torso_1000',
    'ms':'/models/char/tt_a_chr_dgm_shorts_torso_1000',
    'ls':'/models/char/tt_a_chr_dgl_shorts_torso_1000',
    'sd':'/models/char/tt_a_chr_dgs_skirt_torso_1000',
    'md':'/models/char/tt_a_chr_dgm_skirt_torso_1000',
    'ld':'/models/char/tt_a_chr_dgl_skirt_torso_1000'
}
toonBodyScales = {
    'mouse':0.6,
    'cat':0.73,
    'duck':0.66,
    'rabbit':0.74,
    'horse':0.85,
    'dog':0.85,
    'monkey':0.68,
    'bear':0.85,
    'pig':0.77
}
legHeightDict = {
    's':1.5,
    'm':2.0,
    'l':2.75
}
torsoHeightDict = {
    's':1.5,
    'm':1.75,
    'l':2.25,
    'ss':1.5,
    'ms':1.75,
    'ls':2.25,
    'sd':1.5,
    'md':1.75,
    'ld':2.25
}

# Animations
LegsAnimDict = {}
TorsoAnimDict = {}
HeadAnimDict = {}
Phase3AnimList = (
    ('neutral', 'neutral'),
    ('run', 'run')
)
Phase3_5AnimList = (
    ('walk', 'walk'),
    ('teleport', 'teleport'),
    ('book', 'book'),
    ('jump', 'jump'),
    ('running-jump', 'running-jump'),
    ('jump-squat', 'jump-zstart'),
    ('jump-idle', 'jump-zhang'),
    ('jump-land', 'jump-zend'),
    ('running-jump-squat', 'leap_zstart'),
    ('running-jump-idle', 'leap_zhang'),
    ('running-jump-land', 'leap_zend'),
    ('pushbutton', 'press-button'),
    ('throw', 'pie-throw'),
    ('victory', 'victory-dance'),
    ('sidestep-left', 'sidestep-left'),
    ('conked', 'conked'),
    ('cringe', 'cringe'),
    ('wave', 'wave'),
    ('shrug', 'shrug'),
    ('angry', 'angry'),
    ('tutorial-neutral', 'tutorial-neutral'),
    ('left-point', 'left-point'),
    ('right-point', 'right-point'),
    ('right-point-start', 'right-point-start'),
    ('give-props', 'give-props'),
    ('give-props-start', 'give-props-start'),
    ('right-hand', 'right-hand'),
    ('right-hand-start', 'right-hand-start'),
    ('duck', 'duck'),
    ('sidestep-right', 'jump-back-right'),
    ('periscope', 'periscope')
)
Phase4AnimList = (
    ('sit', 'sit'),
    ('sit-start', 'intoSit'),
    ('swim', 'swim'),
    ('tug-o-war', 'tug-o-war'),
    ('sad-walk', 'losewalk'),
    ('sad-neutral', 'sad-neutral'),
    ('up', 'up'),
    ('down', 'down'),
    ('left', 'left'),
    ('right', 'right'),
    ('applause', 'applause'),
    ('confused', 'confused'),
    ('bow', 'bow'),
    ('curtsy', 'curtsy'),
    ('bored', 'bored'),
    ('think', 'think'),
    ('battlecast', 'fish'),
    ('cast', 'cast'),
    ('castlong', 'castlong'),
    ('fish-end', 'fishEND'),
    ('fish-neutral', 'fishneutral'),
    ('fish-again', 'fishAGAIN'),
    ('reel', 'reel'),
    ('reel-H', 'reelH'),
    ('reel-neutral', 'reelneutral'),
    ('pole', 'pole'),
    ('pole-neutral', 'poleneutral'),
    ('slip-forward', 'slip-forward'),
    ('slip-backward', 'slip-backward'),
    ('catch-neutral', 'gameneutral'),
    ('catch-run', 'gamerun'),
    ('catch-eatneutral', 'eat_neutral'),
    ('catch-eatnrun', 'eatnrun'),
    ('catch-intro-throw', 'gameThrow'),
    ('swing', 'swing'),
    ('pet-start', 'petin'),
    ('pet-loop', 'petloop'),
    ('pet-end', 'petend'),
    ('scientistJealous', 'scientistJealous'),
    ('scientistEmcee', 'scientistEmcee'),
    ('scientistWork', 'scientistWork'),
    ('scientistGame', 'scientistGame')
)
Phase5AnimList = (
    ('water-gun', 'water-gun'),
    ('hold-bottle', 'hold-bottle'),
    ('firehose', 'firehose'),
    ('spit', 'spit'),
    ('tickle', 'tickle'),
    ('smooch', 'smooch'),
    ('happy-dance', 'happy-dance'),
    ('sprinkle-dust', 'sprinkle-dust'),
    ('juggle', 'juggle'),
    ('climb', 'climb'),
    ('sound', 'shout'),
    ('toss', 'toss'),
    ('hold-magnet', 'hold-magnet'),
    ('hypnotize', 'hypnotize'),
    ('struggle', 'struggle'),
    ('lose', 'lose'),
    ('melt', 'melt')
)
Phase5_5AnimList = (
    ('takePhone', 'takePhone'),
    ('phoneNeutral', 'phoneNeutral'),
    ('phoneBack', 'phoneBack'),
    ('bank', 'jellybeanJar'),
    ('callPet', 'callPet'),
    ('feedPet', 'feedPet'),
    ('start-dig', 'into_dig'),
    ('loop-dig', 'loop_dig'),
    ('water', 'water')
)
Phase6AnimList = (
    ('headdown-putt', 'headdown-putt'),
    ('into-putt', 'into-putt'),
    ('loop-putt', 'loop-putt'),
    ('rotateL-putt', 'rotateL-putt'),
    ('rotateR-putt', 'rotateR-putt'),
    ('swing-putt', 'swing-putt'),
    ('look-putt', 'look-putt'),
    ('lookloop-putt', 'lookloop-putt'),
    ('bad-putt', 'bad-putt'),
    ('badloop-putt', 'badloop-putt'),
    ('good-putt', 'good-putt')
)
Phase9AnimList = (
    ('push', 'push'),
)
Phase10AnimList = (
    ('leverReach', 'leverReach'),
    ('leverPull', 'leverPull'),
    ('leverNeutral', 'leverNeutral')
)
PhaseAnimLists = {
    'phase_3':Phase3AnimList,
    'phase_3.5':Phase3_5AnimList,
    'phase_4':Phase4AnimList,
    'phase_5':Phase5AnimList,
    'phase_5.5':Phase5_5AnimList,
    'phase_6':Phase6AnimList,
    'phase_9':Phase9AnimList,
    'phase_10':Phase10AnimList
}

def compileAnimLists():
    """
    "Lazy instantiation" of LegsAnimDict, TorsoAnimDict, and HeadAnimDict.
    Compiles the animation lists into dictionaries that follow the format of:
        anim->filename.
    Lazy instantiation is used to increase start-up performance.
    """

    def makeAnimDict(phaseStr, animList, partDict, globalAnimDict):
        for key, value in partDict.items():
            globalAnimDict.setdefault(key, {})
            for anim in animList:
                globalAnimDict[key][anim[0]] = phaseStr + value + anim[1]

    for phaseStr, animList in PhaseAnimLists.items():
        makeAnimDict(phaseStr, animList, LegDict, LegsAnimDict)
        makeAnimDict(phaseStr, animList, TorsoDict, TorsoAnimDict)
        filteredHeadDict = {k: v for k, v in HeadDict.items() if 'd' in k}
        makeAnimDict(phaseStr, animList, filteredHeadDict, HeadAnimDict)

def unloadPhaseAnims(phaseStr='phase_3'):
    """
    Unloads the animations of the provided phase file on the local avatar. This
    function also has a set of pure code legibility functions:
        unloadBasicAnims(), unloadTutorialBattleAnims(), unloadMinigameAnims(),
        unloadBattleAnims(), unloadSellbotHQAnims(), unloadCashbotHQAnims().
    """
    animList = PhaseAnimLists.get(phaseStr)
    if not animList:
        raise ValueError("Tried to unload nonexistent phase '%s'" % phaseStr)
    elif not hasattr(base, 'localAvatar'):
        raise AttributeError(
            "Tried to unload phase '%s' on undefined avatar" % phaseStr)
    for anim in animList:
        if anim[0] in LegsAnimDict[base.localAvatar.style.legs]:
            base.localAvatar.unloadAnims([anim[0]], 'legs', None)
        elif anim[0] in TorsoAnimDict[base.localAvatar.style.torso]:
            base.localAvatar.unloadAnims([anim[0]], 'torso', None)
        elif 'd' in base.localAvatar.style.head:
            if anim[0] in HeadAnimDict[base.localAvatar.style.head]:
                base.localAvatar.unloadAnims([anim[0]], 'head', None)

def unloadBasicAnims():
    unloadPhaseAnims('phase_3')

def unloadTutorialBattleAnims():
    unloadPhaseAnims('phase_3.5')

def unloadMinigameAnims():
    unloadPhaseAnims('phase_4')

def unloadBattleAnims():
    unloadPhaseAnims('phase_5')

def unloadSellbotHQAnims():
    unloadPhaseAnims('phase_9')

def unloadCashbotHQAnims():
    unloadPhaseAnims('phase_10')

# Dialog
DogDialogueArray = []
CatDialogueArray = []
HorseDialogueArray = []
RabbitDialogueArray = []
MouseDialogueArray = []
DuckDialogueArray = []
MonkeyDialogueArray = []
BearDialogueArray = []
PigDialogueArray = []

def loadDialog():
    loadPath = 'phase_3.5/audio/dial/'
    DogDialogueFiles = (
        'AV_dog_short', 'AV_dog_med', 'AV_dog_long', 'AV_dog_question',
        'AV_dog_exclaim', 'AV_dog_howl'
    )
    for filename in DogDialogueFiles:
        DogDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

    catDialogueFiles = (
        'AV_cat_short', 'AV_cat_med', 'AV_cat_long', 'AV_cat_question',
        'AV_cat_exclaim', 'AV_cat_howl'
    )
    for filename in catDialogueFiles:
        CatDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

    horseDialogueFiles = (
        'AV_horse_short', 'AV_horse_med', 'AV_horse_long', 'AV_horse_question',
        'AV_horse_exclaim', 'AV_horse_howl'
    )
    for filename in horseDialogueFiles:
        HorseDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

    rabbitDialogueFiles = (
        'AV_rabbit_short', 'AV_rabbit_med', 'AV_rabbit_long',
        'AV_rabbit_question', 'AV_rabbit_exclaim', 'AV_rabbit_howl'
    )
    for filename in rabbitDialogueFiles:
        RabbitDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

    mouseDialogueFiles = (
        'AV_mouse_short', 'AV_mouse_med', 'AV_mouse_long', 'AV_mouse_question',
        'AV_mouse_exclaim', 'AV_mouse_howl'
    )
    for filename in mouseDialogueFiles:
        MouseDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

    duckDialogueFiles = (
        'AV_duck_short', 'AV_duck_med', 'AV_duck_long', 'AV_duck_question',
        'AV_duck_exclaim', 'AV_duck_howl'
    )
    for filename in duckDialogueFiles:
        DuckDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

    monkeyDialogueFiles = (
        'AV_monkey_short', 'AV_monkey_med', 'AV_monkey_long',
        'AV_monkey_question', 'AV_monkey_exclaim', 'AV_monkey_howl'
    )
    for filename in monkeyDialogueFiles:
        MonkeyDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

    bearDialogueFiles = (
        'AV_bear_short', 'AV_bear_med', 'AV_bear_long', 'AV_bear_question',
        'AV_bear_exclaim', 'AV_bear_howl'
    )
    for filename in bearDialogueFiles:
        BearDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

    pigDialogueFiles = (
        'AV_pig_short', 'AV_pig_med', 'AV_pig_long', 'AV_pig_question',
        'AV_pig_exclaim', 'AV_pig_howl'
    )
    for filename in pigDialogueFiles:
        PigDialogueArray.append(base.loadSfx(loadPath + filename + '.mp3'))

def unloadDialog():
    """
    Convenience function for deleting the loaded dialog sound effects.
    """
    DogDialogueArray[:] = []
    CatDialogueArray[:] = []
    HorseDialogueArray[:] = []
    RabbitDialogueArray[:] = []
    MouseDialogueArray[:] = []
    DuckDialogueArray[:] = []
    MonkeyDialogueArray[:] = []
    BearDialogueArray[:] = []
    PigDialogueArray[:] = []
    
Shirts = [
 'phase_3/maps/desat_shirt_1.jpg',
 'phase_3/maps/desat_shirt_2.jpg',
 'phase_3/maps/desat_shirt_3.jpg',
 'phase_3/maps/desat_shirt_4.jpg',
 'phase_3/maps/desat_shirt_5.jpg',
 'phase_3/maps/desat_shirt_6.jpg',
 'phase_3/maps/desat_shirt_7.jpg',
 'phase_3/maps/desat_shirt_8.jpg',
 'phase_3/maps/desat_shirt_9.jpg',
 'phase_3/maps/desat_shirt_10.jpg',
 'phase_3/maps/desat_shirt_11.jpg',
 'phase_3/maps/desat_shirt_12.jpg',
 'phase_3/maps/desat_shirt_13.jpg',
 'phase_3/maps/desat_shirt_14.jpg',
 'phase_3/maps/desat_shirt_15.jpg',
 'phase_3/maps/desat_shirt_16.jpg',
 'phase_3/maps/desat_shirt_17.jpg',
 'phase_3/maps/desat_shirt_18.jpg',
 'phase_3/maps/desat_shirt_19.jpg',
 'phase_3/maps/desat_shirt_20.jpg',
 'phase_3/maps/desat_shirt_21.jpg',
 'phase_3/maps/desat_shirt_22.jpg',
 'phase_3/maps/desat_shirt_23.jpg',
 'phase_4/maps/female_shirt1b.jpg',
 'phase_4/maps/female_shirt2.jpg',
 'phase_4/maps/female_shirt3.jpg',
 'phase_4/maps/male_shirt1.jpg',
 'phase_4/maps/male_shirt2_palm.jpg',
 'phase_4/maps/male_shirt3c.jpg',
 'phase_4/maps/shirt_ghost.jpg',
 'phase_4/maps/shirt_pumkin.jpg',
 'phase_4/maps/holiday_shirt1.jpg',
 'phase_4/maps/holiday_shirt2b.jpg',
 'phase_4/maps/holidayShirt3b.jpg',
 'phase_4/maps/holidayShirt4.jpg',
 'phase_4/maps/female_shirt1b.jpg',
 'phase_4/maps/female_shirt5New.jpg',
 'phase_4/maps/shirtMale4B.jpg',
 'phase_4/maps/shirt6New.jpg',
 'phase_4/maps/shirtMaleNew7.jpg',
 'phase_4/maps/femaleShirtNew6.jpg',
 'phase_4/maps/Vday1Shirt5.jpg',
 'phase_4/maps/Vday1Shirt6SHD.jpg',
 'phase_4/maps/Vday1Shirt4.jpg',
 'phase_4/maps/Vday_shirt2c.jpg',
 'phase_4/maps/shirtTieDyeNew.jpg',
 'phase_4/maps/male_shirt1.jpg',
 'phase_4/maps/StPats_shirt1.jpg',
 'phase_4/maps/StPats_shirt2.jpg',
 'phase_4/maps/ContestfishingVestShirt2.jpg',
 'phase_4/maps/ContestFishtankShirt1.jpg',
 'phase_4/maps/ContestPawShirt1.jpg',
 'phase_4/maps/CowboyShirt1.jpg',
 'phase_4/maps/CowboyShirt2.jpg',
 'phase_4/maps/CowboyShirt3.jpg',
 'phase_4/maps/CowboyShirt4.jpg',
 'phase_4/maps/CowboyShirt5.jpg',
 'phase_4/maps/CowboyShirt6.jpg',
 'phase_4/maps/4thJulyShirt1.jpg',
 'phase_4/maps/4thJulyShirt2.jpg',
 'phase_4/maps/shirt_Cat7_01.jpg',
 'phase_4/maps/shirt_Cat7_02.jpg',
 'phase_4/maps/contest_backpack3.jpg',
 'phase_4/maps/contest_leder.jpg',
 'phase_4/maps/contest_mellon2.jpg',
 'phase_4/maps/contest_race2.jpg',
 'phase_4/maps/PJBlueBanana2.jpg',
 'phase_4/maps/PJRedHorn2.jpg',
 'phase_4/maps/PJGlasses2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_valentine2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_desat4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_gardening2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_party1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_party2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_summer1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_summer2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_marathon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_toonTask1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_toonTask2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_valentine3.jpg',
 'phase_4/maps/tt_t_chr_shirt_scientistC.jpg',
 'phase_4/maps/tt_t_chr_shirt_scientistA.jpg',
 'phase_4/maps/tt_t_chr_shirt_scientistB.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mailbox.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trashcan.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_loonyLabs.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_hydrant.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_whistle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_cogbuster.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_victoryParty01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_victoryParty02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotVPIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_jellyBeans.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_doodle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloweenTurtle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_greentoon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_getConnectedMoverShaker.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racingGrandPrix.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotVPIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_pirate.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_dinosaur.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_anniversary.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sora.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_slappy.jpg'
]
BoyShirts = [
 (0, 0),
 (1, 1),
 (2, 2),
 (3, 3),
 (4, 4),
 (5, 5),
 (8, 8),
 (9, 9),
 (10, 0),
 (11, 0),
 (14, 10),
 (16, 0),
 (17, 0),
 (18, 12),
 (19, 13)
]
GirlShirts = [
 (0, 0),
 (1, 1),
 (2, 2),
 (3, 3),
 (5, 5),
 (6, 6),
 (7, 7),
 (9, 9),
 (12, 0),
 (13, 11),
 (15, 11),
 (16, 0),
 (20, 0),
 (21, 0),
 (22, 0)
]

Sleeves = ['phase_3/maps/desat_sleeve_1.jpg',
 'phase_3/maps/desat_sleeve_2.jpg',
 'phase_3/maps/desat_sleeve_3.jpg',
 'phase_3/maps/desat_sleeve_4.jpg',
 'phase_3/maps/desat_sleeve_5.jpg',
 'phase_3/maps/desat_sleeve_6.jpg',
 'phase_3/maps/desat_sleeve_7.jpg',
 'phase_3/maps/desat_sleeve_8.jpg',
 'phase_3/maps/desat_sleeve_9.jpg',
 'phase_3/maps/desat_sleeve_10.jpg',
 'phase_3/maps/desat_sleeve_15.jpg',
 'phase_3/maps/desat_sleeve_16.jpg',
 'phase_3/maps/desat_sleeve_19.jpg',
 'phase_3/maps/desat_sleeve_20.jpg',
 'phase_4/maps/female_sleeve1b.jpg',
 'phase_4/maps/female_sleeve2.jpg',
 'phase_4/maps/female_sleeve3.jpg',
 'phase_4/maps/male_sleeve1.jpg',
 'phase_4/maps/male_sleeve2_palm.jpg',
 'phase_4/maps/male_sleeve3c.jpg',
 'phase_4/maps/shirt_Sleeve_ghost.jpg',
 'phase_4/maps/shirt_Sleeve_pumkin.jpg',
 'phase_4/maps/holidaySleeve1.jpg',
 'phase_4/maps/holidaySleeve3.jpg',
 'phase_4/maps/female_sleeve1b.jpg',
 'phase_4/maps/female_sleeve5New.jpg',
 'phase_4/maps/male_sleeve4New.jpg',
 'phase_4/maps/sleeve6New.jpg',
 'phase_4/maps/SleeveMaleNew7.jpg',
 'phase_4/maps/female_sleeveNew6.jpg',
 'phase_4/maps/Vday5Sleeve.jpg',
 'phase_4/maps/Vda6Sleeve.jpg',
 'phase_4/maps/Vday_shirt4sleeve.jpg',
 'phase_4/maps/Vday2cSleeve.jpg',
 'phase_4/maps/sleeveTieDye.jpg',
 'phase_4/maps/male_sleeve1.jpg',
 'phase_4/maps/StPats_sleeve.jpg',
 'phase_4/maps/StPats_sleeve2.jpg',
 'phase_4/maps/ContestfishingVestSleeve1.jpg',
 'phase_4/maps/ContestFishtankSleeve1.jpg',
 'phase_4/maps/ContestPawSleeve1.jpg',
 'phase_4/maps/CowboySleeve1.jpg',
 'phase_4/maps/CowboySleeve2.jpg',
 'phase_4/maps/CowboySleeve3.jpg',
 'phase_4/maps/CowboySleeve4.jpg',
 'phase_4/maps/CowboySleeve5.jpg',
 'phase_4/maps/CowboySleeve6.jpg',
 'phase_4/maps/4thJulySleeve1.jpg',
 'phase_4/maps/4thJulySleeve2.jpg',
 'phase_4/maps/shirt_sleeveCat7_01.jpg',
 'phase_4/maps/shirt_sleeveCat7_02.jpg',
 'phase_4/maps/contest_backpack_sleeve.jpg',
 'phase_4/maps/Contest_leder_sleeve.jpg',
 'phase_4/maps/contest_mellon_sleeve2.jpg',
 'phase_4/maps/contest_race_sleeve.jpg',
 'phase_4/maps/PJSleeveBlue.jpg',
 'phase_4/maps/PJSleeveRed.jpg',
 'phase_4/maps/PJSleevePurple.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_desat4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_gardening2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_party1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_party2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_summer1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_summer2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_marathon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_toonTask1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_toonTask2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine3.jpg',
 'phase_4/maps/tt_t_chr_shirtSleeve_scientist.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mailbox.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trashcan.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_loonyLabs.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_hydrant.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_whistle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_cogbuster.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_victoryParty01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_victoryParty02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotVPIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_jellyBeans.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_doodle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloweenTurtle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_greentoon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_getConnectedMoverShaker.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racingGrandPrix.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotVPIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_pirate.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_dinosaur.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_anniversary.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sora.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_slappy.jpg']
BoyShorts = ['phase_3/maps/desat_shorts_1.jpg',
 'phase_3/maps/desat_shorts_2.jpg',
 'phase_3/maps/desat_shorts_4.jpg',
 'phase_3/maps/desat_shorts_6.jpg',
 'phase_3/maps/desat_shorts_7.jpg',
 'phase_3/maps/desat_shorts_8.jpg',
 'phase_3/maps/desat_shorts_9.jpg',
 'phase_3/maps/desat_shorts_10.jpg',
 'phase_4/maps/VdayShorts2.jpg',
 'phase_4/maps/shorts4.jpg',
 'phase_4/maps/shorts1.jpg',
 'phase_4/maps/shorts5.jpg',
 'phase_4/maps/CowboyShorts1.jpg',
 'phase_4/maps/CowboyShorts2.jpg',
 'phase_4/maps/4thJulyShorts1.jpg',
 'phase_4/maps/shortsCat7_01.jpg',
 'phase_4/maps/Blue_shorts_1.jpg',
 'phase_4/maps/Red_shorts_1.jpg',
 'phase_4/maps/Purple_shorts_1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter2.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter3.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter4.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_valentine2.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_fishing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_party1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_summer1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween2.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_trolley1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween4.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween3.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistA.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistB.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistC.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_cogbuster.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloweenTurtle.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_greentoon1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racingGrandPrix.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_pirate.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_dinosaur.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf03.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf04.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf05.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_racing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_sora.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_slappy.jpg']
SHORTS = 0
SKIRT = 1
GirlBottoms = [('phase_3/maps/desat_skirt_1.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_2.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_3.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_4.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_5.jpg', SKIRT),
 ('phase_3/maps/desat_shorts_1.jpg', SHORTS),
 ('phase_3/maps/desat_shorts_5.jpg', SHORTS),
 ('phase_3/maps/desat_skirt_6.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_7.jpg', SKIRT),
 ('phase_3/maps/desat_shorts_10.jpg', SHORTS),
 ('phase_4/maps/female_skirt1.jpg', SKIRT),
 ('phase_4/maps/female_skirt2.jpg', SKIRT),
 ('phase_4/maps/female_skirt3.jpg', SKIRT),
 ('phase_4/maps/VdaySkirt1.jpg', SKIRT),
 ('phase_4/maps/skirtNew5.jpg', SKIRT),
 ('phase_4/maps/shorts5.jpg', SHORTS),
 ('phase_4/maps/CowboySkirt1.jpg', SKIRT),
 ('phase_4/maps/CowboySkirt2.jpg', SKIRT),
 ('phase_4/maps/4thJulySkirt1.jpg', SKIRT),
 ('phase_4/maps/skirtCat7_01.jpg', SKIRT),
 ('phase_4/maps/Blue_shorts_1.jpg', SHORTS),
 ('phase_4/maps/Red_shorts_1.jpg', SHORTS),
 ('phase_4/maps/Purple_shorts_1.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_skirt_winter1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_winter2.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_winter3.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_winter4.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_valentine1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_valentine2.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_fishing1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_gardening1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_party1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_racing1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_summer1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_golf1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_halloween1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_halloween2.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_saveBuilding1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_trolley1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_halloween3.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_halloween4.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_shorts_scientistA.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_shorts_scientistB.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_shorts_scientistC.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_cogbuster.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_halloween5.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_halloweenTurtle.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_skirt_greentoon1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_racingGrandPrix.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_bee.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_pirate.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_skirt_pirate.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_shorts_supertoon.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_vampire.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_dinosaur.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_skirt_golf02.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_racing03.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_golf03.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_golf04.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_racing04.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_racing05.jpg', SKIRT)]
 
ClothesColors = [VBase4(0.933594, 0.265625, 0.28125, 1.0),
 VBase4(0.863281, 0.40625, 0.417969, 1.0),
 VBase4(0.710938, 0.234375, 0.4375, 1.0),
 VBase4(0.992188, 0.480469, 0.167969, 1.0),
 VBase4(0.996094, 0.898438, 0.320312, 1.0),
 VBase4(0.550781, 0.824219, 0.324219, 1.0),
 VBase4(0.242188, 0.742188, 0.515625, 1.0),
 VBase4(0.433594, 0.90625, 0.835938, 1.0),
 VBase4(0.347656, 0.820312, 0.953125, 1.0),
 VBase4(0.191406, 0.5625, 0.773438, 1.0),
 VBase4(0.285156, 0.328125, 0.726562, 1.0),
 VBase4(0.460938, 0.378906, 0.824219, 1.0),
 VBase4(0.546875, 0.28125, 0.75, 1.0),
 VBase4(0.570312, 0.449219, 0.164062, 1.0),
 VBase4(0.640625, 0.355469, 0.269531, 1.0),
 VBase4(0.996094, 0.695312, 0.511719, 1.0),
 VBase4(0.832031, 0.5, 0.296875, 1.0),
 VBase4(0.992188, 0.480469, 0.167969, 1.0),
 VBase4(0.550781, 0.824219, 0.324219, 1.0),
 VBase4(0.433594, 0.90625, 0.835938, 1.0),
 VBase4(0.347656, 0.820312, 0.953125, 1.0),
 VBase4(0.96875, 0.691406, 0.699219, 1.0),
 VBase4(0.996094, 0.957031, 0.597656, 1.0),
 VBase4(0.855469, 0.933594, 0.492188, 1.0),
 VBase4(0.558594, 0.589844, 0.875, 1.0),
 VBase4(0.726562, 0.472656, 0.859375, 1.0),
 VBase4(0.898438, 0.617188, 0.90625, 1.0),
 VBase4(1.0, 1.0, 1.0, 1.0),
 VBase4(0.0, 0.2, 0.956862, 1.0),
 VBase4(0.972549, 0.094117, 0.094117, 1.0),
 VBase4(0.447058, 0.0, 0.90196, 1.0)]
 
allColorsList = [VBase4(1.0, 1.0, 1.0, 1.0),
 VBase4(0.96875, 0.691406, 0.699219, 1.0),
 VBase4(0.933594, 0.265625, 0.28125, 1.0),
 VBase4(0.863281, 0.40625, 0.417969, 1.0),
 VBase4(0.710938, 0.234375, 0.4375, 1.0),
 VBase4(0.570312, 0.449219, 0.164062, 1.0),
 VBase4(0.640625, 0.355469, 0.269531, 1.0),
 VBase4(0.996094, 0.695312, 0.511719, 1.0),
 VBase4(0.832031, 0.5, 0.296875, 1.0),
 VBase4(0.992188, 0.480469, 0.167969, 1.0),
 VBase4(0.996094, 0.898438, 0.320312, 1.0),
 VBase4(0.996094, 0.957031, 0.597656, 1.0),
 VBase4(0.855469, 0.933594, 0.492188, 1.0),
 VBase4(0.550781, 0.824219, 0.324219, 1.0),
 VBase4(0.242188, 0.742188, 0.515625, 1.0),
 VBase4(0.304688, 0.96875, 0.402344, 1.0),
 VBase4(0.433594, 0.90625, 0.835938, 1.0),
 VBase4(0.347656, 0.820312, 0.953125, 1.0),
 VBase4(0.191406, 0.5625, 0.773438, 1.0),
 VBase4(0.558594, 0.589844, 0.875, 1.0),
 VBase4(0.285156, 0.328125, 0.726562, 1.0),
 VBase4(0.460938, 0.378906, 0.824219, 1.0),
 VBase4(0.546875, 0.28125, 0.75, 1.0),
 VBase4(0.726562, 0.472656, 0.859375, 1.0),
 VBase4(0.898438, 0.617188, 0.90625, 1.0),
 VBase4(0.7, 0.7, 0.8, 1.0),
 VBase4(0.3, 0.3, 0.35, 1.0)]
 
MATColorsList = [VBase4(0.96875, 0.691406, 0.699219, 1.0),
 VBase4(0.933594, 0.265625, 0.28125, 1.0),
 VBase4(0.863281, 0.40625, 0.417969, 1.0),
 VBase4(0.710938, 0.234375, 0.4375, 1.0),
 VBase4(0.570312, 0.449219, 0.164062, 1.0),
 VBase4(0.640625, 0.355469, 0.269531, 1.0),
 VBase4(0.996094, 0.695312, 0.511719, 1.0),
 VBase4(0.832031, 0.5, 0.296875, 1.0),
 VBase4(0.992188, 0.480469, 0.167969, 1.0),
 VBase4(0.996094, 0.898438, 0.320312, 1.0),
 VBase4(0.996094, 0.957031, 0.597656, 1.0),
 VBase4(0.855469, 0.933594, 0.492188, 1.0),
 VBase4(0.550781, 0.824219, 0.324219, 1.0),
 VBase4(0.242188, 0.742188, 0.515625, 1.0),
 VBase4(0.304688, 0.96875, 0.402344, 1.0),
 VBase4(0.433594, 0.90625, 0.835938, 1.0),
 VBase4(0.347656, 0.820312, 0.953125, 1.0),
 VBase4(0.191406, 0.5625, 0.773438, 1.0),
 VBase4(0.558594, 0.589844, 0.875, 1.0),
 VBase4(0.285156, 0.328125, 0.726562, 1.0),
 VBase4(0.460938, 0.378906, 0.824219, 1.0),
 VBase4(0.546875, 0.28125, 0.75, 1.0),
 VBase4(0.726562, 0.472656, 0.859375, 1.0),
 VBase4(0.898438, 0.617188, 0.90625, 1.0),
 VBase4(0.7, 0.7, 0.8, 1.0),
 VBase4(0.3, 0.3, 0.35, 1.0)]
