import pygame.sprite
import game_settings
import player_bullet
import os

file_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.dirname(file_path)


class Player(pygame.sprite.Sprite):
    def __init__(self, player_bullet_group):
        super().__init__()
        self.player_images = {
            "south": pygame.image.load(os.path.join(file_path, "img", "spaceship_south.png")),
            "north": pygame.image.load(os.path.join(file_path, "img", "spaceship_north.png")),
            "east": pygame.image.load(os.path.join(file_path, "img", "spaceship_east.png")),
            "west": pygame.image.load(os.path.join(file_path, "img", "spaceship_west.png")),
            "southeast": pygame.image.load(os.path.join(file_path, "img", "spaceship_southeast.png")),
            "northeast": pygame.image.load(os.path.join(file_path, "img", "spaceship_northeast.png")),
            "southwest": pygame.image.load(os.path.join(file_path, "img", "spaceship_southwest.png")),
            "northwest": pygame.image.load(os.path.join(file_path, "img", "spaceship_northwest.png")),
        }
        self.player_bullet_images = {
            "northwest+southeast": pygame.image.load(
                os.path.join(file_path, "img", "player_bullet_northwest+southeast.png")),
            "northeast+southwest": pygame.image.load(
                os.path.join(file_path, "img", "player_bullet_northeast+southwest.png")),
            "east+west": pygame.image.load(os.path.join(file_path, "img", "player_bullet_east+west.png")),
            "north+south": pygame.image.load(os.path.join(file_path, "img", "player_bullet_north+south.png")),
        }
        self.image = self.player_images["south"]
        self.player_bullet_image = self.player_bullet_images["north+south"]
        self.rect = self.image.get_rect()
        self.player_bullet_group = player_bullet_group
        self.rect.centerx = game_settings.WIDTH // 2
        self.rect.top = game_settings.HEIGHT // 2
        # Player Variables
        self.speed = 7
        self.health = 3
        self.direction_x = 0
        self.direction_y = 1
        self.is_alive = True
        self.invincible = False
        self.invincibility_time = 0
        self.bullet_sound = pygame.mixer.Sound(os.path.join(file_path, "audio", "player_bullet.wav"))
        self.time = pygame.time.get_ticks()

    def update(self):
        self.move()
        self.shoot()

    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.is_alive and pygame.time.get_ticks() - self.time > 125 and len(
                self.player_bullet_group) < 6:
            self.bullet_sound.play()
            self.time = pygame.time.get_ticks()
            if self.direction_x == 0 and self.direction_y == 1:
                player_bullet.PlayerBullet(self.rect.left, self.rect.centery, self.player_bullet_group,
                                          self.player_bullet_image, self.direction_x, self.direction_y)
                player_bullet.PlayerBullet(self.rect.right, self.rect.centery, self.player_bullet_group,
                                          self.player_bullet_image, self.direction_x, self.direction_y)
            elif self.direction_x == 0 and self.direction_y == -1:
                player_bullet.PlayerBullet(self.rect.left, self.rect.centery, self.player_bullet_group,
                                          self.player_bullet_image, self.direction_x, self.direction_y)
                player_bullet.PlayerBullet(self.rect.right, self.rect.centery, self.player_bullet_group,
                                          self.player_bullet_image, self.direction_x, self.direction_y)
            else:
                player_bullet.PlayerBullet(self.rect.centerx, self.rect.top, self.player_bullet_group,
                                          self.player_bullet_image, self.direction_x, self.direction_y)
                player_bullet.PlayerBullet(self.rect.centerx, self.rect.bottom, self.player_bullet_group,
                                          self.player_bullet_image, self.direction_x, self.direction_y)

    def reset(self):
        self.rect.centerx = game_settings.WIDTH // 2
        self.invincible = True
        self.invincibility_time = pygame.time.get_ticks()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_UP] and self.rect.top > 0 and self.rect.left > 0:
            self.image = self.player_images["southeast"]
            self.player_bullet_image = self.player_bullet_images["northwest+southeast"]
            self.direction_x = 1
            self.direction_y = 1
            self.rect.x -= self.speed - 2
            self.rect.y -= self.speed - 2
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and self.rect.bottom < game_settings.HEIGHT and self.rect.left > 0:
            self.image = self.player_images["northeast"]
            self.player_bullet_image = self.player_bullet_images["northeast+southwest"]
            self.direction_x = 1
            self.direction_y = -1
            self.rect.x -= self.speed - 2
            self.rect.y += self.speed - 2
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP] and self.rect.right < game_settings.WIDTH and self.rect.top > 100:
            self.image = self.player_images["southwest"]
            self.player_bullet_image = self.player_bullet_images["northeast+southwest"]
            self.direction_x = -1
            self.direction_y = 1
            self.rect.x += self.speed - 2
            self.rect.y -= self.speed - 2
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and self.rect.right < game_settings.WIDTH and self.rect.bottom < game_settings.HEIGHT:
            self.image = self.player_images["northwest"]
            self.player_bullet_image = self.player_bullet_images["northwest+southeast"]
            self.direction_x = -1
            self.direction_y = -1
            self.rect.x += self.speed - 2
            self.rect.y += self.speed - 2
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.image = self.player_images["east"]
            self.player_bullet_image = self.player_bullet_images["east+west"]
            self.direction_x = 1
            self.direction_y = 0
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.right < game_settings.WIDTH:
            self.image = self.player_images["west"]
            self.player_bullet_image = self.player_bullet_images["east+west"]
            self.direction_x = -1
            self.direction_y = 0
            self.rect.x += self.speed
        elif keys[pygame.K_UP] and self.rect.top > 0:
            self.image = self.player_images["south"]
            self.player_bullet_image = self.player_bullet_images["north+south"]
            self.direction_x = 0
            self.direction_y = 1
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.bottom < game_settings.HEIGHT:
            self.image = self.player_images["north"]
            self.player_bullet_image = self.player_bullet_images["north+south"]
            self.direction_x = 0
            self.direction_y = -1
            self.rect.y += self.speed
