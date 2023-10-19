from db import *
from model import *
import pytest


# -- Location tests --
def location_helper():
    normal_init = Location("location1", (1, 2))
    return normal_init


class TestLocation():
    # def test_location_init():
    def test_normal_init(self):
        location1 = location_helper()
        assert str(location1) == str(Location("location1", (1, 2)))

    def test_empty_title_init(self):
        with pytest.raises(TypeError) as e_info:
            location2 = Location("", (3, 3))

    def test_no_title_init(self):
        with pytest.raises(TypeError) as e_info:
            location3 = Location(None, (3, 3))

    def test_negative_coord_init(self):
        with pytest.raises(ValueError) as e_info:
            location4 = Location("location4", (-1, -1))

    def test_no_coord_init(self):
        with pytest.raises(TypeError) as e_info:
            location5 = Location("location5", None)
            location6 = Location("location6", (None, None))

    def test_empty_init(self):
        with pytest.raises(TypeError) as e_info:
            location7 = Location()

    def test_location_todict(self):
        location_dict = dict(location_helper())
        assert location_dict == {'title': 'location1', 'coordinates': (1, 2)}

    def test_location_tost(self):
        location_str = str(location_helper())
        assert location_str == "Location: location1, coordinates:(1, 2)"

# -- Activity tests --


def activity_helper():
    return Activity('normal_activity', (1, 2), 10)


class TestActivity():
    # def test_activity_init(self):
    def test_normal_init(self):
        activity1 = activity_helper()
        assert str(
            activity1) == 'Location: normal_activity, coordinates:(1, 2), cost:10'

    def test_empty_str_init(self):
        with pytest.raises(TypeError) as e_info:
            activity2 = Activity("", (1, 2), 5)

    def test_none_str_init(self):
        with pytest.raises(TypeError) as e_info:
            activity3 = Activity(None, (1, 2), 3)

    def test_zero_cord_init(self):
        activity4 = Activity("normal", (0, 0), 5)
        assert str(activity4) == "Location: normal, coordinates:(0, 0), cost:5"

    def test_neg_cord_init(self):
        with pytest.raises(ValueError) as e_info:
            activity5 = Activity("normal", (-1, -1), 5)

    def test_no_cord_init(self):
        with pytest.raises(TypeError) as e_info:
            activity6 = Activity("normal", None, 5)
            activity7 = Activity("normal", (None, None), 5)

    def test_zero_cost_init(self):
        activity8 = Activity('normal', (1, 1), 0)

    def test_no_cost_init(self):
        with pytest.raises(TypeError) as e_info:
            activity9 = Activity('normal', (1, 1), None)

    def test_neg_cost_init(self):
        with pytest.raises(ValueError) as e_info:
            activity10 = Activity('normal', (1, 1), -1)

    def test_normal_activity_tostr(self):
        # TODO abnormal tests
        activity_str = str(activity_helper())
        assert activity_str == "Location: normal_activity, coordinates:(1, 2), cost:10"

    # def test_activity_iter(self):
    #     iter_activity=iter(activity_helper())
    #     #TODO abnormal activity_iter
    #     assert type(iter_activity)== iter()

    def test_activity_todict(self):
        dict_activity = dict(activity_helper())

        assert dict_activity == {'location': {
            'title': 'normal_activity', 'coordinates': (1, 2)}, 'cost': 10}
        # TODO abnormal activity_dict

    def test_activity_fromdict(self):
        activity_dict = Activity.from_dic(dict(activity_helper()))
        assert dict(activity_dict) == dict(activity_helper())

# -- City tests -- #


def city_helper():

    activity = Activity('secondactivity', (100, 100), 10)
    return City('city', (0, 0), [activity_helper(), activity])


class TestCity():
    # def test_city_init(self):
    def test_normal_city_init(self):
        city1 = city_helper()
        assert str(city1) == 'city: coordinates: (0, 0), '\
                             'Activities: '\
                             '[Location: normal_activity, coordinates:(1, 2), cost:10, '\
                             'Location: secondactivity, coordinates:(100, 100), cost:10]'

    def test_city_init_one_activity(self):
        location = location_helper()
        city2 = City(location.title, location.coordinates, activity_helper())

        assert str(city2) == 'location1: coordinates: (1, 2), '\
            'Activities: [Location: normal_activity, coordinates:(1, 2), cost:10]'

    def test_city_init_no_activity(self):
        city3 = City('location1', (1, 2), None)
        assert str(city3) == 'location1: coordinates: (1, 2), '\
                             'Activities: [None]'

    def test_city_init_no_location(self):
        with pytest.raises(TypeError) as e:
            city4 = City(None, activity_helper())

    def test_city_append_activity(self):
        city5 = city_helper()
        activity = Activity('thirdactivity', (100, 100), 10)
        city5.append_activity(activity)
        assert str(city5) == 'city: coordinates: (0, 0), '\
            'Activities: [Location: normal_activity, coordinates:(1, 2), cost:10, '\
            'Location: secondactivity, coordinates:(100, 100), cost:10, '\
            'Location: thirdactivity, coordinates:(100, 100), cost:10]'

    def test_city_todict(self):
        city6 = dict(city_helper())
        assert city6 == {'city':
                         {'Coordinates': (0, 0),
                          'Activities': [
                             {'location': {'title': 'normal_activity',
                                           'coordinates': (1, 2)}, 'cost': 10},
                             {'location': {'title': 'secondactivity',
                                           'coordinates': (100, 100)}, 'cost': 10}]}}

    def test_city_fromdict(self):
        city8 = City.from_dic(dict(city_helper()))
        assert dict(city8) == dict(city_helper())

    # TODO Potentially wrong
    def test_city_to_json(self):
        city9 = city_helper().to_json()
        assert city9 == {'city':
                         {'Coordinates': [0, 0],
                          'Activities': [
                             {'location': {'title': 'normal_activity',
                                           'coordinates': [1, 2]}, 'cost': 10},
                             {'location': {'title': 'secondactivity', 'coordinates': [100, 100]}, 'cost': 10}]}}

# -- Country tests --


def test_country_init():
    pass


def test_country_update_city():
    pass


def test_country_delete_city():
    pass

# -- Model tests --


def test_model_init():
    pass


def test_model_setactive():
    pass


def test_model_listhandler():
    pass


if __name__ == "__main__":
    pass
