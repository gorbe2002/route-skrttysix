import pygame
from sys import exit

# game setup
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Route Skrtty-Six")
clock = pygame.time.Clock() 
game_active = False

# game logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
