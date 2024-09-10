class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __mul__(self, other):
        numerator = self.a * other.a
        denominator = self.b * other.b
        common_divisor = Fraction.gcd(numerator, denominator)
        return Fraction(int(numerator / common_divisor), int(denominator / common_divisor))

    def __add__(self, other):
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        common_divisor = Fraction.gcd(numerator, denominator)
        return Fraction(int(numerator / common_divisor), int(denominator / common_divisor))

    def __sub__(self, other):
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        common_divisor = Fraction.gcd(numerator, denominator)
        return Fraction(int(numerator / common_divisor), int(denominator / common_divisor))

    def __eq__(self, other):
        numerator1 = self.a * other.b
        numerator2 = other.a * self.b
        return numerator1 == numerator2

    def __gt__(self, other): #больше
        numerator1 = self.a * other.b
        numerator2 = other.a * self.b
        return numerator1 > numerator2

    def __lt__(self, other):
        numerator1 = self.a * other.b
        numerator2 = other.a * self.b
        return numerator1 < numerator2

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)
assert str(f_c) == 'Fraction: 7, 6' #Вел в расчет сокращение дроби, поэтому результа не 21, 18
f_d = f_b * f_a
print(f_d)
assert str(f_d) == 'Fraction: 1, 3' #Вел в расчет сокращение дроби, поэтому результа не 6, 18
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6' #Вел в расчет сокращение дроби, поэтому результа не 3, 18
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
