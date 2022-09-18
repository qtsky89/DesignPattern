#!/bin/env python
import sys


class Singleton():
    value: 'Singleton' = None  # type: ignore

    @classmethod
    def get_instance(cls) -> 'Singleton':
        if cls.value is None:
            print('inside')
            cls.value = Singleton()
        return cls.value


def main(argv):
    Singleton.get_instance()
    Singleton.get_instance()


if __name__ == '__main__':
    main(sys.argv[1:])
