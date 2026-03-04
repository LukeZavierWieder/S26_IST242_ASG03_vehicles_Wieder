'''
Holds data for the sedan vehicle class
'''
from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel

class Sedan(Vehicle):
    '''
    Creates the sedan class of vehicles
    '''

    # Constructor
    def __init__(self, manufacturer: Manufacturer,
                model: AutoModel, mpg: float):
        super().__init__(manufacturer, model, mpg)

    # Specify the abstract method
    def number_of_wheels(self):
        return 4
    # Getter
    # Create release year getter
    @property
    def release_year(self):
        return self.model.first_year
    
    # Printing sedan
    def __str__(self):
        return (
            f"({self._manufacturer}) {self._model}, mpg: {self._mpg:.2f}"
        )
    
    