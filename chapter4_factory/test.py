#!/bin/env python
import sys
from pizza_store import NyStylePizzaStore


def main(argv):
    ps = NyStylePizzaStore()
    p = ps.orderPizza("cheese")
    print(p.get_name())


if __name__ == '__main__':
    main(sys.argv[1:])
