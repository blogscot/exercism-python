EARTH = 31557600

years = {'Earth': EARTH,
         'Mercury': EARTH * 0.2408467,
         'Venus': EARTH * 0.61519726,
         'Mars': EARTH * 1.8808158,
         'Jupiter': EARTH * 11.862615,
         'Saturn': EARTH * 29.447498,
         'Uranus': EARTH * 84.016846,
         'Neptune': EARTH * 164.79132,
         }


class SpaceAge:
    def years_on(self, planet):
        return round(self.seconds / years[planet], 2)

    def __init__(self, seconds):
        self.seconds = float(seconds)

    def on_earth(self):
        return self.years_on('Earth')

    def on_mercury(self):
        return self.years_on('Mercury')

    def on_venus(self):
        return self.years_on('Venus')

    def on_mars(self):
        return self.years_on('Mars')

    def on_jupiter(self):
        return self.years_on('Jupiter')

    def on_saturn(self):
        return self.years_on('Saturn')

    def on_uranus(self):
        return self.years_on('Uranus')

    def on_neptune(self):
        return self.years_on('Neptune')
