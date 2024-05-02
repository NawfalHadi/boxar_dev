import pygame, sys

sys.path.append('../../')

from Config import Config
from Helper import UIMaker

class ShadowBoxScene:
    def __init__(self, screen, init_value):
        self.screen = screen
        self.init_value = init_value  # Value passed from Sync Move Scene

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            self.screen.fill(Config.WHITE)
            font = pygame.font.Font(None, 36)
            status_text = "Shadow Boxing: Active" if self.init_value else "Shadow Boxing: Inactive"
            text_surf = font.render(status_text, True, Config.BLACK)
            text_rect = text_surf.get_rect(center=(Config.WINDOW_SIZE[0] // 2, Config.WINDOW_SIZE[1] // 2))
            self.screen.blit(text_surf, text_rect)

            pygame.display.flip()

        return None