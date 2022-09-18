#!/bin/env python
from abc import ABCMeta, abstractmethod
import sys


class CaffeineBeverage(metaclass=ABCMeta):
    @abstractmethod
    def _brew(self):
        raise NotImplementedError

    @abstractmethod
    def _add_condiments(self):
        raise NotImplementedError

    def _boil_water(self):
        print('boiling water')

    def _pour_in_cup(self):
        print('pour in cup')

    def prepare_recipe(self):
        self._boil_water()
        self._brew()
        self._pour_in_cup()
        self._add_condiments()


class Coffee(CaffeineBeverage):
    def _brew(self):
        print('brew conffee bean')

    def _add_condiments(self):
        print('add milk')


class Tea(CaffeineBeverage):
    def _brew(self):
        print('brew tea leaves')

    def _add_condiments(self):
        print('add lemon')


def main(argv):
    t: CaffeineBeverage = Tea()
    t.prepare_recipe()

    print()

    t: CaffeineBeverage = Coffee()
    t.prepare_recipe()


if __name__ == '__main__':
    main(sys.argv[1:])
