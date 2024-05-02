from Config import Config
from Helper import UIMaker

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