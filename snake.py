#https://www.youtube.com/watch?v=PGsuOm8PL_c
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 500))

rect = pygame.Rect(30, 50, 100, 10)

timer = pygame.time.Clock()

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pygame.Color("blue"))
    
    pygame.draw.rect(screen, pygame.Color("white"), rect)

    pygame.display.update()
    timer.tick(60)
