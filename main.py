import pygame
from sys import exit

# classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/player/f1car.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (250,475))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 5

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 5

    def apply_barriers(self):
        if self.rect.left < 100: self.rect.left = 100
        if self.rect.right > 400: self.rect.right = 400

    def update(self):
        self.player_input()
        self.apply_barriers()

# helper functions
def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = font.render(f"Score: {current_time}", True, "Black")
    score_rect = score_surf.get_rect(center = (250,30))
    screen.blit(score_surf, score_rect)
    return current_time

# game setup
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Route Skrtty-Six")
clock = pygame.time.Clock()
font = pygame.font.Font("graphics/SuperBoy.ttf", 30)
game_active = True # change to False when intro screen is added
start_time = 0
score = 0

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
        score = display_score()

        player.draw(screen)
        player.update()

    pygame.display.update()
    clock.tick(60)
