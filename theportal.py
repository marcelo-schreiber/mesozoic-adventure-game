import pygame
from settings import WIDTH, HEIGHT, FPS, font
from mainmenu import calculate_position

portal = pygame.image.load('sprites/portal.png')
portal = pygame.transform.scale(
    portal, (WIDTH, 2*HEIGHT))

portal_rect = portal.get_rect()
portal_rect.y = -HEIGHT
portal_rect.x = 0


running = True


def draw(screen):
    global portal
    global running

    text_1 = 'It time travelled to the mesozoic era...'
    screen.fill('black')

    screen.blit(portal, (portal_rect.x, portal_rect.y))
    # move to the right
    screen.blit(font.render(text_1, True, 'white'),
                calculate_position(text_1, WIDTH / 2, HEIGHT / 2 - 300))

    # make portal wiggle and fade
    if portal_rect.y < HEIGHT/2:
        portal_rect.y += 5
        portal.set_alpha(portal.get_alpha() - 0.35)
        if portal.get_alpha() < 72:
            running = False
    else:
        portal_rect.y += 16
        portal = pygame.transform.rotate(portal, 7)


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
