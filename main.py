from models import Point, Grid, Robot
from path_planning import PathPlannerFactory
def main():
    start_pt = Point(0, 0)
    end_pt = Point(2, 2)
    width = 3
    height = 3
    grid = Grid(width, height)
    robot = Robot(start_pt, grid)
    
    planner_type = "dijkstra"  # Could be "astar" or "bfs"
    planner = PathPlannerFactory.get_planner(planner_type)
    print(f"Using planner: {planner.__class__.__name__}")

    robot.navigate(end_pt, planner)
    
if __name__ == '__main__':
    main()