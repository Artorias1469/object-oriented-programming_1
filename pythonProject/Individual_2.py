class Money:
    def __init__(self, rubles=0, kopecks=0):
        self.rubles = rubles + kopecks // 100
        self.kopecks = kopecks % 100

    def __add__(self, other):
        return Money(self.rubles + other.rubles, self.kopecks + other.kopecks)

    def __sub__(self, other):
        total_kopecks = (self.rubles * 100 + self.kopecks) - (other.rubles * 100 + other.kopecks)
        return Money(total_kopecks // 100, total_kopecks % 100)

    def __mul__(self, multiplier):
        total_kopecks = (self.rubles * 100 + self.kopecks) * multiplier
        return Money(total_kopecks // 100, total_kopecks % 100)

    def __truediv__(self, divisor):
        total_kopecks = (self.rubles * 100 + self.kopecks) / divisor
        return Money(int(total_kopecks // 100), int(total_kopecks % 100))

    def __lt__(self, other):
        return (self.rubles, self.kopecks) < (other.rubles, other.kopecks)

    def __le__(self, other):
        return (self.rubles, self.kopecks) <= (other.rubles, other.kopecks)

    def __eq__(self, other):
        return (self.rubles, self.kopecks) == (other.rubles, other.kopecks)

    def __str__(self):
        return f"{self.rubles},{str(self.kopecks).zfill(2)}"

# Ввод и вывод данных можно вынести за пределы класса
def read_money():
    rubles = int(input("Введите сумму в рублях: "))
    kopecks = int(input("Введите сумму в копейках: "))
    return Money(rubles, kopecks)

def display_money(money):
    print(f"Сумма: {money}")

# Демонстрация возможностей класса
if __name__ == "__main__":
    money1 = Money(100, 50)
    money2 = Money(200, 75)

    print("Сумма 1:")
    display_money(money1)
    print("Сумма 2:")
    display_money(money2)

    sum_money = money1 + money2
    print("Сумма:")
    display_money(sum_money)

    diff_money = money1 - money2
    print("Разность:")
    display_money(diff_money)

    multiplied_money = money1 * 2.5
    print("Умноженная сумма:")
    display_money(multiplied_money)

    divided_money = money1 / 2
    print("Делёная сумма:")
    display_money(divided_money)

    print(f"Сумма 1 меньше суммы 2: {money1 < money2}")