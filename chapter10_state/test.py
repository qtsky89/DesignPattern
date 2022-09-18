#!/bin/env python
import sys

from machine import GumballMachine


def main(argv):
    g = GumballMachine(10)
    g.insert_quarter()


if __name__ == '__main__':
    main(sys.argv[1:])
