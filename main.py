from models import Point, Grid, Robot
from path_planning import PathPlannerFactory
import argparse
import yaml
import json


def extract_point(config, key):
    x, y = config[key]
    return Point(x, y)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', '-c', type=str,
                        default='configs/default.yaml')
    parser.add_argument('--is_vis', '-v', action='store_true',
                        help='visualize robot navigation process')
    args = parser.parse_args()

    # Reading a YAML file
    with open(args.config_path, 'r') as file:
        config = yaml.safe_load(file)

    print(json.dumps(config, indent=4))

    # parse yaml parameters
    start_pt = extract_point(config["robot"], "start_pt")
    end_pt = extract_point(config["robot"], "end_pt")
    width = config["grid"]["width"]
    height = config["grid"]["height"]

    # create planner
    planner = PathPlannerFactory.get_planner(config["planner_name"])
    print(f"Using planner: {planner.__class__.__name__}")

    # init primary components
    grid = Grid(width, height)
    robot = Robot(start_pt, grid, planner, args.is_vis)

    for obstacle in config["grid"]["obstacles"]:
        grid.add_obstacle(obstacle[0], obstacle[1])

    # first navigate
    nav_success = robot.navigate(end_pt)
    if not nav_success:
        print(f"\nRobot cannot find a valid path from {start_pt} to {end_pt}")

    # switch path planner
    new_planner = PathPlannerFactory.get_planner("bfs")
    print(f"Using planner: {planner.__class__.__name__}")
    robot.set_path_planner(new_planner)

    # second navigate
    nav_success = robot.navigate(end_pt=Point(8, 8))
    if not nav_success:
        print(f"\nRobot cannot find a valid path from {start_pt} to {end_pt}")


if __name__ == '__main__':
    main()
