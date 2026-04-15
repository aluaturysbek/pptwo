import pygame

class Ball:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen  # Store the screen reference
        self.radius = 25
        self.color = (255, 0, 0)  # Red color
        self.x = screen_width // 2  # Start position (centered)
        self.y = screen_height // 2
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 20  # Move by 20 pixels per key press

    def move(self, keys):
        # Move the ball based on arrow key input
        if keys[pygame.K_LEFT]:
            if self.x - self.radius - self.speed >= 0:
                self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            if self.x + self.radius + self.speed <= self.screen_width:
                self.x += self.speed
        if keys[pygame.K_UP]:
            if self.y - self.radius - self.speed >= 0:
                self.y -= self.speed
        if keys[pygame.K_DOWN]:
            if self.y + self.radius + self.speed <= self.screen_height:
                self.y += self.speed

    def draw(self):
        # Draw the ball on the screen
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)