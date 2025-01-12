class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        return Rectangle(1, (self.width * self.height + other.width * other.height))
        # Другой вариант реализации(не пойму из условия по каким правилам вычислять стороны):
        # total_square = self.get_square() + other.get_square()
        # new_width = math.sqrt(total_square)
        # new_height = total_square / new_width
        # return Rectangle(new_width, new_height)
        # Но при таком варианте строны float и это значительно усложняет ведь нужно применять окуругления и точные значения маловероятны

    def __mul__(self, n):
        return Rectangle(1, (self.width * self.height * n))
        # Другой вариант реализации(не пойму из условия по каким правилам вычислять стороны):
        # total_square = self.get_square() * n
        # new_width = math.sqrt(total_square)
        # new_height = total_square / new_width
        # return Rectangle(new_width, new_height)
        # Но при таком варианте строны float и это значительно усложняет ведь нужно применять окуругления и точные значения маловероятны

    def __str__(self):
        return (f'Width: {self.width}\n'
                f'Height: {self.height} \n'
                f'Square: {self.width * self.height}')


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1)
print(r2)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
print(r3)
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
print(r4)
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print(Rectangle(3, 6) == Rectangle(2, 9))
