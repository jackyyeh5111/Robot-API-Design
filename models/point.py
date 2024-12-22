from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented
