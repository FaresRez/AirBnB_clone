#!/usr/bin/python3
"""
This module defines the command-line interp.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = "(hbtn) "
    classes_names = {"BaseModel": BaseModel, "User": User, "Place": Place,
                     "State": State, "City": City, "Amenity": Amenity,
                     "Review": Review}

    def verify_class(self, input):
        """Verify if the class name exists"""
        words = input.split()
        if len(words) == 0:
            print("** class name missing **")
            return None
        if words[0] not in self.classes_names:
            print("** class doesn't exist **")
            return None
        if len(words) == 1:
            print("** instance id missing **")
            return None
        return f"{words[0]}.{words[1]}"
        

    def __init__(self):
        """Initialize the command interpreter"""
        super().__init__()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def default(self, line: str):
        """Called on an input line"""
        if '.' in line and line.endswith('.all()'):
            check = line.split('.')
            if check[0] in self.classes_names:
                object_list = []
                for obj in storage.all().values():
                    if obj.__class__.__name__ == check[0]:
                        object_list.append(obj.__str__())
                print(object_list)
            else:
                print("** class doesn't exist **")
            return
    
        if line == "EOF":
            return self.do_EOF(line)
        print(f"*** Unknown syntax: {line}")
        return False

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if line == "":
            print("** class name missing **")
        elif line not in self.classes_names:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes_names[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string rep of an instance based on the class,id"""
        key = self.verify_class(line)
        if not key:
            return
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        key = self.verify_class(line)
        if not key:
            return
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """prints all string rep of all ins based or not on the class name"""
        words = line.split()
        
        if len(words) == 1:
            if words[0] not in self.classes_names:
                print("** class doesn't exist **")
                return
        object_list = []
        for obj in storage.all().values():
            object_list.append(obj.__str__())
        print(object_list)

    def do_update(self, line):
        """updates an instance based on the class name and id by adding or"""
        words = line.split()
        names = ["name", "my_number"]
        if len(words) == 0:
            print("** class name missing **")
            return
        
        if words[0] not in self.classes_names:
            print("** class doesn't exist **")
            return
        
        if len(words) == 1:
            print("** instance id missing **")
            return
        
        key = f"{words[0]}.{words[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        
        if len(words) == 2:
            print("** attribute name missing **")
            return

        if len(words) == 3:
            print("** value missing **")
            return


        obj = storage.all()[key]
        setattr(obj, words[2], words[3].strip('"'))
        storage.save()
        



if __name__ == '__main__':
    HBNBCommand().cmdloop()
