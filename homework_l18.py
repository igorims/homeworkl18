"""
Создать класс Дробное число со знаком (Fractions). Число должно быть представлено
двумя полями: целая часть - длинное целое со знаком, дробная часть - беззнаковое
короткое целое. Реализовать арифметические операции сложения, вычитания, умножения
и операции сравнения.
"""


class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    LIGHTGRAY = "\033[37m"


# Комментарий. По заданию не очень понятно, нужно ли складывать и сравнивать целые и дробные числа ОДНОГО числа,
# указанного при определении инстанса (решение 1), или производить операции над двумя инстансами класса
# (решение 2), поэтому сделал оба решения.

# Решение 1
class FractionNum:
    def __init__(self, number):
        self.number = str(number)

        integer, decimal = self.number.split('.')
        self.integer = int(integer)
        self.decimal = int(decimal)

        print(f'{bcolors.OKGREEN}Number: {self.number}{bcolors.ENDC}')

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


# Решение 2.
# В объект вводятся 2 числа. По дробной части проходится проверка на положительное/отрицательное число, а
# также на ввод в виде строки (чтобы, например, написать 003), строка также проверяется на ввод отрицательного значения.
# Далее из обоих чисел делается одно число number и производятся необходимые операции

class FractionNum1:
    counter = 1

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        if isinstance(num2, str):
            if self.num2.startswith('-'):
                num2 = num2[1:]
            self.number = str(num1) + "." + num2

        else:
            self.number = str(num1) + "." + str(abs(num2))
        self.number = float(self.number)

        print(f'{bcolors.OKGREEN}Number {self.counter}: {self.number}{bcolors.ENDC}')

        FractionNum1.counter += 1

    def __add__(self, other):
        print(f'{self.number} + {other.number} = {self.number + other.number}')

    def __sub__(self, other):
        print(f'{self.number} - {other.number} = {(self.number - other.number):.2}')

    def __mul__(self, other):
        print(f'{self.number} * {other.number} = {(self.number * other.number):.4}')

    def __eq__(self, other):
        print(f'{self.number} == {other.number} is {self.number == other.number}')

    def __ne__(self, other):
        print(f'{self.number} != {other.number} is {self.number != other.number}')

    def __lt__(self, other):
        print(f'{self.number} < {other.number} is {self.number < other.number}')

    def __le__(self, other):
        print(f'{self.number} <= {other.number} is {self.number <= other.number}')

    def __gt__(self, other):
        print(f'{self.number} > {other.number} is {self.number > other.number}')

    def __ge__(self, other):
        print(f'{self.number} >= {other.number} is {self.number >= other.number}')


def main():
    print(f'{bcolors.HEADER}Решение 1{bcolors.ENDC}')
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

    print()
    print(f'{bcolors.HEADER}Решение 2{bcolors.ENDC}')
    testNum1 = FractionNum1(10, -2000)
    testNum2 = FractionNum1(5, '-003')
    testNum3 = FractionNum1(-30, '000050')
    testNum1 + testNum2
    testNum1 - testNum2
    testNum1 * testNum2
    testNum1 == testNum2
    testNum1 != testNum2
    testNum1 < testNum2
    testNum1 <= testNum2
    testNum1 > testNum2
    testNum1 >= testNum2


if __name__ == '__main__':
    main()
