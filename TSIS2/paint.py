import pygame
import datetime
from tools import flood_fill

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Final Paint")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
color = (0, 0, 255)

screen.fill(BLACK)

# Modes
mode = "pencil"

# Brush size
radius = 5

# Drawing helpers
start_pos = None
last_pos = None
temp_surface = screen.copy()

# Text tool
text_mode = False
input_text = ""
text_pos = (0, 0)


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # ⌨️ Keyboard
        if event.type == pygame.KEYDOWN:

            # Colors
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_y:
                color = (255, 255, 0)

            # Modes
            elif event.key == pygame.K_q:
                mode = "pencil"
            elif event.key == pygame.K_w:
                mode = "line"
            elif event.key == pygame.K_e:
                mode = "rect"
            elif event.key == pygame.K_t:
                mode = "circle"
            elif event.key == pygame.K_f:
                mode = "fill"
            elif event.key == pygame.K_x:
                mode = "text"
            elif event.key == pygame.K_z:
                mode = "erase"

            # Brush sizes
            elif event.key == pygame.K_1:
                radius = 2
            elif event.key == pygame.K_2:
                radius = 5
            elif event.key == pygame.K_3:
                radius = 10

            # Save
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                pygame.image.save(screen, filename)
                print("Saved:", filename)

            # Clear
            elif event.key == pygame.K_c:
                screen.fill(BLACK)
                temp_surface = screen.copy()

            # Text input
            if text_mode:
                if event.key == pygame.K_RETURN:
                    font = pygame.font.SysFont(None, 30)
                    txt = font.render(input_text, True, color)
                    screen.blit(txt, text_pos)
                    text_mode = False

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    input_text += event.unicode

        # 🖱️ Mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode in ["line", "rect", "circle"]:
                start_pos = event.pos
                temp_surface = screen.copy()

            elif mode == "fill":
                flood_fill(screen, event.pos[0], event.pos[1], color, WIDTH, HEIGHT)

            elif mode == "text":
                text_mode = True
                text_pos = event.pos
                input_text = ""

        # 🖱️ Mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            if start_pos:
                end_pos = event.pos

                if mode == "line":
                    pygame.draw.line(screen, color, start_pos, end_pos, radius)

                elif mode == "rect":
                    x = min(start_pos[0], end_pos[0])
                    y = min(start_pos[1], end_pos[1])
                    w = abs(end_pos[0] - start_pos[0])
                    h = abs(end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, color, (x, y, w, h), radius)

                elif mode == "circle":
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    r = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, r, radius)

            start_pos = None
            last_pos = None
            temp_surface = screen.copy()

        # 🖱️ Mouse motion
        if event.type == pygame.MOUSEMOTION:

            if pygame.mouse.get_pressed()[0] and mode == "pencil":
                if last_pos:
                    pygame.draw.line(screen, color, last_pos, event.pos, radius)
                last_pos = event.pos

            elif pygame.mouse.get_pressed()[0] and mode == "erase":
                pygame.draw.circle(screen, BLACK, event.pos, radius)

            elif start_pos and mode in ["line", "rect", "circle"]:
                screen.blit(temp_surface, (0, 0))

                if mode == "line":
                    pygame.draw.line(screen, color, start_pos, event.pos, radius)

                elif mode == "rect":
                    x = min(start_pos[0], event.pos[0])
                    y = min(start_pos[1], event.pos[1])
                    w = abs(event.pos[0] - start_pos[0])
                    h = abs(event.pos[1] - start_pos[1])
                    pygame.draw.rect(screen, color, (x, y, w, h), radius)

                elif mode == "circle":
                    dx = event.pos[0] - start_pos[0]
                    dy = event.pos[1] - start_pos[1]
                    r = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, r, radius)

    # UI
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 30))
    font = pygame.font.SysFont(None, 24)
    info = f"Mode: {mode} | Color: {color} | Size: {radius}"
    text = font.render(info, True, WHITE)
    screen.blit(text, (10, 5))

    if text_mode:
        font = pygame.font.SysFont(None, 30)
        preview = font.render(input_text, True, color)
        screen.blit(preview, text_pos)

    pygame.display.flip()
    clock.tick(60)