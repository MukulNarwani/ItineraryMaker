from db import *
from model import *
a=ItineraryDB()

#get country tests
#get cities tests
# print(list(a.get_cities('Switzerland')))
#get city tests
def test_get_city():
    print(list(a.get_city('Switzerland','zermatt')))
    print(list(a.get_city('Switzerland','zeswrmatt')))
def test_get_cities():
    print(list(a.get_cities('Switzerland')))
    print(list(a.get_cities('Switzerlandasd')))
def test_get_countries():
    print(list(a.get_countries()))


def test_add_country():
    a.add_country('NotSwitzerland')
    print(list(a.get_countries()))
def test_add_city():
    city_dict=dict(City(Location('a',(1,2)),[Activity('act',(1,2),123)]))
    print(city_dict)
    a.add_city('NotSwitzerland',
                city_dict)
    print(list(a.get_cities('NotSwitzerland')))
def test_add_cit_many_activities():
    activities=[Activity('act',(1,2),123),Activity('dada',(12,22),000)]
    city_dict=dict(City(Location('a',(1,2)),activities))
    print(city_dict)
    a.add_city('NotSwitzerland',
                city_dict)
    print(list(a.get_cities('NotSwitzerland')))

if __name__=="__main__":
    test_add_cit_many_activities()
