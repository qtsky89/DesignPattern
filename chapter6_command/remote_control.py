#!/bin/env python
from command import Command


class SimpleRemoteControl:
    def __init__(self):
        self.__slot: Command = None  # type: ignore

    def set_command(self, command: Command):
        self.__slot = command

    def button_was_pressed(self):
        self.__slot.execute()
