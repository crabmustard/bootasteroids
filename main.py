import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateables, drawables) 
    Asteroid.containers = (asteroids, drawables, updateables)
    AsteroidField.containers = updateables
    Shot.containers = (updateables, drawables, shots)

    asteroid_field = AsteroidField()

    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateables:
            obj.update(dt)
        
        for ast in asteroids:
            if ast.collides_with(player):
                print("Game Over")
                sys.exit()
            for bullet in shots:
                if ast.collides_with(bullet):
                    ast.split()
                    bullet.kill()
        screen.fill("black")

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FRAMES_PER_SECOND) / 1000
        
        



if __name__ == "__main__":
    main()

