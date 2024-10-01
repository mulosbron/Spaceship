import pygame
import os

file_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.dirname(file_path)


class Collision(pygame.sprite.Sprite):
    def __init__(self, center, entity):
        super().__init__()
        self.entity = entity
        self.image = pygame.image.load(os.path.join(file_path, "img", f"{self.entity}.png"))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.time = pygame.time.get_ticks()

    def update(self):
        if self.entity == "meteor_explosion" and pygame.time.get_ticks() - self.time > 3000:
            self.kill()
        elif self.entity == "player_explosion" and pygame.time.get_ticks() - self.time > 5000:
            self.kill()
