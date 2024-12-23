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

    # init primary components
    grid = Grid(width, height)
    robot = Robot(start_pt, grid, args.is_vis)

    # create planner
    planner = PathPlannerFactory.get_planner(config["planner_name"])
    print(f"Using planner: {planner.__class__.__name__}")

    # navigate
    robot.navigate(end_pt, planner)


if __name__ == '__main__':
    main()
