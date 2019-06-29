#!/usr/bin/python3
""" command interpreter """


import cmd


class HBNBCommand(cmd.Cmd):
    """ interpreter of commands"""
    prompt = '(hbnb)'

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
