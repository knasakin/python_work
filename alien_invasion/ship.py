import pygame


class Ship:
    """Класс для управления кораблем."""

    def __init__(self, ai_game):  # ai_game - экземпляр класса AlienInvasion
        """Инициализирует корабль и задает его начальную позицию."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  # Позволяет разместить корабль в нужной позиции экрана
        self.image = pygame.image.load('images/ship.bmp')  # Загружает изображение корабля и получает прямоугольник
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # Каждый новый корабль появляется у нижнего края экрана
        self.x = float(self.rect.x)  # Сохранение вещественной координаты центра корабля
        self.moving_right = False  # Флаг перемещения вправо
        self.moving_left = False  # Флаг перемещения влево

    def blitme(self):
        """Рисует корабль в текущей позиции."""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x  # Обновление атрибута rect на основании self.x

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
