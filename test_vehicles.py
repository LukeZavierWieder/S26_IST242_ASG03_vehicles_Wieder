'''
This is the unit testing file
Tester: Luke Wieder

Run the script using:
    pytest -v
'''

import pytest
from manufacturer import Manufacturer

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