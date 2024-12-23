from models import Point, Grid, Robot
from path_planning import PathPlannerFactory
import argparse
import yaml


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--config_path', '-c', type=str, required=True)
    parser.add_argument('--is_vis', '-v', action='store_true',
                        help='visualize robot navigation process')
    args = parser.parse_args()

    # Reading a YAML file
    # with open("config.yaml", "r") as file:
    #     config = yaml.safe_load(file)

    # print(config)

    start_pt = Point(0, 0)
    end_pt = Point(2, 2)
    width = 3
    height = 3
    grid = Grid(width, height)
    robot = Robot(start_pt, grid, args.is_vis)

    planner_type = "dijkstra"  # Could be "astar" or "bfs"
    planner = PathPlannerFactory.get_planner(planner_type)
    print(f"Using planner: {planner.__class__.__name__}")

    robot.navigate(end_pt, planner)


if __name__ == '__main__':
    main()
