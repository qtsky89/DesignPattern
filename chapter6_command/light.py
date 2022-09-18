#!/bin/env python

class Light:
    def __init__(self, location: str):
        self.__location = location

    def on(self):
        print(f'{self.__location} light is on')

    def off(self):
        print(f'{self.__location} light is off')

    def execute(self):
        self.on()
