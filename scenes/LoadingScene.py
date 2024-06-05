import sys
import pygame
import time

import mediapipe as mp
import pickle

sys.path.append('../')

from Config import Config
from Helper import UIMaker

class LoadingScene:
    def __init__(self, screen):
        self.screen = screen
        self.mp_drawing = None
        self.mp_holistic = None
        self.test = None
        self.model = None

    def display_loading_message(self, message="Loading..", progress=0):
        self.screen.fill(Config.WHITE)
        UIMaker.draw_text(self.screen, message, (Config.WINDOW_SIZE[0] // 2, Config.WINDOW_SIZE[1] // 2), font_size=30, text_color=Config.BLACK)
        # Draw a progress bar
        progress_width = 200  # Adjust the width of the progress bar
        progress_rect = pygame.Rect((Config.WINDOW_SIZE[0] // 2 - progress_width // 2, Config.WINDOW_SIZE[1] // 2 + 50), (progress_width * progress // 100, 20))
        pygame.draw.rect(self.screen, Config.BLACK, progress_rect)
        pygame.display.flip()

    def load_model(self):
        with open('models/boxing_form_v3.pkl', 'rb') as f:
            self.model = pickle.load(f)

    def load_resources(self):
        self.display_loading_message("Loading Resources..")
        time.sleep(1)

        global mp_drawing, mp_holistic, test
        mp_drawing = mp.solutions.drawing_utils
        mp_holistic = mp.solutions.holistic
        self.test = "test"

        self.mp_drawing = mp_drawing
        self.mp_holistic = mp_holistic
        self.model = self.load_model()

        for progress in range(0, 101, 10):
            self.display_loading_message("Loading Resources..", progress)
            time.sleep(0.5)

        self.display_loading_message("Resources loaded successfully!")
        time.sleep(1)  # Short pause to show the message

    