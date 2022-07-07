# 9.1. Ресторан
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.__dict__)

    def open_restaurant(self):
        print('Ресторан открыт')


if __name__ == '__main__':
    restaurant = Restaurant('Napoli', 'Italian food')

    for key, value in restaurant.__dict__.items():
        print(f'{key}={value}')

    restaurant.describe_restaurant()
    restaurant.open_restaurant()
