from .trip import Trip


class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, input):
        if not hasattr(self, 'name'):
            if type(input) == str and 1 <= len(input) <= 15:
                self._name = input
            else:
                raise Exception('invalid visitor name type')
        else:
            raise Exception('cannot change visitor name')

    def trips(self):
        all_trips = Trip.get_all()
        return [trip for trip in all_trips if trip.visitor == self]
# Returns a list of all trips for that visitor
# The list of trips must contain type Trip

    def nationalparks(self):
        unique_set = set([trip.national_park for trip in self.trips()])
        return list(unique_set)
# Returns a unique list of all parks who that visitor has visited.
# The list of national parks must contain type NationalPark

    def create_trip(self, national_park, start_date, end_date):
        Trip(self, national_park, start_date, end_date)
# given a national park object, a start_date and end_date (as a string), creates a new Trip and associates it with that visitor and national park.
