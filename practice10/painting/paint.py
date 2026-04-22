import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint Program")
    clock = pygame.time.Clock()

    radius = 5
    mode = "draw"   # draw / rect / circle / erase
    color = (0, 0, 255)  # default blue
    points = []

    start_pos = None  # for shapes

    while True:
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                # 🎨 Color selection
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                elif event.key == pygame.K_y:
                    color = (255, 255, 0)

                # 🛠️ Mode selection
                elif event.key == pygame.K_1:
                    mode = "draw"
                elif event.key == pygame.K_2:
                    mode = "rect"
                elif event.key == pygame.K_3:
                    mode = "circle"
                elif event.key == pygame.K_4:
                    mode = "erase"

                # Clear screen
                elif event.key == pygame.K_c:
                    screen.fill((0, 0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode in ["rect", "circle"]:
                    start_pos = event.pos

                if event.button == 1:
                    radius = min(50, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if start_pos:
                    end_pos = event.pos

                    if mode == "rect":
                        rect = pygame.Rect(
                            start_pos[0],
                            start_pos[1],
                            end_pos[0] - start_pos[0],
                            end_pos[1] - start_pos[1]
                        )
                        pygame.draw.rect(screen, color, rect, 2)

                    elif mode == "circle":
                        center = start_pos
                        radius_circle = int(
                            ((end_pos[0] - start_pos[0])**2 +
                             (end_pos[1] - start_pos[1])**2) ** 0.5
                        )
                        pygame.draw.circle(screen, color, center, radius_circle, 2)

                start_pos = None

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    if mode == "draw":
                        pygame.draw.circle(screen, color, event.pos, radius)
                    elif mode == "erase":
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        # UI text
        font = pygame.font.SysFont(None, 24)
        info = f"Mode: {mode} | Color: {color} | Size: {radius}"
        text = font.render(info, True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

main()