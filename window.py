import pygame

class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = None

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def quit(self):
        pygame.quit()