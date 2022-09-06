#!/usr/bin/python3
"""
    console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        defining class attributes
    """
    # adding custom the prompt text
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """defining exit function"""
        exit(0)

    def do_EOF(self, arg):
        """defining EOF function"""
        print('')
        exit(0)

    def do_help(self, arg):
        """
        will print help text on the terminal
        """
        if arg == 'quit':
            print('Quit command to exit the program')
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
