import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbtn) "

    def __init__(self):
        super().__init__()

    def do_test (self, line):
        """this is a test"""
        print(f"welcome to my cmd {line}")

    def do_create (self, line):
        """Creates a new instance and save it to new instance"""
        if line == "":
            print("** class name missing **")
        elif False:
            print("** class doesn't exist **")

    def do_show (self, line):
        """Shows all instances of a class"""
        
    def do_quit (self, line):
        """Quit command to exit the program"""
        return True

    def default(self, line):
        print("unknown command")


    def emptyline(self):
        pass

    def do_EOF(self, line):
        """exit the program"""
        return True
    
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()