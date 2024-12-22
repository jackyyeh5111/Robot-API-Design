from typing import List, Tuple
from .point import Point
from .grid import Grid


class Robot:
    def __init__(self, cur_pt: Point, grid: Grid):
        self.cur_pt = cur_pt
        self.grid = grid

    def navigate(self, end_pt: Point) -> bool:
        if not self.grid.isValidPoint(end_pt):
            return False

        path = self.grid.pathPlanning(self.cur_pt, end_pt)

        # Control the robot's movement
        for next_pt in path:
            direction = next_pt - self.cur_pt
            self.move(direction)
        return True

    def move(self, direction: Point):
        self.actuate(direction)
        self.cur_pt = self.cur_pt + direction

    def actuate(self, direction: Point):
        print(f"Move direction: {direction}")
