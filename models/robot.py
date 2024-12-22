from typing import List, Tuple
from dataclasses import dataclass, field
from .point import Point
from .grid import Grid

class Robot:
    def __init__(self, cur_pt: Point, grid: Grid):
        self.cur_pt = cur_pt
        self.grid = grid

    def navigate(self, end_pt: Point):
        path = self.grid.path_planning(self.cur_pt, end_pt)
        for i in range(1, len(path)):
            next_pt = path[i]
            direction = (next_pt[0] - self.cur_pt[0],
                         next_pt[1] - self.cur_pt[1])
            self.move(direction)

    def move(self, direction: Point):
        self.actuate(direction)
        self.cur_pt = (self.cur_pt[0] + direction[0],
                       self.cur_pt[1] + direction[1])

    def actuate(self, direction: Point):
        print(f"Move direction: {direction}")
