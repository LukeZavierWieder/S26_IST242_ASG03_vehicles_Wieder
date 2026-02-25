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
    
    