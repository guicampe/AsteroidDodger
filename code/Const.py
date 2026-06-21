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
SPAWN_TIME = 1000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324