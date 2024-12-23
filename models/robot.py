from typing import List, Tuple
from .point import Point
from .grid import Grid
from path_planning import PathPlanner
import os
import time

class Visualizer:
    def __init__(self, grid: Grid):
        self.grid = grid

    def reset(self):
        self.canvas = [['-' for _ in range(self.grid.width)]
                       for _ in range(self.grid.height)]

        # draw obstacles
        for pt in self.grid.obstacles:
            self.vis_grid[pt.y][pt.x] = 'X'

    def update(self, robot_pos: Point, delay: float = 1.):
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        self.reset()

        # Update robot's position
        self.canvas[robot_pos.y][robot_pos.x] = 'R'

        # Display the grid
        for row in self.canvas:
            print(' '.join(row))
        
class Robot:
    def __init__(self, cur_pt: Point, grid: Grid, is_vis: bool):
        self.cur_pt = cur_pt
        self.grid = grid
        self.is_vis = is_vis
        if self.is_vis:
            self.visualizer = Visualizer(self.grid)

    def navigate(self, end_pt: Point, path_planner: PathPlanner) -> bool:
        if not self.grid.is_valid_point(end_pt):
            return False

        path = path_planner.plan(self.cur_pt, end_pt, self.grid)

        if self.is_vis:
            self.visualizer.update(self.cur_pt)
                
        # Control the robot's movement
        for next_pt in path:
            if self.cur_pt == next_pt:
                continue
            direction = next_pt - self.cur_pt
                
            if self.is_vis:
                self.visualizer.update(self.cur_pt + direction)
                
            self.move(direction)
            
            # keep display frame for 1 sec
            if self.is_vis:
                time.sleep(1.0)
            
        return True

    def move(self, direction: Point):
        print(f'Move from {self.cur_pt} to {self.cur_pt + direction}')
        self.cur_pt = self.cur_pt + direction
