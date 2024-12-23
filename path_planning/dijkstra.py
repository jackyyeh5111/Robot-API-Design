from .path_planner import PathPlanner
from models import Point, Grid
from typing import List
from models import Point
import heapq  # For priority queue implementation


class Dijkstra(PathPlanner):
    def plan(self, start: Point, end: Point, grid: Grid) -> List[Point]:
        # Convert obstacles to a set for fast lookup
        obstacle_set = set(obstacle for obstacle in grid.obstacles)

        # Directions for moving (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Priority queue for the open list
        open_list = []
        heapq.heappush(open_list, (0, start))  # (cost, point)

        # Dictionary to store the shortest path to each point
        came_from = {}

        # Dictionary to store the cost to reach each point
        g_score = {start: 0}

        while open_list:
            cur_cost, cur_point = heapq.heappop(open_list)

            # If we reach the goal, reconstruct the path
            if cur_point == end:
                path = []
                while cur_point in came_from:
                    path.append(cur_point)
                    cur_point = came_from[cur_point]
                path.append(start)
                path.reverse()
                return path

            # Explore neighbors
            for dx, dy in directions:
                nb_pt = Point(cur_point.x + dx, cur_point.y + dy)

                # Skip obstacles or out-of-bounds points
                if nb_pt in obstacle_set or not grid.is_valid_point(nb_pt):
                    continue

                tentative_g_score = g_score.get(
                    cur_point, float('inf')) + 1

                # If this path is better, update the score and the came_from map
                if nb_pt not in g_score or tentative_g_score < g_score[nb_pt]:
                    g_score[nb_pt] = tentative_g_score
                    came_from[nb_pt] = cur_point
                    heapq.heappush(open_list, (tentative_g_score, nb_pt))

        # If we exit the loop without finding a path, return an empty list (no path)
        return []
