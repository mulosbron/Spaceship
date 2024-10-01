import pygame
import player
from scenes import MainMenu, Game, Scores
from scene_control import SceneControl

WIDTH, HEIGHT = 1250, 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
running = True


def start():
    # Pygame Initialization
    pygame.init()

    # FPS
    FPS = 120
    clock = pygame.time.Clock()

    # Player Bullet Group
    player_bullet_group = pygame.sprite.Group()

    # Player Group
    player_group = pygame.sprite.Group()
    player_object = player.Player(player_bullet_group)
    player_group.add(player_object)

    # Meteorite Group
    meteorite_group = pygame.sprite.Group()

    # Health Group
    health_group = pygame.sprite.Group()

    # Game Class
    game_object = Game(player_group, player_bullet_group, meteorite_group, health_group)
    menu_object = MainMenu(window)
    scores_object = Scores(window)
    scene_object = SceneControl(menu_object, game_object, scores_object)

    # Game Loop
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game
        scene_object.update()
        if scene_object.status == "main_menu":
            scene_object.draw()
        elif scene_object.status == "score":
            scene_object.draw()
        elif scene_object.status == "play":
            # Game
            scene_object.draw()
            # Meteorite
            meteorite_group.update()
            meteorite_group.draw(window)
            # Health
            health_group.update()
            health_group.draw(window)
            # Player
            player_group.update()
            player_group.draw(window)
            # Player Bullet
            player_bullet_group.update()
            player_bullet_group.draw(window)

        # Window Update and FPS
        pygame.display.flip()
        clock.tick(FPS)

    # Quit Game
    pygame.quit()
