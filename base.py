from typing import List, Union, Tuple
from pydantic import ValidationError

from exceptions import PointNotNumbersException, PointNotInDiapasonExeption
from validators import DiapasonValidator


class Diapason:
    """
    class that Represent diapason of numbers:
    Diapason([1, 2.9, 5])

    ----------_______________---------
    0         1     2.9      5     6
    """

    def __init__(self, points: List[Union[int, float]]):
        try:
            DiapasonValidator(points=points)
        except ValidationError as ex:

            raise PointNotNumbersException(
                f'Points must be valid integers or float \n '
                f'{ex.errors()[0]['msg']} \n'
                f'"{ex.errors()[0]['input']}"'
            )
        self.points = [float(point) for point in points]
        self.points.sort()
        self.start_point = min(self.points)
        self.end_point = max(self.points)

    @property
    def is_point(self) -> bool:
        return self.start_point == self.end_point

    @property
    def length(self) -> float:
        return self.end_point - self.start_point

    def touch(self, other) -> bool:
        return touch(self, other)

    def intersects(self, other) -> bool:
        return intersects(self, other)

    def crosses(self, other) -> bool:
        return crosses(self, other)

    def distance(self, other) -> float:
        return distance(self, other)

    def move(self, step: float) -> None:
        move(self, step)

    def __len__(self):
        return self.length

    def __str__(self):
        return f'Diapason({self.points})'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.start_point == other.start_point and self.end_point == other.end_point

    def __add__(self, other):
        return Diapason(points=self.points + other.points)

    def __contains__(self, item):
        return contains(self, item)


def touch(d_1: Diapason, d_2: Diapason) -> bool:
    """
    d_1 = Diapason([1, 2])
    d_2 = Diapason([2, 3])
    d_1.touch(d_2)
    True
    """

    if d_1.start_point <= d_2.start_point <= d_1.end_point:
        return True
    if d_1.start_point <= d_2.end_point <= d_1.end_point:
        return True
    return False


def intersects(d_1: Diapason, d_2: Diapason):
    """
    d_1 = Diapason([1, 3])
    d_2 = Diapason([2, 4])
    d_1.intersects(d_2)
    True
    """

    if d_1.start_point < d_2.start_point < d_1.end_point:
        return True
    if d_1.start_point < d_2.end_point < d_1.end_point:
        return True
    return False


def crosses(d_1: Diapason, d_2: Diapason):
    """
    d_1 = Diapason([1, 3])
    d_2 = Diapason([3, 4])
    d_1.intersects(d_2)
    True
    """

    if d_1.start_point == d_2.end_point or d_1.end_point == d_2.start_point:
        return True
    return False


def contains(d_1: Diapason, d_2: Diapason) -> bool:
    """
    d_2 in d_1
    """
    if d_1.start_point <= d_2.start_point < d_1.end_point:
        if d_1.start_point < d_2.end_point <= d_1.end_point:
            return True
    return False


def common(diapasons_list: List[Diapason]):
    pass


def distance(d_1: Diapason, d_2: Diapason):
    if d_1.touch(d_2):
        return 0
    return min(
        abs(d_1.end_point - d_2.start_point),
        abs(d_1.start_point - d_2.end_point)
    )


def move(diapason: Diapason, step: float):
    for index, _ in enumerate(diapason.points):
        diapason.points[index] += step
    diapason.start_point = min(diapason.points)
    diapason.end_point = max(diapason.points)


def split_by_point(diapason: Diapason, split_point: float) -> Tuple[Diapason]:
    if not Diapason([split_point]).touch(diapason) or Diapason([split_point]).crosses(diapason):
        raise PointNotInDiapasonExeption(
            f'Point {split_point} not in diapason {diapason}'
        )
    left_d = Diapason(
        [p for p in diapason.points if p <= split_point]
    )

    