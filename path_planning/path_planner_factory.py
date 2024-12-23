from .path_planner import PathPlanner
from .dijkstra import Dijkstra
from path_planning.bfs import BFS
# from path_planning.astar import AStar


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


# Example usage
if __name__ == "__main__":
    planner_type = "dijkstra"  # Could be "astar" or "bfs"
    planner = PathPlannerFactory.get_planner(planner_type)
    print(f"Using planner: {planner.__class__.__name__}")
