import pygame
from drawboard import NonCollideTiles


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, collide_tiles, poweup_tiles, noncollide_tiles):
        super().__init__()
        self.width = width
        self.height = height
        self.name = 'blue'
        self.image = pygame.image.load('din/blue.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.collide_tiles = collide_tiles
        self.powerup_tiles = poweup_tiles
        self.noncollide_tiles = noncollide_tiles
        self.hp = 100
        self.player_direction = 0
        self.player_speed = 8

    def can_move(self):
        return self.rect.x % 64 == 0 and self.rect.y % 64 == 0

    def is_alive(self):
        return self.hp > 0

    def collide_powerup(self):
        powerup_list = pygame.sprite.spritecollide(
            self, self.powerup_tiles, True)

        for powerup in powerup_list:
            if powerup.type_of_powerup == 'attack':
                self.hp += 10
                # substitute with noncollide tile
                self.noncollide_tiles.add(NonCollideTiles(
                    powerup.rect.x, powerup.rect.y, 64, 64, 'white')
                )
                powerup.kill()

    def move(self):
        keys = pygame.key.get_pressed()

        # check collision
        if keys[pygame.K_d]:
            self.rect.x += self.player_speed
            self.player_direction = 0

        elif keys[pygame.K_a]:
            self.rect.x -= self.player_speed
            self.player_direction = 1

        elif keys[pygame.K_w]:
            self.rect.y -= self.player_speed
            self.player_direction = 2

        elif keys[pygame.K_s]:
            self.rect.y += self.player_speed
            self.player_direction = 3

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

        elif self.player_direction == 2:
            self.image = player_left

        elif self.player_direction == 3:
            self.image = player_right

        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

    def check_collision(self):
        # check collision on each axis separately using player direction to determine which axis to check
        # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN

        collide_list = pygame.sprite.spritecollide(
            self, self.collide_tiles, False)

        if len(collide_list) > 0:
            if self.player_direction == 0:
                self.rect.x -= self.player_speed

            elif self.player_direction == 1:
                self.rect.x += self.player_speed

            elif self.player_direction == 2:
                self.rect.y += self.player_speed

            else:
                self.rect.y -= self.player_speed

    def kill(self):
        super().kill()
        print(f'{self.name} is dead.')
        pygame.quit()
        quit()

    def animate(self):
        if self.player_direction == 0:
            self.rect.x += self.player_speed

        elif self.player_direction == 1:
            self.rect.x -= self.player_speed

        elif self.player_direction == 2:
            self.rect.y -= self.player_speed

        else:
            self.rect.y += self.player_speed

    def update(self):
        if not self.is_alive():  # TODO: add game over screen
            self.kill()
            return

        if self.can_move():
            self.move()
        else:
            self.animate()
        self.check_collision()
        self.draw()
        self.collide_powerup()
