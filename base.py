from typing import List, Union
from pydantic import ValidationError

from exceptions import PointsListNotNumbersException
from validators import DiapasonValidator
import utils


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

            raise PointsListNotNumbersException(
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
        return utils.diapasons_touch(self, other)

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
        return utils.diapason_contains(item, self)


# if __name__ == '__main__':
#     d1 = Diapason([6, 7, 8])
#     d2 = Diapason([6, 7, "lllll"])
#
#     print(d1 == d2)
#     print(d1 != d2)
#     print(d1.points == d2.points)
#     print(d1 in d2)
#     print(d1.touch(d2))
#     print(d1 == d2)
#     print(d1)
#     print(d2)
#     print(d1 + d2)
