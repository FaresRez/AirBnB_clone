import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = "(hbtn) "

    def __init__(self):
        super().__init__()

    def do_test(self, line):
        """this is a test"""
        print(f"welcome to my cmd {line}")

    def do_create(self, line):
        """Creates a new instance and save it to new instance"""
        if line == "":
            print("** class name missing **")
        elif False:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Shows all instances of a class"""

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
