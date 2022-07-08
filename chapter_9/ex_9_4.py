# 9.4. Посетители
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.__dict__)

    def open_restaurant(self):
        print('Ресторан открыт')

    def set_number_served(self, number_served: int):
        self.number_served = number_served

    def increment_number_served(self, number_served: int):
        self.number_served += number_served


if __name__ == '__main__':
    restaurant = Restaurant('Napoli', 'Italian food', 3)
    restaurant.describe_restaurant()
    restaurant.set_number_served(4)
    restaurant.describe_restaurant()
    restaurant.increment_number_served(50)
    restaurant.describe_restaurant()
