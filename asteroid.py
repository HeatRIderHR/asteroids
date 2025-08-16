import pygame
from constants import *
from circleshape import CircleShape
import random
from updateFunctions import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.timeAlive = 0
    def draw(self, screen):
        pygame.draw.circle(screen, "#ffffff",  self.position, self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
        self.timeAlive += 1 * dt
        if self.timeAlive > 3:
            print(self.position)
            self.position = screenWrapEntity(self.position)
        
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
        
