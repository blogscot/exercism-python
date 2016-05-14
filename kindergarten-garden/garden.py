class Garden(object):

    _names = "Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()
    _plants = dict((p[0], p) for p in "Clover Grass Radishes Violets".split())

    def __init__(self, plants, students=_names):
        self._students = {v: k * 2 for k, v in enumerate(sorted(students))}
        p = plants.split('\n')
        self._row1, self._row2 = p[0], p[1]

    def plants(self, student):
        pos = self._students[student]
        child_plants = list(self._row1[pos:pos+2] + self._row2[pos:pos+2])
        return map(lambda x: self._plants[x], child_plants)
