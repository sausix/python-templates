#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is a template for using your code safely as importable class
for other programs.
The file name represents your file or program as module
as example: main_as_class
The class version allows more structuring and running your
code in multiple instances without interfering global variables.
"""

import sys


class MyTemplateApp:
    """
    I'm the docstring of your class!
    MyTemplateApp contains a simple program that can be used
    by other applications.
    """

    def __init__(self, instancename: str):
        """
        This is the initialize method being called when your app class
        has just being created with:
            MyTemplateApp()
        This template example wants an instancename so the caller
        needs to supply it and should of course store your app's instance:
            myApp = MyTemplateApp("I'm an isolated app stored in myApp")
        """

        # self always represents the namespace of the particular instance of
        #  your app.
        # Members of your class are created only here.
        # Don't create other members into outside of __init__ later!

        # Typically store passed arguments
        self.name = instancename

        # Create some members and fill with defaults.
        self.title = "My App!"
        self.main_call_count = 0

    def welcome(self):
        """
        I'm the docstring of welcome function of MyTemplateApp class.

        This ist an example function.
        Just provide public functions like this.
        They may be called by other members in this class or from outside.

        You will mostly declare 'self' as first argument in all functions
        in a class.
        'self' always refers to your particular instance and provides access
        to your members and variables.
        """

        print("Hello from", self.name, "also called", self.title)

    def main(self, *args: tuple, **kwargs: dict) -> int:
        """
        I'm the docstring of the main function of MyTemplateApp class.

        This is the main function of the template class.
        """

        # Your main program code is just following
        # ============================================================

        # Why not hide private functions in the main function namespace?
        def private_welcome():
            print("Secret function says: Hello World!")

        # Now call a public function. It's a member of this class.
        self.welcome()  # Always give a welcome first

        private_welcome()  # Run a very own private welcome function

        # Now print args and kwargs if passed to this function
        for arg in args:
            print("Arg:", arg)

        for key, value in kwargs.items():
            print("Keyword", key, "=", value)

        # ============================================================
        # End of main function. Return 0 because it ran fine.
        return 0


if __name__ == "__main__":
    # In general there's no need to check if __name__ == "__main__" when
    # using classes because there should be nothing else on top level.
    # Your app class should also be imported specifically like this in
    #  other programs:
    #     from main_as_class import MyTemplateApp
    #
    # Neverless this mechanism prevents immediate execution of remainig code
    #  in top level of your file when it is being imported in a sloppy way
    #  by another programs like this:
    #     import main_as_class
    #
    # Remaining supplimentary code may still be a command line wrapper like this:

    # Create an instance of your app and pass a custom instancename:
    myApp = MyTemplateApp("Commandline")

    # Call a public function of your app class.
    # Always omit 'self' parameter because they're added internally.
    # self will then represent this 'myApp' instance in function bodies.
    myApp.welcome()  # Call the welcome function now.

    # Now run your main function
    # It will call welcome() again.
    exitcode = myApp.main(*sys.argv[1:])  # Pass all command line options to args

    # Return your exit code to the caller and exit gracefully.
    sys.exit(exitcode)
