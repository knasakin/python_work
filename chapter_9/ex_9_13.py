# 9.13. Кубики
from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        throws = [randint(1, self.sides) for _ in range(10)]
        print(*throws)


d1 = Die(6)
d1.roll_die()

d2 = Die(10)
d2.roll_die()

d3 = Die(20)
d3.roll_die()
