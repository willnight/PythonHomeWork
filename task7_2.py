from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Coat(Clothes):

    @property
    def tissue_consumption(self):
        return round((self.size / 6.5) + 0.5)


class Jacket(Clothes):

    @property
    def tissue_consumption(self):
        return round((self.size * 2) + 0.3) / 100


cloth = Clothes
coat = Coat(8)
print(f"{coat.tissue_consumption}м ткани")
print("-" * 30)
jacket = Jacket(165)
print(f"{jacket.tissue_consumption}м ткани")
print("-" * 30)
print(f"{coat + jacket}м ткани")
