import pygame

class UIMaker:
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