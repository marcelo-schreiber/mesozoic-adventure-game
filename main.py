import pygame
from settings import arrayMaps, WIDTH, HEIGHT, FPS
from drawboard import draw_board
from player import Player
from enemy import Enemy
from settings import TILE_SIZE, font, mesozoic_eras

from mainmenu import calculate_position

from cutscene import thefall, theportal, mainmenu, level_pass, game_over, credits

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

# set caption
pygame.display.set_caption('Blue\'s Adventure in the Mesozoic Era')
pygame.display.set_icon(pygame.image.load('sprites/blue.png'))
pygame.mixer.music.load('sounds/menu_theme.mp3')
pygame.mixer.music.set_volume(0.3)


def main():
    mainmenu().play()
    thefall().play()
    theportal().play()
    current_level_idx = 0

    # initial cutscene is the level pass too

    running = True
    is_paused = False
    has_passed_level = True

    pygame.mixer.music.load('sounds/Triassic_theme.mp3')
    pygame.mixer.music.play(-1)  # -1 is for infinite loop of the music

    while current_level_idx < len(arrayMaps):
        current_map = arrayMaps[current_level_idx]
        collide_tiles, noncollide_tiles, powerup_tiles, enemy_group, player_group, player = draw_board(
            current_map, mesozoic_eras[current_level_idx])

        if has_passed_level:
            level_pass(mesozoic_eras[current_level_idx]).play()
            pygame.mixer.music.load(
                f'sounds/{mesozoic_eras[current_level_idx]}_theme.mp3')
            pygame.mixer.music.play(-1)
            has_passed_level = False

        running = True

        while running:
            if len(enemy_group) == 0 or len(powerup_tiles) == 0:
                has_passed_level = True
                current_level_idx += 1
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_level_idx = 5
                    running = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        is_paused = not is_paused

            if is_paused:
                # draw the pause screen
                screen.blit(font.render('Paused', True, 'red'),
                            calculate_position('Paused', WIDTH / 2, HEIGHT / 2))
                pygame.display.update()
                timer.tick(FPS)
                continue

            screen.fill('black')

            collide_tiles.draw(screen)
            noncollide_tiles.draw(screen)
            powerup_tiles.draw(screen)

            player_group.draw(screen)
            player_group.update(current_map)
            if not player.is_alive():
                running = False

            enemy_group.draw(screen)
            enemy_group.update(player, current_map)

            timer.tick(FPS)
            pygame.display.update()  # update the display

    # if the player has passed all the levels
    if current_level_idx == len(arrayMaps):
        game_over().play()
        credits().play()

    pygame.display.quit()
    pygame.quit()


if __name__ == '__main__':  # if the file is run directly
    main()
