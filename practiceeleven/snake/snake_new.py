import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Advanced")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)

# Score
score = 0

# 🍎 Food list (multiple foods now)
foods = []


# 🔹 Generate food with random weight and timer
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)

        if (x, y) not in snake:
            value = random.choice([1, 3, 5])  # different weights

            food = {
                "pos": (x, y),
                "value": value,
                "spawn_time": pygame.time.get_ticks(),
                "lifetime": random.randint(3000, 7000)  # 3–7 seconds
            }
            return food


# spawn first food
foods.append(generate_food())


# 🔹 Draw score
font = pygame.font.SysFont(None, 30)
def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            elif event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            elif event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)

    # Move snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # ❌ Wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # ❌ Self collision
    if head in snake:
        print("Game Over")
        pygame.quit()
        sys.exit()

    snake.insert(0, head)

    # ⏳ Remove expired food
    current_time = pygame.time.get_ticks()
    foods = [f for f in foods if current_time - f["spawn_time"] < f["lifetime"]]

    # 🍎 Check eating
    for food in foods:
        if head == food["pos"]:
            score += food["value"]
            foods.remove(food)
            foods.append(generate_food())
            break
    else:
        snake.pop()

    # 🆕 Ensure at least 1 food exists
    if len(foods) == 0:
        foods.append(generate_food())

    # Drawing
    screen.fill((0, 0, 0))

    # Snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    # 🍎 Draw foods with different colors based on value
    for food in foods:
        if food["value"] == 1:
            color = RED
        elif food["value"] == 3:
            color = YELLOW
        else:
            color = BLUE

        pygame.draw.rect(screen, color, (*food["pos"], CELL, CELL))

    draw_score()

    pygame.display.flip()
    clock.tick(8)