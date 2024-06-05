import pygame
import sys

sys.path.append('../../')

from Config import Config
from Helper import UIMaker

class TutorialScene:
    def __init__(self, screen):
        self.screen = screen
        self.footer_height = Config.FOOTER_SIZE
        
    def handle_events(self, event):
        pass

    def run(self):
        pass