#!/usr/bin/python3
"""define a class HBNBCommand contains the entry point of the cmd
interpreter"""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """representation of HBNBCommand
    Args:
        prompt (string): the cmd prompt
    """
    prompt = "(hbnb) "
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program
        Usage: quite
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Usage: show <class> <id> or <class>.show>id>)
        Creates an instance of the BaseModel
        saves it to the JSON file) and prints the id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                new_instance = HBNBCommand.__classes[class_name]()
                storage.save()
                print(new_instance.id)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = arg.split()
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_show(self, arg):
        """Print the strng representation of an
        instance on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) < 1:
                print("** instance id missing **")
            else:
                cls_name = args[0]
                cls = HBNBCommand.__classes
                if cls is None:
                    print("** class doesn't exist **")
                else:
                    if len(args) < 2:
                        print("** instance id missing **")
                    else:
                        obj_id = args[1]
                        key = "{}.{}".format(cls_name, obj_id)
                        all_objs = storage.all()
                        obj = all_objs
                        if obj is None:
                            print("** no instance found **")
                        else:
                            print(obj)

    def do_destroy(self, arg):
        """deletes an instance based on the class and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) < 1:
                print("** instance id missing **")
            else:
                cls_name = args[0]
                cls = HBNBCommand.__classes.get(cls_name)
                if cls is None:
                    print("** class doesn't exist **")
                else:
                    if len(args) < 2:
                        print("** instance id missing **")
                    else:
                        obj_id = args[1]
                        key = "{}.{}".format(cls_name, obj_id)
                        all_objs = storage.all()
                        obj = all_objs.get(key)
                        if obj is None:
                            print("** no instance found **")
                        else:
                            del all_objs[key]
                            BaseModel.save_to_file(all_objs)

    def do_all(self, args):
        """
        Prints all string represenration of all
            instances based or not on the class name
        Args:
            arg_list (int): number of arguments
            objects (dict): defining a dict
        Usage: all [<class name>]
        """
        arg_list = args.split()
        objects = []

        if not arg_list:
            objects += storage.all().values()
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            for objects in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    objects.append(obj.__str__())
                elif len(argl) == 0:
                    objects.append(obj.__str__())
            print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute.
            Usage: update <class name> <id>
            <attribute name> "<attribute value>"
        Args:
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = " ".join(args[3:])
        opt1 = "id"
        opt2 = "created_at"
        opt3 = "updated_at"
        if attr_name == opt1 or attr_name == opt2 or attr_name == opt3:
            return
        if hasattr(obj, attr_name):
            attr_value = type(getattr(obj, attr_name))(attr_value)
            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            setattr(obj, attr_name, attr_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
