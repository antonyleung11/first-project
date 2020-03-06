import sys  # used to append new module paths/folders which ur modules u wish to import are located in


import module_to_be_imported  # when you import a module, it automatically runs all the functions and the print statements in that module
import module_to_be_imported as mod  # this gives 'module to be imported' a nickname
from module_to_be_imported import find_index  # only imports the find_index
from module_to_be_imported import (
    find_index as fi,
)  # gives the imported function a nickname


courses = ["History", "Math", "Physics", "Compsci"]

# calling the module's function.
index = module_to_be_imported.find_index(
    courses, "Math"
)  # to call the module's function you must state the module name . function name

print(index)

# calling the module's nickname

mod.find_index(courses, "History")

# if you use from module import function, you don't need to use the nickname / module name anymore

find_index(courses, "Physics")

# import sys -
print("\n" "import sys")
print(
    sys.path
)  # prints list of paths on this machine that python will look for modules

# standard lib - there are many modules available that you can import that already have pre-written function for you to use eg..
import random
import math
import datetime
import calendar

print(
    "\n" + random.choice(courses)
)  # remember to call the imported module random. ____

# import os
import os

print(os.getcwd())  # prints out the current working directory
