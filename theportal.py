import pygame
from settings import WIDTH, HEIGHT, FPS, font, TILE_SIZE
from mainmenu import calculate_position


class Cutscene():
    def __init__(self, screen):
        self.screen = screen
        self.portal = pygame.image.load('sprites/portal.png')
        self.portal = pygame.transform.scale(
            self.portal, (WIDTH, 2*HEIGHT))
        self.portal_rect = self.portal.get_rect()
        self.portal_rect.x = 0
        self.portal_rect.y = -HEIGHT  # start above the screen
        self.is_running = True

        self.timer = pygame.time.Clock()

    def draw_portal(self):
        self.screen.blit(self.portal, self.portal_rect)

    def move_portal(self):
        if self.portal_rect.y < HEIGHT/2:
            if self.portal.get_alpha() < 90:
                self.is_running = False
            self.portal_rect.y += 5
            self.portal.set_alpha(self.portal.get_alpha() - 0.4)

    def draw_text(self):
        text_1 = 'It time travelled to the mesozoic era...'
        self.screen.blit(font.render(text_1, True, 'white'),
                         calculate_position(text_1, WIDTH / 2, HEIGHT / 2 - 300))

    def draw(self):
        self.screen.fill('black')

        self.draw_portal()
        self.move_portal()

        self.draw_text()

    def play(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    self.is_running = False

            self.draw()
            self.timer.tick(FPS)
            pygame.display.update()  # update the display
