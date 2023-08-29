import pygame
from nastroiki import *
class Player():
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.speed = 2.1

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.x += self.speed * cos_a
            self.y += self.speed * sin_a
        if keys[pygame.K_DOWN]:
            self.x += -self.speed * cos_a
            self.y += -self.speed * sin_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02



