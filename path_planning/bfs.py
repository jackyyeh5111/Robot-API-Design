from .path_planner import PathPlanner
from models import Point, Grid
from typing import List
from collections import deque  # For queue implementation


class BFS(PathPlanner):
    def plan(self, start: Point, end: Point, grid: Grid) -> List[Point]:
        # Convert obstacles to a set for fast lookup
        obstacle_set = set(obstacle for obstacle in grid.obstacles)

        # Directions for moving (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Queue for the open list (FIFO queue for BFS)
        open_list = deque([start])  # Points to explore
        came_from = {}  # Dictionary to store the path
        came_from[start] = None  # Start has no predecessor

        while open_list:
            cur_point = open_list.popleft()

            # If we reach the goal, reconstruct the path
            if cur_point == end:
                path = []
                while cur_point is not None:
                    path.append(cur_point)
                    cur_point = came_from[cur_point]
                path.reverse()
                return path

            # Explore neighbors
            for dx, dy in directions:
                nb_pt = Point(cur_point.x + dx, cur_point.y + dy)

                # Skip obstacles or out-of-bounds points
                if nb_pt in obstacle_set or not grid.is_valid_point(nb_pt):
                    continue

                # If the neighbor hasn't been visited yet
                if nb_pt not in came_from:
                    came_from[nb_pt] = cur_point
                    open_list.append(nb_pt)

        # If we exit the loop without finding a path, return an empty list (no path)
        return []
