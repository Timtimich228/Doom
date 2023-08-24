import pygame
from nastroiki import *
class Player():
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.speed = 2.1

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.x += self.speed * math.cos(self.angle)
            self.y -= self.speed * math.sin(self.angle)
        if key[pygame.K_UP]:
            self.x -= self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)
        if key[pygame.K_LEFT]:
            self.angle -= 0.03

        if key[pygame.K_RIGHT]:
            self.angle += 0.03

