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
    'Meteor_01': 5,
    'Meteor_02': 5,
}

EVENT_ENEMY = pygame.USEREVENT + 1

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
SPAWN_TIME = 2500

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324