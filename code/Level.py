import sys

import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, play):
        self.window = window
        self.name = name
        self.play = play
        self.current_scene = 1
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Bg', scene=self.current_scene))

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()