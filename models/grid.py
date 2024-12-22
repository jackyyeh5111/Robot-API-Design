from typing import List, Tuple
from dataclasses import dataclass, field
from .point import Point

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