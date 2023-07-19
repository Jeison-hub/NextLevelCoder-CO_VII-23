import pygame
import random
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
class ObstacleManager:

    def __init__(self, game):
        self.game = game
        self.has_obstacle = False
        self.obstacle = None 

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()
            
        self.has_obstacle = self.obstacle.update(self.game.game_speed)
        if self.game.player.rect.colliderect(self.obstacle.rect):
            pygame.time.delay(600)
            game.playing = False


    def create_obstacle(self):
        obstacle_type = random.choice([Cactus, Bird])
        self.obstacle = obstacle_type()
        self.has_obstacle = True

    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)