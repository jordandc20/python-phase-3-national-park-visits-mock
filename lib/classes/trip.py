from .visitor import Visitor
from .national_park import NationalPark


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if type(national_park) == NationalPark:
            self._national_park = national_park
        else:
            raise Exception("Not valid park")

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if type(visitor) == Visitor:
            self._visitor = visitor
        else:
            raise Exception("Not valid visitor")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if start_date and type(start_date) == str:
            self._start_date = start_date
        # else:
        #     raise Exception("Not valid start_date")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if end_date and type(end_date) == str:
            self._end_date = end_date
        # else:
        #     raise Exception("Not valid end_date")
