#!/bin/env python
from command import Command
from typing import List


class SimpleRemoteControl:
    def __init__(self):
        self.__slot: Command = None  # type: ignore

    def set_command(self, command: Command):
        self.__slot = command

    def button_was_pressed(self):
        self.__slot.execute()


class RemoteControl:
    def __init__(self):
        self.__on_commands: List[Command] = [None] * 7  # type: ignore
        self.__off_commands: List[Command] = [None] * 7  # type: ignore

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.__on_commands[slot] = on_command
        self.__off_commands[slot] = off_command

    def on_command_pushed(self, slot: int):
        self.__on_commands[slot].execute()

    def off_command_pushed(self, slot: int):
        self.__off_commands[slot].execute()
