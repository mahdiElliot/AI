class State:
    def __init__(self, location, status, previous_status, holding, capacity, varaityNumber_things):
        self.location = location
        self.status = status
        self.previous_status = previous_status
        self.holding = holding
        self.capacity = capacity
        self.varaityNumber_things = varaityNumber_things

    def __repr__(self):
        return "{0}, {1}, {2}, {3}".format(self.location, self.status,
                                        self.previous_status, self.holding)