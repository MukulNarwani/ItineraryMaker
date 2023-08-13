import mysql.connector
from mysql.connector import Error
import pandas as pd
import abc
from db import *


class Location(metaclass=abc.ABCMeta):
    def __init__(self,location,googleMapLocation):
        self.location=location
        self.googleMapLocation=googleMapLocation
    @abc.abstractmethod
    def get_csv_line(self):
        return f'{self.location}, {self.googleMapLocation}'
    
    
class City(Location):
    
    def __init__(self,location,googleMapLocation,**loActivity):
        super().__init__(location,googleMapLocation)
        if(type(loActivity)==list):
            self.loActivity=loActivity
        else:
            self.loActivity=list()
    def get_csv_line(self):
        return super().get_csv_line()
    def append_activity(self,activity):   
        self.loActivity.append(activity)
            
class Activity(Location):
    
    def __init__(self,title,googleMapLocation,cost,):
        super().__init__(title,googleMapLocation)
        self.cost=cost
    
    def get_csv_line(self):
        return super().get_csv_line() + f', {self.cost}'

# a=Activity('act','act1','act2')
# b=City('city','city2',loActivity=[a])
def CityHandler():
    #handle loading and returning a city
    location = input('location? ')
    googleMapLocation = input('location? ')
    return City(location,googleMapLocation)
def ActivityHandler():
    activity = input('activity title? ')
    activity_location = input('activity location? ')
    activity_cost = input('activity cost? ')  
    return Activity(activity,activity_location,activity_cost)
 
def model():
    city=CityHandler()
    while(input('would you like to make an activity?(y/n) ') == 'y'):
        activity=ActivityHandler()
        city.append_activity(activity)
    return city

cityCSVSaver(model())