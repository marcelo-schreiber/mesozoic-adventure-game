import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, collide_tiles):
        super().__init__()

        self.width = width
        self.height = height
        self.name = 'blue'
        self.image = pygame.image.load('din/blue.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.collide_tiles = collide_tiles

        self.hp = 100
        self.player_direction = 0

        #   BINDER
        self.isMoving = False
        self.nextX, self.nextY = self.rect.x, self.rect.y
        self.speedX, self.speedY = 0, 0

    def is_alive(self):
        return self.hp > 0

    def moving(self):
        if not self.isMoving:
            return

        if (self.nextX == self.rect.x and self.nextY == self.rect.y):
            self.speedX, self.speedY = 0, 0
            self.isMoving = False
        self.rect.x += self.speedX
        self.rect.y += self.speedY

    def move(self):
        keys = pygame.key.get_pressed()

        if self.isMoving:
            return

        if keys[pygame.K_d]:
            self.player_direction = 0
            self.nextX, self.nextY = self.rect.x + 64, self.rect.y

        elif keys[pygame.K_a]:
            self.player_direction = 1
            self.nextX, self.nextY = self.rect.x - 64, self.rect.y

        elif keys[pygame.K_w]:
            self.player_direction = 2
            self.nextX, self.nextY = self.rect.x, self.rect.y - 64

        elif keys[pygame.K_s]:
            self.player_direction = 3
            self.nextX, self.nextY = self.rect.x, self.rect.y + 64
        else:
            return

        if not self.check_collision(self.nextX, self.nextY):
            self.isMoving = True
            self.speedX, self.speedY = (self.nextX - self.rect.x) / 4, (self.nextY - self.rect.y) / 4

    def check_collision(self, x, y):
        for i in self.collide_tiles:
            if (x != i.rect.x or y != i.rect.y):
                continue
            if (i.id == "POWERUP"):
                i.kill(self.collide_tiles)
                return False
            elif (i.id == "WALL"):
                return True
        return False

    def draw(self):

        # load player image
        player_left = pygame.image.load('din/blue.png').convert_alpha()  # left
        player_right = pygame.image.load(
            'din/blur.png').convert_alpha()  # right

        # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN
        if self.player_direction == 0:
            self.image = player_right

        elif self.player_direction == 1:
            self.image = player_left

        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

    def kill(self):
        super().kill()
        print(f'{self.name} is dead.')
        pygame.quit()
        quit()

    def update(self):
        if not self.is_alive():  # TODO: add game over screen
            self.kill()
            return

        self.moving()
        self.move()

        self.draw()
