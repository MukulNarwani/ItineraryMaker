import mysql.connector
from mysql.connector import Error
import pandas as pd
import abc
from dataclasses import dataclass
from db import *

@dataclass
class Location():
    location:str
    coordinates:(int,int)
    def __str__(self):
        return f'Location:{self.location}, coordinates:{self.coordinates}'
class City():
    def __init__(self,location,coordinates,**loActivity):
        self.location=Location(location,coordinates)
        if(type(loActivity)==list):
            self.loActivity=loActivity
        else:
            self.loActivity=list()   
    def append_activity(self,activity):   
        self.loActivity.append(activity)
    @staticmethod
    def from_json(doc)->object:
        pass
    def to_json(cls)->str:
        tmp=','.join([str(x) for x in cls.loActivity])
        return f'{str(cls.location)}, Activity:{tmp} '

                        
class Activity():
    def __init__(self,title,coordinates,cost,):
        self.cost=cost
        self.location=Location(title,coordinates)
    def __str__(self):
        return f'{self.location}, cost:{self.cost}'
    
class Model():
    def __init__(self) -> None:
        self.db = ItineraryDB()
    def list_handler(cls,country=None,city=None):
        if not country:
            return cls.db.get_countries()
        elif city:
            cls.db.get_city(country,city)
        else:
            cls.db.get_cities(country)
    def add_handler(cls,country,city):
        cls.db.add_city(country,city)
    def update_handler(cls):
        cls.model.update_handler()
    def delete_handler(cls):
        cls.model.delete_handler()