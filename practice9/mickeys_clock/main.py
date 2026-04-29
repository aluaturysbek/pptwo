import pygame
import time
from clock import Clock

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey's Clock")

# Load clock object
clock = Clock(screen)

# Main loop
running = True
while running:
    screen.fill((173, 216, 230))  # Fill screen with color

    # Update and draw the clock
    clock.update()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()