import pygame
from ball import Ball

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball Game")

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Create the Ball object and pass the screen reference, width, and height
ball = Ball(screen, screen_width, screen_height)

# Main game loop
running = True
while running:
    # Fill the screen with white background
    screen.fill((255, 255, 255))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key events for movement
    keys = pygame.key.get_pressed()
    ball.move(keys)

    # Draw the ball on the screen
    ball.draw()

    # Update the display
    pygame.display.update()

    # Control the frame rate (60 frames per second)
    clock.tick(60)

# Quit pygame
pygame.quit()