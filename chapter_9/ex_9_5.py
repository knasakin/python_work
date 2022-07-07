# 9.5. Попытки входа
class User:
    def __init__(self, first_name: str, last_name: str, login_attempts: 3, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

        if kwargs:
            for key, value in kwargs.items():
                self.__dict__[key] = value

    def describe_user(self):
        print(self.__dict__)

    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


u = User('konstantin', 'nasakin', 2, location='VLZ')

u.increment_login_attempts()
u.increment_login_attempts()
print(u.login_attempts)

u.reset_login_attempts()
print(u.login_attempts)
