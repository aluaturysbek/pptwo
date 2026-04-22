import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Create screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# Font for score
font = pygame.font.SysFont("Arial", 20)

# Score
score = 0


# ---------------- ENEMY ----------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load and resize image
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 80))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 6)

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ---------------- PLAYER ----------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load and resize image
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (50, 80))

        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ---------------- COIN ----------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load and resize image
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5)

        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Create objects
P1 = Player()
E1 = Enemy()
C1 = Coin()


# ---------------- GAME LOOP ----------------
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update
    P1.update()
    E1.move()
    C1.move()

    # Coin collision
    if P1.rect.colliderect(C1.rect):
        score += 1
        C1.spawn()

    # Draw everything
    DISPLAYSURF.fill(WHITE)

    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    C1.draw(DISPLAYSURF)

    # Draw score (top right)
    score_text = font.render(f"Coins: {score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (280, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)