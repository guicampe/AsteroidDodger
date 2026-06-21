import random

from code.Enemy import Enemy
from code.Background import Background
from code.Const import WIN_WIDTH, BACKGROUND_SCENES, WIN_HEIGHT, ENEMY_LIST
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
            case 'Enemy':
                enemy_name = random.choice(ENEMY_LIST)
                spawn_y = random.randint(30, WIN_HEIGHT - 30)
                return Enemy(enemy_name, (WIN_WIDTH, spawn_y))
