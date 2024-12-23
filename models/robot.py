from .point import Point
from .grid import Grid
from path_planning import PathPlanner


class Visualizer:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.canvas = []

    def reset(self):
        # draw grid
        self.canvas = [['-' for _ in range(self.grid.width)]
                       for _ in range(self.grid.height)]

        # Mark the target on the canvas
        self.canvas[self.target.y][self.target.x] = 'T'

        # Mark obstacles on the canvas
        for pt in self.grid.obstacles:
            self.canvas[pt.y][pt.x] = 'X'

    def set_target(self, target: Point):
        self.target = target

    def display_legend(self):
        print("R: robot"
              "\nT: target"
              "\nX: obstacle"
              "\n-: empty space")

    def display_canvas(self):
        for row in self.canvas:
            print(' '.join(row))

    def update(self, robot_pos: Point):
        """
        Updates the grid canvas with the robot's current position and prints the grid.
        """
        self.reset()
        self.canvas[robot_pos.y][robot_pos.x] = 'R'
        self.display_canvas()


class Robot:
    def __init__(self, cur_pt: Point, grid: Grid, path_planner: PathPlanner):
        self.cur_pt = cur_pt
        self.grid = grid
        self.path_planner = path_planner
        self.visualizer = Visualizer(grid)

    def set_grid(self, new_grid: Grid):
        self.grid = new_grid

    def set_path_planner(self, path_planner: PathPlanner):
        """ allow switching path planner in runtime """
        self.path_planner = path_planner

    def navigate(self, end_pt: Point) -> bool:
        """
        Navigates the robot from its current position to the specified target point.

        Args:
            end_pt (Point): The target point to navigate to.

        Returns:
            bool: True if a valid path is found and navigation is completed successfully,
                False if the target point is invalid or no path exists.
        """

        # boundary check
        if not self.grid.is_valid_point(end_pt):
            return False

        # delegate path_planner to do planning
        path = self.path_planner.plan(self.cur_pt, end_pt, self.grid)

        # empty path means no possible route from start to end
        if len(path) == 0:
            return False

        # visualize robot path planning
        self.visualizer.display_legend()
        print(f'\nStart path planning from {self.cur_pt} to {end_pt}')
        self.visualizer.set_target(end_pt)
        self.visualizer.update(self.cur_pt)

        # Control the robot's movement
        for next_pt in path:
            if self.cur_pt == next_pt:
                continue

            # four possible directions (left, right, up , down)
            direction = next_pt - self.cur_pt
            self.move(direction)
            self.visualizer.update(self.cur_pt)

        return True

    def move(self, direction: Point):
        """
        Moves the robot in the specified direction.
        """
        print(f'\nMove from {self.cur_pt} to {self.cur_pt + direction}')
        self.cur_pt = self.cur_pt + direction
