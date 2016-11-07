import sys
import pygame

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            sys.exit()

    screen.fill(pygame.Color("black"))
    pygame.display.flip()
    clock.tick(60)
