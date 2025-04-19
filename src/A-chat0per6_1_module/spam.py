'''
When a module named spam is imported, the interpreter first searches for a built-in module with that name. These module names are listed in sys.builtin_module_names. 
If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path.

 sys.path is initialized from these locations:

The directory containing the input script (or the current directory when no file is specified).

PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).

The installation-dependent default (by convention including a site-packages directory, handled by the site module). Look into the site-package under your Lib 

PYTHONPATH  you can export it and indicate the root location for example "src" is the root 

'''
import sys
from numpy.compat.py3k import asunicode # I am importing a function from Lib/site-package/numpy/compat/py3k.py
# "numpy" is a python package (main package for the numpy library or application )
# "compat" is a python subpackage
# py3k is a python module ( file ) called py3k.py
# asunicode is a function inside the py3k module . I can import a class even or a global variable (on the file level)

print(sys.builtin_module_names) # see the output

print(sys.path) # see the output

# You can add a path into your application to search for your module in different places 
import sys
sys.path.append('/ufs/guido/lib/python')
