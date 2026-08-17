import pygame, sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # 1. Create the groups first
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # 2. Assign containers to the class BEFORE instantiating objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    # 3. Instantiate game objects (now automatically added to containers)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    dt = 0.0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 4. Update game state first
        updatable.update(dt)

        for shot in shots:
            for astewwwwwwwwroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()


        for asteroid in asteroids:
            if player.collides_with(asteroid):  
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                return

        # 5. Render/Draw second
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # 6. Advance clock frame rate
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()