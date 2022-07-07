# 9.6. Киоск с мороженым
from ex_9_1 import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=None):
        if flavors is None:
            self.flavors = []

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        print(self.flavors)


i = IceCreamStand('Napoli', 'Italian food', ['basic', 'chocolate'])
print(i.__dict__)
i.print_flavors()
