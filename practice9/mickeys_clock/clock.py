import pygame
import time
import math

class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.clock_center = (300, 300)

        # Load Mickey Mouse hand images
        self.right_hand = pygame.image.load("images/left_hand.png")
        self.left_hand = pygame.image.load("images/left_hand.png")

    def calculate_angle(self, hand_type, current_time):
        if hand_type == "minute":
            return 6 * current_time  # Every minute moves 6 degrees
        elif hand_type == "second":
            return 6 * current_time  # Every second moves 6 degrees

    def rotate_image(self, image, angle):
        return pygame.transform.rotate(image, angle)

    def update(self):
        # Get current time (minutes and seconds)
        current_time = time.localtime()
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Calculate the rotation angles for both hands
        minute_angle = self.calculate_angle("minute", minutes)
        second_angle = self.calculate_angle("second", seconds)

        # Rotate the hands
        right_hand_rotated = self.rotate_image(self.right_hand, -minute_angle)
        left_hand_rotated = self.rotate_image(self.left_hand, -second_angle)

        # Position the hands on the clock
        right_hand_rect = right_hand_rotated.get_rect(center=self.clock_center)
        left_hand_rect = left_hand_rotated.get_rect(center=self.clock_center)

        # Draw the hands on the screen
        self.screen.blit(right_hand_rotated, right_hand_rect)
        self.screen.blit(left_hand_rotated, left_hand_rect)

        # Draw the clock center (for reference)
        pygame.draw.circle(self.screen, (255, 255, 255), self.clock_center, 5)