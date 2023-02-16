import pygame
from settings import WIDTH, HEIGHT, FPS

font = pygame.font.SysFont('Roboto', 36)

def calculate_position(text, x, y):
    text_width, text_height = font.size(text)
    return (x - text_width / 2, y - text_height / 2)


def draw(screen):
    text_1 = 'Blue\'s Adventure in the Mesozoic Era'
    text_2 = 'Press any key to start...'
    text_3 = 'Team One Games\' first project.'
    
    screen.fill('black')
    screen.blit(font.render(text_1, True, 'white'),
                calculate_position(text_1, WIDTH / 2, HEIGHT / 2 - 300))
    screen.blit(font.render(text_2, True,
                'white'),  calculate_position(text_2, WIDTH / 2, HEIGHT / 2 - 150))
    screen.blit(font.render(text_3, True,
                'white'),  calculate_position(text_3, WIDTH / 2, HEIGHT / 2))


def cutscene(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                running = False

        draw(screen)

        pygame.display.update()  # update the display
