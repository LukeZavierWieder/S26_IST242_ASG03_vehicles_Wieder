'''
Holds data for the sedan vehicle class
'''

class Sedan:
    '''
    Creates the sedan class
    '''

    def __init__(self, manufacturer, model, mpg: float):
        # Manufacturer
        self._manufacturer = manufacturer
        # Auto Model
        self._model = model
        # Miles per Gallon
        self._mpg = mpg
    
    