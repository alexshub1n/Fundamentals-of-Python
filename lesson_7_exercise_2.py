from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def expense(self):
        pass

    def all_expense(self, all_clothes):
        sum_exp = 0
        for i in all_clothes:
            sum_exp += i.expense
        return sum_exp


class Сoat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def expense(self):
        coat_exp = self.v / 6.5 + 0.5
        return coat_exp


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def expense(self):
        costume_exp = 2 * self.h + 0.3
        return costume_exp


my_coat = Сoat(200)
my_costume = Costume(10)
my_costume_2 = Costume(15)
all_clothes = [my_coat, my_costume, my_costume_2]

print(my_coat.expense)
print(my_costume.expense)
print(my_costume_2.expense)

print(my_coat.all_expense(all_clothes))
# print(my_costume.all_expense(all_clothes))
