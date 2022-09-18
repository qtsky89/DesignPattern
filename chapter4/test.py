#!/bin/env python
import sys
from pizza import NystylePizza


def main(argv):
    p = NystylePizza()
    p.cut()


if __name__ == '__main__':
    main(sys.argv[1:])
