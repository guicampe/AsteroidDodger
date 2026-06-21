import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_ORANGE, WIN_WIDTH, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # music
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, 'Aster   id', C_WHITE, (256, 45))
            self.menu_text(60, 'D  dger', C_WHITE, (320, 73))

            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i], C_ORANGE, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='MS Mincho', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)