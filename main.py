from typing import Tuple, List
from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: int

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented


@dataclass
class Grid:
    width: int
    height: int
    obstacles: List[Point] = field(default_factory=list)

    def addObstacle(self, x: int, y: int):
        self.obstacles.append(Point(x, y))

    def path_planning(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Point]:
        # Placeholder path planning logic
        # Returns a straight-line path for simplicity
        return [start, end]

class Robot:
    def __init__(self, cur_pt: Tuple[int, int], grid: Grid):
        self.cur_pt = cur_pt
        self.grid = grid

    def navigate(self, end_pt: Tuple[int, int]):
        path = self.grid.path_planning(self.cur_pt, end_pt)
        for i in range(1, len(path)):
            next_pt = path[i]
            direction = (next_pt[0] - self.cur_pt[0], next_pt[1] - self.cur_pt[1])
            self.move(direction)

    def move(self, direction: Tuple[int, int]):
        self.actuate(direction)
        self.cur_pt = (self.cur_pt[0] + direction[0], self.cur_pt[1] + direction[1])

    def actuate(self, direction: Tuple[int, int]):
        print(f"Move direction: {direction}")


def main():
    start_pt = Point(0, 0)
    width = 3
    height = 3
    grid = Grid(width, height)
    robot = Robot(start_pt, grid)

if __name__ == '__main__':
    main()