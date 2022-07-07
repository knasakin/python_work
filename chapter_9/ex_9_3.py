# 9.3. Пользователи
class User:
    def __init__(self, first_name, last_name, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name

        if kwargs:
            for key, value in kwargs.items():
                self.__dict__[key] = value

    def describe_user(self):
        print(self.__dict__)

    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}')


if __name__ == '__main__':
    u1 = User('konstantin', 'nasakin', location='VLZ')
    u1.describe_user()
    u1.greet_user()

    u2 = User('Petya', 'Ivanov')
    u2.describe_user()
    u2.greet_user()
