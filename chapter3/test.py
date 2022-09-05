#!/bin/env python
import sys
from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self._description = 'no description'

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self._description = 'espresso'

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self._description = 'houseblend'

    def cost(self) -> float:
        return 0.89


class CondimentDecorator(Beverage):
    # TODO: why I choose this architecture ??
    def __init__(self):
        self._beverage: Beverage = None

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_description(self) -> str:
        return f'{self._beverage.get_description()}, mocha'

    def cost(self) -> float:
        return self._beverage.cost() + 0.2


def main(argv):
    b: Beverage = Espresso()

    print(f'{b.get_description()}, ${b.cost()}')

    b2: Beverage = HouseBlend()
    b2 = Mocha(b2)

    print(f'{b2.get_description()}, ${b2.cost()}')


if __name__ == '__main__':
    main(sys.argv[1:])
