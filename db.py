import mysql.connector
from mysql.connector import Error
import csv 
import os
import glob
from model import *
from pymongo import MongoClient



class ItineraryDB():
    
    def __init__(self,HOST="localhost",PORT=27017):
        self.client = MongoClient(HOST, PORT)
        self.database= self.client['Itinerary']
      
    #--create
    # def add_country(self,country):
    #     self.database.createCollection(country.strip().lower())
    def add_city(self,country,city):
        self.database[country].insert_one(city.to_json)
    #--read
    def get_countries(self):
        return self.database.collection_names()
    
    def get_cities(self,country):
        if not(country in self.get_countries()):
            raise ValueError(f'{country} not in Countries ') 
        #[x['City'] for x in list(self.database[country].find())]
        return list(self.database[country].find())
    
    def get_city(self,country,city):
        #TODO: Check exists?
        return list(self.database[country].find({'City':city}))
    #--update
    def update_city(self,country,city):
        if not(country in self.get_countries()):
            raise ValueError(f'{country} not in Countries ') 
        self.database[country].find_one_and_update({'City':city.location},
                                                   {'$set':{'coordinates':city.coordinates,'activities':city.activities}},
                                                   projection = { "coordinates" : 1, "activities" : 1 })
    #--delete
    # delete country
    # delete city 
    
#TODO Class TransportDB?
#TODO Class layers?
#TODO SCHEMA validation