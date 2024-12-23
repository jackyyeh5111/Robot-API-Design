from abc import ABC, abstractmethod
from typing import List
from models import Point, Grid


class PathPlanner(ABC):
    @abstractmethod
    def plan(self, start: Point, end: Point, grid: Grid) -> List[Point]:
        raise NotImplementedError("Subclasses must implement this method")

from .dijkstra import Dijkstra
from .bfs import BFS

class PathPlannerFactory:
    """Factory class to create instances of path planning strategies."""

    @staticmethod
    def get_planner(planner_type: str) -> PathPlanner:
        """Returns the appropriate path planner instance.

        Returns:
            PathPlanner: An instance of the desired path planner.
        """
        planners = {
            "dijkstra": Dijkstra,
            "bfs": BFS,
            # "astar": AStar,
        }

        if planner_type.lower() in planners:
            return planners[planner_type.lower()]()
        else:
            raise ValueError(f"Unknown planner type: {planner_type}")
