import pygame
import sys

sys.path.append('../')

from Config import Config
from Helper import UIMaker

class SyncMoveScene:
    def __init__(self, screen):
        self.screen = screen
        self.footer_height = Config.FOOTER_SIZE
        self.exit_button = {
            "pos": (Config.WINDOW_SIZE[0] - 250, Config.WINDOW_SIZE[1] - 20),
            "size": (200, 50),
            "label": "Exit",
            "color": Config.BUTTON_NORMAL_COLOR
        }

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            button_rect = pygame.Rect(self.exit_button['pos'], self.exit_button['size'])
            if button_rect.collidepoint(mouse_pos):
                return False  # Returning False will indicate to exit this scene
        return True
    
    def run(self):
        running = True
        result = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    result = True

                running = self.handle_events(event)

            self.screen.fill(Config.WHITE)  # Clear the screen with a fixed color
    
            # Draw the footer
            UIMaker.draw_footer(
                self.screen, self.footer_height, Config.GREY, "Sync Move Scene",
                (20, Config.WINDOW_SIZE[1] - 20), self.exit_button,
                Config.BUTTON_FONT_SIZE, Config.BUTTON_TEXT_COLOR
            )
            
            pygame.display.flip()

        pygame.quit()
        sys.exit()