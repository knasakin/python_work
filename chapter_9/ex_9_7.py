# 9.7. Администратор
from ex_9_3 import User


class Admin(User):
    def __init__(self, first_name, last_name, privileges=None, *args, **kwargs):
        if privileges is None:
            privileges = []

        super().__init__(first_name, last_name, *args, **kwargs)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


if __name__ == '__main__':
    permissions = ["разрешено добавлять сообщения", "разрешено банить пользователей"]
    a = Admin('konstantin', 'nasakin', permissions, location='VLZ')
    a.show_privileges()
