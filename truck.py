'''
Holds data for the truck vehicle class
'''
from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel


class Truck(Vehicle):
    '''
    Creates the truck class
    '''
     # Constructor
    def __init__(self, manufacturer: Manufacturer,
                model: AutoModel, mpg: float,
                is_dually: bool = False):
        super().__init__(manufacturer, model, mpg)
        # Additional truck attribute
        self._is_dually = is_dually
    
    # Specify the abstract method
    def number_of_wheels(self):
        return 6 if self._is_dually else 4
    
    # Getter
    @property
    def is_dually(self):
        return self._is_dually
    @property
    def release_year(self):
        '''
        Returns the first production year
        '''
        return self._years[0]
    # Create release year getter
    @property
    def release_year(self):
        return self.model.first_year
    
    # Printing truck
    def __str__(self):
        return (
            f"({self._manufacturer}) {self._model}, mpg: {self._mpg:.2f}"
            f" Is dually truck: {self._is_dually})"
        )
    