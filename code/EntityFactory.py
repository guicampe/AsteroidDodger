import random

from code.Enemy import Enemy
from code.Background import Background
from code.Const import WIN_WIDTH, BACKGROUND_SCENES, WIN_HEIGHT
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0), scene: int = 1):
        match entity_name:
            case 'Bg':
                list_bg = []
                for bg_name in BACKGROUND_SCENES[scene]:
                    list_bg.append(Background(bg_name, (0, 0)))
                    list_bg.append(Background(bg_name, (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, (WIN_HEIGHT / 2)))
            case 'Meteor_01':
                return Enemy('Meteor_01', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Meteor_02':
                return Enemy('Meteor_02', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))