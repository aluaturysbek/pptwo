import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Advanced Paint")
    clock = pygame.time.Clock()

    color = (0, 0, 255)
    mode = "draw"  # draw / square / rtriangle / etriangle / rhombus
    start_pos = None

    screen.fill((0, 0, 0))

    while True:
        for event in pygame.event.get():

            # ❌ Exit conditions
            if event.type == pygame.QUIT:
                return

            # ⌨️ Keyboard controls
            if event.type == pygame.KEYDOWN:

                # 🎨 Color selection
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)

                # 🛠️ Shape modes
                elif event.key == pygame.K_1:
                    mode = "draw"
                elif event.key == pygame.K_2:
                    mode = "square"
                elif event.key == pygame.K_3:
                    mode = "rtriangle"
                elif event.key == pygame.K_4:
                    mode = "etriangle"
                elif event.key == pygame.K_5:
                    mode = "rhombus"

                # 🧹 Clear screen
                elif event.key == pygame.K_c:
                    screen.fill((0, 0, 0))

            # 🖱️ Mouse pressed → start drawing shape
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos

            # 🖱️ Mouse released → draw shape
            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos

                if start_pos is None:
                    continue

                x1, y1 = start_pos
                x2, y2 = end_pos

                # 🟦 Draw square
                if mode == "square":
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    rect = pygame.Rect(x1, y1, side, side)
                    pygame.draw.rect(screen, color, rect, 2)

                # 📐 Right triangle
                elif mode == "rtriangle":
                    points = [
                        (x1, y1),
                        (x2, y1),
                        (x1, y2)
                    ]
                    pygame.draw.polygon(screen, color, points, 2)

                # 🔺 Equilateral triangle
                elif mode == "etriangle":
                    side = abs(x2 - x1)
                    height = int((math.sqrt(3) / 2) * side)

                    points = [
                        (x1, y1),
                        (x1 + side, y1),
                        (x1 + side // 2, y1 - height)
                    ]
                    pygame.draw.polygon(screen, color, points, 2)

                # 🔷 Rhombus
                elif mode == "rhombus":
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2

                    points = [
                        (center_x, y1),      # top
                        (x2, center_y),      # right
                        (center_x, y2),      # bottom
                        (x1, center_y)       # left
                    ]
                    pygame.draw.polygon(screen, color, points, 2)

                start_pos = None

            # ✏️ Free drawing
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0] and mode == "draw":
                    pygame.draw.circle(screen, color, event.pos, 3)

        # 🧾 UI text
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Mode: {mode}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

main()