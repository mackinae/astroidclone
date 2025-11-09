import sys
import pygame
from constants import *
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt = 0
    
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable,drawable)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    astrofield = AsteroidField()
    player = Player(shots, x= SCREEN_WIDTH / 2, y= SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for astroid in asteroids:
            if astroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if astroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    astroid.split()
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()