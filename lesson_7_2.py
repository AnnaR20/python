from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fabric(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    def fabric(self):
        self.fabriccons = round((self.v / 6.5 + 0.5), 2)
        print('Расход ткани', self.fabriccons)

    def __add__(self, other):
        print('Общий расход ткани', self.fabriccons + other.fabriccons)


class Suit(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    def fabric(self):
        self.fabriccons = round((self.h * 2 + 3), 2)
        print('Расход ткани', self.fabriccons)

    def __add__(self, other):
        print('Общий расход ткани', self.fabriccons + other.fabriccons)


coat1 = Coat(48)
coat1.fabric()
suit1 = Suit(1.80)
suit1.fabric()
coat1 + suit1
