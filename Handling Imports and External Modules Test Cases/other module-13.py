#Calling a function defined in an imported module with mismatched argument types

import _m
_m.f("hola")
_m.f(12)  # E: Argument 1 to "f" has incompatible type "int"; expected "str"
[file _m.py]
def f(c):
  print(c)