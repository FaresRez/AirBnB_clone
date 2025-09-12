#!/usr/bin/python3
"""
This module defines the command-line interp.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = "(hbtn) "

    def __init__(self):
        """Initialize the command interpreter"""
        super().__init__()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def default(self, line):
        """Called on an input line"""
        print("unknown command")

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_EOF(self, line):
        """exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
