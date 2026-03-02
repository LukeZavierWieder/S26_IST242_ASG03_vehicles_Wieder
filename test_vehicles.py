'''
This is the unit testing file
Tester: Luke Wieder

Run the script using:
    pytest -v
'''

import pytest

from manufacturer import Manufacturer
from auto_model import AutoModel
from vehicle import Vehicle
from sedan import Sedan
'''
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

class TestAutoModel:
    def test_contructor_and_getters(self):
        am = AutoModel("F150", True, [2020, 2021, 2022])
        assert am.get_name == "F150"
        assert am.get_in_production == True
        assert am.get_years == [2020, 2021, 2022]
    
    def test_years_defensive_copy(self):
        original_list = [2020, 2021]
        am = AutoModel("F150", True, original_list)
        original_list.clear()
        assert am.get_years == [2020, 2021]
'''
'''
class TestSedan:

    @pytest.fixture
    def civic(self):
        return Sedan(
            Manufacturer("Honda", "Japan"),
            AutoModel("Civic", False, [1996, 1997, 1998]),
            28.0,
        )

    def test_number_of_wheels(self, civic):
        assert civic.number_of_wheels() == 4

    def test_release_year(self, civic):
        assert civic.release_year == 1996

    def test_mpg(self, civic):
        assert civic.mpg == pytest.approx(28.0)

    def test_manufacturer(self, civic):
        assert civic.manufacturer.name == "Honda"
        assert civic.manufacturer.country == "Japan"

    def test_model_name(self, civic):
        assert civic.model.name == "Civic"

    def test_how_far_with(self, civic):
        assert civic.how_far_with(10) == pytest.approx(280.0)
        assert civic.how_far_with(0) == pytest.approx(0.0)

    def test_str_contains_required_parts(self, civic):
        s = str(civic)
        assert "(Honda, Japan)" in s
        assert "Civic" in s
        assert "28.00" in s

    def test_str_does_not_contain_dually(self, civic):
        s = str(civic)
        assert "dually" not in s.lower()

    def test_is_instance_of_vehicle(self, civic):
        assert isinstance(civic, Vehicle)
'''