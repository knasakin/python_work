# 9.8. Привилегии
from ex_9_7 import Admin


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


permissions = ["разрешено добавлять сообщения", "разрешено банить пользователей"]
