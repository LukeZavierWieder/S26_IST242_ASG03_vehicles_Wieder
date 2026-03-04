'''
Holds a private list of vehicles
'''
from vehicle import Vehicle

class Garage:
    '''
    Creates the garage class
    '''
    # Constructer
    def __init__(self):
        '''
        Initialize empty list for garage
        '''
        self._vehicles: list[Vehicle] = []
    

    # getters
    def add_vehicle(self, vehicle: Vehicle):
        '''
        Add a vehicle to the garage
        '''
        self._vehicle.append(vehicle)
    
    def clear_garage(self):
        '''
        Empties the garage of vehicles
        '''
        self._vehicle.clear()

    def remove_vehicle(self, vehicle: Vehicle):
        '''
        Takes vehicle out of garage
        '''
        self._vehicle.pop(vehicle)

    @property
    def vehicles(self):
        '''
        Returns a copy of the internal list of vehicles
        '''
        return list[self._vehicles]
    
    def sort_by_release_year(self):
        '''
        Sorts garage based on release year
        '''
        self._vehicle.sort()
    
    # Printing
    def __str__(self):
        return "\n".join(str(v) for v in self._vehicles)