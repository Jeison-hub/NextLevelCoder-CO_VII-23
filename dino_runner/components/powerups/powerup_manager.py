import pygame
import random
from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.components.powerups.shield import Shield
from dino_runner.utils.constants import HIGHJUMP, HIGHJUMP_TYPE, SHIELD_TYPE

class PowerUpManager:

    def __init__(self, game):
        self.game = game
        self.current_powerup = None
        self.has_powerup = False
        self.next_powerup_show = 10

    def update(self, game):
        if not self.has_powerup and game.score == self.next_powerup_show:
            self.create_powerup()
        if self.has_powerup:
            self.has_powerup = self.current_powerup.update(game.game_speed)
            if game.player.rect.colliderect(self.current_powerup.rect):
                self.has_powerup = False
                self.next_powerup_show = self.generate_next_powerup_show()

    def generate_next_powerup_show(self):
        return random.randint(200, 500)

    def create_powerup(self):
        powerup_type = random.choice([SHIELD_TYPE, HIGHJUMP_TYPE])
        if powerup_type == SHIELD_TYPE:
            self.current_powerup = Shield()
        else:
            self.current_powerup = HIGHJUMP()
        self.has_powerup = True

    def draw(self, screen):
        if self.has_powerup:
            self.current_powerup.draw(screen)
   
          