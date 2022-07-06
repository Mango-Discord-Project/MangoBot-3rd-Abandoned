def round(number: int | float, ndigits: int = None) -> int | float:
    """_summary_

    Args:
        number (int | float): _description_
        ndigits (int, optional): _description_. Defaults to None.

    Returns:
        int | float: _description_
        
    Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
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

if __name__ == "__main__":
    from random import random, randint
    # for i in {randint(0, 10) + random() for i in range(10)}:
    #     print(f"{i} -> {round(i, 3)}")
    for i in range(len(str(3.1415926))-1):
        print(f"{i}: {round(3.1415926, i)}")