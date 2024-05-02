from Config import Config
from Helper import UIMaker

from scenes.SyncMoveScene import SyncMoveScene
from scenes.ShadowBoxing.ShadowboxScene import ShadowBoxScene

import pygame
import sys

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode(Config.WINDOW_SIZE)
pygame.display.set_caption(Config.WINDOW_TITLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                for key, value in Config.MENUS.items():
                    button_rect = pygame.Rect(value['pos'], value['size'])
                    if button_rect.collidepoint(mouse_pos):
                        
                        if key == "shadow_box":
                            # Run Sync Move Scene
                            sync_scene = SyncMoveScene(screen)
                            result = sync_scene.run()
                            # Transition to Shadow Box Scene with the result from Sync Move Scene
                            shadow_box_scene = ShadowBoxScene(screen, result)
                            shadow_box_scene.run()

    screen.fill(Config.WHITE)

    # Draw buttons using the properties from Config
    for key, attrs in Config.MENUS.items():
        pos, size, label = attrs['pos'], attrs['size'], attrs['label']

        color = Config.BUTTON_NORMAL_COLOR if not UIMaker.is_hover(pos, size) else Config.BUTTON_HOVER_COLOR
        UIMaker.draw_button(screen, color, pos, size, label, Config.BUTTON_FONT_SIZE, Config.BUTTON_TEXT_COLOR)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()