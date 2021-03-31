"""
Создать класс Дробное число со знаком (Fractions). Число должно быть представлено
двумя полями: целая часть - длинное целое со знаком, дробная часть - беззнаковое
короткое целое. Реализовать арифметические операции сложения, вычитания, умножения
и операции сравнения.
"""


class FractionNum:
    def __init__(self, number):
        self.number = str(number)

        integer, decimal = self.number.split('.')
        self.integer = int(integer)
        self.decimal = int(decimal)

    def __add__(self, other):
        print(f'{self.integer} + {self.decimal} = {self.integer + self.decimal}')

    def __sub__(self, other):
        print(f'{self.integer} - {self.decimal} = {self.integer - self.decimal}')

    def __mul__(self, other):
        print(f'{self.integer} * {self.decimal} = {self.integer * self.decimal}')

    def __eq__(self, other):
        print(f'{self.integer} == {self.decimal} is {self.integer == self.decimal}')

    def __ne__(self, other):
        print(f'{self.integer} != {self.decimal} is {self.integer != self.decimal}')

    def __lt__(self, other):
        print(f'{self.integer} < {self.decimal} is {self.integer < self.decimal}')

    def __le__(self, other):
        print(f'{self.integer} <= {self.decimal} is {self.integer <= self.decimal}')

    def __gt__(self, other):
        print(f'{self.integer} > {self.decimal} is {self.integer > self.decimal}')

    def __ge__(self, other):
        print(f'{self.integer} >= {self.decimal} is {self.integer >= self.decimal}')


def main():
    testNum = FractionNum(12.5)
    testNum + testNum
    testNum - testNum
    testNum * testNum
    testNum == testNum
    testNum != testNum
    testNum < testNum
    testNum <= testNum
    testNum > testNum
    testNum >= testNum


if __name__ == '__main__':
    main()
