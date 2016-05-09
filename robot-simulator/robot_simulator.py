
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:

    def __init__(self, bearing=NORTH, x_pos=0, y_pos=0):
        self.coordinates = x_pos, y_pos
        self.bearing = bearing

    def turn(self, direction):
        self.bearing = (self.bearing + direction + 4) % 4

    def turn_left(self):
        self.turn(-1)

    def turn_right(self):
        self.turn(1)

    def advance(self):
        {NORTH: self.move_north,
         EAST: self.move_east,
         SOUTH: self.move_south,
         WEST: self.move_west}[self.bearing]()

    def simulate(self, seq):
        for action in seq:
            {'R': self.turn_right,
             'L': self.turn_left,
             'A': self.advance}[action]()

    def move_north(self):
        x, y = self.coordinates
        self.coordinates = x, y + 1

    def move_east(self):
        x, y = self.coordinates
        self.coordinates = x + 1, y

    def move_south(self):
        x, y = self.coordinates
        self.coordinates = x, y - 1

    def move_west(self):
        x, y = self.coordinates
        self.coordinates = x - 1, y

