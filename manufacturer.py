'''
This holds manufacturer data for different car manufacturers
'''
class manufacturer():
    '''
    Creates the manufacturer class.
    '''
    
    # Constructer
    def __init__(self, name : str, country : str):
        # Name of manufacturer
        self.__name = name
        # Country in which manufacturer is based
        self.__country = country

    # Properties
    @property
    def get_name(self):
        '''
        returns the name
        
        Parameter:
            self: 
        '''
        return self.__name 
    

    @property
    def get_country(self):
        '''
        returns the country
        
        Parameter: 
            self
        '''
        return self.__country