import csv 
import os
import glob
from pymongo import MongoClient



class ItineraryDB():
    
    def __init__(self,HOST="localhost",PORT=27017):
        self.client = MongoClient(HOST, PORT)
        self.database= self.client['Itinerary']
      
    #--create
    def add_country(cls,country):
        cls.database[country.strip().lower()]
    def add_city(cls,country,city_json):
        cls.database[country].insert_one(city_json)
    #--read
    def get_countries(cls):
        return cls.database.list_collections()
    
    def get_cities(cls,country):
        # if not(country in cls.get_countries()):
        #     raise ValueError(f'{country} not in Countries ') 
        #[x['City'] for x in list(cls.database[country].find())]
        return list(cls.database[country].find())
    
    def get_city(cls,country,city):
        #TODO: Check exists?
        return  (cls.database[country].find({'title':city}))
    #--update
    def update_city(cls,country,city):
        if not(country in cls.get_countries()):
            raise ValueError(f'{country} not in Countries ') 
        cls.database[country].find_one_and_update({'City':city.location},
                                                   {'$set':{'coordinates':city.coordinates,'activities':city.activities}},
                                                   projection = { "coordinates" : 1, "activities" : 1 })
    #--delete
    def delete_country(cls,country):
        cls.database.drop(country)
    def delete_city(cls,country,city):
        cls.database[country].deleteOne(city)
    
#TODO Class TransportDB?
#TODO Class layers?
#TODO SCHEMA validation
