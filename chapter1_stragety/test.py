#!/bin/env python
import sys
from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError

class FlyWithWing(FlyBehavior):
    def fly(self):
        print('fly with wing')

class Duck:
    def __init__(self):
        self.fly_behavior: FlyBehavior = None

    def perform_fly(self):
        self.fly_behavior.fly()

class DuckWithWing(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWing()
    

def main(argv):
    d = DuckWithWing()
    d.perform_fly()
    

if __name__ == '__main__':
    main(sys.argv[1:])
