import pygame
from settings import WIDTH, HEIGHT, FPS, font


def calculate_position(text, x, y):
    text_width, text_height = font.size(text)
    return (x - text_width / 2, y - text_height / 2)


class MainMenu():
    def __init__(self, screen):
        self.screen = screen
        self.is_running = True

    def draw(self):
        text_1 = 'Blue\'s Adventure in the Mesozoic Era'
        text_2 = 'Press any key to start...'
        text_3 = 'Team One Games\' first project.'

        self.screen.fill('black')
        self.screen.blit(font.render(text_1, True, 'white'),
                         calculate_position(text_1, WIDTH / 2, HEIGHT / 2 - 300))
        self.screen.blit(font.render(text_2, True,
                                     'white'),  calculate_position(text_2, WIDTH / 2, HEIGHT / 2 - 150))
        self.screen.blit(font.render(text_3, True,
                                     'white'),  calculate_position(text_3, WIDTH / 2, HEIGHT / 2))

    def play(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.is_running = False

            self.draw()

            pygame.display.update()  # update the display
