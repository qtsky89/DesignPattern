#!/bin/env python
import sys
from command import LightOnCommand
from simple_remote_control import SimpleRemoteControl
from light import Light


def main(argv):
    remote = SimpleRemoteControl()
    light = Light('Seoul')
    light_on = LightOnCommand(light)

    remote.set_command(light_on)
    remote.button_was_pressed()


if __name__ == '__main__':
    main(sys.argv[1:])
