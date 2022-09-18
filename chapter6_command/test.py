#!/bin/env python
import sys
from command import LightOffCommand, LightOnCommand
from remote_control import RemoteControl
from light import Light


def main(argv):
    remote = RemoteControl()
    light = Light('Seoul')
    remote.set_command(0, LightOnCommand(light), LightOffCommand(light))
    remote.on_btn_pushed(0)
    remote.off_btn_pushed(0)
    remote.undo_btn_pushed()


if __name__ == '__main__':
    main(sys.argv[1:])
