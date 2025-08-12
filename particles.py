import pygame
from constants import *
from circleshape import CircleShape
import random

class Explosion(CircleShape):
    def __init__(self, x, y, radius = EXPLOSION_MAX_SIZE):
        super().__init__(x, y, radius)
        self.lifeTime = EXPLOSION_LIFE_TIME
        self.hasNotSplit = True
        
    def draw(self, screen):
        pygame.draw.circle(screen, "#dd0022",  self.position, self.radius)
        
    def update(self, dt):
        if self.hasNotSplit:
            self.hasNotSplit = False
            self.split()
        self.lifeTime -= 1 *dt
        self.radius = EXPLOSION_MAX_SIZE * (self.lifeTime / EXPLOSION_LIFE_TIME)
        if self.lifeTime <= 0:
            self.kill()
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius == EXPLOSION_MIN_SIZE:
            return
        for i in range(0 , 5):
            splitAngle = random.uniform(0,360)
            self.newExplosion(splitAngle)

    
    def newExplosion(self, angle):
        
        explosion = Explosion(self.position.x, self.position.y, self.radius - EXPLOSION_DECAY)
        explosion.velocity = (pygame.Vector2(0, random.randint(50, 250)).rotate(angle))
        explosion.size = random.randint(EXPLOSION_MIN_SIZE, EXPLOSION_MAX_SIZE)
        explosion.hasNotSplit = False
        self.kill()
        