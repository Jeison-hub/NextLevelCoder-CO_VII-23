import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING, CLOUD


class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    DUCK_POS_Y = 340
    JUMP_VEL = 8

    def __init__(self):
        super().__init__()
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jumping_velocity = self.JUMP_VEL
        self.cloud_obj1 = CLOUD(CLOUD, 600, 80)
        self.cloud_obj2 = CLOUD(CLOUD, 1000, 120)

    def update(self, user_input,speed):
        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.running:
            self.run()
        if self.step_index >= 10:
            self.step_index = 0

        if (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.jumping:
            self.running = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.running = False
            self.ducking = False
            self.jumping = True
        elif not self.jumping:
            self.running = True
            self.ducking = False
            self.jumping = False

        self.cloud_obj1.update(speed * 0.5)
        self.cloud_obj2.update(speed * 0.5)

    def draw(self, screen):
        self.cloud_obj1.draw(screen)
        self.cloud_obj2.draw(screen)
     
        screen.blit(self.image, self.rect)

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jumping_velocity * 4
        self.jumping_velocity -= 0.8
        if self.rect.y >= self.POS_Y:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jumping_velocity = self.JUMP_VEL

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.DUCK_POS_Y
        self.step_index += 1

  