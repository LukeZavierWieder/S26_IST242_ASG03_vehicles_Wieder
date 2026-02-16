'''
This is the unit testing file
Tester: Luke Wieder

Run the script using:
    pytest -v
'''

import pytest

from manufacturer import Manufacturer
from auto_model import AutoModel

class TestManufacturer:
    def test_constructor_and_getters(self):
        m = Manufacturer("Ford", "USA")
        assert m.get_name == "Ford"
        assert m.get_country == "USA"
        m = Manufacturer("Honda", "Japan")
        assert m.get_name == "Honda"
        assert m.get_country == "Japan"

    def test_str(self):
        m = Manufacturer("BMW", "Germany")
        assert str(m) == "(BMW, Germany)"

class AutoModel:
    def test_contructor_and_getters(self):
        am = AutoModel("F150", True, [2020, 2021, 2022])
        assert am.get_name == "F150"
        assert am.get_in_production == True
        assert am.get_year == [2020, 2021, 2022]
    
    def test_years_defensive_copy(self):
        original_list = [2020, 2021]
        am = AutoModel("F150", True, original_list)
        original_list.clear()
        assert am.get_years == [2020, 2021]