import pygame


class Actor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, hp, name):
        super().__init__()
        self.width = width
        self.height = height
        self.hp = hp
        self.direction = 0
        self.imageHolder = pygame.image.load(f'sprites/{name}.png').convert_alpha()
        self.image = self.imageHolder
        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name

    def is_alive(self):
        return self.hp > 0

    def kill(self):
        if not self.is_alive():  # idk why I have to make another check
            super().kill()
