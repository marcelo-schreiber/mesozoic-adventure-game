import pygame
from enemy import Enemy
from player import Player
from settings import TILE_SIZE

PATH = 0
WALL = 1
INVINCIBLE = 2
ZAWARUDO = 3
PLAYER = 4
EORAPTOR = 5
YIQI = 6
PTEDOAUSTRO = 7

class CollideTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class PowerUpTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, type):
        super().__init__()
        self.type_of_powerup = type
        self.image = pygame.image.load(f'sprites/{self.type_of_powerup}.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))

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
    enemy_group = pygame.sprite.Group()
    player_group = pygame.sprite.GroupSingle()
    player = Player(0, 0, 0, None, None, None, None)
    # loop through level array
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == WALL:
                collide_tiles.add(CollideTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'black'))
                continue
            elif level[row][col] == PATH:
                powerup_tiles.add(PowerUpTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'scooby'))
            elif level[row][col] == INVINCIBLE:
                powerup_tiles.add(PowerUpTile(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'invinc'))
            elif level[row][col] == EORAPTOR:
                enemy_group.add(Enemy('eoraptor', col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, 1, 1, 1))
            elif level[row][col] == YIQI:
                enemy_group.add(Enemy('yi qi', col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, 1, 1, -1))
            elif level[row][col] == PTEDOAUSTRO:
                enemy_group.add(Enemy('ptedoaustro', col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, 1, -1, -1))
            elif level[row][col] == PLAYER:
                player = Player(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, collide_tiles, powerup_tiles, noncollide_tiles, enemy_group)
                player_group.add(player)

            noncollide_tiles.add(NonCollideTiles(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE, 'white'))

    return collide_tiles, noncollide_tiles, powerup_tiles, enemy_group, player_group, player
