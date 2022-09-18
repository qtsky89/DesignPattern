#!/bin/env python
from abc import ABCMeta, abstractmethod
from light import Light


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute():
        raise NotImplementedError


class LightOnCommand (Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()
