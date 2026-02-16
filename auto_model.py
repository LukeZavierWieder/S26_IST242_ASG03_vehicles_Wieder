'''
Holds data on years the models are produced
'''
class AutoModel:
    '''
    Creates the auto model class
    '''

    def __init__(self, name : str, in_production : bool, years : list[int]):
        # Name of Auto Model
        self.__name = name
        # If the model is still in production
        self.__in_production = in_production
        # Years of production
        self.__years = years

    
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
    def get_in_production(self):
        '''
        returns the name
        
        Parameter:
            self: 
        '''
        return self.__in_production 
    
    @property
    def get_years(self):
        '''
        returns the name
        
        Parameter:
            self: 
        '''
        return self.__years