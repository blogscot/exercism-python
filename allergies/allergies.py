
allergens = ["eggs", "peanuts", "shellfish", "strawberries",
             "tomatoes", "chocolate", "pollen", "cats"]


class Allergies:

    def __init__(self, value):
        self.lst = [item for index, item in enumerate(allergens) if value & (1 << index)]

    def is_allergic_to(self, item):
        return item in self.lst
