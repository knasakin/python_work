import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')  # Загрузка изображения
        self.rect = self.image.get_rect()  # назначение атрибута rect

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)  # Сохранение точной горизонтальной позиции пришельца

    def update(self):
        """Перемещает пришельца вправо."""

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x  # обновление позиции прямоугольника пришельца

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
