import pygame.sprite
import game_settings


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, player_bullet_group, image, direction_x, direction_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.speed = 7
        player_bullet_group.add(self)

    def update(self):
        self.move()
        if (self.rect.bottom < 0 or self.rect.top > game_settings.HEIGHT) \
                or (self.rect.left < 0 or self.rect.right > game_settings.WIDTH):
            self.kill()

    def move(self):
        self.rect.x -= self.speed * 1.5 * self.direction_x
        self.rect.y -= self.speed * 1.5 * self.direction_y
