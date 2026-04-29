# tools.py

def flood_fill(surface, x, y, new_color, width, height):
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        px, py = stack.pop()

        if surface.get_at((px, py)) == target_color:
            surface.set_at((px, py), new_color)

            for nx, ny in [
                (px + 1, py), (px - 1, py),
                (px, py + 1), (px, py - 1)
            ]:
                if 0 <= nx < width and 0 <= ny < height:
                    stack.append((nx, ny))