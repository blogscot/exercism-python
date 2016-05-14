class Garden(object):

    _names = "Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()

    _plant_values = "Clover Grass Radishes Violets".split()
    _plant_keys = "C G R V".split()
    _plants = dict(zip(_plant_keys, _plant_values))

    def __init__(self, plants, students=_names):
        self._children = dict(zip(sorted(students), range(len(students))))
        p = plants.split('\n')
        self._row1 = p[0]
        self._row2 = p[1]

    def plants(self, child):
        first_plant = self._children[child] * 2
        child_plants = [self._row1[first_plant], self._row1[first_plant+1],
                        self._row2[first_plant], self._row2[first_plant + 1]]

        return map(lambda x: self._plants[x], child_plants)

