import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import EVENT_ENEMY, SPAWN_TIME, C_WHITE, WIN_HEIGHT, C_GREEN
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name, play):
        self.window = window
        self.name = name
        self.play = play
        self.current_scene = 1
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Bg', scene=self.current_scene))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

        self.scene_start_time = pygame.time.get_ticks()
        self.scene_duration_ms = 10_000

    def change_scene(self, scene: int):
        self.current_scene = scene
        self.entity_list = [e for e in self.entity_list if not e.name.startswith('Bg')]
        self.entity_list.extend(EntityFactory.get_entity('Bg', scene=self.current_scene))

    def check_scene_progress(self):
        elapsed = pygame.time.get_ticks() - self.scene_start_time
        if elapsed >= self.scene_duration_ms and self.current_scene < 4:
            self.change_scene(self.current_scene + 1)
            self.scene_start_time = pygame.time.get_ticks()

    def run(self):
        # music
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.check_scene_progress()
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if ent.name == 'Player':
                    self.level_text(20, f'Health {ent.health}', C_GREEN, (10, 0))
                    self.level_text(20, f'Score {ent.score}', C_GREEN, (10, 20))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Times New Roman', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
