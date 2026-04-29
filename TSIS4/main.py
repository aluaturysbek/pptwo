import pygame
import sys
from game import SnakeGame
from db import *
from settings import load_settings
from ui import *

pygame.init()

screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

game = SnakeGame()
settings = load_settings()

state = "MENU"
username = ""
player_id = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == "MENU" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                player_id = get_or_create_player(username)
                state = "GAME"
            else:
                username += event.unicode

        if state == "GAME":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.direction = (0,-20)
                if event.key == pygame.K_DOWN:
                    game.direction = (0,20)
                if event.key == pygame.K_LEFT:
                    game.direction = (-20,0)
                if event.key == pygame.K_RIGHT:
                    game.direction = (20,0)

    # STATES
    if state == "MENU":
        screen.fill((0,0,0))
        draw_text(screen, "Enter Username: " + username, 150, 150)

    elif state == "GAME":
        alive = game.move()

        if not alive:
            save_game(player_id, game.score, game.level)
            state = "MENU"
            game.reset()
            username = ""

        screen.fill((0,0,0))

        for s in game.snake:
            pygame.draw.rect(screen,(0,200,0),(*s,20,20))

        pygame.draw.rect(screen,(255,0,0),(*game.food,20,20))
        pygame.draw.rect(screen,(120,0,0),(*game.poison,20,20))

        for o in game.obstacles:
            pygame.draw.rect(screen,(100,100,100),(*o,20,20))

    pygame.display.update()
    clock.tick(game.speed)