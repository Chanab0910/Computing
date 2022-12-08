def calc_grade(mark: int) -> str:

    if not isinstance(mark, int):
        raise TypeError("It has to be an integer")
    elif mark > 350:
        raise ValueError("That mark is too high")
    elif mark < 0:
        raise ValueError("That mark is too low")
    elif mark > 263:
        return 'A*'
    elif mark > 228:
        return 'A'
    elif mark > 188:
        return 'B'
    elif mark > 149:
        return 'C'
    elif mark > 110:
        return 'D'
    elif mark > 71:
        return 'E'
    else:
        return 'U'


if __name__ == '__main__':
    print(calc_grade(6))

