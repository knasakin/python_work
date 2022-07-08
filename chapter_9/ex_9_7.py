# 9.7. Администратор
from ex_9_3 import User
from ex_9_8 import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, *args, **kwargs):
        super().__init__(first_name, last_name, *args, **kwargs)
        self.privileges = Privileges()

    def show_privileges(self):
        print(self.privileges)


if __name__ == '__main__':
    permissions = ["разрешено добавлять сообщения", "разрешено банить пользователей"]
    a = Admin('konstantin', 'nasakin', permissions, location='VLZ')
    a.show_privileges()
