#!/bin/env python
from abc import ABCMeta, abstractmethod
from typing import List
import sys


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def next(self):
        raise NotImplementedError


class Menu(metaclass=ABCMeta):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        raise NotImplementedError


class CafeMenu(Menu):
    def create_iterator(self) -> Iterator:
        return DinerMenuIterator(['omelet', 'hotcake', 'sosauge'])


class DinerMenuIterator(Iterator):
    def __init__(self, menu: List[str]) -> None:
        self.__menu = menu
        self.__index = -1

    def has_next(self) -> bool:
        if self.__index + 1 <= len(self.__menu) - 1:
            return True

        return False

    def next(self) -> str:
        self.__index += 1
        return self.__menu[self.__index]


class Waitress:
    def __init__(self, cafe_menu: Menu) -> None:
        self.__cafe_menu = cafe_menu

    def print_menu(self):
        cafe_iterator = self.__cafe_menu.create_iterator()
        self.print_menu_iterator(cafe_iterator)

    def print_menu_iterator(self, iterator: Iterator):
        while iterator.has_next():
            print(iterator.next())


def main(argv):
    c = CafeMenu()
    w = Waitress(c)
    w.print_menu()


if __name__ == '__main__':
    main(sys.argv[1:])
