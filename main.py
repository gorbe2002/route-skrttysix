import pygame
from sys import exit

# classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/player/f1car.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (250,500))

# game setup
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Route Skrtty-Six")
clock = pygame.time.Clock() 
game_active = True # change to False when intro screen is added

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

# Background
background_surf = pygame.image.load("graphics/background.png").convert()

# game logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.blit(background_surf, (0,0))

        player.draw(screen)

    pygame.display.update()
    clock.tick(60)
