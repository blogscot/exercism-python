EARTH = 31557600.0

planet_data = {'earth': EARTH,
               'mercury': EARTH * 0.2408467,
               'venus': EARTH * 0.61519726,
               'mars': EARTH * 1.8808158,
               'jupiter': EARTH * 11.862615,
               'saturn': EARTH * 29.447498,
               'uranus': EARTH * 84.016846,
               'neptune': EARTH * 164.79132,
               }


class SpaceAge:

    def __init__(self, seconds):
        self.seconds = seconds
        for planet, period in planet_data.items():
            setattr(self, "on_" + planet,
                    lambda p=period: round(seconds / p, 2))
