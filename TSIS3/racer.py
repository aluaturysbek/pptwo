import pygame, random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# ---------------- PLAYER ----------------
class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/Player.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect(center=(200, 500))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# ---------------- TRAFFIC ----------------
class TrafficCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(50, 300)
        self.rect.y = -100
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# ---------------- COIN ----------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base = pygame.image.load("assets/Coin.png")

        self.value = random.choice([1, 3, 5])

        size = 20 if self.value == 1 else 30 if self.value == 3 else 40
        self.image = pygame.transform.scale(self.base, (size, size))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 300)
        self.rect.y = -50

    def update(self):
        self.rect.y += 4
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# ---------------- POWERUP ----------------
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["nitro", "shield", "repair"])

        self.image = pygame.Surface((25, 25))
        self.image.fill((0, 255, 0) if self.type == "nitro"
                        else (0, 0, 255) if self.type == "shield"
                        else (255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 300)
        self.rect.y = -60

    def update(self):
        self.rect.y += 3
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()