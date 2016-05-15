
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:

    def __init__(self, bearing=NORTH, x_pos=0, y_pos=0):
        self.coordinates = x_pos, y_pos
        self.bearing = bearing
        self.move = {NORTH: (0, 1), EAST: (1, 0),
                     SOUTH: (0, -1), WEST: (-1, 0)}

    def turn(self, direction):
        self.bearing = (self.bearing + direction + 4) % 4

    def turn_left(self):
        self.turn(-1)

    def turn_right(self):
        self.turn(1)

    def advance(self):
        self.coordinates = tuple(map(sum, zip(self.coordinates,
                                              self.move[self.bearing])))

    def simulate(self, seq):
        for action in seq:
            {'R': self.turn_right,
             'L': self.turn_left,
             'A': self.advance}[action]()

