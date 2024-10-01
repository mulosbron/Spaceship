import pygame.sprite
import game_settings
import random
import os

file_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.dirname(file_path)


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(file_path, "img", "meteorite.png"))
        self.rect = self.image.get_rect()
        self.speed = 3
        self.points = 5
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])
        coordinate_options = [
            {'x': (game_settings.WIDTH // 2, game_settings.WIDTH), 'y': (0, 5)},
            {'x': (game_settings.WIDTH - 5, game_settings.WIDTH), 'y': (0, game_settings.HEIGHT // 2)},
            {'x': (0, game_settings.WIDTH // 2), 'y': (0, 5)},
            {'x': (0, 5), 'y': (0, game_settings.HEIGHT // 2)},
            {'x': (0, game_settings.WIDTH // 2), 'y': (game_settings.HEIGHT - 5, game_settings.HEIGHT)},
            {'x': (0, 5), 'y': (game_settings.HEIGHT // 2, game_settings.HEIGHT)},
            {'x': (game_settings.WIDTH // 2, game_settings.WIDTH), 'y': (game_settings.HEIGHT - 5, game_settings.HEIGHT)},
            {'x': (game_settings.WIDTH - 5, game_settings.WIDTH), 'y': (game_settings.HEIGHT // 2, game_settings.HEIGHT)}
        ]
        selected = random.choice(coordinate_options)
        self.rect.centerx = random.randint(*selected['x'])
        self.rect.centery = random.randint(*selected['y'])

    def update(self):
        self.move()

    def move(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        if self.rect.left <= -50 or self.rect.right >= game_settings.WIDTH + 50:
            self.direction_x *= -1
        if self.rect.top <= -50 or self.rect.bottom >= game_settings.HEIGHT + 50:
            self.direction_y *= -1


class Meteor2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(file_path, "img", "meteorite2.png"))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.points = 10
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])
        coordinate_options = [
            {'x': (game_settings.WIDTH // 2, game_settings.WIDTH), 'y': (0, 5)},
            {'x': (game_settings.WIDTH - 5, game_settings.WIDTH), 'y': (0, game_settings.HEIGHT // 2)},
            {'x': (0, game_settings.WIDTH // 2), 'y': (0, 5)},
            {'x': (0, 5), 'y': (0, game_settings.HEIGHT // 2)},
            {'x': (0, game_settings.WIDTH // 2), 'y': (game_settings.HEIGHT - 5, game_settings.HEIGHT)},
            {'x': (0, 5), 'y': (game_settings.HEIGHT // 2, game_settings.HEIGHT)},
            {'x': (game_settings.WIDTH // 2, game_settings.WIDTH), 'y': (game_settings.HEIGHT - 5, game_settings.HEIGHT)},
            {'x': (game_settings.WIDTH - 5, game_settings.WIDTH), 'y': (game_settings.HEIGHT // 2, game_settings.HEIGHT)}
        ]
        selected = random.choice(coordinate_options)
        self.rect.centerx = random.randint(*selected['x'])
        self.rect.centery = random.randint(*selected['y'])

    def update(self):
        self.move()

    def move(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        if self.rect.left <= -50 or self.rect.right >= game_settings.WIDTH + 50:
            self.direction_x *= -1
        if self.rect.top <= -50 or self.rect.bottom >= game_settings.HEIGHT + 50:
            self.direction_y *= -1
