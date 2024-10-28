#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Fraction:
    def __init__(self, first: int = 1, second: int = 1):
        if second == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        if first < 0 or second < 0:
            raise ValueError("Числитель и знаменатель должны быть положительными")
        self.first = first
        self.second = second

    def read(self):
        line = input("Введите дробь в формате числитель/знаменатель: ")
        parts = line.split('/')
        if len(parts) != 2:
            raise ValueError("Неправильный формат ввода. Используйте формат 'числитель/знаменатель'")
        self.first, self.second = map(int, parts)
        if self.second == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

    def display(self):
        print(f"{self.first}/{self.second}")

    def ipart(self):
        return self.first // self.second

    @staticmethod
    def make_fraction(first: int, second: int):
        if second == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        return Fraction(first, second)


if __name__ == "__main__":
    # Демонстрация возможностей класса Fraction
    fraction1 = Fraction.make_fraction(5, 3)
    fraction1.display()
    print("Целая часть дроби:", fraction1.ipart())

    fraction2 = Fraction()
    fraction2.read()
    fraction2.display()
    print("Целая часть дроби:", fraction2.ipart())
