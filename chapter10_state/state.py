#!/bin/env python
from abc import ABCMeta, abstractmethod
from machine import GumballMachine


class State(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, machine: GumballMachine):
        self.__machine = machine

    @abstractmethod
    def insert_quarter(self):
        raise NotImplementedError


class NoQuarterState(State):
    def __init__(self, machine: GumballMachine):
        super().__init__(machine)

    def insert_quarter(self):
        print('inserted')
