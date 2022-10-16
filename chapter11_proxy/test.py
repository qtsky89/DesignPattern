#!/bin/env python
import sys


class GumballMachine:
    def __init__(self, location: str, count: int):
        self.__location = location
        self.__count = count

    @property
    def location(self) -> str:
        return self.__location

    @property
    def count(self) -> int:
        return self.__count


class GumballMonitor:
    def __init__(self, m: GumballMachine):
        self.machine = m

    def report(self):
        print(f'location: {self.machine.location}')
        print(f'count: {self.machine.count}')


def main(argv):
    gm = GumballMachine('Seoul', 5)
    monitor = GumballMonitor(gm)
    monitor.report()


if __name__ == '__main__':
    main(sys.argv[1:])
