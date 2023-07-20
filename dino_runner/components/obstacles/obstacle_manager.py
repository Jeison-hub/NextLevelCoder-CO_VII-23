import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE
class ObstacleManager:

    def __init__(self, game):
        self.game = game
        self.has_obstacle = False
        self.obstacle = None 

    def update(self, game):
        self.create_obstacle()
        self.has_obstacle = self.obstacle.update(self.game.game_speed)
        if self.game.player.rect.colliderect(self.obstacle.rect):
            game.playing = False
            
            ##if game.player.type == SHIELD_TYPE:
                ##game.player.type = DEFAULT_TYPE
                ##self.has_obstacle = False
            ##else:
                #pygame.time.delay(400)
                #game.playing = False


    def create_obstacle(self):
        self.obstacle = Cactus()
        self.has_obstacle = True


    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)