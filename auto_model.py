'''
Holds data on years the models are produced
'''
class AutoModel:
    '''
    Creates the auto model class
    '''

    def __init__(self, name : str, in_production : bool, years : list[int]):
        # Name of Auto Model
        self._name = name
        # If the model is still in production
        self._in_production = in_production
        # Years of production
        self._years =list(years)

    
    # Properties
    @property
    def name(self):
        '''
        returns the name
        
        Parameter:
            self: 
        '''
        return self._name 
    
    @property
    def in_production(self):
        '''
        returns the name
        
        Parameter:
            self: 
        '''
        return self._in_production 
    
    @property
    def years(self):
        '''
        returns the name
        
        Parameter:
            self: 
        '''
        return list(self._years)
    @property
    def first_year(self):
        '''
        Returns the first production year
        '''
        return self._years[0]
    
    def __str__(self):
        return f"{self._name} inproduction = {self._in_production}"
        f"  release years = {self._years}"