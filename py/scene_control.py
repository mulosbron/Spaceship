import game_settings


class SceneControl:
    def __init__(self, menu_object, game_object, scores_object):
        self.game_object = game_object
        self.menu_object = menu_object
        self.scores_object = scores_object
        self.status = "main_menu"

    def update(self):
        if self.status == "main_menu":
            action = self.menu_object.check_controls()
            if action == "play":
                self.status = "play"
            elif action == "score":
                self.status = "score"
            elif action == "exit":
                self.status = "exit"
                game_settings.running = False

        elif self.status == "play":
            self.game_object.update()
            if self.game_object.player_object.health <= 0:
                self.status = "main_menu"
                self.game_object.reset_game()
                self.game_object.reset()

        elif self.status == "score":
            action = self.scores_object.check_controls()
            if action == "main_menu":
                self.status = "main_menu"

    def draw(self):
        if self.status == "main_menu":
            self.menu_object.draw_background()
            self.menu_object.draw_buttons()
        elif self.status == "play":
            self.game_object.draw_background()
            self.game_object.draw_hud()
            self.game_object.draw_collisions()
        elif self.status == "score":
            self.scores_object.draw_background()
            self.scores_object.draw()
