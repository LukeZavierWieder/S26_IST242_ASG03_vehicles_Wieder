'''
This holds manufacturer data for different car manufacturers
'''
class Manufacturer:
    '''
    Creates the manufacturer class.
    '''
    
    # Constructer
    def __init__(self, name : str, country : str):
        # Name of manufacturer
        self._name = name
        # Country in which manufacturer is based
        self._country = country

    # Properties (getters)
    @property
    def get_name(self):
        '''
        returns the name
        
        Parameter:
            self: 
        '''
        return self._name 
    

    @property
    def get_country(self):
        '''
        returns the country
        
        Parameter: 
            self
        '''
        return self._country