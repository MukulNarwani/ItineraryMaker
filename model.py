import bson
import pandas as pd
import json
from dataclasses import dataclass
from db import ItineraryDB

@dataclass
class Location():
    title:str
    coordinates:tuple[int,int]
    def __iter__(self):
        tmp={'title':self.title,'coordinates':self.coordinates}
        for key, value in tmp.items():
            yield key,value
    def __dict__(self):
        return {'title':self.title,'coordinates':self.coordinates}
    def __str__(self):
        return f'Location:{self.title}, coordinates:{self.coordinates}'
class Activity():
    def __init__(self,title,coordinates,cost,):
        self.cost=cost
        self.location=Location(title,coordinates)
    def __str__(self):
        return f'{self.location}, cost:{self.cost}'
    def __iter__(self):
        tmp={'location':dict(self.location),'cost':self.cost}
        for key, value in tmp.items():
            yield key,value
    def __dict__(self):
        return {'title':self.location,'cost':self.cost}
    @staticmethod
    def from_dic(doc):
        return Activity(doc['title'],doc['coordinates'],doc['cost'])
    
@dataclass
class City():
    location: Location
    loActivity: list[Activity]

    # def __post_init__(self):
        # if type(self.loActivity)==Activity:
        #     self.loActivity=list(self.loActivity)
    def append_activity(self,activity):   
        self.loActivity.append(activity)
    def __dict__(cls):
        print('called')
        return {'City':{'Location':dict(cls.location),
                        'Activities':[dict(activity) 
                                        for activity in cls.loActivity]}}
    def __iter__(self):
        for key,value in self.__dict__().items():
            yield key, value
    @staticmethod
    def from_dic(doc)->object:
        for activity in doc['activities']:
            Activity.from_dic(activity)
        return City(Location(doc['title'],doc['coord']))
    def to_json(cls)->str:
        tmp=','.join([str(x) for x in cls.loActivity])
        class_str=f'{str(cls.location)}, Activity:{tmp} '
        return class_str

class Country:
    
    
    def __init__(self,cities: str) -> None:
        self.cities=[]
        self.parse_json(cities)
    def parse_json(self,json_str):
        json_cities=json.loads(json_str)
        for city in json_cities:
            self.cities.append(City.from_dic(city))
    
class Model():

    def __init__(self) -> None:
        self.db = ItineraryDB()
        self.activeCountry=None

    def set_active_country(cls,country)->None:
        if(country in cls.db.get_countries()):
            #load country
            cities=cls.db.get_cities(country)
            Country(cities)
        else:
            cls.db.add_country(country)
        
    def list_handler(cls,country=None,city=None):
        if not country:
            return cls.db.get_countries()
        elif city:
            cls.db.get_city(country,city)
        else:
            cls.db.get_cities(country)
    def add_handler(cls,city):
        cls.db.add_city(cls.activeCountry,city)
    def update_handler(cls,cityName,field: dict):
        cls.db.update_city(cls.activeCountry,cls.db.get_city(cls.activeCountry,cityName).title)
    def delete_handler(cls,city=None):
        if city:
            cls.db.delete_handler()