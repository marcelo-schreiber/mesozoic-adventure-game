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
collide_tiles, noncollide_tiles, powerup_tiles, enemy_group, player_group, player = draw_board(arrayMap)

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
        enemy_group.update(player, arrayMap)

        timer.tick(FPS)
        pygame.display.update()  # update the display

    pygame.display.quit()
    pygame.quit()


if __name__ == '__main__':  # if the file is run directly
    main()
