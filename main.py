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

    original_list = [2020, 2021]

    am = AutoModel("F150", True, original_list)

    print(am.get_years)

    original_list.clear()

    print(am.get_years)


if __name__ == "__main__":
    # Call the "main" function
    main()
