# B
import pygame

BACKGROUND_SCENES = {
    1: ['Bg0', 'Bg1', 'Bg2', 'Bg3'],
    2: ['Bg4', 'Bg5', 'Bg6'],
    3: ['Bg7', 'Bg8'],
    4: ['Bg9', 'Bg10']
}

# C
C_WHITE = (255, 255, 255)
C_ORANGE = (255, 128, 0)
C_RED = (255, 0, 0)
C_YELLOW = (255, 255, 128)
C_GREEN = (0, 255, 0)
C_ORANGE_STRONG = (255, 165, 0)

# E
ENTITY_SPEED = {
    'Bg0': 2,
    'Bg1': 3,
    'Bg2': 1,
    'Bg3': 4,
    'Bg4': 2,
    'Bg5': 1,
    'Bg6': 3,
    'Bg7': 2,
    'Bg8': 1,
    'Bg9': 2,
    'Bg10': 1,
    'Player': 3,
}

ENTITY_HEALTH = {
    'Bg0': 999,
    'Bg1': 999,
    'Bg2': 999,
    'Bg3': 999,
    'Bg4': 999,
    'Bg5': 999,
    'Bg6': 999,
    'Bg7': 999,
    'Bg8': 999,
    'Bg9': 999,
    'Bg10': 999,
    'Player': 3,
    'Bomb_01': 1,
    'Bomb_02': 1,
    'Crystal': 1,
    'Meteor_01': 1,
    'Meteor_02': 1,
    'Meteor_03': 1,
    'Meteor_04': 1,
    'Meteor_05': 1,
    'Meteor_06': 1,
    'Meteor_07': 1,
    'Meteor_08': 1,
    'Meteor_09': 1,
    'Meteor_10': 1,
}

EVENT_ENEMY = pygame.USEREVENT + 1

ENEMY_LIST = (
    'Bomb_01',
    'Bomb_02',
    'Crystal',
    'Meteor_01',
    'Meteor_02',
    'Meteor_03',
    'Meteor_04',
    'Meteor_05',
    'Meteor_06',
    'Meteor_07',
    'Meteor_08',
    'Meteor_09',
    'Meteor_10'
)

ENEMY_SPEED = {
    'Bomb_01': 5,
    'Bomb_02': 5,
    'Crystal': 3,
    'Meteor_01': 4,
    'Meteor_02': 3,
    'Meteor_03': 5,
    'Meteor_04': 4,
    'Meteor_05': 6,
    'Meteor_06': 4,
    'Meteor_07': 5,
    'Meteor_08': 4,
    'Meteor_09': 5,
    'Meteor_10': 2,
}

ENTITY_DAMAGE = {
    'Bg0': 0,
    'Bg1': 0,
    'Bg2': 0,
    'Bg3': 0,
    'Bg4': 0,
    'Bg5': 0,
    'Bg6': 0,
    'Bg7': 0,
    'Bg8': 0,
    'Bg9': 0,
    'Bg10': 0,
    'Player': 1,
    'Bomb_01': 1,
    'Bomb_02': 1,
    'Crystal': 1,
    'Meteor_01': 1,
    'Meteor_02': 1,
    'Meteor_03': 1,
    'Meteor_04': 1,
    'Meteor_05': 1,
    'Meteor_06': 1,
    'Meteor_07': 1,
    'Meteor_08': 1,
    'Meteor_09': 1,
    'Meteor_10': 1,
}

ENTITY_SCORE = {
    'Bg0': 0,
    'Bg1': 0,
    'Bg2': 0,
    'Bg3': 0,
    'Bg4': 0,
    'Bg5': 0,
    'Bg6': 0,
    'Bg7': 0,
    'Bg8': 0,
    'Bg9': 0,
    'Bg10': 0,
    'Player': 0,
    'Bomb_01': 1,
    'Bomb_02': 1,
    'Crystal': 1,
    'Meteor_01': 1,
    'Meteor_02': 1,
    'Meteor_03': 1,
    'Meteor_04': 1,
    'Meteor_05': 1,
    'Meteor_06': 1,
    'Meteor_07': 1,
    'Meteor_08': 1,
    'Meteor_09': 1,
    'Meteor_10': 1,
}

# M
MENU_OPTION = ('PLAY',
               'EXIT'
               )

# P
PLAYER_KEY_UP = pygame.K_UP
PLAYER_KEY_DOWN = pygame.K_DOWN
PLAYER_KEY_LEFT = pygame.K_LEFT
PLAYER_KEY_RIGHT = pygame.K_RIGHT

# S
SPAWN_TIME = 500

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324