import pygame
from settings import TILE_SIZE


class CollideTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PowerUpTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type_of_powerup = 'attack'


class NonCollideTiles(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def draw_board(level):
    # each block should have a width of 30 pixels and a height of 30 pixels
    # (the board should be 30 blocks wide and 30 blocks high)
    # create new sprite group
    collide_tiles = pygame.sprite.Group()
    noncollide_tiles = pygame.sprite.Group()
    powerup_tiles = pygame.sprite.Group()
    # loop through level array
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == 1:
                collide_tiles.add(CollideTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'black'))
            elif level[row][col] == 0:
                noncollide_tiles.add(NonCollideTiles(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'white'))
            elif level[row][col] == 2:
                powerup_tiles.add(PowerUpTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'green'))

    return collide_tiles, noncollide_tiles, powerup_tiles
