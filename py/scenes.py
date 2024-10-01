import pygame
import game_settings
import meteor
import collision
import health
import os
from player import Player
import csv
from datetime import datetime

file_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.dirname(file_path)


def draw_text(text, font, color, window, x, y):
    text_object = font.render(text, 1, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    window.blit(text_object, text_rect)


class Game:
    def __init__(self, player_group, player_bullet_group, meteor_group, health_group):
        self.level_no = 0
        self.score = 0
        self.time_elapsed = 0
        self.paused = False
        self.start_time = pygame.time.get_ticks()
        # Groups
        self.meteor_group = meteor_group
        self.health_group = health_group
        self.player_group = player_group
        self.player_object = self.player_group.sprites()[0]
        self.player_bullet_group = player_bullet_group
        self.collision_group = pygame.sprite.Group()
        # Background
        self.background = pygame.image.load(os.path.join(file_path, "img", "background2.png"))
        # Sounds and Music
        self.meteor_explosion_sound = pygame.mixer.Sound(os.path.join(file_path, "audio", "player_hit.wav"))
        self.player_explosion_sound = pygame.mixer.Sound(os.path.join(file_path, "audio", "meteor_hit.wav"))
        self.health_effect_sound = pygame.mixer.Sound(os.path.join(file_path, "audio", "health.wav"))
        pygame.mixer.music.load(os.path.join(file_path, "audio", "background_music.wav"))
        pygame.mixer.music.play(-1)
        # Game Font
        self.font = pygame.font.Font(os.path.join(file_path, "font", "game_font.ttf"), 64)

    def update(self):
        self.check_collisions()
        self.collision_group.update()
        self.check_level_completion()
        self.check_invincibility()
        self.calculate_time()

    def reset(self):
        self.level_no = 0
        self.score = 0
        self.time_elapsed = 0
        self.start_time = pygame.time.get_ticks()

        self.meteor_group.empty()
        self.health_group.empty()
        self.player_group.empty()
        self.player_bullet_group.empty()
        self.collision_group.empty()

        player_object = Player(self.player_bullet_group)
        self.player_group.add(player_object)
        self.player_object = player_object

        self.spawn_meteors()

    def check_invincibility(self):
        if self.player_object.invincible:
            if pygame.time.get_ticks() - self.player_object.invincibility_time > 2000:
                self.player_object.invincible = False

    def spawn_meteors(self):
        meteor_reduction = 1
        self.level_no += 1
        if self.level_no != 1:
            self.spawn_health()
        if self.level_no > 5:
            meteor_reduction = 5
        for i in range(2 + ((3 * self.level_no) // meteor_reduction)):
            meteor_object = meteor.Meteor()
            self.meteor_group.add(meteor_object)
        if self.level_no > 3:
            for i in range(3 * (self.level_no // 3)):
                meteor_object = meteor.Meteor2()
                self.meteor_group.add(meteor_object)

    def spawn_health(self):
        health_object = health.Health()
        self.health_group.add(health_object)

    def check_level_completion(self):
        if not self.meteor_group:
            if self.player_object.health > 0:
                self.spawn_meteors()

    def check_collisions(self):
        bullet_meteor_collisions = pygame.sprite.groupcollide(self.player_bullet_group, self.meteor_group, True, True)
        for collided in bullet_meteor_collisions.values():
            for meteor_object in collided:
                self.score += meteor_object.points
                effect_type = "meteor_explosion"
                explosion = collision.Collision(meteor_object.rect.center, effect_type)
                self.meteor_explosion_sound.play()
                self.collision_group.add(explosion)

        if not self.player_object.invincible:
            player_meteor_collision = pygame.sprite.groupcollide(self.player_group, self.meteor_group, False, True)
            for collided in player_meteor_collision:
                effect_type = "player_explosion"
                explosion = collision.Collision(self.player_object.rect.center, effect_type)
                self.collision_group.add(explosion)
                self.player_explosion_sound.play()
                collided.health -= 1
                if collided.health <= 0:
                    self.player_group.remove(collided)
                self.check_game_status()

        player_health_collision = pygame.sprite.groupcollide(self.player_group, self.health_group, False, True)
        for player, health_items in player_health_collision.items():
            for health_object in health_items:
                player.health += health_object.points
                self.health_effect_sound.play()

    def check_game_status(self):
        self.player_bullet_group.empty()
        self.player_object.reset()
        if self.player_object.health != 0:
            self.pause()

    def pause(self):
        self.paused = True
        draw_text("You hit a meteor!",
                  self.font,
                  (0, 206, 209),
                  game_settings.window,
                  100, 200)
        draw_text("Press 'ENTER' to continue!",
                  self.font,
                  (0, 206, 209),
                  game_settings.window,
                  100, 350)

        self.player_object.rect.centerx = game_settings.WIDTH / 2
        self.player_object.rect.centery = game_settings.HEIGHT / 2

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.paused = False
                        self.start_time = pygame.time.get_ticks() - self.time_elapsed * 1000
                        return
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()

    def draw_background(self):
        game_settings.window.blit(self.background, (0, 0))

    def create_hud(self, text, size, color, position):
        hud_surface = pygame.Surface(size)
        hud_surface.set_colorkey((0, 0, 0))
        hud_text = self.font.render(text, True, color)
        hud_surface.blit(hud_text, (0, 0))
        game_settings.window.blit(hud_surface, position)

    def draw_hud(self):
        self.create_hud("Health: " + str(self.player_object.health),
                        (300, 100),
                        (0, 206, 209),
                        (game_settings.WIDTH - 225, 10))

        self.create_hud("Level: " + str(self.level_no),
                        (300, 100),
                        (0, 206, 209),
                        (game_settings.WIDTH - 225, 75))

        self.create_hud("Score: " + str(self.score),
                        (300, 100),
                        (0, 206, 209),
                        (15, 10))

        self.create_hud("Time: " + str(self.time_elapsed),
                        (300, 100),
                        (0, 206, 209),
                        (15, 75))

    def draw_collisions(self):
        self.collision_group.draw(game_settings.window)

    def calculate_score(self):
        time_score = self.time_elapsed // 5
        level_score = self.level_no * 10
        self.score = self.score + level_score - time_score

    def save_score(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score_file_path = os.path.join(file_path, 'score', 'scores.csv')

        with open(score_file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, self.score])

    def reset_game(self):
        self.calculate_score()
        self.save_score()

        draw_text(f"TOTAL SCORE: {self.score}",
                  self.font,
                  (0, 206, 209),
                  game_settings.window,
                  100, 150)

        draw_text("You have lost all your lives!",
                  self.font,
                  (0, 206, 209),
                  game_settings.window,
                  100, 250)

        draw_text("Press 'ENTER' to return to the main menu!",
                  self.font,
                  (0, 206, 209),
                  game_settings.window,
                  100, 350)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "enter_pressed"
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()

    def calculate_time(self):
        if not self.paused:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
            self.time_elapsed = elapsed_time


class MainMenu:
    def __init__(self, window):
        self.play_button, self.scores_button, self.exit_button = None, None, None
        self.mouse_x, self.mouse_y = 0, 0
        self.clicked = False
        self.window = window
        self.font = pygame.font.Font(os.path.join(file_path, "font", "game_font.ttf"), 64)
        self.background = pygame.image.load(os.path.join(file_path, "img", "background1.png"))

    def update(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.check_controls()

    def draw_buttons(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.play_button = pygame.Rect(50, 200, 200, 75)
        self.scores_button = pygame.Rect(50, 300, 200, 75)
        self.exit_button = pygame.Rect(50, 400, 200, 75)

        transparent_surface = pygame.Surface((200, 75), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 0))
        self.window.blit(transparent_surface, (50, 200))
        self.window.blit(transparent_surface, (50, 300))
        self.window.blit(transparent_surface, (50, 400))

        play_color = (127, 255, 212) if self.play_button.collidepoint(self.mouse_x, self.mouse_y) else (0, 206, 209)
        scores_color = (127, 255, 212) if self.scores_button.collidepoint(self.mouse_x, self.mouse_y) else (0, 206, 209)
        exit_color = (127, 255, 212) if self.exit_button.collidepoint(self.mouse_x, self.mouse_y) else (0, 206, 209)

        draw_text("Play", self.font, play_color, self.window, 50, 200)
        draw_text("Scores", self.font, scores_color, self.window, 50, 300)
        draw_text("Exit", self.font, exit_color, self.window, 50, 400)

    def check_controls(self):
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        if not self.clicked and mouse_pressed:
            if self.play_button.collidepoint(mouse_pos):
                self.clicked = True
                return "play"
            elif self.scores_button.collidepoint(mouse_pos):
                self.clicked = True
                return "score"
            elif self.exit_button.collidepoint(mouse_pos):
                self.clicked = True
                return "exit"

        if not mouse_pressed:
            self.clicked = False

    def draw_background(self):
        game_settings.window.blit(self.background, (0, 0))


class Scores:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(os.path.join(file_path, "font", "game_font.ttf"), 64)
        self.score_list = ""
        self.background = pygame.image.load(os.path.join(file_path, "img", "background3.png"))
        self.status = ""

    def fetch_scores(self):
        score_file_path = os.path.join(file_path, 'score', 'scores.csv')
        scores = []
        with open(score_file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
                score = int(row[1])
                scores.append((date, score))

        scores.sort(key=lambda x: (-x[1], x[0]))
        self.score_list = scores

    def draw_background(self):
        game_settings.window.blit(self.background, (0, 0))
        self.fetch_scores()

    def draw(self):
        for i, (date, score) in enumerate(self.score_list[:10]):
            text = f"{i + 1}. Score: {score} - Date: {date.strftime('%Y-%m-%d %H:%M:%S')}"
            draw_text(text, self.font, (0, 206, 209), self.window, 50, 50 + i * 50)
        draw_text("Press 'ENTER' to return to the main menu", self.font, (0, 206, 209), self.window, 50, 600)

    def check_controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return "main_menu"
