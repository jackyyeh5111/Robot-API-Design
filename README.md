# Robot-API-Design

## Overview
Robot navigate from start to end in the grid, avoid all obstacles along the way. 

## Design Highlights
To ensure a modular and extensible architecture, the following designs have been implemented:
1. Strategy pattern <br>
Allows users to switch the robot's path-planning strategy dynamically at runtime.
2. Factory pattern <br>
Encapsulates the `PathPalnner` object creation process by providing an interface to create objects without specifying their concrete classes. This delegation promotes loose coupling and enhances code reuse and extensibility.
3. YAML Configuration <br>
Allow users to modify parameters without altering the codebase.

## UML
<img width="600" alt="image" src="https://github.com/user-attachments/assets/90ca6f91-6c0f-4899-8ebb-553f2391f5e5" />

## Folder Structure
```
project/
├── main.py               # Entry point for the program
├── models/               # Folder for data models and core classes
│   ├── __init__.py       
│   ├── point.py          # Contains the Point class
│   ├── grid.py           # Contains the Grid class
│   ├── robot.py          # Contains the Robot class and its visualization class
├── path_planning/        # Folder for various path planning algo and interface
│   ├── __init__.py       
│   ├── bfs.py
│   ├── dijkstra.py
│   ├── path_planner.py   # Interface for PathPlanner algo class and PathPlannerFactory
├── configs/              # YAML configuration files
│   ├── default.yaml
```

## Config Structure
Configurations are defined in a YAML style. Example:
```yaml
robot:
  start_pt: [0, 0] # (x, y)
  end_pt: [3, 1]

grid:
  width: 4
  height: 2
  
  # Define multiple obstacles here
  obstacles: [ 
    [0, 1], # (x, y)
    [2, 0],
  ]

planner_name: "dijkstra" # support "dijkstra" or "bfs"
```

## Quick Starter Guide

### Setup
1. Clone repo
    ```
    $ git clone https://github.com/jackyyeh5111/Robot-API-Design.git && cd Robot-API-Design
    ```
2. Activate virtual environment and install dependencies
    ```
    $ pip install -r requirements.txt
    ```

### Usage
```
$ python3 main.py [-c CONFIG_PATH]

ex: 
python3 main.py -c configs/default.yaml
```

Example output (using `default.yaml`):
```
R: robot
T: target
X: obstacle
-: empty space

Start path planning from Point(x=0, y=0) to Point(x=3, y=1)
R - X -
X - - T

Move from Point(x=0, y=0) to Point(x=1, y=0)
- R X -
X - - T

Move from Point(x=1, y=0) to Point(x=1, y=1)
- - X -
X R - T

Move from Point(x=1, y=1) to Point(x=2, y=1)
- - X -
X - R T

Move from Point(x=2, y=1) to Point(x=3, y=1)
- - X -
X - - R
```

Example output (using `fail_plan.yaml`)
```
Robot cannot find a valid path from Point(x=0, y=0) to Point(x=2, y=2)
```
