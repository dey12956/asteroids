import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    score = 0
    font = pygame.font.SysFont("Chalkduster", 36) 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    lives = 5
    heart_img = pygame.image.load("heart.png").convert_alpha()
    heart_img = pygame.transform.scale(heart_img, (36, 36))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    flicker_timer = 0

    AsteroidField()

    while True:
        # exit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update objects
        updatable.update(dt)

        # paint the screen black
        screen.fill((0, 0, 0))

        #draw objects
        for thing in drawable:
            flicker_timer += dt
            if player.invincible and isinstance(thing, Player):
                if int(flicker_timer / 0.2) % 2 == 0:
                    continue
            thing.draw(screen)

        # rendering score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # rendering lives
        for i in range(lives):
            screen.blit(heart_img, (10 + i * 35, 50))

        # new frame
        pygame.display.flip()

        # collision mechanisms
        if not player.invincible:
            for asteroid in asteroids:
                if asteroid.detect_collision(player):
                    lives -= 1
                    if lives > 0:
                        player.respawn()
                    else:
                        game_over_text = font.render("GAME OVER!", True, (255, 255, 255))
                        screen.blit(game_over_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                        sys.exit()
                for shot in shots:
                    if asteroid.detect_collision(shot):
                        asteroid.split()
                        shot.kill()
                        score += 1

        player.respawn_update(dt)

        # fps = 60, calculate dt
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()