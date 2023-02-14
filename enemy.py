import pygame
from entity import Entity

font = pygame.font.SysFont('freesansbold.ttf', 24)


class Enemy(Entity):
    def __init__(self, name, x, y, width, height, hp):
        super().__init__(x, y, width, height, hp, name)

        self.is_attacking = True

    def draw(self):
        # load player image
        enemy_right = pygame.image.load(
            f'din/{self.name}r.png').convert_alpha()
        enemy_left = pygame.image.load(
            f'din/{self.name}l.png').convert_alpha()  # left
        # 0 - RIGHT, 1 - LEFT, 2 - UP, 3 - DOWN

        if self.direction == 0:
            self.image = enemy_right

        elif self.direction == 1:
            self.image = enemy_left

        elif self.direction == 2:
            self.image = enemy_left

        elif self.direction == 3:
            self.image = enemy_right

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

    def switch_attack_mode(self):
        self.is_attacking = not self.is_attacking

    def update(self):
        if not self.is_alive():
            self.kill()
            return
        self.draw()
