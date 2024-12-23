import os
import time
from typing import List
from models import Point, Grid, Robot
from path_planning import Dijkstra

class Visualizer:
    def __init__(self, width: int, height: int, obstacles: List[Point]):
        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.reset()
        
    def reset(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.obstacles:
                    self.grid[y][x] = 'X'
                else:
                    self.grid[y][x] = '-'
        

    def update(self, robot_pos: Point):
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        self.reset()

        # Update robot's position
        robot_x, robot_y = robot_pos
        self.grid[robot_y][robot_x] = 'R'

        # Display the grid
        for row in self.grid:
            print(' '.join(row))

    def run(self, path: List[Point], delay: float = 0.5):
        for position in path:
            self.update(position)
            time.sleep(delay)


# Example usage
if __name__ == "__main__":
    start_pt = Point(0, 0)
    end_pt = Point(2, 2)
    width = 3
    height = 3
    grid = Grid(width, height)
    robot = Robot(start_pt, grid)

    planner = Dijkstra()
    path = planner.plan(start_pt, end_pt, grid)

    # width = 5
    # height = 5
    # obstacles = [(1, 1), (3, 2), (2, 3)]  # List of obstacle coordinates
    # start = (0, 0)
    # path = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2)]

    visualizer = Visualizer(width, height, obstacles)
    visualizer.run(path, delay=0.5)
