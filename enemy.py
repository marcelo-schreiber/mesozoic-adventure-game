import pygame
from actor import Actor
from settings import FPS, TILE_SIZE, font
from math import sqrt


class Enemy(Actor):
    def __init__(self, name, x, y, size, hp, hor, ver):
        super().__init__(x, y, size, size, hp, name)

        self.is_attacking = True
        self.time = 0
        self.timeout_seconds = 5  # 5 SECONDS

        #   BINDER
        self.isMoving = False
        self.speedX, self.speedY = 0, 0
        self.pellets = []
        self.hor, self.ver = hor, ver

        self.speedSet = 8
        self.canHurt = True
        self.frango = pygame.image.load(f'sprites/chicken.png').convert_alpha()

    def draw(self):
        # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN

        if not self.is_attacking:
            self.image = self.frango       

        elif self.direction == 0:
            self.image = self.imageR

        elif self.direction == 1:
            self.image = self.imageL

        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        # draw a text above the enemy
        text = font.render(
            f'{self.is_attacking}', True, 'red')
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.y - 10))
        screen = pygame.display.get_surface()
        screen.blit(text, text_rect)

    def calculate_distance(self, x1, y1, x2, y2):
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def farmost_point(self, noncollide_tiles, x1, y1):
        maior = 0
        x, y = 0, 0
        for i in noncollide_tiles:
            r = self.calculate_distance(i.rect.x, i.rect.y, x1, y1)
            if maior < r:
                maior = r
                x, y = i.rect.x, i.rect. y
        return x, y

    def take_damage(self, level, noncollide_tiles, player):
        if not self.canHurt:
            return

        self.canHurt = False
        self.isMoving = False
        self.is_attacking = True
        self.speedSet = 1
        self.pellets.clear()
        cY, cX = self.rect.y // TILE_SIZE, self.rect.x // TILE_SIZE
        x, y = self.farmost_point(
            noncollide_tiles, player.rect.x, player.rect.y)
        self.findpath(cY, cX, y // TILE_SIZE, x // TILE_SIZE, level)

    def timer(self):
        self.time += 1
        if self.time >= self.timeout_seconds * FPS:
            self.is_attacking = True
            self.time = 0

    def findpath(self, x, y, dX, dY, level):
        if level[x][y] == 1:
            return False

        for i in self.pellets:
            if i == [x * TILE_SIZE, y * TILE_SIZE]:
                return False

        self.pellets.append([x * TILE_SIZE, y * TILE_SIZE])

        if x == dX and y == dY:
            return True

        if self.findpath(x - self.hor, y, dX, dY, level):
            return True
        if self.findpath(x, y + self.ver, dX, dY, level):
            return True
        if self.findpath(x + self.hor, y, dX, dY, level):
            return True
        if self.findpath(x, y - self.ver, dX, dY, level):
            return True

        self.pellets.pop()
        return False

    # Anda em direção ao próximo nodo até estar na mesma posição.
    # Ao chegar, retira o nodo da lista e permite o cálculo do próximo nodo.
    def move(self):
        if not self.isMoving:
            return

        # detect direction with speedx and speedy
        if self.speedX > 0:
            self.direction = 0
        elif self.speedX < 0:
            self.direction = 1

        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if self.rect.x == self.pellets[0][1] and self.rect.y == self.pellets[0][0]:
            self.isMoving = False
            self.pellets.pop(0)

    # Calcula o próximo nodo ao qual se locomover.
    # Se não houver mais nodos, recalcula-se o caminho até o player
    def next_pellet(self, player, level):
        if self.isMoving:
            return
        try:
            self.speedX = (self.pellets[0][1] - self.rect.x) // self.speedSet
            self.speedY = (self.pellets[0][0] - self.rect.y) // self.speedSet
            self.isMoving = True
        except:
            self.speedSet = 8
            self.canHurt = True
            pY = player.rect.y // TILE_SIZE
            pX = player.rect.x // TILE_SIZE
            cY = self.rect.y // TILE_SIZE
            cX = self.rect.x // TILE_SIZE
            self.findpath(cY, cX, pY, pX, level)

    def update(self, player, level):
        if not super().is_alive():
            self.kill()
            return

        if not self.is_attacking:
            self.timer()

        self.next_pellet(player, level)
        self.move()

        self.draw()
