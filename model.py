import mysql.connector
from mysql.connector import Error
import pandas as pd
import abc
import csv


class Location(metaclass=abc.ABCMeta):
    def __init__(self,location,googleMapLocation):
        self.location=location
        self.googleMapLocation=googleMapLocation
    @abc.abstractmethod
    def get_csv_line(self):
        return f'{self.location}, {self.googleMapLocation}'
    
    
class City(Location):
    #TODO CATCH ERRORS
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
        
    @staticmethod
    def city_from_csv(city_file):
        with open(city_file,'r') as f:
            header=f.readline()
            activites_csv=f.readlines()
        city_headers=[x.strip() for x in header.split(', ')]
        print(city_headers)
        activities=[]
        for line in activites_csv:
            if len(line.strip()) > 0:
                activities.append(Activity.from_csv(line))    
    
        return City(*city_headers,loActivity=activities)
                        
class Activity(Location):
    #TODO CATCH ERRORS
    def __init__(self,title,googleMapLocation,cost,):
        super().__init__(title,googleMapLocation)
        self.cost=cost
    
    def get_csv_line(self):
        return super().get_csv_line() + f', {self.cost}'
    @staticmethod
    def from_csv(csv_line):
        #Throw catche rrror here
        line=[x.strip() for x in csv_line.split(', ')]
        try:
            return Activity(*line)
        except Exception as e:
            print(f'Failed loading {line}')
            print(e)
        