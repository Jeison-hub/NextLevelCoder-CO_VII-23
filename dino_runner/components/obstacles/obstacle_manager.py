import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.highjump import HighJump  # Importa la clase HighJump
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE

class ObstacleManager:

    def __init__(self, game):
        self.game = game
        self.has_obstacle = False
        self.obstacle = None
        self.is_invulnerable = False  # Bandera para indicar si el jugador es invulnerable con el escudo

    def update(self, game):
        if not self.has_obstacle:
            self.create_obstacle()

        if self.has_obstacle:
            if not self.is_invulnerable:
                self.has_obstacle = self.obstacle.update(self.game.game_speed)

                # Manejar colisión entre el jugador y el obstáculo
                if self.game.player.rect.colliderect(self.obstacle.rect):
                    if isinstance(self.obstacle, Shield):  # Verificar si el obstáculo es de tipo Shield
                        self.game.player.type = SHIELD_TYPE  # Obtener el shield
                        self.is_invulnerable = True  # Hacer al jugador invulnerable con el escudo
                        self.has_obstacle = False  # Eliminar el shield del juego
                    else:
                        if self.game.player.type == SHIELD_TYPE:
                            self.game.player.type = DEFAULT_TYPE
                        pygame.time.delay(400)
                        game.playing = False

            else:
                self.is_invulnerable = False  # Perder la invulnerabilidad después de colisionar con un obstáculo

    def create_obstacle(self):
        obstacle_type = random.choice(["cactus", "bird", "shield", "highjump"])  # Agregar "highjump" a la lista
        if obstacle_type == "cactus":
            self.obstacle = Cactus()
        elif obstacle_type == "bird":
            self.obstacle = Bird()
        elif obstacle_type == "shield":  # Agregar la condición para "shield"
            self.obstacle = Shield()
        else:  # Agregar la condición para "highjump"
            self.obstacle = HighJump()
        self.has_obstacle = True

    def draw(self, screen):
        if self.has_obstacle:
            self.obstacle.draw(screen)
