# Functions are first-class citizens in Python:

# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.

def myfunc(a, b):
    return a + b

funcs = [myfunc]

print(funcs[0])
#<function myfunc at 0x00000267E94A2550>

print(funcs[0](2, 3))
#5

print(myfunc(6,14))
#20