import pygame
from settings import WIDTH, HEIGHT, FPS, font
from mainmenu import calculate_position


pygame.mixer.init()
pygame.mixer.music.load('sounds/waa.mp3')
pygame.mixer.music.set_volume(0.2)

blue = pygame.image.load('sprites/bluer.png')
blue = pygame.transform.scale(
    blue, (64, 64))

blue_rect = blue.get_rect()
blue_rect.y = HEIGHT / 2

# draw a green rectangle to be the ground
ground = pygame.Surface((WIDTH/2 + 100, 64))
other_ground = pygame.Surface((WIDTH/2 - 164, 64))
other_ground.fill('green')
ground.fill('green')

other_ground_rect = other_ground.get_rect()
ground_rect = ground.get_rect()
other_ground_rect.y = HEIGHT - blue_rect.y + 64
other_ground_rect.x = WIDTH/2 + 164
ground_rect.y = HEIGHT - blue_rect.y + 64


def calculate_position(text, x, y):
    text_width, text_height = font.size(text)
    return (x - text_width / 2, y - text_height / 2)


running = True


def draw(screen):
    global blue
    global running
    text_1 = 'In the beginning, there was blue.'
    screen.fill('black')
    screen.blit(ground, (ground_rect.x, ground_rect.y))
    screen.blit(other_ground, (other_ground_rect.x, other_ground_rect.y))
    screen.blit(font.render(text_1, True, 'white'),
                calculate_position(text_1, WIDTH / 2, HEIGHT / 2 - 300))
    screen.blit(blue, (blue_rect.x, blue_rect.y))
    # move to the right
    if blue_rect.x < WIDTH/2 + 100:
        blue_rect.x += 5
        pygame.mixer.music.play()
    else:
        # Play the music
        blue_rect.y += 12
        blue = pygame.transform.rotate(blue, -7)

    if blue_rect.y > HEIGHT:
        running = False


def cutscene(screen):
    global running

    timer = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                running = False

        draw(screen)
        # change to 20 fps
        timer.tick(FPS)

        pygame.display.update()  # update the display
