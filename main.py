from models import Point, Grid, Robot
from path_planning import PathPlannerFactory
import argparse
import yaml


def extract_point(config, key):
    x, y = config[key]
    return Point(x, y)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', '-c', type=str,
                        default='configs/default.yaml')
    args = parser.parse_args()

    # Reading a YAML file
    print(f"Load config file: {args.config_path}")
    with open(args.config_path, 'r') as file:
        config = yaml.safe_load(file)

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
    robot = Robot(start_pt, grid, planner)

    for obstacle in config["grid"]["obstacles"]:
        grid.add_obstacle(obstacle[0], obstacle[1])

    # first navigate
    print("\n----------------")
    nav_success = robot.navigate(end_pt)
    if not nav_success:
        print(f"\nRobot cannot find a valid path from {start_pt} to {end_pt}")


if __name__ == '__main__':
    main()
