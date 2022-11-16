import pygame

from fighter import Fighter

pygame.init()

# Create game window
SCREEN_SIZE = (1000, 600)
screen = pygame.display.set_mode(size=(SCREEN_SIZE))
pygame.display.set_caption("Brawler")

# set framerate
clock = pygame.time.Clock()
FPS = 60


# Load background image
bg_image = pygame.image.load(
    "Assets/images/background/background.jpg").convert_alpha()

# Function for drawing background image


def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_SIZE))
    screen.blit(scaled_bg, (0, 0))


# Create two instances of fighters
scorpion = Fighter(200, 310)
subzero = Fighter(700, 310)

# Game loop
run = True
while run:

    clock.tick(FPS)

    # draw background image
    draw_bg()

    # move fighters
    scorpion.move()
    subzero.move()

    # Draw fighter
    scorpion.draw(screen)
    subzero.draw(screen)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()


# exit pygame
pygame.quit()
