#!/bin/env python
import sys
from enum import Enum, auto


class COIN(Enum):
    SOLD_OUT = 0
    NO_QUARTER = auto()
    HAS_QUARTER = auto()
    SOLD = auto()


class GumballMachine:
    def __init__(self, count: int):
        self.__state = COIN.SOLD_OUT
        self.__count = count

        if self.__count > 0:
            self.__state = COIN.NO_QUARTER

    def insert_quarter(self):
        if self.__state == COIN.HAS_QUARTER:
            print('coin is already inserted')
        elif self.__state == COIN.NO_QUARTER:
            self.__state = COIN.HAS_QUARTER
            print('coin inserted')
        elif self.__state == COIN.SOLD_OUT:
            print('sold out. try next time')
        else:
            print('please wait')


def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
