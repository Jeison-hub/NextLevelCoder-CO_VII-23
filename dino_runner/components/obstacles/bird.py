import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self):
        image_list = BIRD
        selected_image = random.choice(image_list)
        super().__init__(selected_image)
        self.rect.y = random.choice([370, 310, 350])  
        self.speed = 15
        self.index = 0
        self.counter = 0

    def update(self, speed):
        self.rect.x -= self.speed

  
        if self.counter % 5 == 0:
            self.index += 1
        self.counter += 1
        if self.index >= len(BIRD):
            self.index = 0
        self.image = BIRD[self.index]

   
        if self.rect.y == 250:
            self.rect.y = random.choice([270, 310, 350])
        elif self.rect.y == 380:
            self.rect.y = random.choice([250, 390, 350, 400])
        elif self.rect.y == 250:
            self.rect.y = random.choice([265, 300, 350])

        
        if self.rect.right < 0:
           
            return False

        return True

    
   