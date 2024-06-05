import pygame
from Config import Config

class UIMaker:
    @staticmethod
    def draw_button(screen, color, position, size, text, font_size=36, text_color=(0, 0, 0)):
        font = pygame.font.Font(None, font_size)
        button_rect = pygame.Rect(position, size)
        pygame.draw.rect(screen, color, button_rect)
        
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    def is_hover(position, size):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(position, size)
        return button_rect.collidepoint(mouse_pos)
    
    @staticmethod
    def draw_footer(screen, footer_height, footer_color, text, text_position, button_props, font_size=36, text_color=(0, 0, 0)):
        # Draw the footer background
        footer_rect = pygame.Rect(0, Config.WINDOW_SIZE[1] - footer_height, Config.WINDOW_SIZE[0], footer_height)
        pygame.draw.rect(screen, footer_color, footer_rect)

        # Draw the text on the footer
        font = pygame.font.Font(None, font_size)
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(bottomleft=text_position)
        screen.blit(text_surf, text_rect)

        # Draw the button in the footer
        UIMaker.draw_button(screen, button_props['color'], button_props['pos'], button_props['size'], button_props['label'])

    @staticmethod
    def draw_text(screen, text, position, font_size=36, text_color=(0, 0, 0)):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, text_color)
        screen.blit(text_surface, position)