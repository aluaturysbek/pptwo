import pygame
import random

WIDTH, HEIGHT = 600, 400
CELL = 20

WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (200,0,0)
DARK_RED = (120,0,0)

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(100,100),(80,100),(60,100)]
        self.direction = (20,0)
        self.score = 0
        self.level = 1
        self.speed = 7

        self.food = self.spawn_food()
        self.poison = self.spawn_food()

        self.obstacles = []
        self.shield = False

    def spawn_food(self):
        while True:
            pos = (random.randrange(0, WIDTH, CELL),
                   random.randrange(0, HEIGHT, CELL))
            if pos not in self.snake:
                return pos

    def spawn_obstacles(self):
        self.obstacles = []
        for _ in range(self.level * 3):
            self.obstacles.append(self.spawn_food())

    def move(self):
        head = (self.snake[0][0]+self.direction[0],
                self.snake[0][1]+self.direction[1])

        # walls
        if head[0]<0 or head[0]>=WIDTH or head[1]<0 or head[1]>=HEIGHT:
            if self.shield:
                self.shield = False
            else:
                return False

        # self collision
        if head in self.snake:
            if self.shield:
                self.shield = False
            else:
                return False

        # obstacle collision
        if head in self.obstacles:
            return False

        self.snake.insert(0, head)

        # food
        if head == self.food:
            self.score += 1
            self.food = self.spawn_food()

            if self.score % 4 == 0:
                self.level += 1
                self.speed += 1
                if self.level >= 3:
                    self.spawn_obstacles()
        else:
            self.snake.pop()

        # poison
        if head == self.poison:
            self.snake = self.snake[:-2]
            self.poison = self.spawn_food()

            if len(self.snake) <= 1:
                return False

        return True