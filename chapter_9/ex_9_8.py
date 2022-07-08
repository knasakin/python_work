# 9.8. Привилегии
from ex_9_3 import User


class Admin(User):
    def __init__(self, first_name, last_name, *args, **kwargs):
        super().__init__(first_name, last_name, *args, **kwargs)
        self.privileges = Privileges()

    def show_privileges(self):
        print(self.privileges)


class Privileges:
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено банить пользователей"]

    def show_privileges(self):
        print(self.privileges)


if __name__ == '__main__':
    a = Admin('konstantin', 'nasakin', 'blabla@mail.ru')
    a.privileges.show_privileges()
