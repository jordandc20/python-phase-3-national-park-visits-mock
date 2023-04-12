

class Visitor:

    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        # else:
        #     raise Exception("Not valid name")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        # else:
        #     raise Exception("Not valid name")

    def trips(self):
        from .trip import Trip

        return [trip for trip in Trip.all if trip.visitor == self]

    def nationalparks(self):
        unique_set = set([trip.national_park for trip in self.trips()])
        return list(unique_set)

    def create_trip(self, national_park=None, start_date=None, end_date=None):
        from .trip import Trip
        if national_park and start_date and end_date:
            Trip(self, national_park, start_date, end_date)
        else:
            raise Exception("Not enough inputs")
