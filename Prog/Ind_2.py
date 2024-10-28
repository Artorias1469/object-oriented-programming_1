#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money:
    def __init__(self, rubles: int, kopecks: int):
        if kopecks >= 100:
            self.rubles = rubles + kopecks // 100
            self.kopecks = kopecks % 100
        else:
            self.rubles = rubles
            self.kopecks = kopecks

    def read(self):
        rubles, kopecks = map(int, input("Введите сумму в формате рубли,копейки: ").split(","))
        self.__init__(rubles, kopecks)

    def display(self):
        print(f"{self.rubles},{self.kopecks:02d}")

    def add(self, other):
        total_kopecks = self.rubles * 100 + self.kopecks + other.rubles * 100 + other.kopecks
        return Money(0, total_kopecks)

    def subtract(self, other):
        total_kopecks = abs((self.rubles * 100 + self.kopecks) - (other.rubles * 100 + other.kopecks))
        return Money(0, total_kopecks)

    def multiply(self, multiplier: float):
        total_kopecks = int((self.rubles * 100 + self.kopecks) * multiplier)
        return Money(0, total_kopecks)

    def divide(self, divisor: float):
        if divisor == 0:
            raise ValueError("Деление на ноль невозможно")
        total_kopecks = int((self.rubles * 100 + self.kopecks) / divisor)
        return Money(0, total_kopecks)

    def __eq__(self, other):
        return (self.rubles == other.rubles) and (self.kopecks == other.kopecks)

    def __lt__(self, other):
        return (self.rubles * 100 + self.kopecks) < (other.rubles * 100 + other.kopecks)

    def __le__(self, other):
        return (self.rubles * 100 + self.kopecks) <= (other.rubles * 100 + other.kopecks)


if __name__ == "__main__":
    money1 = Money(100, 50)
    money1.display()

    money2 = Money(0, 0)
    money2.read()
    money2.display()

    sum_money = money1.add(money2)
    print("Сумма двух сумм:")
    sum_money.display()

    diff_money = money1.subtract(money2)
    print("Разность двух сумм:")
    diff_money.display()

    multiplied_money = money1.multiply(1.5)
    print("Умножение на 1.5:")
    multiplied_money.display()

    divided_money = money1.divide(2)
    print("Деление на 2:")
    divided_money.display()

    print("Сравнение сумм:")
    print("money1 == money2:", money1 == money2)
    print("money1 < money2:", money1 < money2)
    print("money1 <= money2:", money1 <= money2)
