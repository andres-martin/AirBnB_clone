#!/usr/bin/python3
""" command interpreter """


import cmd
from models import clases
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ interpreter of commands"""
    prompt = '(hbnb)'
    up_clases = clases

    def do_quit(self, args):
        """ quit command """
        quit()

    def do_EOF(self, args):
        """ EOF command """
        quit()

    def do_help(self, args):
        """ details of a command"""
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """ back to the prompt"""
        return

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        argumentos = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if (argumentos[0] in self.up_clases):
            print("existe")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
