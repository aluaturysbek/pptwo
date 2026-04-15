import pygame
import time
import math

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey's Clock")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load Mickey Mouse hand images (You will need to replace these with your actual image paths)
right_hand = pygame.image.load("right_hand.png")  # Right hand (minutes hand)
left_hand = pygame.image.load("left_hand.png")  # Left hand (seconds hand)

# Set the center of the clock
clock_center = (300, 300)

# Function to calculate the angle for the minute and second hands
def calculate_angle(hand_type, current_time):
    if hand_type == "minute":
        # The angle for minutes: 360 degrees / 60 minutes
        return 6 * current_time  # Every minute moves 6 degrees
    elif hand_type == "second":
        # The angle for seconds: 360 degrees / 60 seconds
        return 6 * current_time  # Every second moves 6 degrees

# Function to rotate an image to a specific angle
def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    # Fill screen with black
    screen.fill(BLACK)

    # Get current time (seconds and minutes)
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate the rotation angles for both hands
    minute_angle = calculate_angle("minute", minutes)
    second_angle = calculate_angle("second", seconds)

    # Rotate the hands
    right_hand_rotated = rotate_image(right_hand, -minute_angle)  # Negative for clockwise rotation
    left_hand_rotated = rotate_image(left_hand, -second_angle)

    # Position the hands on the clock
    right_hand_rect = right_hand_rotated.get_rect(center=clock_center)
    left_hand_rect = left_hand_rotated.get_rect(center=clock_center)

    # Draw the hands on the screen
    screen.blit(right_hand_rotated, right_hand_rect)
    screen.blit(left_hand_rotated, left_hand_rect)

    # Draw the clock center (for reference)
    pygame.draw.circle(screen, WHITE, clock_center, 5)

    # Update the display
    pygame.display.update()

    # Limit frames per second to 60 (update every second)
    clock.tick(60)

    # Handle quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()