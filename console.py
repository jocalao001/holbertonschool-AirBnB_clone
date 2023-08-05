#!/usr/bin/python3
# console.py
# Jose Tirado <5698@holbertonstudents.com>
"""Define a console implementation."""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.__init__ import models_classes
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Represent a console of HBNBCommand."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Secures a clean exit."""
        return True

    def emptyline(self):
        """Stop the last executed command"""
        pass

    def do_create(self, arg):
        """Create a new instances of BaseModel
        class, save it into a JSON file and print id.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in models_classes:
            print("** class doesn't exist **")
        else:
            new_instance = models_classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representationof an instance
        based on the class name
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class
        name and id; saves the change into de json file
        """
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")

        elif args[0] not in models_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            instances = storage.all()
            if key not in instances.keys():
                print("** no instance found **")
            else:
                del instances[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        obj_list = []
        cls_k = models_classes.keys()
        if not arg:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif arg in cls_k:
            for obj in storage.all().values():
                if isinstance(obj, models_classes[arg]):
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, arg):
        """ """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            instances = storage.all()
            if key not in instances.keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            else:
                obj = instances[key]
                setattr(obj, args[2], args[3])
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
