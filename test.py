from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import ast
import os
import builtins

caster = getattr(__builtin__, 'float')
print(caster)