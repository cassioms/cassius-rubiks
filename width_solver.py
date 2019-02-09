from copy import deepcopy


class WidthSearchSolver:

    BAD_MOVES = {
        "U": ["U", "U'", "U2"],
        "U'": ["U", "U'", "U2"],
        "U2": ["U", "U'", "U2"],
        "D": ["D", "D'", "D2"],
        "D'": ["D", "D'", "D2"],
        "D2": ["D", "D'", "D2"],
        "F": ["F", "F'", "F2"],
        "F'": ["F", "F'", "F2"],
        "F2": ["F", "F'", "F2"],
        "B": ["B", "B'", "B2"],
        "B'": ["B", "B'", "B2"],
        "B2": ["B", "B'", "B2"],
        "L": ["L", "L'", "L2"],
        "L'": ["L", "L'", "L2"],
        "L2": ["L", "L'", "L2"],
        "R": ["R", "R'", "R2"],
        "R'": ["R", "R'", "R2"],
        "R2": ["R", "R'", "R2"],
    }

    @classmethod
    def solve(cls, scrambled_cube):
        sequences = [move for move in scrambled_cube.moves]
        iterations = 0
        while True:
            cube = deepcopy(scrambled_cube)
            iterations += 1

            current_sequence = sequences[0]
            print("Trying sequence: {}".format(current_sequence))
            cube.apply_sequence(moves=current_sequence)

            last_move = current_sequence.split(sep=" ")[-1]
            if WidthSearchSolver.is_solved(cube):
                print("Found a solution: {}".format(current_sequence))
                print("Took {} iterations to find the solution".format(len(sequences)))
                break

            for move in cube.moves:
                if last_move and move in WidthSearchSolver.BAD_MOVES[last_move]:
                    continue

                new_move_sequence = "{} {}".format(current_sequence, move)
                sequences.append(new_move_sequence)
            sequences.remove(current_sequence)

    @classmethod
    def is_solved(cls, cube):
        return cube.is_solved()
