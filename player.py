import pygame
from actor import Actor
from settings import TILE_SIZE, PLAYER_HP, PLAYER_NAME


class Player(Actor):
    def __init__(self, x, y, size, collide_tiles, poweup_tiles, noncollide_tiles, enemy_group):
        super().__init__(x, y, size, size, PLAYER_HP, PLAYER_NAME)
        self.enemy_group = enemy_group
        self.collide_tiles = collide_tiles
        self.powerup_tiles = poweup_tiles
        self.noncollide_tiles = noncollide_tiles

        self.damage = 5
        self.player_speed = TILE_SIZE / 8

        #   BINDER :)
        self.points = 0

    def can_move(self):
        return self.rect.x % TILE_SIZE == 0 and self.rect.y % TILE_SIZE == 0

    def collide_powerup(self):
        powerup_list = pygame.sprite.spritecollide(
            self, self.powerup_tiles, True)

        for powerup in powerup_list:
            if powerup.type_of_powerup == 'invinc':
                for enemy in self.enemy_group:
                    enemy.is_attacking = False
                    enemy.time = 0
                powerup.kill()
            elif powerup.type_of_powerup == 'scooby':
                self.points += 10
                powerup.kill()

    def take_damage(self, damage):
        self.hp -= damage

    def move(self):
        keys = pygame.key.get_pressed()

        # check collision
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x = (self.rect.x // TILE_SIZE) * TILE_SIZE
            self.rect.x += self.player_speed
            self.direction = 0

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x = (self.rect.x // TILE_SIZE) * TILE_SIZE
            self.rect.x -= self.player_speed
            self.direction = 1

        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y = (self.rect.y // TILE_SIZE) * TILE_SIZE
            self.rect.y -= self.player_speed
            self.direction = 2

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y = (self.rect.y // TILE_SIZE) * TILE_SIZE
            self.rect.y += self.player_speed
            self.direction = 3

    def draw(self):
        # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN
        if self.direction == 0:
            self.image = self.imageR

        elif self.direction == 1:
            self.image = self.imageL

        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

    def check_collision(self):
        # check collision on each axis separately using player direction to determine which axis to check
        # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN

        collide_list = pygame.sprite.spritecollide(
            self, self.collide_tiles, False)

        if len(collide_list) > 0:
            if self.direction == 0:
                self.rect.x -= self.player_speed

            elif self.direction == 1:
                self.rect.x += self.player_speed

            elif self.direction == 2:
                self.rect.y += self.player_speed

            else:
                self.rect.y -= self.player_speed

    def collide_enemy(self, level):
        enemy_list = pygame.sprite.spritecollide(self, self.enemy_group, True)

        for enemy in enemy_list:
            if enemy.canHurt == False:
                return

            if enemy.is_attacking:
                self.take_damage(self.damage)
            else:
                enemy.take_damage(level, self.noncollide_tiles, self)

    def get_direction(self):
        keys = pygame.key.get_pressed()

        is_horizontal = self.direction != 2 and self.direction != 3
        is_vertical = self.direction != 0 and self.direction != 1

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and is_horizontal:
            self.direction = 0

        elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and is_horizontal:
            self.direction = 1

        elif (keys[pygame.K_w] or keys[pygame.K_UP]) and is_vertical:
            self.direction = 2

        elif (keys[pygame.K_s] or keys[pygame.K_UP]) and is_vertical:
            self.direction = 3

    def animate(self):

        if self.direction == 0:
            self.rect.x += self.player_speed

        elif self.direction == 1:
            self.rect.x -= self.player_speed

        elif self.direction == 2:
            self.rect.y -= self.player_speed

        else:
            self.rect.y += self.player_speed

        self.get_direction()

    def player_kill(self):
        self.kill()
        pygame.quit()
        quit()

    def update(self, level):
        if not self.is_alive():
            self.player_kill()
            return

        if self.can_move():
            self.move()
        else:
            self.animate()

        self.check_collision()
        self.collide_powerup()
        self.collide_enemy(level)

        self.draw()
