import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # size of each snake block

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Clock (controls speed)
clock = pygame.time.Clock()
speed = 7  # initial speed

# Font for score/level
font = pygame.font.SysFont(None, 30)

# Snake initial position
snake = [(100, 100), (80, 100), (60, 100)]
direction = (20, 0)  # moving right

# Score & level
score = 0
level = 1


# Function to generate food NOT on snake
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if (x, y) not in snake:
            return (x, y)


food = generate_food()


# Function to draw text (score & level)
def draw_info():
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))


# Game loop
while True:
    # Handle events (keyboard, quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Change direction with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 20):
                direction = (0, -20)
            if event.key == pygame.K_DOWN and direction != (0, -20):
                direction = (0, 20)
            if event.key == pygame.K_LEFT and direction != (20, 0):
                direction = (-20, 0)
            if event.key == pygame.K_RIGHT and direction != (-20, 0):
                direction = (20, 0)

    # Move snake
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    new_head = (head_x, head_y)

    # 🚧 Check wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over! Hit the wall.")
        pygame.quit()
        sys.exit()

    # 🚧 Check collision with itself
    if new_head in snake:
        print("Game Over! Hit yourself.")
        pygame.quit()
        sys.exit()

    # Add new head
    snake.insert(0, new_head)

    # 🍎 Check if food eaten
    if new_head == food:
        score += 1
        food = generate_food()  # new food

        # 🎯 Level system (every 4 points)
        if score % 4 == 0:
            level += 1
            speed += 2  # increase speed

    else:
        snake.pop()  # remove tail if no food eaten

    # Drawing
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Draw score & level
    draw_info()

    pygame.display.update()

    # Control speed
    clock.tick(speed)