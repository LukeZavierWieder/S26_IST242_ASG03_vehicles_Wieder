'''
Holds the vehicle class data
'''
from abc import ABC, abstractmethod
from functools import total_ordering # Sorting purposes
from manufacturer import Manufacturer
from auto_model import AutoModel

@total_ordering
class Vehicle(ABC):
    '''
    Creates the abstract base vehicle class
    '''
    # Constructor
    def __init__(self, manufacturer : Manufacturer,
                 model: AutoModel, mpg: float):
        self._manufacturer = manufacturer
        self._model = model
        self._mpg = mpg
    
    # Getters
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @property
    def model(self):
        return self._model
    
    @property
    def mpg(self):
        return self._mpg
    
    # Concrete method
    def how_far_with(self, num_of_gallons: int):
        return self._mpg * num_of_gallons
    
    # Abstract method
    @abstractmethod
    def number_of_wheels(self):
        ...

    # Comparisons 
    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.release_year == other.release_year

    def __lt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        return self.release_year < other.release_year

    def __hash__(self):
        return hash(self.release_year)
    
    
