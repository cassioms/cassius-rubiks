from copy import deepcopy


class RubiksCube:

    MOVES = ("U", "U'", "U2",
             "D", "D'", "D2",
             "L", "L'", "L2",
             "R", "R'", "R2",
             "F", "F'", "F2",
             "B", "B'", "B2")

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

    def __repr__(self):
        return 'Top: {}\n'.format(self.faces['top']) +\
               'Down: {}\n'.format(self.faces['down']) +\
               'Front: {}\n'.format(self.faces['front']) +\
               'Back: {}\n'.format(self.faces['back']) +\
               'Left: {}\n'.format(self.faces['left']) +\
               'Right: {}\n'.format(self.faces['right'])

    def apply_sequence(self, moves):
        pass

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

    def u(self):
        direct_face = 'top'
        self.clockwise_move(direct_face)

        adjacent_faces = {
            'left': 'front',
            'back': 'left',
            'right': 'back',
            'front': 'right'
        }

        tmp_faces = {}
        for face in adjacent_faces:
            tmp_faces[face] = deepcopy(self.faces[face])
            for index in [1, 2, 3]:
                if adjacent_faces[face] == 'back':
                    tmp_faces[face][index] = self.faces[adjacent_faces[face]][index + 4]
                else:
                    tmp_faces[face][index] = self.faces[adjacent_faces[face]][index]
        for face in adjacent_faces:
            for index in [1, 2, 3]:
                if face == 'back':
                    self.faces[face][index + 4] = tmp_faces[face][index]
                else:
                    self.faces[face][index] = tmp_faces[face][index]

    def u2(self):
        self.u()
        self.u()

    def u_prime(self):
        self.u2()
        self.u()

    def d(self):
        # TODO Fix D Moves!!!

        direct_face = 'down'
        self.clockwise_move(direct_face)

        adjacent_faces = {
            'left': 'back',
            'front': 'left',
            'right': 'front',
            'back': 'right'
        }

        tmp_faces = {}
        for face in adjacent_faces:
            tmp_faces[face] = deepcopy(self.faces[face])
            for index in [5, 6, 7]:
                tmp_faces[face][index] = self.faces[adjacent_faces[face]][index]
        for face in adjacent_faces:
            for index in [5, 6, 7]:
                self.faces[face][index] = tmp_faces[face][index]

    def d2(self):
        self.d()
        self.d()

    def d_prime(self):
        self.d2()
        self.d()

    def r(self):
        direct_face = 'right'
        self.clockwise_move(direct_face)

        adjacent_faces = {
            'front': 'down',
            'top': 'front',
            'back': 'top',
            'down': 'back'
        }
        tmp_faces = {}
        for face in adjacent_faces:
            tmp_faces[face] = deepcopy(self.faces[face])
            for index in [3, 4, 5]:
                tmp_faces[face][index] = self.faces[adjacent_faces[face]][index]
        for face in adjacent_faces:
            for index in [3, 4, 5]:
                self.faces[face][index] = tmp_faces[face][index]

    def r2(self):
        self.r()
        self.r()

    def r_prime(self):
        self.r2()
        self.r()


if __name__ == '__main__':
    cube = RubiksCube()
    cube.r()
    cube.u()
    cube.r_prime()
    cube.u_prime()
    print(cube)
