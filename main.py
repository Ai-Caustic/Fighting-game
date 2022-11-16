import pygame

pygame.init()

# Create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

# Load background image
bg_image = pygame.image.load("")

# Game loop
run = True
while run:

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# exit pygame
pygame.quit()
