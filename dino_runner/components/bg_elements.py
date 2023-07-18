import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD

class Cloud:
    cloud_x = 600, 80
    cloud_y = 1000, 120
    cloud_speed = 14

    def update (self, game_speed):
        for cloud_id in range(len(self.cloud_speed)):
            self.cloud_x[cloud_id] -= game_speed * self.cloud_speed[cloud_id]
    
    def draw (self, screen):
        self.draw_cloud(screen)

    def draw_cloud(self, screen):
        for cloud_id in range (len(self.cloud_x)):
            if self.cloud_x[cloud_id] + screen.get_width() <= -CLOUD.get_width():
                self.cloud_x[cloud_id] = random.randrange(0, 150)
                self.cloud_y[cloud_id] = random.randrange(0, 125)
                self.cloud_speed[cloud_id] = random.randrange (3,17)/10
            screen.blit(CLOUD, (screen.get_width() + self.cloud_x[cloud_id], self.cloud_y[cloud_id]))    
