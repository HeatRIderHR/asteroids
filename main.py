import pygame
from constants import *
from player import *
from circleshape import *


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    timeClock = pygame.time.Clock()
    dt = 0 
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        pygame.display.flip()
        
        player1.draw(screen)
        
        dt = timeClock.tick(60) / 1000

if __name__ == "__main__":
    main()
