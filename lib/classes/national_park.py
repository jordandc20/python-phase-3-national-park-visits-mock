from .trip import Trip


class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, input):
        if not hasattr(self, 'name'):
            if type(input) == str:
                self._name = input
            else:
                raise Exception('invalid national park name type')
        else:
            raise Exception('cannot change visitor name')

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
# Returns a list of all trips planned for this national park
# The list of trips must contain type trip

    def visitors(self):
        unique_list = set([trip.visitor for trip in self.trips()])
        return list(unique_list)
# Returns a unique list of all visitors a national park has received
# The list of visitors must contain type Visitor

    def total_visits(self):
        return len(self.trips())
# Returns the total number of times that park has been visited

    def best_visitor(self):
        all_visits = [trip.visitor for trip in self.trips()]
        return max(set(all_visits), key=all_visits.count)
# Returns the Visitor
