'''
Holds the main logic of the project
'''
from manufacturer import Manufacturer
from auto_model import AutoModel
def main():
    '''
    Contains the primary logic of the program. 

    Parameters:
        None.

    Returns:
        None.
    '''
    m = Manufacturer("Ford", "USA")
    print(m.get_name)
    print(m.get_country)
    print(m)
    
    a_m = AutoModel("Fiesta", False, "1976 - 2023")


if __name__ == "__main__":
    # Call the "main" function
    main()
