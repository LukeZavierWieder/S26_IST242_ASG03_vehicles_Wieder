'''
Holds data on years the models are produced
'''
class auto_model():
    '''
    Creates the auto model class
    '''

    def __init__(self, name : str, in_production : bool, years : list[int]):
        self.__name = name
        self.__in_production = in_production
        self.__years = years

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