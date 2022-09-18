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
    def create_iterator() -> Iterator:
        raise NotImplementedError


class DinerMenuIterator(Iterator):
    def __init__(self, menu: List[str]) -> None:
        self.__menu = menu
        self.__index = -1

    def has_next(self) -> bool:
        if self.__index + 1 <= len(self.__menu) - 1:
            return True

        return False

    def next(self):
        self.__index += 1
        return self.__menu[self.__index]


def main(argv):
    print('hello world')


if __name__ == '__main__':
    main(sys.argv[1:])
