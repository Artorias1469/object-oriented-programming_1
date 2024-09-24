class Fraction:
    def __init__(self, numerator=1, denominator=1):
        if not (isinstance(numerator, int) and numerator > 0):
            raise ValueError("Числитель должен быть положительным целым числом")
        if not (isinstance(denominator, int) and denominator > 0):
            raise ValueError("Знаменатель должен быть положительным целым числом")
        self.__numerator = numerator
        self.__denominator = denominator

    def ipart(self):
        if self.__denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        return self.__numerator // self.__denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator


def read_fraction(prompt=None):
    line = input() if prompt is None else input(prompt)
    parts = list(map(int, line.split("/")))
    if len(parts) != 2:
        raise ValueError("Неправильный формат дроби")
    return Fraction(parts[0], parts[1])


def display_fraction(fraction):
    print(f"{fraction.numerator}/{fraction.denominator}")


if __name__ == "__main__":
    f1 = Fraction(5, 2)
    display_fraction(f1)
    print(f"Целая часть: {f1.ipart()}")

    f2 = read_fraction("Введите дробь (числитель/знаменатель): ")
    display_fraction(f2)
    print(f"Целая часть: {f2.ipart()}")