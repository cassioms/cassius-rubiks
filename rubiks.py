from copy import deepcopy


class RubiksCube:

    @classmethod
    def generate_solved_state(cls):
        return {
            'top': ['Yellow'] * 9,
            'down': ['White'] * 9,
            'left': ['Red'] * 9,
            'right': ['Orange'] * 9,
            'front': ['Green'] * 9,
            'back': ['Blue'] * 9,
        }

    def __init__(self):
        self.faces = RubiksCube.generate_solved_state()
        self.solved_faces = deepcopy(self.faces)
        self.moves = {
            "U": self.up,
            "U'": self.up_prime,
            "U2": self.up2,
            "D": self.down,
            "D'": self.down_prime,
            "D2": self.down2,
            "L": self.left,
            "L'": self.left_prime,
            "L2": self.left2,
            "R": self.right,
            "R'": self.right_prime,
            "R2": self.right2,
            "F": self.front,
            "F'": self.front_prime,
            "F2": self.front2,
            "B": self.back,
            "B'": self.back_prime,
            "B2": self.back2
        }
        self.inverses = {
            "U": "U'",
            "U'": "U",
            "U2": "U2",
            "D": "D'",
            "D'": "D",
            "D2": "D2",
            "L": "L'",
            "L'": "L",
            "L2": "L2",
            "R": "R'",
            "R'": "R",
            "R2": "R2",
            "F": "F'",
            "F'": "F",
            "F2": "F2",
            "B": "B'",
            "B'": "B",
            "B2": "B2"
        }

    def __repr__(self):
        return 'Top: {}\n'.format(self.faces['top']) +\
               'Down: {}\n'.format(self.faces['down']) +\
               'Front: {}\n'.format(self.faces['front']) +\
               'Back: {}\n'.format(self.faces['back']) +\
               'Left: {}\n'.format(self.faces['left']) +\
               'Right: {}\n'.format(self.faces['right'])

    def inverse_sequence(self, moves):
        split_moves = moves.split(sep=' ')
        return " ".join(
            [self.inverses[move] for move in split_moves[::-1]]
        )

    def is_solved(self):
        return self.faces == self.solved_faces

    def apply_sequence(self, moves):
        split_moves = moves.split(sep=' ')
        for move in split_moves:
            self.moves[move]()

    def clockwise_move(self, face):
        self.faces[face] = [self.faces[face][0],
                            self.faces[face][7],
                            self.faces[face][8],
                            self.faces[face][1],
                            self.faces[face][2],
                            self.faces[face][3],
                            self.faces[face][4],
                            self.faces[face][5],
                            self.faces[face][6]]

    def up(self, n=1):
        direct_face = 'top'
        adjacent_faces = {
            'left': {'from_face': 'front', 'from': [1, 2, 3], 'to': [1, 2, 3]},
            'back': {'from_face': 'left', 'from': [1, 2, 3], 'to': [5, 6, 7]},
            'right': {'from_face': 'back', 'from': [5, 6, 7], 'to': [1, 2, 3]},
            'front': {'from_face': 'right', 'from': [1, 2, 3], 'to': [1, 2, 3]}
        }
        for _ in range(n):
            self.move(direct_face=direct_face, adjacent_faces=adjacent_faces)

    def up2(self):
        self.up(n=2)

    def up_prime(self):
        self.up(n=3)

    def down(self, n=1):
        direct_face = 'down'
        adjacent_faces = {
            'left': {'from_face': 'back', 'from': [1, 2, 3], 'to': [5, 6, 7]},
            'front': {'from_face': 'left', 'from': [5, 6, 7], 'to': [5, 6, 7]},
            'right': {'from_face': 'front', 'from': [5, 6, 7], 'to': [5, 6, 7]},
            'back': {'from_face': 'right', 'from': [5, 6, 7], 'to': [1, 2, 3]}
        }
        for _ in range(n):
            self.move(direct_face=direct_face, adjacent_faces=adjacent_faces)

    def down2(self):
        self.down(n=2)

    def down_prime(self):
        self.down(n=3)

    def right(self, n=1):
        direct_face = 'right'
        adjacent_faces = {
            'front': {'from_face': 'down', 'from': [3, 4, 5], 'to': [3, 4, 5]},
            'top': {'from_face': 'front', 'from': [3, 4, 5], 'to': [3, 4, 5]},
            'back': {'from_face': 'top', 'from': [3, 4, 5], 'to': [3, 4, 5]},
            'down': {'from_face': 'back', 'from': [3, 4, 5], 'to': [3, 4, 5]}
        }
        for _ in range(n):
            self.move(direct_face=direct_face, adjacent_faces=adjacent_faces)

    def right2(self):
        self.right(n=2)

    def right_prime(self):
        self.right(n=3)

    def left(self, n=1):
        direct_face = 'left'
        adjacent_faces = {
            'front': {'from_face': 'top', 'from': [1, 7, 8], 'to': [1, 7, 8]},
            'down': {'from_face': 'front', 'from': [1, 7, 8], 'to': [1, 7, 8]},
            'back': {'from_face': 'down', 'from': [1, 7, 8], 'to': [1, 7, 8]},
            'top': {'from_face': 'back', 'from': [1, 7, 8], 'to': [1, 7, 8]}
        }
        for _ in range(n):
            self.move(direct_face=direct_face, adjacent_faces=adjacent_faces)

    def left2(self):
        self.left(n=2)

    def left_prime(self):
        self.left(n=3)

    def front(self, n=1):
        direct_face = 'front'
        adjacent_faces = {
            'top': {'from_face': 'left', 'from': [5, 4, 3], 'to': [7, 6, 5]},
            'right': {'from_face': 'top', 'from': [7, 6, 5], 'to': [1, 8, 7]},
            'down': {'from_face': 'right', 'from': [1, 8, 7], 'to': [3, 2, 1]},
            'left': {'from_face': 'down', 'from': [1, 2, 3], 'to': [3, 4, 5]}
        }
        for _ in range(n):
            self.move(direct_face=direct_face, adjacent_faces=adjacent_faces)

    def front2(self):
        self.front(n=2)

    def front_prime(self):
        self.front(n=3)

    def back(self, n=1):
        direct_face = 'back'
        adjacent_faces = {
            'top': {'from_face': 'right', 'from': [3, 4, 5], 'to': [1, 2, 3]},
            'left': {'from_face': 'top', 'from': [1, 2, 3], 'to': [7, 8, 1]},
            'down': {'from_face': 'left', 'from': [1, 8, 7], 'to': [7, 6, 5]},
            'right': {'from_face': 'down', 'from': [5, 6, 7], 'to': [3, 4, 5]}
        }
        for _ in range(n):
            self.move(direct_face=direct_face, adjacent_faces=adjacent_faces)

    def back2(self):
        self.back(n=2)

    def back_prime(self):
        self.back(n=3)

    def move(self, direct_face, adjacent_faces):
        self.clockwise_move(direct_face)
        tmp_faces = {}
        for face in adjacent_faces:
            tmp_faces[face] = deepcopy(self.faces[face])
            for indexes in zip(adjacent_faces[face]['from'], adjacent_faces[face]['to']):
                tmp_faces[face][indexes[1]] = self.faces[adjacent_faces[face]['from_face']][indexes[0]]
        for face in adjacent_faces:
            for index in adjacent_faces[face]['to']:
                self.faces[face][index] = tmp_faces[face][index]
