import pygame
from actor import Actor
from settings import FPS, TILE_SIZE

pygame.init()

font = pygame.font.SysFont('Roboto', 24)

class Enemy(Actor):
    def __init__(self, name, x, y, width, height, hp):
        super().__init__(x, y, width, height, hp, name)

        self.is_attacking = True
        self.time = 0
        self.timeout_seconds = 5 # 5 SECONDS

        #   BINDER
        self.isMoving = False
        self.speedX, self.speedY = 0,0
        self.pellets = []

    def draw(self):
        # load player image
        enemy_right = pygame.image.load(
            f'sprites/{self.name}r.png').convert_alpha()
        enemy_left = pygame.image.load(
            f'sprites/{self.name}l.png').convert_alpha()  # left
        # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN

        if self.direction == 0:
            self.image = enemy_right

        elif self.direction == 1:
            self.image = enemy_left

        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        # draw a text above the enemy
        text = font.render(
            f'{self.name, self.hp, self.is_attacking}', True, 'red')
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.y - 10))
        screen = pygame.display.get_surface()
        screen.blit(text, text_rect)

    def take_damage(self, damage):
        self.hp -= damage

    def timer(self):
        self.time += 1
        if self.time >= self.timeout_seconds * FPS:
            self.switch_attack_mode()
            self.time = 0
        
    def switch_attack_mode(self):
        self.is_attacking = not self.is_attacking

    # Encontra um caminho até o player através de backtracking.
    def findpath(self, x, y, dX, dY, level):
        if level[x][y] == 1:
            return False

        for i in self.pellets:
            if i == [x * TILE_SIZE, y * TILE_SIZE]:
                return False
        
        self.pellets.append([x * TILE_SIZE, y * TILE_SIZE])

        if x == dX and y == dY:
            return True

        if self.findpath(x + 1, y, dX, dY, level):
            return True
        if self.findpath(x, y + 1, dX, dY, level):
            return True
        if self.findpath(x - 1, y, dX, dY, level):
            return True
        if self.findpath(x, y - 1, dX, dY, level):
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
            self.speedX = (self.pellets[0][1] - self.rect.x) // 8
            self.speedY = (self.pellets[0][0] - self.rect.y) // 8
            self.isMoving = True
        except:
            pY = player.rect.y // TILE_SIZE
            pX = player.rect.x // TILE_SIZE
            cY = self.rect.y // TILE_SIZE
            cX = self.rect.x // TILE_SIZE
            self.findpath(cY, cX, pY, pX, level)

    def update(self, player, level):
        if not self.is_alive():
            self.kill()
            return

        if not self.is_attacking:
            self.timer()

        self.next_pellet(player, level)
        self.move()

        # for i in self.pellets:
        #     screen = pygame.display.get_surface()
        #     pygame.draw.rect(screen, (255,0,0), pygame.Rect(i[1] + 16, i[0] + 16, 16, 16))

        self.draw()
        