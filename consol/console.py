#!/usr/bin/python3
""" The consol """


import cmd
from models.base_model import BaseModel
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    bnbclass = ["BaseModel", "User"]

    def do_quit(self, arg):
        """ Exit the interpriter """

        return True

    def do_EOF(self, arg):
       """ exit the command """

       return True

    def do_create(self, arg):
       """ create new object """

       if arg:
         args = arg.split()
         if args[0] in self.bnbclass:
           o_class = globals()[args[0]]
           obj = o_class()
           obj.save()
           print(obj.id)
         else:
           print("** class doesn't exist **")
       else:
           print("** class name missing **")

    def do_show(self, arg):
        """ show obj """

        if arg:
            args = arg.split()
            if args[0] not in self.bnbclass:
                print("** class doesn't exist **")
            if args[0] in self.bnbclass and len(args) < 2:
                print("** instance id missing **")
            if args[0] in self.bnbclass and len(args) > 1:
                dic = models.storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in dic:
                    print(dic[key])
                else:
                    print("** no instance found **")

        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ delete object """

        if arg:
            args = arg.split()
            if args[0] not in self.bnbclass:
                print("** class doesn't exist **")
            if args[0] in self.bnbclass and len(args) < 2:
                print("** instance id missing **")
            if args[0] in self.bnbclass and len(args) > 1:
                dic = models.storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in dic:
                    del dic[key]
                    models.storage.save()

        else:
            print("** class name missing **")

    def do_all(self, arg):
        """ print all instances """

        if arg:
            args = arg.split()
            if args[0] not in self.bnbclass:
                print("** class doesn't exist **")
            else:
                ls = []
                dic = models.storage.all()
                for key, value in dic.items():
                    name, c_id = key.split(".")
                    if args[0] == name:
                        ls.append(str(value))
                print(ls)
        else:
            ls = []
            dic = models.storage.all()
            for key, value in dic.items():
                ls.append(str(value))
            print(ls)

    def do_update(self, arg):
        """ update object """

        if arg:
            args = arg.split()
            if args[0] not in self.bnbclass:
                print("** class doesn't exist **")
            if args[0] in self.bnbclass and len(args) < 2:
                print("** instance id missing **")
            if args[0] in self.bnbclass and len(args) > 1:
                key = "{}.{}".format(args[0], args[1])
                dic = models.storage.all()
                if key not in dic:
                    print("** no instance found **")
                elif key in dic and len(args) < 3:
                    print("** attribute name missing **")
                elif key in dic and len(args) < 4:
                    print("** value missing **")
                elif key in dic and len(args) > 3:
                    setattr(dic[key], args[2], args[3])
                    dic[key].save()
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
