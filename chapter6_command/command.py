#!/bin/env python
from abc import ABCMeta, abstractmethod
from light import Light


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute():
        raise NotImplementedError

    @abstractmethod
    def undo():
        raise NotImplementedError


class LightOnCommand (Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand (Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()
