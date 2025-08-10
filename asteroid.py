import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "#ffffff",  self.position, self.radius)
        
    def update(self, dt):
       self.position += self.velocity * dt
        
    def asteroids():
       pass
   
    def collision(self, other):
       pass