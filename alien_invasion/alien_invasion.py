import sys
import pygame
import csv
from datetime import datetime
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # настройки для fullscreen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)  # Создание экземпляра для хранения игровой статистики
        self.score_board = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  # Группа для хранения всех летящих снарядов
        self.aliens = pygame.sprite.Group()  # Группа для хранения флота пришельцев
        self._create_fleet()

        self.play_button = Button(self, "Play")  # Создание кнопки Play

    def run_game(self):
        """Запуск основного цикла игры."""

        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()  # устанавливаем первоначальный темп игры

            self.stats.reset_stats()
            self.stats.game_active = True
            self.score_board.prep_score()
            self.score_board.prep_level()
            self.score_board.prep_ships()

            # Очистка списков пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре.
            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)  # Указатель мыши скрывается

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)  # Создание выстрела
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""

        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():  # перебирать нужно копию группы для изменения bullets
            if bullet.rect.bottom <= 0:  # Если снаряд пересек границу, он удаляется из bullets
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами."""

        # Удаление снарядов и пришельцев, участвующих в коллизиях.
        # Проверка попаданий в пришельцев
        # При обнаружении попадания удалить снаряд и пришельца

        # Проверка коллизий "снаряд корабля — пришелец"
        # groupcollide - возвращает словарь со снарядами и пришельцами
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)  # начисляем очки
            self.score_board.prep_score()  # отображаем обновлённый счёт
            self.score_board.check_high_score()

        if not self.aliens:
            # Уничтожение существующих снарядов и создание нового флота.
            self.bullets.empty()  # все существующие снаряды убираются
            self._create_fleet()  # заполняет экран пришельцами
            self.settings.increase_speed()  # увеличиваем темп игры

            # Увеличение уровня
            self.stats.level += 1
            self.score_board.prep_level()

    def _create_fleet(self):
        """Создание флота вторжения."""

        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)  # Создание пришельца, он не войдёт во флот, нужно знать его ширину и высоту
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width  # ширина пришельца
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота вторжения.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду."""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # alien.x - доступное горизонтальное пространство и количество пришельцев, которые в нем поместятся
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Проверяет, достиг ли флот края экрана, с последующим обновлением позиций всех пришельцев во флоте."""

        self._check_fleet_edges()
        self.aliens.update()

        # Проверка коллизий "пришелец — корабль"
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Проверить, добрались ли пришельцы до нижнего края экрана.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""

        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)  # отрисовка пришельца
        self.score_board.show_score()  # Вывод информации о счете

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def write_first_record(self, score):
        """Записывает первый рекорд в файл"""

        with open('records.csv', mode='a') as file:
            current_datetime = datetime.now()
            fieldnames = ['Points', 'Datetime']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Points': score, 'Datetime': current_datetime})

    def write_other_records(self, score):
        """Дозаписывает остальные рекорды"""

        with open('records.csv', mode='a') as file:
            current_datetime = datetime.now()
            writer = csv.writer(file)
            writer.writerow([score, current_datetime])

    def csvfile_existence_check(self):
        """Проверяет наличие файла records.csv"""
        try:
            with open('records.csv'):
                pass
        except FileNotFoundError:
            return False
        else:
            return True

    def read_csv(self, score):
        """Возвращает True если такой рекорд(score) уже есть в файле, иначе False"""

        with open('records.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Points'] == str(score):
                    return True
            return False

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""

        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1  # Уменьшение ships_left
            self.score_board.prep_ships()  # обновление панели счета
            self.aliens.empty()  # Очистка списка пришельцев
            self.bullets.empty()  # Очистка списка снарядов
            self._create_fleet()   # Создание нового флота
            self.ship.center_ship()  # размещение корабля в центре
            sleep(0.5)
        else:
            if not self.csvfile_existence_check() and self.stats.high_score > 0:
                self.write_first_record(self.stats.high_score)
                print('сработал csvfile_existence_check')
            else:
                if not self.read_csv(self.stats.high_score):
                    self.write_other_records(self.stats.high_score)
                    print('сработал read_csv')

            self.stats.game_active = False
            pygame.mouse.set_visible(True)


if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
