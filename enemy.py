import pygame

font = pygame.font.SysFont('freesansbold.ttf', 24)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, enemy_x, enemy_y, width, height, hp, damage, player):
        super().__init__()

        self.width = width
        self.height = height
        self.player = player
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

        elif self.direction == 2:
            self.image = player_left

        elif self.direction == 3:
            self.image = player_right

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

    def move(self):
        pass

    def kill(self):
        super().kill()
        print(f'{self.name} is dead.')

    def update(self):
        if not self.is_alive():
            self.kill()
            return

        if self.is_attacking:
            self.attack(self.player, self.damage)
        else:
            self.take_damage(self.damage)
        self.switch_attack_mode()
        self.draw()
