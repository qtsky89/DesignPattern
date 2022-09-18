#!/bin/env python

from enum import Enum, auto
from state import NoQuarterState


class COIN(Enum):
    SOLD_OUT = 0
    NO_QUARTER = auto()
    HAS_QUARTER = auto()
    SOLD = auto()


class GumballMachine:
    def __init__(self, count: int):
        self.__state = NoQuarterState(self)
        self.__count = count

    def insert_quarter(self):
        self.__state.insert_quarter()
