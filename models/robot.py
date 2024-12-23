from typing import List, Tuple
from .point import Point
from .grid import Grid
from path_planning import PathPlanner


class Robot:
    def __init__(self, cur_pt: Point, grid: Grid):
        self.cur_pt = cur_pt
        self.grid = grid

    def navigate(self, end_pt: Point, path_planner: PathPlanner) -> bool:
        if not self.grid.is_valid_point(end_pt):
            return False

        path = path_planner.plan(self.cur_pt, end_pt, self.grid)

        # Control the robot's movement
        for next_pt in path:
            if self.cur_pt == next_pt:
                continue
            direction = next_pt - self.cur_pt
            self.move(direction)
        return True

    def move(self, direction: Point):
        print(f'Move from {self.cur_pt} to {self.cur_pt + direction}')
        self.cur_pt = self.cur_pt + direction
