import re

class NationalPark:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        #allow setting of name if it hasnt been set yet
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after it is set.")
        
        #validate name
        if isinstance(value, str) and len(value) >= 3 :
            self._name = value
        else:
            raise TypeError ("Name must be a string with atleast 3 characters.")
        
    def trips(self):
        pass
    
    def visitors(self):
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass


class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        if isinstance(visitor, Visitor):
            self.visitor = visitor
        else:
            raise TypeError("This is not an istance of the Visitor class")
        
        if isinstance(national_park, NationalPark):
            self.national_park = national_park
        else:
            raise TypeError("This is not an instance of the NationalPark class")
               

        self.start_date = start_date
        self.end_date = end_date
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if self._validate_date_format(value):
            if isinstance(value, str) and len(value) >= 7 :
                self._start_date = value
            else:
                raise TypeError("start_date must be a string and atleast 7 characters long")
        else:
            raise ValueError("Start date must be a string in the format September 1st'(month day)")
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if self._validate_date_format(value):
            if isinstance(value, str) and len(value) >= 7 :
                self._end_date = value
            else:
                raise TypeError("end_date must be a string at least 7 characters long")
            
        else:
            raise ValueError("End date must be string in the format 'month day")

    def _validate_date_format(self, date_str):
        pattern = r'^[A-Z][a-z]+ \d{1,2}(st|nd|rd|th)$'

        return bool(re.match(pattern, date_str))
        
class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name (self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise TypeError("name must be  a string in the range 1-15 characters") 
               
    def trips(self):
        pass
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass