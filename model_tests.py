from db import *
from model import *

# -- Location tests --
def test_location_init():
    def normal_init():    
        location1=Location("location1",(1,2))
    def empty_title_init():
        location2=Location("",(3,3))
def test_location_todict():
    pass
def test_location_tost():
    pass

# -- Activity tests --
def test_activity_init():
    pass
def test_activity_tostr():
    pass
def test_activity_iter():
    pass
def test_activity_todict():
    pass
def test_activity_fromdict():
    pass

# -- City tests --
def test_city_init():
    pass
def test_city_append_activity():
    pass
def test_city_todict():
    pass
def test_city_iter():
    pass
def test_city_fromdict():
    pass
def test_city_to_json():
    pass

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
    test_location_init()