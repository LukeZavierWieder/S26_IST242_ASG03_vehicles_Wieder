'''
Holds the main logic of the project
'''
from manufacturer import manufacturer
from auto_model import auto_model
def main():
    '''
    Contains the primary logic of the program. 

    Parameters:
        None.

    Returns:
        None.
    '''
    m = manufacturer("Ford", "USA")
    a_m = auto_model("Fiesta", False, "1976 - 2023")


if __name__ == "__main__":
    # Call the "main" function
    main()
