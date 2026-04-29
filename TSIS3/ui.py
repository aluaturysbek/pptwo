import pygame

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.SysFont("Arial", 20)

    def draw(self, screen):
        pygame.draw.rect(screen, (100,100,100), self.rect)
        txt = self.font.render(self.text, True, (255,255,255))
        screen.blit(txt, (self.rect.x + 20, self.rect.y + 10))

        mouse = pygame.mouse.get_pressed()
        if self.rect.collidepoint(pygame.mouse.get_pos()) and mouse[0]:
            return True
        return False