from typing import Iterable

def round(number: int | float, ndigits: int = None) -> int | float:
    """Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

    Args:
        number (int | float): int or float, float will be processed.
        ndigits (int, optional): round digits. Defaults to None.

    Returns:
        int | float: rounded int or float
    """
    if isinstance(number, int):
        return number
    elif isinstance(number, float):
        integral, fractional = str(number).split(".")
        if ndigits == len(fractional):
            return number
        if ndigits is None or ndigits == 0:
            return int(integral) + (int(fractional[0]) >= 5)
        print(fractional[:ndigits])
        return int(integral) + float(f"0.{int(fractional[:ndigits])+((int(fractional[ndigits]) >= 5))}")
    else:
        raise TypeError(f"type {type(number).__name__} is not available")

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

def stringFormat(string: str, format: dict) -> str:
    """Format string with dict

    Args:
        string (str): string
        format (dict): format table

    Returns:
        str: formated string
    """
    return string.format(**format)

del Iterable

# if __name__ == "__main__":
#     from random import random, randint
#     # for i in {randint(0, 10) + random() for i in range(10)}:
#     #     print(f"{i} -> {round(i, 3)}")
#     for i in range(len(str(3.1415926))-1):
#         print(f"{i}: {round(3.1415926, i)}")