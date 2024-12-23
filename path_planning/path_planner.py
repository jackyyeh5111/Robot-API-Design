from abc import ABC, abstractmethod
from typing import List
from models import Point, Grid


class PathPlanner(ABC):
    @abstractmethod
    def plan(self, start: Point, end: Point, grid: Grid) -> List[Point]:
        raise NotImplementedError("Subclasses must implement this method")

