import pygame

font = pygame.font.SysFont('freesansbold.ttf', 24)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, enemy_x, enemy_y, width, height, hp, damage):
        super().__init__()

        self.width = width
        self.height = height
        self.name = name
        self.image = pygame.image.load(f'din/{name}r.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        self.rect = self.image.get_rect(topleft=(enemy_x, enemy_y))
        self.name = name
        self.hp = hp
        self.damage = damage
        self.is_attacking = True
        self.direction = 0

        #   BINDER
        self.isMoving = False
        self.canPathfind = True
        self.pellets = []
        self.speedX = 0
        self.speedY = 0

    def draw(self):
        # load player image
        player_right = pygame.image.load(
            f'din/{self.name}r.png').convert_alpha()
        player_left = pygame.image.load(
            f'din/{self.name}l.png').convert_alpha()  # left
        # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN

        if self.direction == 0:
            self.image = player_right

        elif self.direction == 1:
            self.image = player_left

        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        # draw a text above the enemy
        text = font.render(
            f'{self.name, self.hp, self.is_attacking}', True, 'red')
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.y - 10))
        screen = pygame.display.get_surface()
        screen.blit(text, text_rect)

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        if self.rect.colliderect(self.player.rect):
            self.hp -= damage
            print(f'{self.name} takes {damage} damage.')
            print(f'{self.name} has {self.hp} health left.')

    def attack(self, player, damage):
        if self.rect.colliderect(player.rect):
            player.hp -= damage
            print(f'{self.name} attacks {player.name} for {damage} damage.')
            print(f'{player.name} has {player.hp} health left.')

    def switch_attack_mode(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x]:  # TODO: change to a timer
            self.is_attacking = not self.is_attacking

    def findPath(self, x, y, dX, dY, level):
        if not self.canPathfind:
            return

        if level[x][y] == 1:
            return False
        for i in self.pellets:
            if (i == [x * 64, y * 64]):
                return False

        self.pellets.append([x * 64, y * 64])

        if x == dX and y == dY:
            self.canPathfind = False
            self.dX = dX * 64
            self.dY = dY * 64
            return True
        
        if self.findPath(x + 1, y, dX, dY, level):
            return True
        if self.findPath(x - 1, y, dX, dY, level):
            return True
        if self.findPath(x, y + 1, dX, dY, level):
            return True
        if self.findPath(x, y - 1, dX, dY, level):
            return True

        self.pellets.pop()
        return False

    def move(self, level, player):
        if self.isMoving:
            self.rect.x += self.speedX
            self.rect.y += self.speedY
            if (self.rect.x == self.pellets[0][1] and self.rect.y == self.pellets[0][0]):
                self.pellets.pop(0)
                self.isMoving = False
            return

        try:
            self.canPathfind = True
            self.speedX = (self.pellets[0][1] - self.rect.x) / 4
            self.speedY = (self.pellets[0][0] - self.rect.y) / 4
            self.isMoving = True
        except:
            print(self.dX, self.dY)

    def kill(self):
        super().kill()
        print(f'{self.name} is dead.')

    def update(self, level ,player):
        if not self.is_alive():
            self.kill()
            return

        if self.is_attacking:
            self.attack(player, self.damage)
        else:
            self.take_damage(self.damage)

        self.findPath(int(self.rect.x / 64), int(self.rect.y / 64), player.coX, player.coY, level)
        self.move(level, player)
        self.switch_attack_mode()
        for i in self.pellets:
            screen = pygame.display.get_surface()
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(i[1] + 16, i[0] + 16, 16, 16))
        self.draw()
