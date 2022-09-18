#!/bin/env python
import sys
from abc import ABCMeta, abstractmethod


class Duck(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        raise NotImplementedError

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class MallardDuck(Duck):
    def quack(self):
        print('quack quack')

    def fly(self):
        print('fly fly')


class Turkey(metaclass=ABCMeta):
    @abstractmethod
    def gobble(self):
        raise NotImplementedError

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class WildTurkey(Turkey):
    def gobble(self):
        print('gobble gobble')

    def fly(self):
        print('fly')


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey) -> None:
        self.__turkey = turkey

    def quack(self):
        self.__turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.__turkey.fly()


def main(argv):
    t: Duck = TurkeyAdapter(WildTurkey())
    t.quack()
    t.fly()


if __name__ == '__main__':
    main(sys.argv[1:])
