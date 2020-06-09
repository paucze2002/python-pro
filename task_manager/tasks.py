# by Paulina Czempiel


class Tasks:
    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description
        self.hash = hash(name + date)

    def __repr__(self):
        return "Tasks('{}', '{}', '{}', '{}')".format(self.name, self.date, self.description, self.hash)

