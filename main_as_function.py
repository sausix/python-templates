#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a template for using your code safely
from command line and as import into other programs
The file name represents your program as module
as example: main_as_function

The point of this mechanism is to wrap your code
into a main function instead of code in top level.
"""

import sys


def main(*args: tuple, **kwargs: dict) -> int:
    """
    I'm your docstring!
    All your code is wrapped into this function instead of on top level of
    the file.
    This template program is calling an own private function and then
    prints optionally supplied arguments.
    
    Of course, your programm may be defined with strict or none arguments
    like this:
        def main() -> int:
    """

    # Your main program code is just following
    # ============================================================

    # Why not hide your functions in the main function namespace?
    def welcome():
        "I'm a secret helper function"
        print("Hello World!")

    welcome()  # Run your very own private function

    # Now just print args and kwargs if present
    for arg in args:
        print("Arg:", arg)

    for key, value in kwargs.items():
        print("Keyword", key, "=", value)

    # ============================================================
    # End of your program. Return 0 because your program ran fine.
    return 0


if __name__ == "__main__":
    # Prevents immediate execution of your program when your package
    #  is being imported by another program like this:
    #     import main_as_function
    #
    # If the other program wants to execute your code as fancy
    #  function, it has to import your main function and run it:
    #     from main_as_function import main
    #     main()
    # or pass args and kwargs if needed:
    #     main("arg1", "arg2", karg1=10, karg2="Hello World")

    # Now run your programm
    exitcode = main(*sys.argv[1:])  # Pass all command line options to args

    # Return your exit code to the caller and exit gracefully.
    sys.exit(exitcode)
