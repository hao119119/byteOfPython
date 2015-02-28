# the built-in dir function to list the identifiers that an object defines.
# For example, for a module, the identifiers include the functions, classes and variables defined in that module.

import sys
print dir(sys)

print dir()

a = 1

print dir()

del a

print dir()
