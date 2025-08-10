import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shotCoolDown = 0 
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "#ffffff", self.triangle(), 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
            
            
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
        self.shotCoolDown -= dt
        if keys[pygame.K_SPACE]:
            
            if self.shotCoolDown <= 0:
                self.shotCoolDown = PLAYER_SHOOT_COOLDOWN
                self.shoot()
            
    def rotate(self, dt):
        
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, self.rotation)
        
        
        
        
class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
    def draw(self, screen):
        pygame.draw.circle(screen, "#ffffff",  self.position, SHOT_RADIUS)
        
    def update(self, dt):
       self.position += pygame.Vector2(0, 1).rotate(self.rotation) * 500 * dt
   
    def collision(self, other):
       pass