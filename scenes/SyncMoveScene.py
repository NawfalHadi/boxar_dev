import pygame
import sys

from .LoadingScene import LoadingScene

sys.path.append('../')

from Config import Config
from Helper import UIMaker

# =============
import mediapipe as mp
import numpy as np
import cv2
# ==============

class SyncMoveScene:
    def __init__(self, screen):
        self.screen = screen
        self.footer_height = Config.FOOTER_SIZE
        self.exit_button = {
            "pos": (Config.WINDOW_SIZE[0] - 250, Config.WINDOW_SIZE[1] - 20),
            "size": (100, 50),
            "label": "Exit",
            "color": Config.BUTTON_NORMAL_COLOR
        }

        self.mp_drawing = None
        self.mp_holistic = None

        # Initialize OpenCV capture
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            sys.exit()
        
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            button_rect = pygame.Rect(self.exit_button['pos'], self.exit_button['size'])
            if button_rect.collidepoint(mouse_pos):
                return False  # Returning False will indicate to exit this scene
        return True
    
    def run(self):
        loading_scene = LoadingScene(self.screen)
        loading_scene.load_resources()

        self.mp_drawing = loading_scene.mp_drawing
        self.mp_holistic = loading_scene.mp_holistic

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

            ret, frame = self.cap.read()
            if not ret:
                print("Error: Could not read frame.")
                continue

            # Convert the frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the image to a Pygame surface
            frame = np.rot90(frame)  # Rotate if needed to fit the orientation
            frame_surface = pygame.surfarray.make_surface(frame)
            
            # Calculate the position to place the camera feed
            camera_rect = frame_surface.get_rect(topleft=(0, 0))

            # Blit the camera feed onto the screen
            self.screen.blit(frame_surface, camera_rect)

            text_position = (20, Config.WINDOW_SIZE[1] - self.footer_height - 40)
            UIMaker.draw_text(self.screen, loading_scene.test, text_position, font_size=24, text_color=Config.BLACK)


            # Draw the footer
            UIMaker.draw_footer(
                self.screen,
                self.footer_height,
                Config.BLACK, "Sync Move Scene",
                (20, Config.WINDOW_SIZE[1] - 20),
                self.exit_button,
                Config.BUTTON_FONT_SIZE, Config.BUTTON_TEXT_COLOR
            )
            
            pygame.display.flip()

        self.cap.release()
        pygame.quit()
        sys.exit()