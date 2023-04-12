

class NationalPark:

    def __init__(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str):
            self._name = name
        # else:
        #     raise Exception('Cannot change')

    def orders(self):
        from .trip import Trip
        return [trip for trip in Trip.all if trip.national_park == self]

    def trips(self):
        return self.orders()
    # Returns a list of all trips planned for this national park

    def visitors(self):
        unique_set = set([trip.visitor for trip in self.trips()])
        return list(unique_set)
    # Returns a unique list of all visitors a national park has received

    def total_visits(self):
        return self.trips()
        # return len(self.trips())
    # Returns the total number of times that park has been visited

    def best_visitor(self):
        all_visitors = [trip.visitor for trip in self.trips()]
        return max(set(all_visitors), key=all_visitors.count)
    # Returns the Visitor
