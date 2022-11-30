import pygame

from fighter import Fighter

pygame.init()

# Create game window
SCREEN_SIZE = (1000, 600)
screen = pygame.display.set_mode(size=(SCREEN_SIZE))
pygame.display.set_caption("Fighting Legend")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# Define colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

# Load background image
bg_image = pygame.image.load(
    "Assets/images/background/background.jpg").convert_alpha()

# load sprite sheets

warrior_sheet = pygame.image.load(
    "Assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load(
    "Assets/images/wizard/Sprites/wizard.png").convert_alpha()

# Define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

# Drawing background image


def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_SIZE))
    screen.blit(scaled_bg, (0, 0))

# drawing health bars


def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))


# Create two instances of fighters
scorpion = Fighter(200, 310, False, WARRIOR_DATA, warrior_sheet,
                   WARRIOR_ANIMATION_STEPS)
subzero = Fighter(700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)

# Game loop
run = True
while run:

    clock.tick(FPS)

    # draw background image
    draw_bg()

    # show player stats
    draw_health_bar(scorpion.health, 20, 20)
    draw_health_bar(subzero.health, 580, 20)

    # move fighters
    scorpion.move(SCREEN_SIZE[0], SCREEN_SIZE[1], screen, subzero)

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
