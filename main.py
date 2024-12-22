from models import Point, Grid, Robot

def main():
    start_pt = Point(0, 0)
    width = 3
    height = 3
    grid = Grid(width, height)
    robot = Robot(start_pt, grid)

    print(grid.obstacles)

if __name__ == '__main__':
    main()