from typing import List
from .point import Point


class Grid:
    def __init__(self, width: int, height: int, obstacles: List[Point] = []):
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def clear_obstacles(self) -> None:
        self.obstacles = []

    def update_grid(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.clearObstacles()

    def is_valid_point(self, pt: Point) -> bool:
        # boundary check
        return pt.x >= 0 and pt.y >= 0 and pt.x < self.width and pt.y < self.height

    def add_obstacle(self, x: int, y: int) -> bool:
        pt = Point(x, y)
        if not self.isValidPoint(pt):
            return False
        self.obstacles.append(pt)
        return True

    def path_planning(self, start: Point, end: Point) -> List[Point]:
        # Placeholder path planning logic
        # Returns a straight-line path for simplicity
        return [start, end]
