import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "#ffffff",  self.position, self.radius)
        
    def update(self, dt):
       self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        splitAngle = random.uniform(20,50)
        self.newAsteroid(splitAngle)
        self.newAsteroid(-splitAngle)
    
    def newAsteroid(self, angle):

        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = self.velocity.rotate(angle) * 1.2
        
