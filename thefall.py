import pygame
from settings import WIDTH, HEIGHT, FPS, font, TILE_SIZE
from mainmenu import calculate_position
from drawboard import CollideTile

pygame.mixer.init()
pygame.mixer.music.load('sounds/waa.mp3')
pygame.mixer.music.set_volume(0.2)


class Cutscene():
    def __init__(self, screen):
        self.screen = screen
        self.blue = pygame.image.load('sprites/blue.png')
        self.blue = pygame.transform.scale(
            self.blue, (TILE_SIZE, TILE_SIZE))
        self.blue_rect = self.blue.get_rect()
        self.blue_rect.x = 0
        self.blue_rect.y = HEIGHT/2
        self.is_running = True

        # create sprite groups
        self.ground_tiles = pygame.sprite.Group()

        # create the ground
        self.ground_tiles.add(CollideTile(
            x=0, y=HEIGHT/2+TILE_SIZE, width=WIDTH/2+TILE_SIZE*2, height=TILE_SIZE, color='green'))

        self.ground_tiles.add(CollideTile(
            x=WIDTH/2+100 + 2*TILE_SIZE, y=HEIGHT/2+TILE_SIZE, width=WIDTH/2+TILE_SIZE*2, height=TILE_SIZE, color='green'))

        self.timer = pygame.time.Clock()

    def draw_blue(self):
        self.screen.blit(self.blue, self.blue_rect)

    def move_blue(self):
        # move to the right
        if self.blue_rect.x < WIDTH/2 + TILE_SIZE * 2:
            self.blue_rect.x += TILE_SIZE//8
            #pygame.mixer.music.play()
        else:
            # Play the music
            self.blue_rect.y += 12
            self.blue = pygame.transform.rotate(self.blue, -7)

        if self.blue_rect.y > HEIGHT:
            self.is_running = False

    def draw_text(self):
        text_1 = 'In the beginning, there was blue.'

        self.screen.blit(font.render(text_1, True, 'white'),
                         calculate_position(text_1, WIDTH / 2, HEIGHT / 2 - TILE_SIZE * 5))

    def draw(self):
        self.screen.fill('black')
        self.draw_text()
        self.draw_blue()
        self.move_blue()
        self.ground_tiles.draw(self.screen)

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
