import pygame, sys
from pygame.locals import *
import random

pygame.init()

# ---------------- SETTINGS ----------------
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Speed control
enemy_speed = 6
speed_increase_step = 5   # every 5 coins → increase speed

# Score
score = 0

# Create screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# Font for UI
font = pygame.font.SysFont("Arial", 20)


# ---------------- ENEMY ----------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load and resize image
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 80))

        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        # Random position at top
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global enemy_speed

        # Move down using dynamic speed
        self.rect.move_ip(0, enemy_speed)

        # Respawn when off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ---------------- PLAYER ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (50, 80))

        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        # Move left
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        # Move right
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ---------------- COIN ----------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load base image
        self.base_image = pygame.image.load("Coin.png")

        self.set_random_coin()

    def set_random_coin(self):
        """
        Randomly assign weight (value) and size
        """
        # Possible coin values
        self.value = random.choice([1, 3, 5])

        # Size depends on value
        if self.value == 1:
            size = (20, 20)
        elif self.value == 3:
            size = (30, 30)
        else:
            size = (40, 40)

        # Resize image
        self.image = pygame.transform.scale(self.base_image, size)
        self.rect = self.image.get_rect()

        # Spawn at random position at top
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        # Move down
        self.rect.move_ip(0, 5)

        # Respawn if off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.set_random_coin()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ---------------- CREATE OBJECTS ----------------
P1 = Player()
E1 = Enemy()
C1 = Coin()


# ---------------- GAME LOOP ----------------
while True:

    # Handle quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update objects
    P1.update()
    E1.move()
    C1.move()

    # ---------------- COLLISION ----------------
    if P1.rect.colliderect(C1.rect):
        score += C1.value   # add coin value instead of +1
        C1.set_random_coin()

        # Increase enemy speed every N coins
        if score % speed_increase_step == 0:
            enemy_speed += 1

    # ---------------- DRAW ----------------
    DISPLAYSURF.fill(WHITE)

    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)

    # Display score (top right)
    score_text = font.render(f"Score: {score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (260, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)