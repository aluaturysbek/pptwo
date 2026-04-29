import pygame, sys
from racer import Player, TrafficCar, Coin, PowerUp
from persistence import save_score, load_scores, save_settings, load_settings
from ui import Button

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20)

# ---------------- STATES ----------------
STATE = "menu"

# ---------------- LOAD DATA ----------------
settings = load_settings()

player = Player()
coins = pygame.sprite.Group()
traffic = pygame.sprite.Group()
powerups = pygame.sprite.Group()

score = 0
distance = 0
player_name = "Player"

# ---------------- UI ----------------
play_btn = Button(150, 200, 100, 40, "PLAY")
quit_btn = Button(150, 260, 100, 40, "QUIT")

def reset_game():
    global score, distance, traffic, coins
    score = 0
    distance = 0
    traffic.empty()
    coins.empty()

# ---------------- MAIN LOOP ----------------
while True:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ---------------- MENU ----------------
    if STATE == "menu":
        if play_btn.draw(screen):
            reset_game()
            STATE = "play"

        if quit_btn.draw(screen):
            pygame.quit()
            sys.exit()

    # ---------------- GAME ----------------
    elif STATE == "play":
        player.update()

        # spawn objects
        if len(traffic) < 3:
            traffic.add(TrafficCar())

        if len(coins) < 2:
            coins.add(Coin())

        if len(powerups) < 1:
            powerups.add(PowerUp())

        # update objects
        traffic.update()
        coins.update()
        powerups.update()

        # collision coins
        for coin in pygame.sprite.spritecollide(player, coins, True):
            score += coin.value

        # collision traffic → game over
        if pygame.sprite.spritecollide(player, traffic, False):
            save_score(player_name, score, distance)
            STATE = "gameover"

        # distance
        distance += 1

        # draw
        player.draw(screen)
        traffic.draw(screen)
        coins.draw(screen)
        powerups.draw(screen)

        text = font.render(f"Score: {score} Distance: {distance}", True, (255,255,255))
        screen.blit(text, (10,10))

    # ---------------- GAME OVER ----------------
    elif STATE == "gameover":
        msg = font.render("GAME OVER - Press M for Menu", True, (255,255,255))
        screen.blit(msg, (60, 250))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]:
            STATE = "menu"

    pygame.display.update()
    clock.tick(60)