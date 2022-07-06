from typing import Iterable
from types import FunctionType

def typeCheck(types: Iterable):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(types) != (len(args) or len(kwargs)):
                raise ValueError("length of types must be eq to function's arg")
            compare_table = [[], []]
            if args or kwargs:
                for item, type_ in zip((args or (kwargs.items())), types):
                    compare_table[isinstance((item if args else item[1]), type_)].append((item, type_))
                if compare_table[0]:
                    string = f"List of wrong parameter type(Positive order): {', '.join(f'{i} -> {t}' for i, t in compare_table[0])}"
                    raise TypeError(string)
            func(*args, **kwargs)
        return wrapper
    return decorator

@typeCheck((int, str, list))
def foo(a, b, c):
    print('pass')

try:
    foo(a=1, b=1, c=[])
except Exception as error:
    print(error)