#!/bin/env python
import sys


class Singleton():
    __value: 'Singleton' = None  # type: ignore

    @classmethod
    def get_instance(cls) -> 'Singleton':
        if cls.__value is None:
            print('inside')
            cls.__value = Singleton()
        return cls.__value


def main(argv):
    Singleton.get_instance()
    Singleton.get_instance()


if __name__ == '__main__':
    main(sys.argv[1:])
