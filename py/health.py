import pygame.sprite
import game_settings
import random
import os

file_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.dirname(file_path)


class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(file_path, "img", "health.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = ((random.randint(100, game_settings.WIDTH - 100),
                              random.randint(100, game_settings.HEIGHT - 100)))
        self.points = 1
