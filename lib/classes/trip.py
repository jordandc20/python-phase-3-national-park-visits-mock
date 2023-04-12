class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

# Trips should be initialized with a visitor, national_park, start_date(str), end_date(str)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, input):
        from .visitor import Visitor
        if isinstance(input, Visitor):
            self._visitor = input
        else:
            raise Exception('invalid visitor')
# Trip property Visitor
# Returns the visitor object for that trip
# Must be of type Visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, input):
        from .national_park import NationalPark
        if type(input) == NationalPark:
            self._national_park = input
        else:
            raise Exception('invalid national park')

# Trip property NationalPark
# Returns the NationalPark object for that trip
# Must be of type NationalPark

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, input):
        if type(input) == str:
            self._start_date = input
        else:
            raise Exception('invalid start date')

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, input):
        if type(input) == str:
            self._end_date = input
        else:
            raise Exception('invalid end date')

    @classmethod
    def get_all(cls):
        return cls.all
