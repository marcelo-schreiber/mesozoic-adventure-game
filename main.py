import pygame
from settings import arrayMap, WIDTH, HEIGHT, FPS
from drawboard import draw_board
from player import Player
from enemy import Enemy
from settings import TILE_SIZE

from mainmenu import cutscene
from thefall import cutscene as cutscene2
from theportal import cutscene as cutscene3
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

# set caption
pygame.display.set_caption('Blue\'s Adventure in the Mesozoic Era')

# sprite groups
collide_tiles, noncollide_tiles, powerup_tiles = draw_board(arrayMap)

enemy_group = pygame.sprite.Group()
enemy_1 = Enemy('eoraptor', 128, 128, TILE_SIZE, TILE_SIZE, 100)
enemy_2 = Enemy('ptedoaustro', 256, 256, TILE_SIZE, TILE_SIZE, 100)
enemy_group.add(enemy_1)
enemy_group.add(enemy_2)

player_group = pygame.sprite.GroupSingle()
player = Player(64, 64, TILE_SIZE, TILE_SIZE, collide_tiles,
                powerup_tiles, noncollide_tiles, enemy_group)
player_group.add(player)


def main():
    cutscene(screen)
    cutscene2(screen)
    cutscene3(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('black')

        collide_tiles.draw(screen)
        noncollide_tiles.draw(screen)
        powerup_tiles.draw(screen)

        player_group.draw(screen)
        player_group.update()

        enemy_group.draw(screen)
        enemy_group.update()

        timer.tick(FPS)
        pygame.display.update()  # update the display

    pygame.display.quit()
    pygame.quit()


if __name__ == '__main__':  # if the file is run directly
    main()
