import pygame
import math
from settings import *


class Cutscene:
    class Actor:
        def __init__(self, name, x, y, width, height):
            try:
                self.image = pygame.image.load(name).convert_alpha()
                self.image = pygame.transform.scale(
                    self.image, (width, height))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.type = "image_file"
            except:
                self.image = name
                self.rect = pygame.Rect(x, y, width, height)
                self.type = "solid_color"

    class Text:
        def __init__(self, string, x, y):
            self.text = string
            self.x = x
            self.y = y

    def __init__(self):
        self.is_running = True
        self.screen = pygame.display.get_surface()
        self.actors = []
        self.texts = []
        self.clock = pygame.time.Clock()

    def createActor(self, name, x, y, width, height):
        actor = self.Actor(name, x, y, width, height)
        self.actors.append(actor)
        return actor

    def createText(self, string, x, y):
        text = self.Text(string, x, y)
        self.texts.append(text)
        return text

    def move_to(self, rect, x, y, percentage):
        if abs(x - rect.x) < percentage and abs(y - rect.y) < percentage:
            return True

        hip = math.sqrt((x - rect.x)**2 + (y - rect.y)**2)

        rect.x += percentage * (x - rect.x)/hip
        rect.y += percentage * (y - rect.y)/hip

        return False

    def timer(self, time):
        if time <= 0:
            return True

        time -= 1
        return False

    def rotate(self, surface, angle):
        return pygame.transform.rotate(surface, angle)

    def draw(self):
        for i in self.actors:
            if i.type == "image_file":
                self.screen.blit(i.image, i.rect)
            else:
                pygame.draw.rect(self.screen, i.image, i.rect)

    def write_texts(self):
        for i in self.texts:
            self.screen.blit(font.render(i.text, True, "white"),
                             self.calculate_text_position(i.text, i.x, i.y))

    def calculate_text_position(self, text, x, y):
        text_width, text_height = font.size(text)
        return (x - text_width / 2, y - text_height / 2)

    def get_text_size(self, text):
        return font.size(text)

    def update_screen(self):
        self.clock.tick(FPS)
        pygame.display.update()

    def play(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.is_running = False

            self.screen.fill("black")
            self.update()
            self.draw()
            self.write_texts()
            self.update_screen()


class mainmenu(Cutscene):
    def __init__(self):
        super().__init__()
        self.createText("Blue\'s Mesozoic Adventure",
                        WIDTH / 2, HEIGHT / 2 - TILE_SIZE * 5)
        self.createText("press space, enter or escape to start",
                        WIDTH / 2, HEIGHT / 2 - TILE_SIZE * 3)
        pygame.mixer.music.play(-1)

    def update(self):
        pass


class thefall(Cutscene):
    def __init__(self):
        super().__init__()
        self.createActor("sprites/bg.png", 0, 0, WIDTH, HEIGHT)
        self.createActor((79, 88, 41), 0, HEIGHT/2+TILE_SIZE,
                         WIDTH/2+TILE_SIZE*2, HEIGHT/2)
        self.createText("In the beggining, there was Blue.",
                        WIDTH / 2, 64)
        self.blue = self.createActor(
            "sprites/blue.png", 0, HEIGHT/2, TILE_SIZE, TILE_SIZE)

    def update(self):
        if not self.move_to(self.blue.rect, WIDTH/2 + TILE_SIZE * 2, self.blue.rect.y, 5):
            return

        if not self.move_to(self.blue.rect, self.blue.rect.x, HEIGHT, 12):
            self.blue.image = self.rotate(self.blue.image, -7)
            return

        self.is_running = False


class game_over(Cutscene):
    def __init__(self):
        super().__init__()
        self.createActor("images/santa ceia.jpg", 0, 0, WIDTH, HEIGHT)
        self.image = self.createActor("images/leo.jpg", WIDTH/4,
                                      HEIGHT, WIDTH / 2, HEIGHT / 2)
        self.text = self.createText(
            "After all, blue arrived in time for Leo's birthday.", WIDTH/2, HEIGHT/2)
        self.text = self.createText(
            "Happy Birthday!", WIDTH/2, HEIGHT/2+TILE_SIZE)

    def update(self):
        if not self.move_to(self.image.rect, WIDTH/4, HEIGHT/4, 3):
            return


class level_pass(Cutscene):
    def __init__(self, text):
        super().__init__()
        self.createActor("sprites/bg.png", 0, 0, WIDTH, HEIGHT)
        self.createActor((79, 88, 41), 0, HEIGHT/2+TILE_SIZE,
                         WIDTH, HEIGHT)

        text_width, text_height = self.get_text_size(text)

        text_x = WIDTH - text_width

        self.createActor((162, 124, 53), text_x - TILE_SIZE - TILE_SIZE//2,
                         HEIGHT/2 - text_height, text_width + TILE_SIZE, text_height + TILE_SIZE//2)

        text = self.createText(f'{text} =>', text_x, HEIGHT/2)

        self.blue = self.createActor(
            "sprites/blue.png", 0, HEIGHT/2, TILE_SIZE, TILE_SIZE)

        pygame.mixer.music.load('sounds/mushroom.mp3')
        pygame.mixer.music.play()

    def update(self):
        if not self.move_to(self.blue.rect, WIDTH, self.blue.rect.y, 12):
            return

        self.is_running = False


class theportal(Cutscene):
    def __init__(self):
        super().__init__()
        self.portal = self.createActor(
            "sprites/portal.png", 0, -HEIGHT, WIDTH, HEIGHT*2)

        self.createText("She time travelled to the Mesozoic Era.",
                        WIDTH / 2, HEIGHT / 2 - TILE_SIZE * 5)

    def update(self):
        if not self.move_to(self.portal.rect, self.portal.rect.x, 0, 10):
            self.portal.image.set_alpha(self.portal.image.get_alpha() - 2)
            return

        self.is_running = False
