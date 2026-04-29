import pygame

WHITE = (255,255,255)

def draw_text(screen, text, x, y):
    font = pygame.font.SysFont(None, 30)
    img = font.render(text, True, WHITE)
    screen.blit(img, (x,y))


def main_menu(screen):
    screen.fill((0,0,0))
    draw_text(screen, "1. Play", 250, 150)
    draw_text(screen, "2. Leaderboard", 250, 200)
    draw_text(screen, "3. Settings", 250, 250)