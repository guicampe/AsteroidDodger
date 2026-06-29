import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import EVENT_ENEMY, SPAWN_TIME, C_WHITE, WIN_HEIGHT, C_GREEN, C_RED, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window: Surface, name: str, play: str, player_score: int):
        self.window = window
        self.name = name
        self.play = play
        self.current_scene = 1
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Bg', scene=self.current_scene))
        player = EntityFactory.get_entity('Player')
        player.score = player_score
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

        self.scene_start_time = pygame.time.get_ticks()
        self.scene_duration_ms = 10_000

    def change_scene(self, scene: int):
        self.current_scene = scene
        non_bg_entities = [e for e in self.entity_list if not e.name.startswith('Bg')]
        new_bgs = EntityFactory.get_entity('Bg', scene=self.current_scene)
        self.entity_list = new_bgs + non_bg_entities

    def check_scene_progress(self):
        elapsed = pygame.time.get_ticks() - self.scene_start_time
        if elapsed >= self.scene_duration_ms and self.current_scene < 4:
            self.change_scene(self.current_scene + 1)
            self.scene_start_time = pygame.time.get_ticks()

    def run(self, player_score: int):
        pygame.mixer_music.load('./asset/Level.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        game_over = False
        while True:
            clock.tick(60)

            player = next((e for e in self.entity_list if e.name == 'Player'), None)
            if player is not None and player.health <= 0:
                game_over = True

            if not game_over:
                self.check_scene_progress()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                if not game_over:
                    ent.move()
                if ent.name == 'Player':
                    self.level_text(20, f'Health {ent.health}', C_GREEN, (10, 0))
                    self.level_text(20, f'Score {ent.score}', C_GREEN, (10, 20))
                    player_score = ent.score

            if game_over:
                self.level_text(64, 'GAME', C_RED, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30), centered=True)
                self.level_text(64, 'OVER', C_RED, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 20), centered=True)
                self.level_text(28, f'Score: {player_score}', C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 80), centered=True)
                self.level_text(20, 'Press any key to return to main menu', C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 140), centered=True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY and not game_over:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
                if game_over and event.type == pygame.KEYDOWN:
                    return

            pygame.display.flip()

            if not game_over:
                EntityMediator.verify_collision(entity_list=self.entity_list)
                EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, centered: bool = False):
        text_font: Font = pygame.font.SysFont(name='Times New Roman', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        if centered:
            text_rect: Rect = text_surf.get_rect(center=text_pos)
        else:
            text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
