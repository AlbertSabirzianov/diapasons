from base import Diapason


def diapasons_touch(d_1: Diapason, d_2: Diapason) -> bool:
    """
    d_1.touch(d_2)
    >>> d_1 = Diapason([1, 2])
    >>> d_2 = Diapason([2, 3])
    >>> d_1.touch(d_2)
    >>> True
    """

    if d_1.start_point <= d_2.start_point <= d_1.end_point:
        return True
    if d_1.start_point <= d_2.end_point <= d_1.end_point:
        return True
    return False


def diapason_contains(d_1: Diapason, d_2: Diapason) -> bool:
    """
    d_2 in d_1
    """
    if d_1.start_point <= d_2.start_point < d_1.end_point:
        if d_1.start_point < d_2.end_point <= d_1.end_point:
            return True
    return False

