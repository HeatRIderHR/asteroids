import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from particles import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids')
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    timeClock = pygame.time.Clock()
    dt = 0 
    
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (explosions, updatable, drawable)
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    pygame.init()
    
    font = pygame.font.Font(None, 32)
    
    score = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black")
        
        for objects in drawable:
            objects.draw(screen)
            
        
        score += 1
        text = font.render(f"Score:{score}", True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 16, SCREEN_HEIGHT // 16)
        screen.blit(text, textRect)
        
        pygame.display.flip()
        if len(explosions) > 100:
            for explosion in explosions:
                explosion.hasNotSplit = False
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    explosion = Explosion(shot.position.x, shot.position.y)
                    asteroid.split()
                    shot.kill()
                
            if player.collision(asteroid):
                print(f"GAME OVER Score:{score}")
                return

        
        dt = timeClock.tick(60) / 1000

if __name__ == "__main__":
    main()
