class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2018 - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            vintage_string = " (vintage)"
            return True
        else:
            vintage_string = ""
            return False
