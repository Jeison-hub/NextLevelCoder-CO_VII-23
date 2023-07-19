import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        image_list = BIRD
        selected_image = random.choice(image_list)
        super().__init__(selected_image)
        self.rect.y = 150

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else Bird[1]
        self.rect = self.image.get_rect()
        self.rect.y = self.POS_Y
        self.step_index += 1
