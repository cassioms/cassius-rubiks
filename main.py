from rubiks import RubiksCube
from width_solver import WidthSearchSolver


if __name__ == '__main__':
    cube = RubiksCube()
    cube.apply_sequence(moves="R U R'")
    solver = WidthSearchSolver()
    solver.solve(scrambled_cube=cube)
