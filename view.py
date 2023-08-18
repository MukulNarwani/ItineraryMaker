from model import *
from db import *

def CityHandler():
    
    #Load a saved city or make a new one
    if not(input('would you like to load a City?(y/n) ')=='y'): 
        return NewCity()
    cities=ItineraryDB.get_cities()
    if len(cities)==0:
        print('Found none at current database path')
        return NewCity()
    cities = {v.split('/')[-1]:v for v in cities}
    print(list(cities.keys()))
    city=input('city name? ')
    if city in cities.keys():
        print(f'loading {city}...')
        return ItineraryDB.load(city)
    else: 
        return NewCity()
            
def  NewCity():
    print('Creating new city...')
    location = input('location? ')
    googleMapLocation = input('google map pin? ')
    print(f'making {location}_City')
    city=City(location,googleMapLocation)
    if not(city==None): 
        return City(location,googleMapLocation)
    else: raise Exception('Null City')
    
def ActivityHandler():
    activity = input('activity title? ')
    activity_location = input('activity location? ')
    activity_cost = input('activity cost? ')  
    return Activity(activity,activity_location,activity_cost)
 
def model():
    try:
        city=CityHandler()
    except Exception as e:
        print('Error loading city, Aborting...')    
        return
    while(input('would you like to make an activity?(y/n) ') == 'y'):
        activity=ActivityHandler()
        city.append_activity(activity)
    print('saving City')
    db=ItineraryDB()
    db.cityCSVSaver(city)

if __name__=="__main__":
    model()



